/**
 * IPC Retry Utility
 * Implements exponential backoff retry logic for IPC calls
 */

import { NETWORK } from '../constants';

export interface RetryOptions {
  maxRetries?: number;
  baseDelay?: number;
  maxDelay?: number;
  shouldRetry?: (error: Error) => boolean;
}

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
    maxRetries = NETWORK.IPC_MAX_RETRIES,
    baseDelay = NETWORK.IPC_RETRY_DELAY_MS,
    maxDelay = 10000,
    shouldRetry = (error: Error) => {
      // Retry on network errors, timeouts, and IPC communication errors
      return (
        error.message.includes('timeout') ||
        error.message.includes('network') ||
        error.message.includes('IPC') ||
        error.message.includes('communication')
      );
    },
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

      // Calculate exponential backoff delay
      const delay = Math.min(baseDelay * Math.pow(2, attempt), maxDelay);

      // Log retry attempt (useful for debugging)
      console.warn(
        `IPC call failed (attempt ${attempt + 1}/${maxRetries + 1}): ${lastError.message}. ` +
        `Retrying in ${delay}ms...`
      );

      // Wait before retrying
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }

  // All retries exhausted
  throw new Error(
    `IPC call failed after ${maxRetries + 1} attempts: ${lastError!.message}`
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
