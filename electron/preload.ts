import { contextBridge, ipcRenderer } from 'electron';

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // User Management
  createUser: (userData: any) => ipcRenderer.invoke('user:create', userData),
  loginUser: (username: string) => ipcRenderer.invoke('user:login', username),
  getAllUsers: () => ipcRenderer.invoke('user:getAll'),
  updateUserPreferences: (userId: number, preferences: any) =>
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

  // Code Execution
  executeCode: (executionData: {
    code: string;
    language: string;
    testCases: any[];
    questionId: number;
  }) => ipcRenderer.invoke('code:execute', executionData),

  submitCode: (submissionData: {
    userId: number;
    questionId: number;
    code: string;
    language: string;
    customTestCases: any[];
  }) => ipcRenderer.invoke('code:submit', submissionData),

  // Design Submissions
  submitDesign: (submissionData: {
    userId: number;
    questionId: number;
    diagramData: any;
    writtenExplanation: string;
    timeSpent: number;
  }) => ipcRenderer.invoke('design:submit', submissionData),

  // Mock Interviews
  startMockInterview: (mockData: { userId: number; interviewType: string }) =>
    ipcRenderer.invoke('mock:start', mockData),
  completeMockInterview: (mockId: number) =>
    ipcRenderer.invoke('mock:complete', mockId),
  getMockInterviewQuestions: (mockId: number) =>
    ipcRenderer.invoke('mock:getQuestions', mockId),
  addQuestionToMock: (mockId: number, questionId: number, orderIndex: number) =>
    ipcRenderer.invoke('mock:addQuestion', mockId, questionId, orderIndex),

  // Feedback
  generateFeedback: (feedbackData: {
    userId: number;
    submissionId: number;
    submissionType: 'code' | 'design';
    mockInterviewId?: number;
  }) => ipcRenderer.invoke('feedback:generate', feedbackData),

  // Progress & Analytics
  getUserProgress: (userId: number) =>
    ipcRenderer.invoke('progress:getByUser', userId),
  getUserStats: (userId: number) =>
    ipcRenderer.invoke('progress:getStats', userId),
  getSubmissionHistory: (userId: number, limit?: number) =>
    ipcRenderer.invoke('submissions:getHistory', userId, limit),
  getUserFeedback: (userId: number, limit?: number) =>
    ipcRenderer.invoke('feedback:getByUser', userId, limit),
});

// Type definitions for TypeScript
export interface ElectronAPI {
  createUser: (userData: any) => Promise<any>;
  loginUser: (username: string) => Promise<any>;
  getAllUsers: () => Promise<any[]>;
  updateUserPreferences: (userId: number, preferences: any) => Promise<void>;
  getQuestions: (category?: string, difficulty?: string) => Promise<any[]>;
  getQuestionById: (questionId: number) => Promise<any>;
  getLeetCodeDetails: (questionId: number) => Promise<any>;
  getMLDesignDetails: (questionId: number) => Promise<any>;
  executeCode: (executionData: any) => Promise<any>;
  submitCode: (submissionData: any) => Promise<any>;
  submitDesign: (submissionData: any) => Promise<any>;
  startMockInterview: (mockData: any) => Promise<any>;
  completeMockInterview: (mockId: number) => Promise<any>;
  getMockInterviewQuestions: (mockId: number) => Promise<any[]>;
  addQuestionToMock: (mockId: number, questionId: number, orderIndex: number) => Promise<any>;
  generateFeedback: (feedbackData: any) => Promise<any>;
  getUserProgress: (userId: number) => Promise<any[]>;
  getUserStats: (userId: number) => Promise<any>;
  getSubmissionHistory: (userId: number, limit?: number) => Promise<any[]>;
  getUserFeedback: (userId: number, limit?: number) => Promise<any[]>;
}

declare global {
  interface Window {
    electronAPI: ElectronAPI;
  }
}
