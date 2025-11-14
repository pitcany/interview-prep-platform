import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { LLMProviderFactory } from './llmProviderFactory';

describe('LLMProviderFactory', () => {
  let originalEnv: NodeJS.ProcessEnv;

  beforeEach(() => {
    // Save original environment
    originalEnv = { ...process.env };
  });

  afterEach(() => {
    // Restore original environment
    process.env = originalEnv;
  });

  describe('provider selection', () => {
    it('selects Claude when CLAUDE_API_KEY is set', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = undefined;
      process.env.LLM_BASE_URL = undefined;

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('claude');
    });

    it('selects OpenAI when OPENAI_API_KEY is set and CLAUDE_API_KEY is not', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_BASE_URL = undefined;

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('openai');
    });

    it('selects Local LLM when LLM_BASE_URL is set and no API keys are set', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = undefined;
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      process.env.LLM_MODEL = 'llama3';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('local');
    });

    it('prefers Claude over OpenAI when both are set', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_BASE_URL = undefined;

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('claude');
    });

    it('prefers OpenAI over Local LLM when both are set', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_BASE_URL = 'http://localhost:8000';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('openai');
    });

    it('throws error when no provider is configured', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = undefined;
      process.env.LLM_BASE_URL = undefined;

      expect(() => LLMProviderFactory.createProvider()).toThrow(
        'No LLM provider configured'
      );
    });
  });

  describe('explicit provider selection', () => {
    it('selects Claude when explicitly specified', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_PROVIDER = 'claude';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('claude');
    });

    it('selects OpenAI when explicitly specified', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_PROVIDER = 'openai';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('openai');
    });

    it('selects Local LLM when explicitly specified', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      process.env.LLM_PROVIDER = 'local';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('local');
    });

    it('throws error when explicit provider is not configured', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.LLM_PROVIDER = 'claude';

      expect(() => LLMProviderFactory.createProvider()).toThrow(
        'CLAUDE_API_KEY environment variable not set'
      );
    });

    it('throws error for unknown explicit provider', () => {
      process.env.LLM_PROVIDER = 'unknown-provider';

      expect(() => LLMProviderFactory.createProvider()).toThrow(
        'Unknown LLM provider: unknown-provider'
      );
    });

    it('handles case-insensitive provider names', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.LLM_PROVIDER = 'CLAUDE';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('claude');
    });
  });

  describe('provider information', () => {
    it('returns provider details for Claude', () => {
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('claude');
      expect(info.configured).toBe(true);
      expect(info.model).toBe('claude-sonnet-4-20250514');
    });

    it('returns provider details for OpenAI', () => {
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.OPENAI_MODEL = 'gpt-4';

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('openai');
      expect(info.configured).toBe(true);
      expect(info.model).toBe('gpt-4');
    });

    it('uses default OpenAI model when not specified', () => {
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.OPENAI_MODEL = undefined;

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.model).toBe('gpt-4o');
    });

    it('returns provider details for Local LLM', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = undefined;
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      process.env.LLM_MODEL = 'llama3';

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('local');
      expect(info.configured).toBe(true);
      expect(info.endpoint).toBe('http://localhost:8000');
      expect(info.model).toBe('llama3');
    });

    it('uses default model for Local LLM when not specified', () => {
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      process.env.LLM_MODEL = undefined;

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.model).toBe('gpt-oss-20b');
    });

    it('returns not configured when no provider is set', () => {
      process.env.CLAUDE_API_KEY = undefined;
      process.env.OPENAI_API_KEY = undefined;
      process.env.LLM_BASE_URL = undefined;

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('none');
      expect(info.configured).toBe(false);
    });

    it('returns not configured for explicit provider without credentials', () => {
      process.env.LLM_PROVIDER = 'claude';
      process.env.CLAUDE_API_KEY = undefined;

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('none');
      expect(info.configured).toBe(false);
    });

    it('handles invalid provider gracefully in getProviderInfo', () => {
      process.env.LLM_PROVIDER = 'invalid-provider';

      const info = LLMProviderFactory.getProviderInfo();

      expect(info.provider).toBe('none');
      expect(info.configured).toBe(false);
    });
  });

  describe('provider priority', () => {
    it('follows priority order: Claude > OpenAI > Local', () => {
      // All three providers configured
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_BASE_URL = 'http://localhost:8000';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('claude');
    });

    it('respects explicit provider over priority', () => {
      // All three providers configured, but local is explicitly selected
      process.env.CLAUDE_API_KEY = 'sk-ant-test-key';
      process.env.OPENAI_API_KEY = 'sk-test-key';
      process.env.LLM_BASE_URL = 'http://localhost:8000';
      process.env.LLM_PROVIDER = 'local';

      const provider = LLMProviderFactory.createProvider();

      expect(provider.getProviderName()).toBe('local');
    });
  });
});
