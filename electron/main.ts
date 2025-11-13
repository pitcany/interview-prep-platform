import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';
import * as url from 'url';
import { config } from 'dotenv';
import { existsSync } from 'fs';
import { DatabaseService } from './services/database';
import { CodeExecutorService } from './services/codeExecutor';
import { LLMProviderFactory, LLMProvider } from './services/llmProviderFactory';

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
  } else {
    config();
  }
}

let mainWindow: BrowserWindow | null = null;
let dbService: DatabaseService;
let codeExecutor: CodeExecutorService;
let llmService: LLMProvider;

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
  const isDevelopment = process.env.NODE_ENV === 'development';

  if (isDevelopment) {
    mainWindow.loadURL('http://localhost:5173');
    // Only open DevTools in development mode
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

    // Initialize LLM provider (auto-selects based on environment variables)
    try {
      llmService = LLMProviderFactory.createProvider();
      const providerInfo = LLMProviderFactory.getProviderInfo();
      console.log(`LLM Provider: ${providerInfo.provider} (model: ${providerInfo.model || 'default'})`);
      if (providerInfo.endpoint) {
        console.log(`LLM Endpoint: ${providerInfo.endpoint}`);
      }
    } catch (error: any) {
      console.warn('No LLM provider configured:', error.message);
      console.warn('AI feedback generation will be disabled.');
      console.warn('Set CLAUDE_API_KEY, OPENAI_API_KEY, or LLM_BASE_URL in .env to enable.');
    }

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
  console.log('🔍 [FEEDBACK] Generation requested:', feedbackData);
  const { userId, submissionId, submissionType, mockInterviewId } = feedbackData;

  // Check if LLM service is available
  if (!llmService) {
    const error = new Error('LLM service is not initialized. Please configure LLM_BASE_URL, CLAUDE_API_KEY, or OPENAI_API_KEY in .env');
    console.error('❌ [FEEDBACK]', error.message);
    throw error;
  }

  console.log('✓ [FEEDBACK] LLM service is available');

  // Get submission details
  let submission: any;
  let question: any;

  try {
    if (submissionType === 'code') {
      console.log('📝 [FEEDBACK] Fetching code submission:', submissionId);
      submission = await dbService.getCodeSubmission(submissionId);
      console.log('📝 [FEEDBACK] Submission data:', JSON.stringify(submission, null, 2));
      console.log('📝 [FEEDBACK] Fetching leetcode question:', submission.question_id);
      question = await dbService.getLeetCodeQuestionDetails(submission.question_id);
      console.log('📝 [FEEDBACK] Question data:', question ? 'Retrieved' : 'NULL');
      if (!question) {
        console.error('❌ [FEEDBACK] Question not found for question_id:', submission.question_id);
      }
    } else {
      console.log('📝 [FEEDBACK] Fetching design submission:', submissionId);
      submission = await dbService.getDesignSubmission(submissionId);
      console.log('📝 [FEEDBACK] Submission data:', JSON.stringify(submission, null, 2));
      console.log('📝 [FEEDBACK] Fetching ML design question:', submission.question_id);
      question = await dbService.getMLDesignQuestionDetails(submission.question_id);
      console.log('📝 [FEEDBACK] Question data:', question ? 'Retrieved' : 'NULL');
      if (!question) {
        console.error('❌ [FEEDBACK] Question not found for question_id:', submission.question_id);
      }
    }
    console.log('✓ [FEEDBACK] Retrieved submission and question data');
  } catch (error: any) {
    console.error('❌ [FEEDBACK] Error retrieving submission/question:', error.message);
    throw error;
  }

  // Validate that we have the required data
  if (!question) {
    const error = new Error(`Question not found for question_id: ${submission.question_id}. The question may not exist in the database.`);
    console.error('❌ [FEEDBACK]', error.message);
    throw error;
  }

  // Generate feedback using Local LLM
  try {
    console.log('🤖 [FEEDBACK] Generating feedback with LLM...');
    const feedback = await llmService.generateFeedback(submission, question, submissionType);
    console.log('✓ [FEEDBACK] Feedback generated successfully');

    // Save feedback
    console.log('💾 [FEEDBACK] Saving feedback to database...');
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
    console.log('✓ [FEEDBACK] Feedback saved successfully, ID:', savedFeedback.id);

    return savedFeedback;
  } catch (error: any) {
    console.error('❌ [FEEDBACK] Error during feedback generation or saving:', error.message);
    console.error('Stack:', error.stack);
    throw error;
  }
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
