/**
 * Error Handling Utilities
 * Provides standardized error classification, user-friendly messages, and recovery strategies
 */

import { ERROR_MESSAGES } from '../constants';

/**
 * Error categories for classification and handling
 */
export enum ErrorCategory {
  NETWORK = 'network',
  TIMEOUT = 'timeout',
  VALIDATION = 'validation',
  AUTHENTICATION = 'authentication',
  AUTHORIZATION = 'authorization',
  NOT_FOUND = 'not_found',
  SERVER_ERROR = 'server_error',
  LLM_ERROR = 'llm_error',
  CODE_EXECUTION = 'code_execution',
  DATABASE = 'database',
  IPC_ERROR = 'ipc_error',
  UNKNOWN = 'unknown',
}

/**
 * Error severity levels
 */
export enum ErrorSeverity {
  LOW = 'low',       // User can continue, minimal impact
  MEDIUM = 'medium', // Feature degraded but app functional
  HIGH = 'high',     // Feature unavailable
  CRITICAL = 'critical', // App unusable
}

/**
 * Classified error with user-friendly information
 */
export interface ClassifiedError {
  category: ErrorCategory;
  severity: ErrorSeverity;
  userMessage: string;
  technicalMessage: string;
  isRetryable: boolean;
  recoverySuggestions: string[];
  originalError?: Error;
}

/**
 * Classify an error and provide user-friendly information
 */
export function classifyError(error: unknown): ClassifiedError {
  const err = error as Error;
  const message = err?.message || String(error);

  // Network errors
  if (
    message.includes('fetch failed') ||
    message.includes('network') ||
    message.includes('ECONNREFUSED') ||
    message.includes('ETIMEDOUT') ||
    message.includes('connection')
  ) {
    return {
      category: ErrorCategory.NETWORK,
      severity: ErrorSeverity.HIGH,
      userMessage: 'Unable to connect. Please check your network connection and try again.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Check your internet connection',
        'Verify the service is running (e.g., Local LLM server)',
        'Check firewall settings',
        'Try again in a few moments',
      ],
      originalError: err,
    };
  }

  // Timeout errors
  if (message.includes('timeout') || message.includes('ETIMEOUT')) {
    return {
      category: ErrorCategory.TIMEOUT,
      severity: ErrorSeverity.MEDIUM,
      userMessage: 'The request took too long. Please try again.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Try again with a simpler request',
        'Check if the service is overloaded',
        'Wait a moment and retry',
      ],
      originalError: err,
    };
  }

  // IPC communication errors
  if (
    message.includes('IPC') ||
    message.includes('Electron API not available') ||
    message.includes('communication')
  ) {
    return {
      category: ErrorCategory.IPC_ERROR,
      severity: ErrorSeverity.CRITICAL,
      userMessage: 'Communication error with the application. Please restart.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Restart the application',
        'Check if the app is running in Electron',
        'Contact support if the issue persists',
      ],
      originalError: err,
    };
  }

  // Validation errors
  if (
    message.includes('validation') ||
    message.includes('invalid') ||
    message.includes('must be') ||
    message.includes('required')
  ) {
    return {
      category: ErrorCategory.VALIDATION,
      severity: ErrorSeverity.LOW,
      userMessage: message, // Validation messages are already user-friendly
      technicalMessage: message,
      isRetryable: false,
      recoverySuggestions: [
        'Check your input and try again',
        'Ensure all required fields are filled',
        'Verify the format of your data',
      ],
      originalError: err,
    };
  }

  // Authentication errors
  if (
    message.includes('authentication') ||
    message.includes('unauthorized') ||
    message.includes('API key') ||
    message.includes('credentials')
  ) {
    return {
      category: ErrorCategory.AUTHENTICATION,
      severity: ErrorSeverity.HIGH,
      userMessage: 'Authentication failed. Please check your credentials.',
      technicalMessage: message,
      isRetryable: false,
      recoverySuggestions: [
        'Verify your API keys in environment variables',
        'Check that credentials are correctly configured',
        'Ensure the API key is valid and not expired',
      ],
      originalError: err,
    };
  }

  // LLM-specific errors
  if (
    message.includes('LLM') ||
    message.includes('feedback') ||
    message.includes('model') ||
    message.includes('openai') ||
    message.includes('claude')
  ) {
    return {
      category: ErrorCategory.LLM_ERROR,
      severity: ErrorSeverity.MEDIUM,
      userMessage: 'Unable to generate AI feedback. You can continue without feedback.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Try generating feedback again',
        'Check if your LLM service is running',
        'Verify API configuration in .env file',
        'Continue practicing without AI feedback',
      ],
      originalError: err,
    };
  }

  // Code execution errors
  if (
    message.includes('execution') ||
    message.includes('compile') ||
    message.includes('runtime') ||
    message.includes('sandbox')
  ) {
    return {
      category: ErrorCategory.CODE_EXECUTION,
      severity: ErrorSeverity.MEDIUM,
      userMessage: 'Unable to execute code. Please check your code for errors.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Check your code for syntax errors',
        'Verify the code compiles in your language',
        'Try running with simpler test cases',
        'Restart the application if the issue persists',
      ],
      originalError: err,
    };
  }

  // Database errors
  if (
    message.includes('database') ||
    message.includes('SQLITE') ||
    message.includes('SQL')
  ) {
    return {
      category: ErrorCategory.DATABASE,
      severity: ErrorSeverity.HIGH,
      userMessage: 'Database error. Your data may not be saved.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Restart the application',
        'Check if the database file is accessible',
        'Verify disk space is available',
        'Run database initialization: npm run db:setup',
      ],
      originalError: err,
    };
  }

  // Not found errors
  if (message.includes('not found') || message.includes('404')) {
    return {
      category: ErrorCategory.NOT_FOUND,
      severity: ErrorSeverity.LOW,
      userMessage: 'The requested item was not found.',
      technicalMessage: message,
      isRetryable: false,
      recoverySuggestions: [
        'Verify the item exists',
        'Refresh the page',
        'Check if the item was deleted',
      ],
      originalError: err,
    };
  }

  // Server errors (5xx)
  if (
    message.includes('500') ||
    message.includes('502') ||
    message.includes('503') ||
    message.includes('server error')
  ) {
    return {
      category: ErrorCategory.SERVER_ERROR,
      severity: ErrorSeverity.HIGH,
      userMessage: 'Server error. Please try again later.',
      technicalMessage: message,
      isRetryable: true,
      recoverySuggestions: [
        'Wait a few moments and try again',
        'Check if the service is experiencing issues',
        'Contact support if the problem persists',
      ],
      originalError: err,
    };
  }

  // Unknown errors
  return {
    category: ErrorCategory.UNKNOWN,
    severity: ErrorSeverity.MEDIUM,
    userMessage: 'An unexpected error occurred. Please try again.',
    technicalMessage: message,
    isRetryable: true,
    recoverySuggestions: [
      'Try the operation again',
      'Restart the application',
      'Check the developer console for details',
      'Contact support if the issue persists',
    ],
    originalError: err,
  };
}

