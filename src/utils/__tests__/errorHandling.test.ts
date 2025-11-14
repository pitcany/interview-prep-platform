import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import {
  classifyError,
  isRetryableError,
  getUserMessage,
  getRecoverySuggestions,
  logError,
  handleError,
  withErrorHandling,
  ErrorCategory,
  ErrorSeverity,
} from '../errorHandling';

describe('errorHandling', () => {
  let consoleErrorSpy: ReturnType<typeof vi.spyOn>;
  let consoleWarnSpy: ReturnType<typeof vi.spyOn>;
  let consoleInfoSpy: ReturnType<typeof vi.spyOn>;

  beforeEach(() => {
    consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
    consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    consoleInfoSpy = vi.spyOn(console, 'info').mockImplementation(() => {});
  });

  afterEach(() => {
    consoleErrorSpy.mockRestore();
    consoleWarnSpy.mockRestore();
    consoleInfoSpy.mockRestore();
  });

  describe('classifyError', () => {
    it('should classify network errors', () => {
      const errors = [
        new Error('fetch failed'),
        new Error('network error occurred'),
        new Error('ECONNREFUSED: connection refused'),
        new Error('connection timeout'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.NETWORK);
        expect(classified.severity).toBe(ErrorSeverity.HIGH);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('connect');
      });
    });

    it('should classify timeout errors', () => {
      const errors = [
        new Error('Request timeout'),
        new Error('ETIMEOUT'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.TIMEOUT);
        expect(classified.severity).toBe(ErrorSeverity.MEDIUM);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('too long');
      });
    });

    it('should classify IPC errors', () => {
      const errors = [
        new Error('IPC communication failed'),
        new Error('Electron API not available'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.IPC_ERROR);
        expect(classified.severity).toBe(ErrorSeverity.CRITICAL);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('Communication error');
      });
    });

    it('should classify validation errors', () => {
      const errors = [
        new Error('validation failed'),
        new Error('Email is invalid'),
        new Error('Field is required'),
        new Error('Value must be a number'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.VALIDATION);
        expect(classified.severity).toBe(ErrorSeverity.LOW);
        expect(classified.isRetryable).toBe(false);
      });
    });

    it('should classify authentication errors', () => {
      const errors = [
        new Error('authentication failed'),
        new Error('Invalid API key'),
        new Error('unauthorized access'),
        new Error('Invalid credentials'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.AUTHENTICATION);
        expect(classified.severity).toBe(ErrorSeverity.HIGH);
        expect(classified.isRetryable).toBe(false);
        expect(classified.userMessage).toContain('Authentication');
      });
    });

    it('should classify LLM errors', () => {
      const errors = [
        new Error('LLM API error'),
        new Error('Failed to generate feedback'),
        new Error('OpenAI service unavailable'),
        new Error('Claude API timeout'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.LLM_ERROR);
        expect(classified.severity).toBe(ErrorSeverity.MEDIUM);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('feedback');
      });
    });

    it('should classify code execution errors', () => {
      const errors = [
        new Error('Code execution failed'),
        new Error('Compilation error'),
        new Error('Runtime error in sandbox'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.CODE_EXECUTION);
        expect(classified.severity).toBe(ErrorSeverity.MEDIUM);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('execute code');
      });
    });

    it('should classify database errors', () => {
      const errors = [
        new Error('database connection failed'),
        new Error('SQLITE_ERROR: table not found'),
        new Error('SQL syntax error'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.DATABASE);
        expect(classified.severity).toBe(ErrorSeverity.HIGH);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('Database');
      });
    });

    it('should classify not found errors', () => {
      const errors = [
        new Error('Resource not found'),
        new Error('404 - Page not found'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.NOT_FOUND);
        expect(classified.severity).toBe(ErrorSeverity.LOW);
        expect(classified.isRetryable).toBe(false);
        expect(classified.userMessage).toContain('not found');
      });
    });

    it('should classify server errors', () => {
      const errors = [
        new Error('500 Internal Server Error'),
        new Error('502 Bad Gateway'),
        new Error('503 Service Unavailable'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.SERVER_ERROR);
        expect(classified.severity).toBe(ErrorSeverity.HIGH);
        expect(classified.isRetryable).toBe(true);
        expect(classified.userMessage).toContain('Server error');
      });
    });

    it('should classify unknown errors', () => {
      const error = new Error('Something went wrong');
      const classified = classifyError(error);

      expect(classified.category).toBe(ErrorCategory.UNKNOWN);
      expect(classified.severity).toBe(ErrorSeverity.MEDIUM);
      expect(classified.isRetryable).toBe(true);
      expect(classified.userMessage).toContain('unexpected');
      expect(classified.originalError).toBe(error);
    });

    it('should handle non-Error objects', () => {
      const classified = classifyError('string error');
      expect(classified.category).toBe(ErrorCategory.UNKNOWN);
      expect(classified.technicalMessage).toBe('string error');
    });

    it('should include recovery suggestions', () => {
      const error = new Error('network error');
      const classified = classifyError(error);

      expect(classified.recoverySuggestions).toBeInstanceOf(Array);
      expect(classified.recoverySuggestions.length).toBeGreaterThan(0);
      expect(classified.recoverySuggestions.some((s) => s.length > 0)).toBe(true);
    });
  });

  describe('isRetryableError', () => {
    it('should return true for retryable errors', () => {
      const retryableErrors = [
        new Error('network error'),
        new Error('timeout'),
        new Error('500 server error'),
        new Error('IPC communication failed'),
      ];

      retryableErrors.forEach((error) => {
        expect(isRetryableError(error)).toBe(true);
      });
    });

    it('should return false for non-retryable errors', () => {
      const nonRetryableErrors = [
        new Error('validation failed'),
        new Error('authentication required'),
        new Error('not found'),
      ];

      nonRetryableErrors.forEach((error) => {
        expect(isRetryableError(error)).toBe(false);
      });
    });
  });

  describe('getUserMessage', () => {
    it('should return user-friendly messages', () => {
      const error = new Error('ECONNREFUSED');
      const message = getUserMessage(error);

      expect(message).toBeTruthy();
      expect(message.length).toBeGreaterThan(0);
      expect(message).not.toContain('ECONNREFUSED'); // Should not expose technical details
    });

    it('should preserve validation messages as they are user-friendly', () => {
      const error = new Error('Email is invalid');
      const message = getUserMessage(error);

      expect(message).toBe('Email is invalid');
    });
  });

  describe('getRecoverySuggestions', () => {
    it('should return recovery suggestions array', () => {
      const error = new Error('network error');
      const suggestions = getRecoverySuggestions(error);

      expect(Array.isArray(suggestions)).toBe(true);
      expect(suggestions.length).toBeGreaterThan(0);
      expect(suggestions.every((s) => typeof s === 'string')).toBe(true);
    });

    it('should provide different suggestions for different error types', () => {
      const networkError = new Error('network error');
      const validationError = new Error('validation failed');

      const networkSuggestions = getRecoverySuggestions(networkError);
      const validationSuggestions = getRecoverySuggestions(validationError);

      expect(networkSuggestions).not.toEqual(validationSuggestions);
    });
  });

  describe('logError', () => {
    it('should log critical errors with console.error', () => {
      const error = new Error('IPC communication failed');
      logError(error, 'Test context');

      expect(consoleErrorSpy).toHaveBeenCalled();
      expect(consoleWarnSpy).not.toHaveBeenCalled();
      expect(consoleInfoSpy).not.toHaveBeenCalled();
    });

    it('should log medium severity errors with console.warn', () => {
      const error = new Error('LLM API failed');
      logError(error);

      expect(consoleWarnSpy).toHaveBeenCalled();
      expect(consoleErrorSpy).not.toHaveBeenCalled();
    });

    it('should log low severity errors with console.info', () => {
      const error = new Error('validation failed');
      logError(error);

      expect(consoleInfoSpy).toHaveBeenCalled();
      expect(consoleErrorSpy).not.toHaveBeenCalled();
    });

    it('should include context in log message', () => {
      const error = new Error('network error');
      logError(error, 'Fetching user data');

      expect(consoleErrorSpy).toHaveBeenCalled();
      const logCall = consoleErrorSpy.mock.calls[0][0] as string;
      expect(logCall).toContain('Fetching user data');
    });
  });

  describe('handleError', () => {
    it('should classify, log, and return error', () => {
      const error = new Error('network error');
      const classified = handleError(error, 'Test context');

      expect(classified.category).toBe(ErrorCategory.NETWORK);
      expect(consoleErrorSpy).toHaveBeenCalled();
    });

    it('should call onError callback if provided', () => {
      const error = new Error('network error');
      const onError = vi.fn();

      handleError(error, 'Test context', onError);

      expect(onError).toHaveBeenCalled();
      expect(onError.mock.calls[0][0].category).toBe(ErrorCategory.NETWORK);
    });

    it('should work without context or callback', () => {
      const error = new Error('test error');
      const classified = handleError(error);

      expect(classified).toBeDefined();
      expect(classified.category).toBeDefined();
    });
  });

  describe('withErrorHandling', () => {
    it('should wrap successful function execution', async () => {
      const fn = vi.fn().mockResolvedValue('success');
      const wrapped = withErrorHandling(fn, 'Test operation');

      const result = await wrapped('arg1', 'arg2');

      expect(result).toBe('success');
      expect(fn).toHaveBeenCalledWith('arg1', 'arg2');
      expect(consoleErrorSpy).not.toHaveBeenCalled();
    });

    it('should catch and handle errors', async () => {
      const error = new Error('network error');
      const fn = vi.fn().mockRejectedValue(error);
      const wrapped = withErrorHandling(fn, 'Test operation');

      await expect(wrapped()).rejects.toThrow();
      expect(consoleErrorSpy).toHaveBeenCalled();
    });

    it('should preserve function arguments', async () => {
      const fn = vi.fn().mockResolvedValue('result');
      const wrapped = withErrorHandling(fn);

      await wrapped(1, 'two', { three: 3 });

      expect(fn).toHaveBeenCalledWith(1, 'two', { three: 3 });
    });

    it('should log error context', async () => {
      const error = new Error('test error');
      const fn = vi.fn().mockRejectedValue(error);
      const wrapped = withErrorHandling(fn, 'Custom context');

      await expect(wrapped()).rejects.toThrow();

      const logCall = consoleWarnSpy.mock.calls[0][0] as string;
      expect(logCall).toContain('Custom context');
    });
  });

  describe('Error categorization edge cases', () => {
    it('should handle errors with multiple matching patterns', () => {
      // "network timeout" could match both network and timeout
      // Should prioritize network (first match)
      const error = new Error('network timeout error');
      const classified = classifyError(error);

      expect(classified.category).toBe(ErrorCategory.NETWORK);
    });

    it('should handle empty error messages', () => {
      const error = new Error('');
      const classified = classifyError(error);

      expect(classified.category).toBe(ErrorCategory.UNKNOWN);
      expect(classified.userMessage).toBeTruthy();
    });

    it('should handle null and undefined', () => {
      const classifiedNull = classifyError(null);
      const classifiedUndefined = classifyError(undefined);

      expect(classifiedNull.category).toBe(ErrorCategory.UNKNOWN);
      expect(classifiedUndefined.category).toBe(ErrorCategory.UNKNOWN);
    });

    it('should handle case insensitive matching', () => {
      const errors = [
        new Error('NETWORK ERROR'),
        new Error('Network Error'),
        new Error('network error'),
      ];

      errors.forEach((error) => {
        const classified = classifyError(error);
        expect(classified.category).toBe(ErrorCategory.NETWORK);
      });
    });
  });

  describe('Recovery suggestions specificity', () => {
    it('should provide LLM-specific recovery suggestions', () => {
      const error = new Error('LLM API failed');
      const classified = classifyError(error);

      expect(
        classified.recoverySuggestions.some((s) =>
          s.toLowerCase().includes('llm')
        )
      ).toBe(true);
    });

    it('should provide database-specific recovery suggestions', () => {
      const error = new Error('SQLITE_ERROR');
      const classified = classifyError(error);

      expect(
        classified.recoverySuggestions.some((s) =>
          s.toLowerCase().includes('database')
        )
      ).toBe(true);
    });

    it('should provide restart suggestions for critical errors', () => {
      const error = new Error('IPC communication failed');
      const classified = classifyError(error);

      expect(
        classified.recoverySuggestions.some((s) =>
          s.toLowerCase().includes('restart')
        )
      ).toBe(true);
    });
  });
});
