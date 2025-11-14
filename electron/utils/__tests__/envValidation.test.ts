import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { validateEnvironmentVariables, validateOrThrow, getValidationReport } from '../envValidation';

describe('Environment Variable Validation', () => {
  const originalEnv = process.env;

  beforeEach(() => {
    // Reset process.env before each test
    process.env = { ...originalEnv };
  });

  afterEach(() => {
    // Restore original env after each test
    process.env = originalEnv;
  });

  describe('validateEnvironmentVariables', () => {
    it('should pass with no LLM provider configured (warnings only)', () => {
      process.env = {};
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.errors).toHaveLength(0);
      expect(result.warnings.length).toBeGreaterThan(0);
      expect(result.warnings[0]).toContain('No LLM provider configured');
    });

    it('should validate Claude API key format', () => {
      process.env.CLAUDE_API_KEY = 'invalid-key';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'CLAUDE_API_KEY')).toBe(true);
      expect(result.errors.find(e => e.variable === 'CLAUDE_API_KEY')?.error).toContain('sk-ant-');
    });

    it('should accept valid Claude API key', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-' + 'x'.repeat(20);
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });

    it('should validate OpenAI API key format', () => {
      process.env.OPENAI_API_KEY = 'invalid-key';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'OPENAI_API_KEY')).toBe(true);
    });

    it('should accept valid OpenAI API key', () => {
      process.env.OPENAI_API_KEY = 'sk-' + 'x'.repeat(25);
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
    });

    it('should validate LLM_BASE_URL format', () => {
      process.env.LLM_BASE_URL = 'not-a-url';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'LLM_BASE_URL')).toBe(true);
      expect(result.errors.find(e => e.variable === 'LLM_BASE_URL')?.error).toContain('valid HTTP');
    });

    it('should accept valid LLM_BASE_URL', () => {
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.warnings.some(w => w.includes('LLM_MODEL'))).toBe(true);
    });

    it('should accept HTTPS URLs for LLM_BASE_URL', () => {
      process.env.LLM_BASE_URL = 'https://api.example.com';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
    });

    it('should validate LLM_PROVIDER values', () => {
      process.env.LLM_PROVIDER = 'invalid-provider';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'LLM_PROVIDER')).toBe(true);
    });

    it('should accept valid LLM_PROVIDER values', () => {
      const validProviders = ['claude', 'openai', 'local'];
      validProviders.forEach(provider => {
        process.env = { LLM_PROVIDER: provider };
        if (provider === 'claude') {
          process.env.CLAUDE_API_KEY = 'sk-ant-' + 'x'.repeat(20);
        } else if (provider === 'openai') {
          process.env.OPENAI_API_KEY = 'sk-' + 'x'.repeat(25);
        } else {
          process.env.LLM_BASE_URL = 'http://localhost:8000';
        }
        const result = validateEnvironmentVariables();
        expect(result.isValid).toBe(true);
      });
    });

    it('should require appropriate env vars for LLM_PROVIDER', () => {
      process.env.LLM_PROVIDER = 'claude';
      // No CLAUDE_API_KEY set
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'CLAUDE_API_KEY')).toBe(true);
    });

    it('should validate SANDBOX_MODE values', () => {
      process.env.SANDBOX_MODE = 'invalid';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.some(e => e.variable === 'SANDBOX_MODE')).toBe(true);
    });

    it('should accept valid SANDBOX_MODE values', () => {
      ['local', 'docker'].forEach(mode => {
        process.env = { SANDBOX_MODE: mode };
        const result = validateEnvironmentVariables();
        expect(result.isValid).toBe(true);
      });
    });

    it('should warn about docker mode not being fully implemented', () => {
      process.env.SANDBOX_MODE = 'docker';
      const result = validateEnvironmentVariables();
      expect(result.warnings.some(w => w.includes('docker'))).toBe(true);
    });

    it('should validate MAX_EXECUTION_TIME range', () => {
      const invalidTimes = ['500', '70000', 'abc', ''];
      invalidTimes.forEach(time => {
        process.env = { MAX_EXECUTION_TIME: time };
        const result = validateEnvironmentVariables();
        if (time && !isNaN(Number(time))) {
          expect(result.isValid).toBe(false);
        }
      });
    });

    it('should accept valid MAX_EXECUTION_TIME', () => {
      ['5000', '10000', '30000'].forEach(time => {
        process.env = { MAX_EXECUTION_TIME: time };
        const result = validateEnvironmentVariables();
        expect(result.isValid).toBe(true);
      });
    });

    it('should validate MAX_MEMORY range', () => {
      const invalidMemory = ['50', '3000', 'abc'];
      invalidMemory.forEach(mem => {
        process.env = { MAX_MEMORY: mem };
        const result = validateEnvironmentVariables();
        if (!isNaN(Number(mem))) {
          expect(result.isValid).toBe(false);
        }
      });
    });

    it('should accept valid MAX_MEMORY', () => {
      ['256', '512', '1024'].forEach(mem => {
        process.env = { MAX_MEMORY: mem };
        const result = validateEnvironmentVariables();
        expect(result.isValid).toBe(true);
      });
    });

    it('should warn about unknown OpenAI models', () => {
      process.env.OPENAI_API_KEY = 'sk-' + 'x'.repeat(25);
      process.env.OPENAI_MODEL = 'unknown-model';
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.warnings.some(w => w.includes('unknown-model'))).toBe(true);
    });

    it('should not warn about known OpenAI models', () => {
      const knownModels = ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo'];
      knownModels.forEach(model => {
        process.env = {
          OPENAI_API_KEY: 'sk-' + 'x'.repeat(25),
          OPENAI_MODEL: model,
        };
        const result = validateEnvironmentVariables();
        expect(result.warnings.some(w => w.includes(model))).toBe(false);
      });
    });
  });

  describe('validateOrThrow', () => {
    it('should not throw when validation passes', () => {
      process.env = {
        CLAUDE_API_KEY: 'sk-ant-' + 'x'.repeat(20),
      };
      expect(() => validateOrThrow()).not.toThrow();
    });

    it('should throw when validation fails', () => {
      process.env = {
        CLAUDE_API_KEY: 'invalid-key',
      };
      expect(() => validateOrThrow()).toThrow('Environment variable validation failed');
    });

    it('should include error details in thrown error', () => {
      process.env = {
        LLM_PROVIDER: 'invalid',
        CLAUDE_API_KEY: 'bad-key',
      };
      expect(() => validateOrThrow()).toThrow('LLM_PROVIDER');
    });
  });

  describe('getValidationReport', () => {
    it('should return success message when valid', () => {
      process.env = {};
      const report = getValidationReport();
      expect(report).toContain('✓ All environment variables are valid');
    });

    it('should return error details when invalid', () => {
      process.env = {
        LLM_PROVIDER: 'invalid',
      };
      const report = getValidationReport();
      expect(report).toContain('✗ Validation failed');
      expect(report).toContain('LLM_PROVIDER');
    });

    it('should include warnings in report', () => {
      process.env = {
        LLM_BASE_URL: 'http://localhost:8000',
      };
      const report = getValidationReport();
      expect(report).toContain('Warnings:');
      expect(report).toContain('LLM_MODEL');
    });
  });

  describe('Complex validation scenarios', () => {
    it('should handle multiple errors', () => {
      process.env = {
        LLM_PROVIDER: 'invalid-provider',
        CLAUDE_API_KEY: 'bad-key',
        SANDBOX_MODE: 'wrong',
        MAX_EXECUTION_TIME: '999999',
      };
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(false);
      expect(result.errors.length).toBeGreaterThanOrEqual(4);
    });

    it('should validate complete OpenAI setup', () => {
      process.env = {
        LLM_PROVIDER: 'openai',
        OPENAI_API_KEY: 'sk-' + 'x'.repeat(30),
        OPENAI_MODEL: 'gpt-4o',
        SANDBOX_MODE: 'local',
        MAX_EXECUTION_TIME: '10000',
        MAX_MEMORY: '512',
      };
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });

    it('should validate complete Local LLM setup', () => {
      process.env = {
        LLM_PROVIDER: 'local',
        LLM_BASE_URL: 'http://localhost:8000',
        LLM_MODEL: 'llama3',
        SANDBOX_MODE: 'docker',
      };
      const result = validateEnvironmentVariables();
      expect(result.isValid).toBe(true);
      expect(result.warnings.some(w => w.includes('docker'))).toBe(true);
    });
  });
});
