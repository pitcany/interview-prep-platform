/**
 * Application Constants
 * Centralized constants to avoid magic numbers and improve code maintainability
 */

// ============================================
// Time Constants (in milliseconds)
// ============================================
export const TIME = {
  /** Mock interview duration: 30 minutes */
  MOCK_INTERVIEW_DURATION: 30 * 60 * 1000,

  /** Code execution timeout: 10 seconds */
  CODE_EXECUTION_TIMEOUT: 10 * 1000,

  /** Toast notification duration: 5 seconds */
  TOAST_DURATION: 5000,

  /** Auto-save debounce delay: 2 seconds */
  AUTO_SAVE_DELAY: 2000,
} as const;

// ============================================
// Limits & Thresholds
// ============================================
export const LIMITS = {
  /** Maximum code size: 100KB */
  MAX_CODE_SIZE: 100 * 1024,

  /** Maximum test cases per question */
  MAX_TEST_CASES: 50,

  /** Recent feedback items to show */
  RECENT_FEEDBACK_LIMIT: 10,

  /** Recent submissions to show */
  RECENT_SUBMISSIONS_LIMIT: 20,

  /** Maximum hints per question */
  MAX_HINTS: 10,

  /** Memory limit for code execution: 512MB */
  CODE_EXECUTION_MEMORY_MB: 512,
} as const;

// ============================================
// Question Configuration
// ============================================
export const QUESTION = {
  /** Number of LeetCode questions in mock interview */
  LEETCODE_MOCK_COUNT: 2,

  /** Number of ML Design questions in mock interview */
  ML_DESIGN_MOCK_COUNT: 1,

  /** Default difficulty for LeetCode mock interviews */
  DEFAULT_MOCK_DIFFICULTY: 'medium' as const,
} as const;

// ============================================
// UI Configuration
// ============================================
export const UI = {
  /** Default editor font size */
  DEFAULT_EDITOR_FONT_SIZE: 14,

  /** Minimum editor font size */
  MIN_EDITOR_FONT_SIZE: 10,

  /** Maximum editor font size */
  MAX_EDITOR_FONT_SIZE: 24,

  /** Code editor themes */
  EDITOR_THEMES: {
    DARK: 'vs-dark',
    LIGHT: 'vs-light',
    HIGH_CONTRAST: 'hc-black',
  },

  /** Chart colors */
  COLORS: {
    EASY: '#22c55e',
    MEDIUM: '#eab308',
    HARD: '#ef4444',
    SOLVED: '#3b82f6',
    ATTEMPTED: '#6b7280',
    SUCCESS: '#10b981',
    ERROR: '#ef4444',
    WARNING: '#f59e0b',
    INFO: '#3b82f6',
  },
} as const;

// ============================================
// API & Network
// ============================================
export const NETWORK = {
  /** Number of retries for failed IPC calls */
  IPC_MAX_RETRIES: 3,

  /** Retry delay multiplier (exponential backoff) */
  IPC_RETRY_DELAY_MS: 1000,

  /** Request timeout for API calls */
  API_TIMEOUT_MS: 30000,
} as const;

// ============================================
// Validation
// ============================================
export const VALIDATION = {
  /** Minimum username length */
  MIN_USERNAME_LENGTH: 3,

  /** Maximum username length */
  MAX_USERNAME_LENGTH: 50,

  /** Email regex pattern */
  EMAIL_REGEX: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,

  /** Minimum password length (if passwords are added later) */
  MIN_PASSWORD_LENGTH: 8,
} as const;

// ============================================
// Storage Keys
// ============================================
export const STORAGE_KEYS = {
  CURRENT_USER: 'current_user',
  PREFERENCES: 'user_preferences',
  LAST_QUESTION: 'last_question',
  DRAFT_CODE: 'draft_code',
} as const;

// ============================================
// Supported Languages
// ============================================
export const LANGUAGES = {
  PYTHON: 'python',
  JAVA: 'java',
  CPP: 'cpp',
} as const;

export const LANGUAGE_DISPLAY_NAMES = {
  [LANGUAGES.PYTHON]: 'Python',
  [LANGUAGES.JAVA]: 'Java',
  [LANGUAGES.CPP]: 'C++',
} as const;

// ============================================
// File Extensions
// ============================================
export const FILE_EXTENSIONS = {
  [LANGUAGES.PYTHON]: '.py',
  [LANGUAGES.JAVA]: '.java',
  [LANGUAGES.CPP]: '.cpp',
} as const;

// ============================================
// Error Messages
// ============================================
export const ERROR_MESSAGES = {
  NETWORK_ERROR: 'Network error. Please check your connection and try again.',
  IPC_TIMEOUT: 'Request timed out. Please try again.',
  CODE_TOO_LARGE: `Code exceeds maximum size of ${LIMITS.MAX_CODE_SIZE / 1024}KB`,
  EMPTY_CODE: 'Code cannot be empty',
  INVALID_EMAIL: 'Please enter a valid email address',
  USERNAME_TOO_SHORT: `Username must be at least ${VALIDATION.MIN_USERNAME_LENGTH} characters`,
  USERNAME_TOO_LONG: `Username cannot exceed ${VALIDATION.MAX_USERNAME_LENGTH} characters`,
  SELECT_QUESTION: 'Please select a question first',
  NO_USER_SELECTED: 'Please log in first',
} as const;

// ============================================
// Success Messages
// ============================================
export const SUCCESS_MESSAGES = {
  CODE_SUBMITTED: 'Code submitted successfully',
  DESIGN_SUBMITTED: 'Design submitted successfully',
  PROGRESS_RESET: 'Progress reset successfully',
  TEST_CASE_ADDED: 'Test case added successfully',
  FEEDBACK_GENERATED: 'Feedback generated successfully',
  USER_CREATED: 'User created successfully',
  PREFERENCES_SAVED: 'Preferences saved successfully',
} as const;
