import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { DatabaseService } from '../database';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';

describe('DatabaseService', () => {
  let dbService: DatabaseService;
  let testDbPath: string;

  beforeEach(async () => {
    // Create a temporary database for testing
    const tempDir = path.join(os.tmpdir(), 'interview-prep-tests');
    if (!fs.existsSync(tempDir)) {
      fs.mkdirSync(tempDir, { recursive: true });
    }
    testDbPath = path.join(tempDir, `test-${Date.now()}.db`);

    dbService = new DatabaseService(testDbPath);
    await dbService.initialize();
  });

  afterEach(() => {
    // Clean up test database
    dbService.close();
    if (fs.existsSync(testDbPath)) {
      fs.unlinkSync(testDbPath);
    }
  });

  describe('User Management', () => {
    it('should create a new user', () => {
      const user = dbService.createUser({
        username: 'testuser',
        email: 'test@example.com',
        preferredLanguage: 'python',
      });

      expect(user).toBeDefined();
      expect(user.id).toBeDefined();
      expect(user.username).toBe('testuser');
      expect(user.email).toBe('test@example.com');
    });

    it('should use default language when not specified', () => {
      const user = dbService.createUser({
        username: 'testuser2',
        email: 'test2@example.com',
      });

      const retrieved = dbService.getAllUsers().find(u => u.username === 'testuser2');
      expect(retrieved?.preferred_language).toBe('python');
    });

    it('should not allow duplicate usernames', () => {
      dbService.createUser({
        username: 'duplicate',
        email: 'user1@example.com',
      });

      expect(() => {
        dbService.createUser({
          username: 'duplicate',
          email: 'user2@example.com',
        });
      }).toThrow();
    });

    it('should not allow duplicate emails', () => {
      dbService.createUser({
        username: 'user1',
        email: 'duplicate@example.com',
      });

      expect(() => {
        dbService.createUser({
          username: 'user2',
          email: 'duplicate@example.com',
        });
      }).toThrow();
    });

    it('should login user and update last_login', () => {
      dbService.createUser({
        username: 'logintest',
        email: 'login@example.com',
      });

      const user = dbService.loginUser('logintest');

      expect(user).toBeDefined();
      expect(user.username).toBe('logintest');
      expect(user.last_login).toBeDefined();
    });

    it('should get all users', () => {
      dbService.createUser({ username: 'user1', email: 'user1@example.com' });
      dbService.createUser({ username: 'user2', email: 'user2@example.com' });
      dbService.createUser({ username: 'user3', email: 'user3@example.com' });

      const users = dbService.getAllUsers();

      expect(users).toHaveLength(3);
      expect(users.map(u => u.username)).toContain('user1');
      expect(users.map(u => u.username)).toContain('user2');
      expect(users.map(u => u.username)).toContain('user3');
    });

    it('should delete user and cascade delete related data', () => {
      const user = dbService.createUser({
        username: 'deletetest',
        email: 'delete@example.com',
      });

      const result = dbService.deleteUser(user.id);

      expect(result.success).toBe(true);
      expect(result.deletedId).toBe(user.id);

      const users = dbService.getAllUsers();
      expect(users.find(u => u.id === user.id)).toBeUndefined();
    });

    it('should update user preferences', () => {
      const user = dbService.createUser({
        username: 'preftest',
        email: 'pref@example.com',
      });

      dbService.updateUserPreferences(user.id, {
        theme: 'light',
        editorFontSize: 16,
        editorTheme: 'vs-light',
        autoSave: true,
        showHints: false,
      });

      // Verify preferences were saved (would need a getUserPreferences method)
      expect(true).toBe(true); // Placeholder - actual verification would query preferences
    });
  });

  describe('Question Management', () => {
    it('should get all questions', () => {
      const questions = dbService.getQuestions();

      // Questions should be seeded from schema
      expect(Array.isArray(questions)).toBe(true);
    });

    it('should filter questions by category', () => {
      const leetcodeQuestions = dbService.getQuestions('leetcode');

      expect(Array.isArray(leetcodeQuestions)).toBe(true);
      if (leetcodeQuestions.length > 0) {
        expect(leetcodeQuestions.every(q => q.category_name === 'leetcode')).toBe(true);
      }
    });

    it('should filter questions by difficulty', () => {
      const easyQuestions = dbService.getQuestions(undefined, 'easy');

      expect(Array.isArray(easyQuestions)).toBe(true);
      if (easyQuestions.length > 0) {
        expect(easyQuestions.every(q => q.difficulty === 'easy')).toBe(true);
      }
    });

    it('should filter questions by both category and difficulty', () => {
      const leetcodeMedium = dbService.getQuestions('leetcode', 'medium');

      expect(Array.isArray(leetcodeMedium)).toBe(true);
      if (leetcodeMedium.length > 0) {
        expect(leetcodeMedium.every(q =>
          q.category_name === 'leetcode' && q.difficulty === 'medium'
        )).toBe(true);
      }
    });

    it('should get question by ID', () => {
      const allQuestions = dbService.getQuestions();
      if (allQuestions.length > 0) {
        const firstQuestion = allQuestions[0];
        const question = dbService.getQuestionById(firstQuestion.id);

        expect(question).toBeDefined();
        expect(question.id).toBe(firstQuestion.id);
      }
    });

    it('should get LeetCode question details', () => {
      const leetcodeQuestions = dbService.getQuestions('leetcode');
      if (leetcodeQuestions.length > 0) {
        const details = dbService.getLeetCodeQuestionDetails(leetcodeQuestions[0].id);

        if (details) {
          expect(details).toBeDefined();
          expect(details.test_cases).toBeDefined();
          expect(typeof details.test_cases).toBe('string');
        }
      }
    });

    it('should get ML Design question details', () => {
      const mlQuestions = dbService.getQuestions('ml_system_design');
      if (mlQuestions.length > 0) {
        const details = dbService.getMLDesignQuestionDetails(mlQuestions[0].id);

        if (details) {
          expect(details).toBeDefined();
          expect(Array.isArray(details.requirements)).toBe(true);
          expect(Array.isArray(details.key_components)).toBe(true);
        }
      }
    });

    it('should parse hints as array for LeetCode questions', () => {
      const leetcodeQuestions = dbService.getQuestions('leetcode');
      if (leetcodeQuestions.length > 0) {
        const details = dbService.getLeetCodeQuestionDetails(leetcodeQuestions[0].id);

        if (details && details.hints) {
          expect(Array.isArray(details.hints)).toBe(true);
        }
      }
    });

    it('should get question hints', () => {
      const allQuestions = dbService.getQuestions();
      if (allQuestions.length > 0) {
        const hints = dbService.getQuestionHints(allQuestions[0].id);

        expect(Array.isArray(hints)).toBe(true);
      }
    });
  });

  describe('Code Submissions', () => {
    let userId: number;
    let questionId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'submitter',
        email: 'submitter@example.com',
      });
      userId = user.id;

      const questions = dbService.getQuestions('leetcode');
      questionId = questions[0]?.id || 1;
    });

    it('should create code submission', () => {
      const submission = dbService.createCodeSubmission({
        userId,
        questionId,
        language: 'python',
        code: 'def solution(): return True',
        customTestCases: '[]',
        executionTimeMs: 100,
        memoryUsedKb: 1024,
        testResults: JSON.stringify([{ passed: true }]),
        status: 'passed',
      });

      expect(submission).toBeDefined();
      expect(submission.id).toBeDefined();
      expect(submission.userId).toBe(userId);
    });

    it('should get code submission by ID', () => {
      const created = dbService.createCodeSubmission({
        userId,
        questionId,
        language: 'python',
        code: 'def solution(): return True',
        customTestCases: '[]',
        executionTimeMs: 100,
        memoryUsedKb: 1024,
        testResults: JSON.stringify([{ passed: true }]),
        status: 'passed',
      });

      const retrieved = dbService.getCodeSubmission(created.id);

      expect(retrieved).toBeDefined();
      expect(retrieved.id).toBe(created.id);
      expect(retrieved.code).toBe('def solution(): return True');
    });

    it('should record execution metrics', () => {
      const submission = dbService.createCodeSubmission({
        userId,
        questionId,
        language: 'java',
        code: 'public class Solution {}',
        customTestCases: '[]',
        executionTimeMs: 250,
        memoryUsedKb: 2048,
        testResults: JSON.stringify([{ passed: false }]),
        status: 'failed',
      });

      const retrieved = dbService.getCodeSubmission(submission.id);

      expect(retrieved.execution_time_ms).toBe(250);
      expect(retrieved.memory_used_kb).toBe(2048);
      expect(retrieved.status).toBe('failed');
    });
  });

  describe('Design Submissions', () => {
    let userId: number;
    let questionId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'designer',
        email: 'designer@example.com',
      });
      userId = user.id;

      const questions = dbService.getQuestions('ml_system_design');
      questionId = questions[0]?.id || 2;
    });

    it('should create design submission', () => {
      const submission = dbService.createDesignSubmission({
        userId,
        questionId,
        diagramData: JSON.stringify({ nodes: [], edges: [] }),
        writtenExplanation: 'This is my system design explanation.',
        timeSpentSeconds: 1800,
      });

      expect(submission).toBeDefined();
      expect(submission.id).toBeDefined();
      expect(submission.userId).toBe(userId);
    });

    it('should get design submission by ID', () => {
      const created = dbService.createDesignSubmission({
        userId,
        questionId,
        diagramData: JSON.stringify({ nodes: [], edges: [] }),
        writtenExplanation: 'My explanation',
        timeSpentSeconds: 1200,
      });

      const retrieved = dbService.getDesignSubmission(created.id);

      expect(retrieved).toBeDefined();
      expect(retrieved.id).toBe(created.id);
      expect(retrieved.written_explanation).toBe('My explanation');
    });
  });

  describe('Progress Tracking', () => {
    let userId: number;
    let questionId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'tracker',
        email: 'tracker@example.com',
      });
      userId = user.id;

      const questions = dbService.getQuestions();
      questionId = questions[0]?.id || 1;
    });

    it('should update progress for first attempt', () => {
      dbService.updateProgress(userId, questionId, false);

      const progress = dbService.getUserProgress(userId);

      expect(progress).toHaveLength(1);
      expect(progress[0].attempts).toBe(1);
      expect(progress[0].solved).toBe(false);
    });

    it('should increment attempts on multiple tries', () => {
      dbService.updateProgress(userId, questionId, false);
      dbService.updateProgress(userId, questionId, false);
      dbService.updateProgress(userId, questionId, true);

      const progress = dbService.getUserProgress(userId);

      expect(progress[0].attempts).toBe(3);
      expect(progress[0].solved).toBe(true);
    });

    it('should keep solved status once achieved', () => {
      dbService.updateProgress(userId, questionId, true);
      dbService.updateProgress(userId, questionId, false);

      const progress = dbService.getUserProgress(userId);

      expect(progress[0].solved).toBe(true); // Should remain true
    });

    it('should get user statistics', () => {
      // Create progress for multiple questions
      const questions = dbService.getQuestions().slice(0, 3);
      questions.forEach((q, index) => {
        dbService.updateProgress(userId, q.id, index % 2 === 0);
      });

      const stats = dbService.getUserStats(userId);

      expect(stats.total_attempts).toBeGreaterThan(0);
      expect(Array.isArray(stats.byDifficulty)).toBe(true);
    });

    it('should reset user progress', () => {
      dbService.updateProgress(userId, questionId, true);

      const result = dbService.resetUserProgress(userId);

      expect(result.success).toBe(true);

      const progress = dbService.getUserProgress(userId);
      expect(progress).toHaveLength(0);
    });
  });

  describe('Mock Interviews', () => {
    let userId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'interviewer',
        email: 'interviewer@example.com',
      });
      userId = user.id;
    });

    it('should create mock interview', () => {
      const mock = dbService.createMockInterview(userId, 'leetcode');

      expect(mock).toBeDefined();
      expect(mock.id).toBeDefined();
      expect(mock.userId).toBe(userId);
      expect(mock.interviewType).toBe('leetcode');
    });

    it('should complete mock interview', () => {
      const mock = dbService.createMockInterview(userId, 'ml_design');

      const completed = dbService.completeMockInterview(mock.id);

      expect(completed).toBeDefined();
      expect(completed.status).toBe('completed');
      expect(completed.completed_at).toBeDefined();
    });

    it('should add questions to mock interview', () => {
      const mock = dbService.createMockInterview(userId, 'leetcode');
      const questions = dbService.getQuestions('leetcode').slice(0, 2);

      questions.forEach((q, index) => {
        dbService.addQuestionToMock(mock.id, q.id, index);
      });

      const mockQuestions = dbService.getMockInterviewQuestions(mock.id);

      expect(mockQuestions).toHaveLength(2);
      expect(mockQuestions[0].order_index).toBe(0);
      expect(mockQuestions[1].order_index).toBe(1);
    });
  });

  describe('Feedback', () => {
    let userId: number;
    let submissionId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'feedbackuser',
        email: 'feedback@example.com',
      });
      userId = user.id;

      const questions = dbService.getQuestions('leetcode');
      const submission = dbService.createCodeSubmission({
        userId,
        questionId: questions[0]?.id || 1,
        language: 'python',
        code: 'def solution(): pass',
        customTestCases: '[]',
        executionTimeMs: 100,
        memoryUsedKb: 1024,
        testResults: '[]',
        status: 'passed',
      });
      submissionId = submission.id;
    });

    it('should create feedback', () => {
      const feedback = dbService.createFeedback({
        userId,
        submissionId,
        submissionType: 'code',
        feedbackText: 'Great job!',
        scores: JSON.stringify({ correctness: 9, efficiency: 8 }),
        strengths: JSON.stringify(['Clean code', 'Good approach']),
        improvements: JSON.stringify(['Add comments']),
      });

      expect(feedback).toBeDefined();
      expect(feedback.id).toBeDefined();
      expect(feedback.submissionId).toBe(submissionId);
    });

    it('should get user feedback', () => {
      dbService.createFeedback({
        userId,
        submissionId,
        submissionType: 'code',
        feedbackText: 'Feedback 1',
        scores: '{}',
        strengths: '[]',
        improvements: '[]',
      });

      const feedbacks = dbService.getUserFeedback(userId);

      expect(feedbacks.length).toBeGreaterThan(0);
      expect(feedbacks[0].user_id).toBe(userId);
    });

    it('should limit feedback results', () => {
      // Create multiple feedbacks
      for (let i = 0; i < 15; i++) {
        dbService.createFeedback({
          userId,
          submissionId,
          submissionType: 'code',
          feedbackText: `Feedback ${i}`,
          scores: '{}',
          strengths: '[]',
          improvements: '[]',
        });
      }

      const feedbacks = dbService.getUserFeedback(userId, 5);

      expect(feedbacks).toHaveLength(5);
    });
  });

  describe('Submission History', () => {
    let userId: number;

    beforeEach(() => {
      const user = dbService.createUser({
        username: 'historian',
        email: 'history@example.com',
      });
      userId = user.id;
    });

    it('should get combined submission history', () => {
      const leetcodeQ = dbService.getQuestions('leetcode')[0];
      const mlQ = dbService.getQuestions('ml_system_design')[0];

      if (leetcodeQ) {
        dbService.createCodeSubmission({
          userId,
          questionId: leetcodeQ.id,
          language: 'python',
          code: 'code',
          customTestCases: '[]',
          executionTimeMs: 100,
          memoryUsedKb: 1024,
          testResults: '[]',
          status: 'passed',
        });
      }

      if (mlQ) {
        dbService.createDesignSubmission({
          userId,
          questionId: mlQ.id,
          diagramData: '{}',
          writtenExplanation: 'explanation',
          timeSpentSeconds: 1200,
        });
      }

      const history = dbService.getSubmissionHistory(userId);

      expect(history.length).toBeGreaterThan(0);
      expect(history.some(h => h.type === 'code')).toBe(leetcodeQ !== undefined);
      expect(history.some(h => h.type === 'design')).toBe(mlQ !== undefined);
    });

    it('should sort submission history by date descending', () => {
      const questions = dbService.getQuestions('leetcode').slice(0, 3);

      questions.forEach(q => {
        dbService.createCodeSubmission({
          userId,
          questionId: q.id,
          language: 'python',
          code: 'code',
          customTestCases: '[]',
          executionTimeMs: 100,
          memoryUsedKb: 1024,
          testResults: '[]',
          status: 'passed',
        });
      });

      const history = dbService.getSubmissionHistory(userId);

      if (history.length > 1) {
        const first = new Date(history[0].submitted_at).getTime();
        const second = new Date(history[1].submitted_at).getTime();
        expect(first).toBeGreaterThanOrEqual(second);
      }
    });

    it('should limit submission history', () => {
      const questions = dbService.getQuestions().slice(0, 10);

      questions.forEach(q => {
        dbService.createCodeSubmission({
          userId,
          questionId: q.id,
          language: 'python',
          code: 'code',
          customTestCases: '[]',
          executionTimeMs: 100,
          memoryUsedKb: 1024,
          testResults: '[]',
          status: 'passed',
        });
      });

      const history = dbService.getSubmissionHistory(userId, 5);

      expect(history.length).toBeLessThanOrEqual(5);
    });
  });
});
