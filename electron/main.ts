import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';
import * as url from 'url';
import { config } from 'dotenv';
import { existsSync } from 'fs';
import { DatabaseService } from './services/database';
import { CodeExecutorService } from './services/codeExecutor';
import { LocalLLMService } from './services/localLLM';

function loadEnvironmentVariables() {
  const candidatePaths = new Set<string>();

  const explicitEnvPath =
    process.env.INTERVIEW_PREP_ENV_FILE ||
    process.env.ELECTRON_ENV_FILE ||
    process.env.ENV_FILE;

  if (explicitEnvPath) {
    candidatePaths.add(path.resolve(explicitEnvPath));
  }

  candidatePaths.add(path.join(process.cwd(), '.env'));
  candidatePaths.add(path.join(__dirname, '.env'));
  candidatePaths.add(path.join(__dirname, '..', '.env'));
  candidatePaths.add(path.join(__dirname, '..', '..', '.env'));

  if (app.isReady()) {
    const appPath = app.getAppPath();
    const appDir = appPath.endsWith('.asar') ? path.dirname(appPath) : appPath;
    candidatePaths.add(path.join(appDir, '.env'));

    candidatePaths.add(path.join(process.resourcesPath, '.env'));
    candidatePaths.add(path.join(path.dirname(app.getPath('exe')), '.env'));
  }

  const envPath = [...candidatePaths].find((candidate) => existsSync(candidate));

  if (envPath) {
    config({ path: envPath });
    console.log('Environment loaded from:', envPath);
  } else {
    config();
    console.warn('No .env file found; relying on existing environment variables.');
  }

  console.log('SANDBOX_MODE:', process.env.SANDBOX_MODE);
  console.log('LLM_BASE_URL:', process.env.LLM_BASE_URL ? 'Set' : 'Not set');
  console.log('LLM_MODEL:', process.env.LLM_MODEL || 'Not set');
  console.log(
    'CLAUDE_API_KEY:',
    process.env.CLAUDE_API_KEY ? 'Set' : 'Not set (deprecated, use LLM_BASE_URL)'
  );
}

let mainWindow: BrowserWindow | null = null;
let dbService: DatabaseService;
let codeExecutor: CodeExecutorService;
let llmService: LocalLLMService;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1200,
    minHeight: 700,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
    titleBarStyle: 'default',
    show: false,
  });

  // Load the app
  if (process.env.NODE_ENV === 'development') {
    mainWindow.loadURL('http://localhost:5173');
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadURL(
      url.format({
        pathname: path.join(__dirname, '../dist-react/index.html'),
        protocol: 'file:',
        slashes: true,
      })
    );
  }

  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// Initialize services
async function initializeServices() {
  try {
    const userDataPath = app.getPath('userData');
    const dbPath = path.join(userDataPath, 'interview-prep.db');
    dbService = new DatabaseService(dbPath);
    await dbService.initialize();

    // Pass userDataPath to avoid Docker /tmp mount issues
    codeExecutor = new CodeExecutorService(userDataPath);
    await codeExecutor.initialize();

    // Initialize Local LLM service
    const llmBaseUrl = process.env.LLM_BASE_URL;
    const llmModel = process.env.LLM_MODEL || 'gpt-oss-20b';

    if (!llmBaseUrl) {
      console.warn('LLM_BASE_URL not set. AI feedback generation will not work. Set LLM_BASE_URL in .env to enable.');
    }
    llmService = new LocalLLMService(llmBaseUrl, llmModel);

    console.log('All services initialized successfully');
  } catch (error) {
    console.error('Failed to initialize services:', error);
    app.quit();
  }
}

