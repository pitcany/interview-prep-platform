/**
 * Input Validation Utilities
 * Centralized validation functions with clear error messages
 */

import { VALIDATION, LIMITS, ERROR_MESSAGES } from '../constants';

export interface ValidationResult {
  isValid: boolean;
  error?: string;
}

/**
 * Validate username format and length
 */
export function validateUsername(username: string): ValidationResult {
  if (!username || username.trim().length === 0) {
    return { isValid: false, error: 'Username is required' };
  }

  const trimmed = username.trim();

  if (trimmed.length < VALIDATION.MIN_USERNAME_LENGTH) {
    return { isValid: false, error: ERROR_MESSAGES.USERNAME_TOO_SHORT };
  }

  if (trimmed.length > VALIDATION.MAX_USERNAME_LENGTH) {
    return { isValid: false, error: ERROR_MESSAGES.USERNAME_TOO_LONG };
  }

  return { isValid: true };
}

/**
 * Validate email format
 */
export function validateEmail(email: string): ValidationResult {
  if (!email || email.trim().length === 0) {
    return { isValid: false, error: 'Email is required' };
  }

  if (!VALIDATION.EMAIL_REGEX.test(email.trim())) {
    return { isValid: false, error: ERROR_MESSAGES.INVALID_EMAIL };
  }

  return { isValid: true };
}

/**
 * Validate code content and size
 */
export function validateCode(code: string): ValidationResult {
  if (!code || code.trim().length === 0) {
    return { isValid: false, error: ERROR_MESSAGES.EMPTY_CODE };
  }

  const sizeInBytes = new Blob([code]).size;
  if (sizeInBytes > LIMITS.MAX_CODE_SIZE) {
    return { isValid: false, error: ERROR_MESSAGES.CODE_TOO_LARGE };
  }

  return { isValid: true };
}

/**
 * Validate test case JSON format
 */
export function validateTestCaseJSON(jsonString: string, fieldName: string = 'JSON'): ValidationResult {
  if (!jsonString || jsonString.trim().length === 0) {
    return { isValid: false, error: `${fieldName} cannot be empty` };
  }

  try {
    JSON.parse(jsonString);
    return { isValid: true };
  } catch (error) {
    return { isValid: false, error: `Invalid ${fieldName} format. Please check your input.` };
  }
}

/**
 * Validate diagram explanation text
 */
export function validateExplanation(text: string, minLength: number = 50): ValidationResult {
  if (!text || text.trim().length === 0) {
    return { isValid: false, error: 'Explanation is required' };
  }

  if (text.trim().length < minLength) {
    return { isValid: false, error: `Explanation must be at least ${minLength} characters` };
  }

  return { isValid: true };
}

/**
 * Validate question selection for mock interviews
 */
export function validateQuestionSelection(
  selectedCount: number,
  requiredCount: number
): ValidationResult {
  if (selectedCount === 0) {
    return { isValid: false, error: 'Please select at least one question' };
  }

  if (selectedCount < requiredCount) {
    return {
      isValid: false,
      error: `Please select ${requiredCount} question(s). Currently selected: ${selectedCount}`,
    };
  }

  if (selectedCount > requiredCount) {
    return {
      isValid: false,
      error: `Please select exactly ${requiredCount} question(s). You have selected ${selectedCount}`,
    };
  }

  return { isValid: true };
}

/**
 * Validate duration (in minutes)
 */
export function validateDuration(duration: number, min: number = 5, max: number = 120): ValidationResult {
  if (duration < min) {
    return { isValid: false, error: `Duration must be at least ${min} minutes` };
  }

  if (duration > max) {
    return { isValid: false, error: `Duration cannot exceed ${max} minutes` };
  }

  return { isValid: true };
}

/**
 * Validate number is within range
 */
export function validateNumberRange(
  value: number,
  min: number,
  max: number,
  fieldName: string = 'Value'
): ValidationResult {
  if (value < min || value > max) {
    return { isValid: false, error: `${fieldName} must be between ${min} and ${max}` };
  }

  return { isValid: true };
}

/**
 * Sanitize user input (basic XSS prevention)
 */
export function sanitizeInput(input: string): string {
  return input
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;')
    .replace(/\//g, '&#x2F;');
}

/**
 * Validate file name (for diagram exports, etc.)
 */
export function validateFileName(fileName: string): ValidationResult {
  if (!fileName || fileName.trim().length === 0) {
    return { isValid: false, error: 'File name is required' };
  }

  // Check for invalid characters
  const invalidChars = /[<>:"/\\|?*\x00-\x1F]/g;
  if (invalidChars.test(fileName)) {
    return { isValid: false, error: 'File name contains invalid characters' };
  }

  if (fileName.length > 255) {
    return { isValid: false, error: 'File name is too long (max 255 characters)' };
  }

  return { isValid: true };
}

/**
 * Validate test case data structure and size
 */
export function validateTestCases(testCasesStr: string): ValidationResult {
  if (!testCasesStr || testCasesStr.trim().length === 0) {
    return { isValid: false, error: 'Test cases cannot be empty' };
  }

  // Check size before parsing
  const sizeInBytes = new Blob([testCasesStr]).size;
  if (sizeInBytes > 1024 * 1024) { // 1MB limit
    return { isValid: false, error: 'Test cases data is too large (max 1MB)' };
  }

  let testCases: any;
  try {
    testCases = JSON.parse(testCasesStr);
  } catch (error) {
    return { isValid: false, error: 'Invalid JSON format for test cases' };
  }

  if (!Array.isArray(testCases)) {
    return { isValid: false, error: 'Test cases must be an array' };
  }

  if (testCases.length === 0) {
    return { isValid: false, error: 'At least one test case is required' };
  }

  if (testCases.length > 100) {
    return { isValid: false, error: 'Too many test cases (max 100)' };
  }

  // Validate structure of each test case
  for (let i = 0; i < testCases.length; i++) {
    const testCase = testCases[i];
    if (!testCase || typeof testCase !== 'object') {
      return { isValid: false, error: `Test case ${i + 1} is invalid` };
    }
    // Accept either 'expected' or 'expectedOutput' field names
    const hasInput = 'input' in testCase;
    const hasExpected = 'expected' in testCase || 'expectedOutput' in testCase;
    if (!hasInput || !hasExpected) {
      return { isValid: false, error: `Test case ${i + 1} must have 'input' and 'expected'/'expectedOutput' fields` };
    }
  }

  return { isValid: true };
}
