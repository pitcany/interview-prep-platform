import { describe, it, expect } from 'vitest';
import {
  validateUsername,
  validateEmail,
  validateCode,
  validateTestCaseJSON,
  validateExplanation,
  validateQuestionSelection,
  validateDuration,
  validateNumberRange,
  validateFileName,
  validateTestCases,
} from '../validation';

describe('validateUsername', () => {
  it('should accept valid usernames', () => {
    expect(validateUsername('john_doe')).toEqual({ isValid: true });
    expect(validateUsername('user123')).toEqual({ isValid: true });
    expect(validateUsername('JohnDoe')).toEqual({ isValid: true });
    expect(validateUsername('a'.repeat(30))).toEqual({ isValid: true });
  });

  it('should reject empty usernames', () => {
    expect(validateUsername('')).toEqual({
      isValid: false,
      error: 'Username is required',
    });
    expect(validateUsername('   ')).toEqual({
      isValid: false,
      error: 'Username is required',
    });
  });

  it('should reject usernames that are too short', () => {
    const result = validateUsername('ab');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('at least');
  });

  it('should reject usernames that are too long', () => {
    const result = validateUsername('a'.repeat(51));
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('cannot exceed');
  });

  it('should trim whitespace', () => {
    expect(validateUsername('  john_doe  ')).toEqual({ isValid: true });
  });
});

describe('validateEmail', () => {
  it('should accept valid email addresses', () => {
    expect(validateEmail('user@example.com')).toEqual({ isValid: true });
    expect(validateEmail('john.doe@company.co.uk')).toEqual({ isValid: true });
    expect(validateEmail('user+tag@example.com')).toEqual({ isValid: true });
    expect(validateEmail('user_123@sub.domain.com')).toEqual({ isValid: true });
  });

  it('should reject empty emails', () => {
    expect(validateEmail('')).toEqual({
      isValid: false,
      error: 'Email is required',
    });
    expect(validateEmail('   ')).toEqual({
      isValid: false,
      error: 'Email is required',
    });
  });

  it('should reject invalid email formats', () => {
    const invalidEmails = [
      'invalid',
      '@example.com',
      'user@',
      'user @example.com',
      'user@example',
      'user..name@example.com',
    ];

    invalidEmails.forEach((email) => {
      const result = validateEmail(email);
      expect(result.isValid).toBe(false);
      expect(result.error).toContain('valid email');
    });
  });

  it('should trim whitespace', () => {
    expect(validateEmail('  user@example.com  ')).toEqual({ isValid: true });
  });
});

describe('validateCode', () => {
  it('should accept valid code', () => {
    const code = 'def solution():\n    return True';
    expect(validateCode(code)).toEqual({ isValid: true });
  });

  it('should reject empty code', () => {
    expect(validateCode('')).toEqual({
      isValid: false,
      error: 'Code cannot be empty',
    });
    expect(validateCode('   \n\n  ')).toEqual({
      isValid: false,
      error: 'Code cannot be empty',
    });
  });

  it('should reject code that is too large', () => {
    // Create code larger than 100KB
    const largeCode = 'x = 1\n'.repeat(20000);
    const result = validateCode(largeCode);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('too large');
  });

  it('should accept code up to the limit', () => {
    // Create code just under 100KB
    const code = 'x = 1\n'.repeat(10000);
    expect(validateCode(code)).toEqual({ isValid: true });
  });
});

describe('validateTestCaseJSON', () => {
  it('should accept valid JSON', () => {
    expect(validateTestCaseJSON('{"key": "value"}')).toEqual({ isValid: true });
    expect(validateTestCaseJSON('[1, 2, 3]')).toEqual({ isValid: true });
    expect(validateTestCaseJSON('null')).toEqual({ isValid: true });
  });

  it('should reject empty strings', () => {
    const result = validateTestCaseJSON('');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('cannot be empty');
  });

  it('should reject invalid JSON', () => {
    const invalidJSON = [
      '{key: value}',
      '[1, 2, 3,]',
      'undefined',
      '{broken',
    ];

    invalidJSON.forEach((json) => {
      const result = validateTestCaseJSON(json);
      expect(result.isValid).toBe(false);
      expect(result.error).toContain('Invalid');
    });
  });

  it('should use custom field name in error message', () => {
    const result = validateTestCaseJSON('', 'Test Data');
    expect(result.error).toContain('Test Data');
  });
});

describe('validateExplanation', () => {
  it('should accept valid explanations', () => {
    const explanation = 'This is a detailed explanation that is long enough to meet the minimum requirements.';
    expect(validateExplanation(explanation)).toEqual({ isValid: true });
  });

  it('should reject empty explanations', () => {
    expect(validateExplanation('')).toEqual({
      isValid: false,
      error: 'Explanation is required',
    });
  });

  it('should reject explanations that are too short', () => {
    const result = validateExplanation('Too short');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('at least 50 characters');
  });

  it('should respect custom minimum length', () => {
    const shortText = 'Short';
    expect(validateExplanation(shortText, 10)).toEqual({
      isValid: false,
      error: 'Explanation must be at least 10 characters',
    });
    expect(validateExplanation(shortText, 3)).toEqual({ isValid: true });
  });
});

describe('validateQuestionSelection', () => {
  it('should accept correct number of selections', () => {
    expect(validateQuestionSelection(3, 3)).toEqual({ isValid: true });
    expect(validateQuestionSelection(1, 1)).toEqual({ isValid: true });
  });

  it('should reject zero selections', () => {
    const result = validateQuestionSelection(0, 3);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('at least one');
  });

  it('should reject too few selections', () => {
    const result = validateQuestionSelection(2, 3);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('select 3');
    expect(result.error).toContain('Currently selected: 2');
  });

  it('should reject too many selections', () => {
    const result = validateQuestionSelection(5, 3);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('exactly 3');
    expect(result.error).toContain('selected 5');
  });
});

