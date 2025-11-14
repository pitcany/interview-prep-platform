/**
 * IPC Type Definitions
 * Shared types for IPC communication between main and renderer processes
 */

// User types
export interface User {
  id: number;
  username: string;
  email: string;
  created_at: string;
  last_login: string | null;
  preferred_language: string;
}

export interface UserPreferences {
  theme: string;
  editorFontSize: number;
  editorTheme: string;
  autoSave: boolean;
  showHints: boolean;
}

// Question types
export interface Question {
  id: number;
  category_id: number;
  category_name: string;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  description: string;
  constraints?: string;
  examples?: string;
  hints?: string[];
  tags?: string[];
  created_at: string;
}

export interface LeetCodeDetails {
  question_id: number;
  title: string;
  description: string;
  difficulty: 'easy' | 'medium' | 'hard';
  function_signature_python?: string;
  function_signature_java?: string;
  function_signature_cpp?: string;
  test_cases: string; // JSON string
  hidden_test_cases: string; // JSON string
  expected_time_complexity?: string;
  expected_space_complexity?: string;
  solution_python?: string;
  solution_java?: string;
  solution_cpp?: string;
  solution_explanation?: string;
  hints: string[];
}

export interface MLDesignDetails {
  id: number;
  question_id: number;
  title: string;
  description: string;
  difficulty: 'easy' | 'medium' | 'hard';
  scenario: string;
  requirements: string[];
  evaluation_criteria: Record<string, unknown>;
  sample_solution: string;
  key_components: string[];
  hints: string[];
}

// Test case types
export interface TestCase {
  input: unknown;
  expected: unknown;
  expectedOutput?: unknown; // Alias for expected
}

export interface TestResult {
  passed: boolean;
  input: unknown;
  expectedOutput: unknown;
  actualOutput: unknown;
  executionTime: number;
  error?: string;
}

// Execution types
export interface ExecutionData {
  code: string;
  language: string;
  testCases: TestCase[];
  questionId: number;
}

export interface ExecutionResult {
  status: 'passed' | 'failed' | 'error' | 'timeout';
  testResults: TestResult[];
  executionTime: number;
  memoryUsed: number;
  errorMessage?: string;
}

// Submission types
export interface CodeSubmissionData {
  userId: number;
  questionId: number;
  code: string;
  language: string;
  customTestCases: TestCase[];
}

export interface CodeSubmission {
  id: number;
  user_id: number;
  question_id: number;
  language: string;
  code: string;
  custom_test_cases: string;
  submitted_at: string;
  execution_time_ms: number;
  memory_used_kb: number;
  test_results: string;
  status: 'passed' | 'failed' | 'error' | 'timeout';
}

export interface DiagramData {
  nodes: Array<{
    id: string;
    type?: string;
    position: { x: number; y: number };
    data: Record<string, unknown>;
  }>;
  edges: Array<{
    id: string;
    source: string;
    target: string;
    [key: string]: unknown;
  }>;
}

export interface DesignSubmissionData {
  userId: number;
  questionId: number;
  diagramData: DiagramData;
  writtenExplanation: string;
  timeSpent: number;
}

export interface DesignSubmission {
  id: number;
  user_id: number;
  question_id: number;
  diagram_data: string;
  written_explanation: string;
  submitted_at: string;
  time_spent_seconds: number;
}

// Mock interview types
export interface MockInterviewData {
  userId: number;
  interviewType: 'leetcode' | 'ml_design';
}

export interface MockInterview {
  id: number;
  user_id: number;
  interview_type: 'leetcode' | 'ml_design';
  started_at: string;
  completed_at: string | null;
  duration_seconds: number;
  status: 'in_progress' | 'completed' | 'abandoned';
}

export interface MockInterviewQuestion {
  id: number;
  mock_interview_id: number;
  question_id: number;
  order_index: number;
  submission_id: number | null;
  submission_type: 'code' | 'design' | null;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
}

// Feedback types
export interface FeedbackData {
  userId: number;
  submissionId: number;
  submissionType: 'code' | 'design';
  mockInterviewId?: number;
}

export interface Feedback {
  id: number;
  user_id: number;
  submission_id: number;
  submission_type: 'code' | 'design';
  mock_interview_id: number | null;
  feedback_text: string;
  scores: string; // JSON string
  strengths: string; // JSON string
  improvements: string; // JSON string
  generated_at: string;
  question_title?: string;
}

export interface FeedbackResponse {
  text: string;
  scores: {
    correctness?: number;
    efficiency?: number;
    codeQuality?: number;
    problemUnderstanding?: number;
    systemDesign?: number;
    scalability?: number;
    communication?: number;
  };
  strengths: string[];
  improvements: string[];
}

// Progress types
export interface UserProgress {
  id: number;
  user_id: number;
  question_id: number;
  attempts: number;
  solved: boolean;
  first_attempt_at: string | null;
  last_attempt_at: string | null;
  best_time_ms: number | null;
  total_time_spent_seconds: number;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  category: string;
}

export interface UserStats {
  total_attempts: number;
  solved_count: number;
  total_time_spent: number;
  byDifficulty: Array<{
    difficulty: 'easy' | 'medium' | 'hard';
    attempts: number;
    solved: number;
  }>;
}

export interface SubmissionHistory {
  type: 'code' | 'design';
  id: number;
  user_id: number;
  question_id: number;
  submitted_at: string;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  // Code submission specific
  language?: string;
  code?: string;
  execution_time_ms?: number;
  memory_used_kb?: number;
  test_results?: string;
  status?: 'passed' | 'failed' | 'error' | 'timeout';
  // Design submission specific
  diagram_data?: string;
  written_explanation?: string;
  time_spent_seconds?: number;
}