/**
 * Check if an error should be retried
 */
export function isRetryableError(error: unknown): boolean {
  const classified = classifyError(error);
  return classified.isRetryable;
}

/**
 * Get a user-friendly error message
 */
export function getUserMessage(error: unknown): string {
  const classified = classifyError(error);
  return classified.userMessage;
}

/**
 * Get recovery suggestions for an error
 */
export function getRecoverySuggestions(error: unknown): string[] {
  const classified = classifyError(error);
  return classified.recoverySuggestions;
}

/**
 * Log error with appropriate severity
 */
export function logError(
  error: unknown,
  context?: string
): void {
  const classified = classifyError(error);

  const logMessage = [
    `[${classified.severity.toUpperCase()}] ${classified.category}`,
    context ? `Context: ${context}` : null,
    `User Message: ${classified.userMessage}`,
    `Technical: ${classified.technicalMessage}`,
    `Retryable: ${classified.isRetryable}`,
  ]
    .filter(Boolean)
    .join('\n  ');

  switch (classified.severity) {
    case ErrorSeverity.CRITICAL:
    case ErrorSeverity.HIGH:
      console.error(logMessage, classified.originalError);
      break;
    case ErrorSeverity.MEDIUM:
      console.warn(logMessage, classified.originalError);
      break;
    case ErrorSeverity.LOW:
      console.info(logMessage);
      break;
  }
}

/**
 * Handle error with automatic classification and logging
 */
export function handleError(
  error: unknown,
  context?: string,
  onError?: (classified: ClassifiedError) => void
): ClassifiedError {
  const classified = classifyError(error);
  logError(error, context);

  if (onError) {
    onError(classified);
  }

  return classified;
}

/**
 * Wrap async function with error handling
 */
export function withErrorHandling<TArgs extends any[], TReturn>(
  fn: (...args: TArgs) => Promise<TReturn>,
  context?: string
): (...args: TArgs) => Promise<TReturn> {
  return async (...args: TArgs): Promise<TReturn> => {
    try {
      return await fn(...args);
    } catch (error) {
      const classified = handleError(error, context);
      throw classified.originalError || error;
    }
  };
}
