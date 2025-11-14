/**
 * Backend Retry Utility
 * Implements exponential backoff retry logic for backend services (LLM APIs, etc.)
 */

export interface RetryOptions {
  maxRetries?: number;
  baseDelay?: number;
  maxDelay?: number;
  shouldRetry?: (error: Error) => boolean;
}

/**
 * Default retry predicate - retry on network and timeout errors
 */
const defaultShouldRetry = (error: Error): boolean => {
  const message = error.message.toLowerCase();
  return (
    message.includes('timeout') ||
    message.includes('network') ||
    message.includes('fetch failed') ||
    message.includes('econnrefused') ||
    message.includes('etimedout') ||
    message.includes('503') ||
    message.includes('502') ||
    message.includes('429') || // Rate limit
    message.includes('connection')
  );
};

/**
 * Retry a function with exponential backoff
 * @param fn Function to retry
 * @param options Retry configuration
 * @returns Result of the function
 */
export async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {}
): Promise<T> {
  const {
    maxRetries = 3,
    baseDelay = 1000,
    maxDelay = 10000,
    shouldRetry = defaultShouldRetry,
  } = options;

  let lastError: Error;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;

      // Don't retry if we've exhausted all attempts
      if (attempt === maxRetries) {
        break;
      }

      // Don't retry if the error is not retryable
      if (!shouldRetry(lastError)) {
        throw lastError;
      }

      // Calculate exponential backoff delay with jitter
      const exponentialDelay = Math.min(baseDelay * Math.pow(2, attempt), maxDelay);
      const jitter = Math.random() * 0.3 * exponentialDelay; // Add up to 30% jitter
      const delay = exponentialDelay + jitter;

      // Log retry attempt
      console.warn(
        `[Retry] Attempt ${attempt + 1}/${maxRetries + 1} failed: ${lastError.message}. ` +
        `Retrying in ${Math.round(delay)}ms...`
      );

      // Wait before retrying
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }

  // All retries exhausted
  throw new Error(
    `Operation failed after ${maxRetries + 1} attempts. Last error: ${lastError!.message}`
  );
}

/**
 * Wrap an async function with retry logic
 * @param fn Function to wrap
 * @param options Retry configuration
 * @returns Wrapped function with retry logic
 */
export function withRetry<TArgs extends any[], TReturn>(
  fn: (...args: TArgs) => Promise<TReturn>,
  options?: RetryOptions
): (...args: TArgs) => Promise<TReturn> {
  return async (...args: TArgs): Promise<TReturn> => {
    return retryWithBackoff(() => fn(...args), options);
  };
}