describe('validateDuration', () => {
  it('should accept valid durations', () => {
    expect(validateDuration(30)).toEqual({ isValid: true });
    expect(validateDuration(60)).toEqual({ isValid: true });
    expect(validateDuration(5)).toEqual({ isValid: true });
    expect(validateDuration(120)).toEqual({ isValid: true });
  });

  it('should reject durations below minimum', () => {
    const result = validateDuration(3);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('at least 5 minutes');
  });

  it('should reject durations above maximum', () => {
    const result = validateDuration(150);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('cannot exceed 120 minutes');
  });

  it('should respect custom min and max', () => {
    expect(validateDuration(15, 10, 20)).toEqual({ isValid: true });
    expect(validateDuration(5, 10, 20).isValid).toBe(false);
    expect(validateDuration(25, 10, 20).isValid).toBe(false);
  });
});

describe('validateNumberRange', () => {
  it('should accept numbers within range', () => {
    expect(validateNumberRange(5, 1, 10)).toEqual({ isValid: true });
    expect(validateNumberRange(1, 1, 10)).toEqual({ isValid: true });
    expect(validateNumberRange(10, 1, 10)).toEqual({ isValid: true });
  });

  it('should reject numbers below minimum', () => {
    const result = validateNumberRange(0, 1, 10);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('between 1 and 10');
  });

  it('should reject numbers above maximum', () => {
    const result = validateNumberRange(11, 1, 10);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('between 1 and 10');
  });

  it('should use custom field name in error message', () => {
    const result = validateNumberRange(100, 1, 10, 'Age');
    expect(result.error).toContain('Age must be between');
  });
});

describe('validateFileName', () => {
  it('should accept valid file names', () => {
    expect(validateFileName('document.txt')).toEqual({ isValid: true });
    expect(validateFileName('my-file_123.pdf')).toEqual({ isValid: true });
    expect(validateFileName('file.with.dots.txt')).toEqual({ isValid: true });
  });

  it('should reject empty file names', () => {
    expect(validateFileName('')).toEqual({
      isValid: false,
      error: 'File name is required',
    });
  });

  it('should reject file names with invalid characters', () => {
    const invalidNames = [
      'file<name>.txt',
      'file>name.txt',
      'file:name.txt',
      'file"name.txt',
      'file/name.txt',
      'file\\name.txt',
      'file|name.txt',
      'file?name.txt',
      'file*name.txt',
    ];

    invalidNames.forEach((name) => {
      const result = validateFileName(name);
      expect(result.isValid).toBe(false);
      expect(result.error).toContain('invalid characters');
    });
  });

  it('should reject file names that are too long', () => {
    const longName = 'a'.repeat(256) + '.txt';
    const result = validateFileName(longName);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('too long');
  });
});

describe('validateTestCases', () => {
  it('should accept valid test cases', () => {
    const validCases = JSON.stringify([
      { input: [1, 2, 3], expectedOutput: 6 },
      { input: [4, 5], expectedOutput: 9 },
    ]);
    expect(validateTestCases(validCases)).toEqual({ isValid: true });
  });

  it('should reject empty test cases', () => {
    expect(validateTestCases('')).toEqual({
      isValid: false,
      error: 'Test cases cannot be empty',
    });
  });

  it('should reject test cases that are too large', () => {
    // Create test cases larger than 1MB
    const largeCases = JSON.stringify(
      Array(50000).fill({ input: 'x'.repeat(50), expectedOutput: 'y'.repeat(50) })
    );
    const result = validateTestCases(largeCases);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('too large');
  });

  it('should reject invalid JSON', () => {
    const result = validateTestCases('{broken json}');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('Invalid JSON');
  });

  it('should reject non-array test cases', () => {
    const result = validateTestCases('{"not": "an array"}');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('must be an array');
  });

  it('should reject empty array', () => {
    const result = validateTestCases('[]');
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('At least one test case');
  });

  it('should reject too many test cases', () => {
    const manyCases = JSON.stringify(
      Array(101).fill({ input: 1, expectedOutput: 2 })
    );
    const result = validateTestCases(manyCases);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('Too many test cases');
  });

  it('should reject test cases with invalid structure', () => {
    const invalidCases = [
      JSON.stringify([null]),
      JSON.stringify(['string']),
      JSON.stringify([123]),
      JSON.stringify([{ onlyInput: 1 }]),
      JSON.stringify([{ onlyExpected: 2 }]),
      JSON.stringify([{ input: 1, wrong: 2 }]),
    ];

    invalidCases.forEach((testCase, index) => {
      const result = validateTestCases(testCase);
      expect(result.isValid).toBe(false);
      expect(result.error).toContain('Test case 1');
    });
  });

  it('should validate each test case in array', () => {
    const cases = JSON.stringify([
      { input: 1, expectedOutput: 2 },
      { input: 3 }, // Missing expectedOutput
      { input: 5, expectedOutput: 6 },
    ]);
    const result = validateTestCases(cases);
    expect(result.isValid).toBe(false);
    expect(result.error).toContain('Test case 2');
  });

  it('should accept test cases with both input and expectedOutput', () => {
    const validCases = JSON.stringify([
      { input: [2, 7, 11, 15], expectedOutput: [0, 1] },
      { input: [3, 2, 4], expectedOutput: [1, 2] },
    ]);
    expect(validateTestCases(validCases)).toEqual({ isValid: true });
  });
});
