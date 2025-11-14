import { contextBridge, ipcRenderer } from 'electron';
import type {
  User,
  UserPreferences,
  Question,
  LeetCodeDetails,
  MLDesignDetails,
  ExecutionData,
  ExecutionResult,
  CodeSubmissionData,
  CodeSubmission,
  DesignSubmissionData,
  DesignSubmission,
  MockInterviewData,
  MockInterview,
  MockInterviewQuestion,
  FeedbackData,
  Feedback,
  UserProgress,
  UserStats,
  SubmissionHistory,
} from './types/ipc';

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // User Management
  createUser: (userData: Omit<User, 'id' | 'created_at' | 'last_login'>) =>
    ipcRenderer.invoke('user:create', userData),
  loginUser: (username: string) => ipcRenderer.invoke('user:login', username),
  getAllUsers: () => ipcRenderer.invoke('user:getAll'),
  deleteUser: (userId: number) => ipcRenderer.invoke('user:delete', userId),
  updateUserPreferences: (userId: number, preferences: UserPreferences) =>
    ipcRenderer.invoke('user:updatePreferences', userId, preferences),

  // Questions
  getQuestions: (category?: string, difficulty?: string) =>
    ipcRenderer.invoke('questions:getAll', category, difficulty),
  getQuestionById: (questionId: number) =>
    ipcRenderer.invoke('questions:getById', questionId),
  getLeetCodeDetails: (questionId: number) =>
    ipcRenderer.invoke('questions:getLeetCodeDetails', questionId),
  getMLDesignDetails: (questionId: number) =>
    ipcRenderer.invoke('questions:getMLDesignDetails', questionId),
  getQuestionHints: (questionId: number) =>
    ipcRenderer.invoke('questions:getHints', questionId),

  // Code Execution
  executeCode: (executionData: ExecutionData) =>
    ipcRenderer.invoke('code:execute', executionData),

  submitCode: (submissionData: CodeSubmissionData) =>
    ipcRenderer.invoke('code:submit', submissionData),

  // Design Submissions
  submitDesign: (submissionData: DesignSubmissionData) =>
    ipcRenderer.invoke('design:submit', submissionData),

  // Mock Interviews
  startMockInterview: (mockData: MockInterviewData) =>
    ipcRenderer.invoke('mock:start', mockData),
  completeMockInterview: (mockId: number) =>
    ipcRenderer.invoke('mock:complete', mockId),
  getMockInterviewQuestions: (mockId: number) =>
    ipcRenderer.invoke('mock:getQuestions', mockId),
  addQuestionToMock: (mockId: number, questionId: number, orderIndex: number) =>
    ipcRenderer.invoke('mock:addQuestion', mockId, questionId, orderIndex),

  // Feedback
  generateFeedback: (feedbackData: FeedbackData) =>
    ipcRenderer.invoke('feedback:generate', feedbackData),

  // Progress & Analytics
  getUserProgress: (userId: number) =>
    ipcRenderer.invoke('progress:getByUser', userId),
  getUserStats: (userId: number) =>
    ipcRenderer.invoke('progress:getStats', userId),
  getSubmissionHistory: (userId: number, limit?: number) =>
    ipcRenderer.invoke('submissions:getHistory', userId, limit),
  getUserFeedback: (userId: number, limit?: number) =>
    ipcRenderer.invoke('feedback:getByUser', userId, limit),
  resetUserProgress: (userId: number) =>
    ipcRenderer.invoke('progress:reset', userId),
});

// Type definitions for TypeScript
export interface ElectronAPI {
  createUser: (userData: Omit<User, 'id' | 'created_at' | 'last_login'>) => Promise<User>;
  loginUser: (username: string) => Promise<User>;
  getAllUsers: () => Promise<User[]>;
  deleteUser: (userId: number) => Promise<{ success: boolean; deletedId: number }>;
  updateUserPreferences: (userId: number, preferences: UserPreferences) => Promise<void>;
  getQuestions: (category?: string, difficulty?: string) => Promise<Question[]>;
  getQuestionById: (questionId: number) => Promise<Question>;
  getLeetCodeDetails: (questionId: number) => Promise<LeetCodeDetails>;
  getMLDesignDetails: (questionId: number) => Promise<MLDesignDetails>;
  getQuestionHints: (questionId: number) => Promise<string[]>;
  executeCode: (executionData: ExecutionData) => Promise<ExecutionResult>;
  submitCode: (submissionData: CodeSubmissionData) => Promise<CodeSubmission>;
  submitDesign: (submissionData: DesignSubmissionData) => Promise<DesignSubmission>;
  startMockInterview: (mockData: MockInterviewData) => Promise<MockInterview>;
  completeMockInterview: (mockId: number) => Promise<MockInterview>;
  getMockInterviewQuestions: (mockId: number) => Promise<MockInterviewQuestion[]>;
  addQuestionToMock: (mockId: number, questionId: number, orderIndex: number) => Promise<void>;
  generateFeedback: (feedbackData: FeedbackData) => Promise<Feedback>;
  getUserProgress: (userId: number) => Promise<UserProgress[]>;
  getUserStats: (userId: number) => Promise<UserStats>;
  getSubmissionHistory: (userId: number, limit?: number) => Promise<SubmissionHistory[]>;
  getUserFeedback: (userId: number, limit?: number) => Promise<Feedback[]>;
  resetUserProgress: (userId: number) => Promise<{ success: boolean }>;
}

declare global {
  interface Window {
    electronAPI: ElectronAPI;
  }
}