// App lifecycle
app.on('ready', async () => {
  loadEnvironmentVariables();
  await initializeServices();
  createWindow();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC Handlers

// User Management
ipcMain.handle('user:create', async (_, userData) => {
  return await dbService.createUser(userData);
});

ipcMain.handle('user:login', async (_, username) => {
  return await dbService.loginUser(username);
});

ipcMain.handle('user:getAll', async () => {
  return await dbService.getAllUsers();
});

ipcMain.handle('user:delete', async (_, userId) => {
  return await dbService.deleteUser(userId);
});

ipcMain.handle('user:updatePreferences', async (_, userId, preferences) => {
  return await dbService.updateUserPreferences(userId, preferences);
});

// Questions
ipcMain.handle('questions:getAll', async (_, category, difficulty) => {
  return await dbService.getQuestions(category, difficulty);
});

ipcMain.handle('questions:getById', async (_, questionId) => {
  return await dbService.getQuestionById(questionId);
});

ipcMain.handle('questions:getLeetCodeDetails', async (_, questionId) => {
  return await dbService.getLeetCodeQuestionDetails(questionId);
});

ipcMain.handle('questions:getMLDesignDetails', async (_, questionId) => {
  return await dbService.getMLDesignQuestionDetails(questionId);
});

// Code Execution
ipcMain.handle('code:execute', async (_, executionData) => {
  const { code, language, testCases } = executionData;
  return await codeExecutor.executeCode(code, language, testCases);
});

ipcMain.handle('code:submit', async (_, submissionData) => {
  const { userId, questionId, code, language, customTestCases } = submissionData;
  
  // Execute code
  const executionResult = await codeExecutor.executeCode(
    code,
    language,
    customTestCases
  );

  // Save submission
  const submission = await dbService.createCodeSubmission({
    userId,
    questionId,
    code,
    language,
    customTestCases: JSON.stringify(customTestCases),
    executionTimeMs: executionResult.executionTime,
    memoryUsedKb: executionResult.memoryUsed,
    testResults: JSON.stringify(executionResult.testResults),
    status: executionResult.status,
  });

  // Update progress
  await dbService.updateProgress(userId, questionId, executionResult.status === 'passed');

  return { submission, executionResult };
});

// Design Submissions
ipcMain.handle('design:submit', async (_, submissionData) => {
  const { userId, questionId, diagramData, writtenExplanation, timeSpent } = submissionData;
  
  const submission = await dbService.createDesignSubmission({
    userId,
    questionId,
    diagramData: JSON.stringify(diagramData),
    writtenExplanation,
    timeSpentSeconds: timeSpent,
  });

  return submission;
});

// Mock Interviews
ipcMain.handle('mock:start', async (_, mockData) => {
  const { userId, interviewType } = mockData;
  return await dbService.createMockInterview(userId, interviewType);
});

ipcMain.handle('mock:complete', async (_, mockId) => {
  return await dbService.completeMockInterview(mockId);
});

ipcMain.handle('mock:getQuestions', async (_, mockId) => {
  return await dbService.getMockInterviewQuestions(mockId);
});

ipcMain.handle('mock:addQuestion', async (_, mockId, questionId, orderIndex) => {
  return await dbService.addQuestionToMockInterview(mockId, questionId, orderIndex);
});

// Feedback Generation
ipcMain.handle('feedback:generate', async (_, feedbackData) => {
  const { userId, submissionId, submissionType, mockInterviewId } = feedbackData;
  
  // Get submission details
  let submission: any;
  let question: any;

  if (submissionType === 'code') {
    submission = await dbService.getCodeSubmission(submissionId);
    question = await dbService.getLeetCodeQuestionDetails(submission.questionId);
  } else {
    submission = await dbService.getDesignSubmission(submissionId);
    question = await dbService.getMLDesignQuestionDetails(submission.questionId);
  }

  // Generate feedback using Local LLM
  const feedback = await llmService.generateFeedback(submission, question, submissionType);

  // Save feedback
  const savedFeedback = await dbService.createFeedback({
    userId,
    submissionId,
    submissionType,
    mockInterviewId,
    feedbackText: feedback.text,
    scores: JSON.stringify(feedback.scores),
    strengths: JSON.stringify(feedback.strengths),
    improvements: JSON.stringify(feedback.improvements),
  });

  return savedFeedback;
});

// Progress & Analytics
ipcMain.handle('progress:getByUser', async (_, userId) => {
  return await dbService.getUserProgress(userId);
});

ipcMain.handle('progress:getStats', async (_, userId) => {
  return await dbService.getUserStats(userId);
});

ipcMain.handle('submissions:getHistory', async (_, userId, limit) => {
  return await dbService.getSubmissionHistory(userId, limit);
});

ipcMain.handle('feedback:getByUser', async (_, userId, limit) => {
  return await dbService.getUserFeedback(userId, limit);
});

// Hints
ipcMain.handle('questions:getHints', async (_, questionId) => {
  return await dbService.getQuestionHints(questionId);
});

// Progress Reset
ipcMain.handle('progress:reset', async (_, userId) => {
  return await dbService.resetUserProgress(userId);
});

// Handle uncaught errors
process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
});

process.on('unhandledRejection', (error) => {
  console.error('Unhandled Rejection:', error);
});
