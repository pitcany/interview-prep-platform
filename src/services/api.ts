// API service for communicating with Electron backend
import type {
  User,
  Question,
  LeetCodeQuestion,
  MLDesignQuestion,
  CodeSubmission,
  DesignSubmission,
  MockInterview,
  Feedback,
  UserProgress,
  UserStats,
  UserPreferences,
  ExecutionResult,
} from '../types';
import { retryWithBackoff } from '../utils/retry';

class APIService {
  private get api() {
    if (!window.electronAPI) {
      throw new Error('Electron API not available');
    }
    return window.electronAPI;
  }

  /**
   * Wrap IPC call with retry logic for network resilience
   */
  private async withRetry<T>(fn: () => Promise<T>): Promise<T> {
    return retryWithBackoff(fn);
  }

  // User Management
  async createUser(userData: {
    username: string;
    email: string;
    preferredLanguage?: string;
  }): Promise<User> {
    return await this.api.createUser(userData);
  }

  async loginUser(username: string): Promise<User> {
    return await this.api.loginUser(username);
  }

  async getAllUsers(): Promise<User[]> {
    return await this.api.getAllUsers();
  }

  async deleteUser(userId: number): Promise<{ success: boolean; deletedId: number }> {
    return await this.api.deleteUser(userId);
  }

  async updateUserPreferences(
    userId: number,
    preferences: UserPreferences
  ): Promise<void> {
    return await this.api.updateUserPreferences(userId, preferences);
  }

  // Questions
  async getQuestions(
    category?: 'leetcode' | 'ml_system_design',
    difficulty?: 'easy' | 'medium' | 'hard'
  ): Promise<Question[]> {
    return this.withRetry(() => this.api.getQuestions(category, difficulty));
  }

  async getQuestionById(questionId: number): Promise<Question> {
    return this.withRetry(() => this.api.getQuestionById(questionId));
  }

  async getLeetCodeDetails(questionId: number): Promise<LeetCodeQuestion> {
    return this.withRetry(() => this.api.getLeetCodeDetails(questionId));
  }

  async getMLDesignDetails(questionId: number): Promise<MLDesignQuestion> {
    return this.withRetry(() => this.api.getMLDesignDetails(questionId));
  }

  async getQuestionHints(questionId: number): Promise<string[]> {
    return this.withRetry(() => this.api.getQuestionHints(questionId));
  }

  // Code Execution
  async executeCode(executionData: {
    code: string;
    language: string;
    testCases: any[];
    questionId: number;
  }): Promise<ExecutionResult> {
    return await this.api.executeCode(executionData);
  }

  async submitCode(submissionData: {
    userId: number;
    questionId: number;
    code: string;
    language: string;
    customTestCases: any[];
  }): Promise<{ submission: CodeSubmission; executionResult: ExecutionResult }> {
    return this.withRetry(() => this.api.submitCode(submissionData));
  }

  // Design Submissions
  async submitDesign(submissionData: {
    userId: number;
    questionId: number;
    diagramData: any;
    writtenExplanation: string;
    timeSpent: number;
  }): Promise<DesignSubmission> {
    return this.withRetry(() => this.api.submitDesign(submissionData));
  }

  // Mock Interviews
  async startMockInterview(mockData: {
    userId: number;
    interviewType: 'leetcode' | 'ml_design';
  }): Promise<MockInterview> {
    return await this.api.startMockInterview(mockData);
  }

  async completeMockInterview(mockId: number): Promise<MockInterview> {
    return await this.api.completeMockInterview(mockId);
  }

  async getMockInterviewQuestions(mockId: number): Promise<any[]> {
    return await this.api.getMockInterviewQuestions(mockId);
  }

  async addQuestionToMock(
    mockId: number,
    questionId: number,
    orderIndex: number
  ): Promise<void> {
    return await this.api.addQuestionToMock(mockId, questionId, orderIndex);
  }

  // Feedback
  async generateFeedback(feedbackData: {
    userId: number;
    submissionId: number;
    submissionType: 'code' | 'design';
    mockInterviewId?: number;
  }): Promise<Feedback> {
    return this.withRetry(() => this.api.generateFeedback(feedbackData));
  }

  // Progress & Analytics
  async getUserProgress(userId: number): Promise<UserProgress[]> {
    return this.withRetry(() => this.api.getUserProgress(userId));
  }

  async getUserStats(userId: number): Promise<UserStats> {
    return this.withRetry(() => this.api.getUserStats(userId));
  }

  async getSubmissionHistory(
    userId: number,
    limit?: number
  ): Promise<(CodeSubmission | DesignSubmission)[]> {
    return this.withRetry(() => this.api.getSubmissionHistory(userId, limit));
  }

  async getUserFeedback(userId: number, limit?: number): Promise<Feedback[]> {
    return this.withRetry(() => this.api.getUserFeedback(userId, limit));
  }

  async resetUserProgress(userId: number): Promise<{ success: boolean }> {
    return await this.api.resetUserProgress(userId);
  }
}

export const api = new APIService();
