// Global type definitions for the Interview Prep Platform

export interface User {
  id: number;
  username: string;
  email: string;
  created_at: string;
  last_login?: string;
  preferred_language: 'python' | 'java' | 'cpp';
}

export interface UserPreferences {
  theme: 'dark' | 'light';
  editorFontSize: number;
  editorTheme: string;
  autoSave: boolean;
  showHints: boolean;
}

export interface Question {
  id: number;
  category_id: number;
  category_name: 'leetcode' | 'ml_system_design';
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  description: string;
  constraints?: string;
  examples?: string;
  hints?: string;
  tags?: string;
  created_at: string;
}

export interface LeetCodeQuestion extends Question {
  function_signature_python?: string;
  function_signature_java?: string;
  function_signature_cpp?: string;
  test_cases: TestCase[];
  expected_time_complexity?: string;
  expected_space_complexity?: string;
  solution_python?: string;
  solution_java?: string;
  solution_cpp?: string;
  solution_explanation?: string;
}

export interface MLDesignQuestion extends Question {
  scenario: string;
  requirements: string[];
  evaluation_criteria: Record<string, string>;
  sample_solution?: string;
  key_components: string[];
}

export interface TestCase {
  input: any;
  expectedOutput: any;
  explanation?: string;
}

export interface TestResult {
  passed: boolean;
  input: any;
  expectedOutput: any;
  actualOutput: any;
  executionTime: number;
  error?: string;
}

export interface ExecutionResult {
  status: 'passed' | 'failed' | 'error' | 'timeout';
  testResults: TestResult[];
  executionTime: number;
  memoryUsed: number;
  errorMessage?: string;
}

export interface CodeSubmission {
  id: number;
  user_id: number;
  question_id: number;
  language: 'python' | 'java' | 'cpp';
  code: string;
  custom_test_cases?: string;
  submitted_at: string;
  execution_time_ms: number;
  memory_used_kb: number;
  test_results: string;
  status: 'passed' | 'failed' | 'error' | 'timeout';
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

export interface MockInterview {
  id: number;
  user_id: number;
  interview_type: 'leetcode' | 'ml_design';
  started_at: string;
  completed_at?: string;
  duration_seconds: number;
  status: 'in_progress' | 'completed' | 'abandoned';
}

export interface MockInterviewQuestion {
  id: number;
  mock_interview_id: number;
  question_id: number;
  order_index: number;
  submission_id?: number;
  submission_type?: 'code' | 'design';
  title: string;
  difficulty: string;
}

export interface Feedback {
  id: number;
  user_id: number;
  submission_id: number;
  submission_type: 'code' | 'design';
  mock_interview_id?: number;
  feedback_text: string;
  scores: FeedbackScores;
  strengths: string[];
  improvements: string[];
  generated_at: string;
  question_title?: string;
}

export interface FeedbackScores {
  correctness?: number;
  efficiency?: number;
  codeQuality?: number;
  problemUnderstanding?: number;
  systemDesign?: number;
  scalability?: number;
  communication?: number;
}

export interface UserProgress {
  id: number;
  user_id: number;
  question_id: number;
  attempts: number;
  solved: boolean;
  first_attempt_at: string;
  last_attempt_at: string;
  best_time_ms?: number;
  total_time_spent_seconds: number;
  title: string;
  difficulty: string;
  category: string;
}

export interface UserStats {
  total_attempts: number;
  solved_count: number;
  total_time_spent: number;
  byDifficulty: {
    difficulty: string;
    attempts: number;
    solved: number;
  }[];
}

// React Flow types for diagram editor
export interface DiagramNode {
  id: string;
  type: string;
  data: {
    label: string;
    [key: string]: any;
  };
  position: {
    x: number;
    y: number;
  };
}

export interface DiagramEdge {
  id: string;
  source: string;
  target: string;
  label?: string;
  type?: string;
}

export interface DiagramData {
  nodes: DiagramNode[];
  edges: DiagramEdge[];
}

// Timer state
export interface TimerState {
  isRunning: boolean;
  timeRemaining: number;
  startTime?: number;
}

// Store types (Zustand)
export interface AppStore {
  currentUser: User | null;
  setCurrentUser: (user: User | null) => void;
  
  preferences: UserPreferences;
  updatePreferences: (prefs: Partial<UserPreferences>) => void;
  
  currentQuestion: Question | null;
  setCurrentQuestion: (question: Question | null) => void;
  
  mockInterview: MockInterview | null;
  setMockInterview: (interview: MockInterview | null) => void;
  
  timerState: TimerState;
  startTimer: (duration: number) => void;
  pauseTimer: () => void;
  resetTimer: () => void;
}
