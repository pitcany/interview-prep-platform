import { ClaudeAPIService } from './claudeAPI';
import { OpenAIService } from './openaiService';
import { LocalLLMService } from './localLLM';
import type {
  CodeSubmission,
  DesignSubmission,
  LeetCodeDetails,
  MLDesignDetails,
} from '../types/ipc';

export type SubmissionForFeedback = CodeSubmission | DesignSubmission;
export type QuestionForFeedback = LeetCodeDetails | MLDesignDetails;

export interface LLMProvider {
  getProviderName(): string;
  generateFeedback(
    submission: SubmissionForFeedback,
    question: QuestionForFeedback,
    submissionType: 'code' | 'design'
  ): Promise<{
    text: string;
    scores: Record<string, number>;
    strengths: string[];
    improvements: string[];
  }>;
}

export interface ProviderInfo {
  provider: 'claude' | 'openai' | 'local' | 'none';
  configured: boolean;
  model?: string;
  endpoint?: string;
}

export class LLMProviderFactory {
  /**
   * Creates an LLM provider based on environment variables.
   *
   * Selection priority (if LLM_PROVIDER is not set):
   * 1. Claude (CLAUDE_API_KEY)
   * 2. OpenAI (OPENAI_API_KEY)
   * 3. Local LLM (LLM_BASE_URL)
   *
   * If LLM_PROVIDER is set, uses that specific provider.
   */
  static createProvider(): LLMProvider {
    const explicitProvider = process.env.LLM_PROVIDER?.toLowerCase();

    if (explicitProvider) {
      return this.createExplicitProvider(explicitProvider);
    }

    return this.createAutoSelectedProvider();
  }

  private static createExplicitProvider(provider: string): LLMProvider {
    switch (provider) {
      case 'claude':
        return this.createClaudeProvider();
      case 'openai':
        return this.createOpenAIProvider();
      case 'local':
        return this.createLocalProvider();
      default:
        throw new Error(`Unknown LLM provider: ${provider}`);
    }
  }

  private static createAutoSelectedProvider(): LLMProvider {
    // Priority 1: Claude
    if (process.env.CLAUDE_API_KEY) {
      return this.createClaudeProvider();
    }

    // Priority 2: OpenAI
    if (process.env.OPENAI_API_KEY) {
      return this.createOpenAIProvider();
    }

    // Priority 3: Local LLM
    if (process.env.LLM_BASE_URL) {
      return this.createLocalProvider();
    }

    throw new Error(
      'No LLM provider configured. Please set one of: CLAUDE_API_KEY, OPENAI_API_KEY, or LLM_BASE_URL'
    );
  }

  private static createClaudeProvider(): LLMProvider {
    const apiKey = process.env.CLAUDE_API_KEY;
    if (!apiKey) {
      throw new Error('CLAUDE_API_KEY environment variable not set');
    }
    return new ClaudeAPIService(apiKey);
  }

  private static createOpenAIProvider(): LLMProvider {
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      throw new Error('OPENAI_API_KEY environment variable not set');
    }
    const model = process.env.OPENAI_MODEL || 'gpt-4o';
    return new OpenAIService(apiKey, model);
  }

  private static createLocalProvider(): LLMProvider {
    const baseUrl = process.env.LLM_BASE_URL;
    if (!baseUrl) {
      throw new Error('LLM_BASE_URL environment variable not set');
    }
    const model = process.env.LLM_MODEL || 'gpt-oss-20b';
    return new LocalLLMService(baseUrl, model);
  }

  /**
   * Returns information about which provider is configured.
   */
  static getProviderInfo(): ProviderInfo {
    const explicitProvider = process.env.LLM_PROVIDER?.toLowerCase();

    try {
      if (explicitProvider) {
        return this.getExplicitProviderInfo(explicitProvider);
      }

      return this.getAutoSelectedProviderInfo();
    } catch {
      return {
        provider: 'none',
        configured: false,
      };
    }
  }

  private static getExplicitProviderInfo(provider: string): ProviderInfo {
    switch (provider) {
      case 'claude':
        if (!process.env.CLAUDE_API_KEY) {
          return { provider: 'none', configured: false };
        }
        return {
          provider: 'claude',
          configured: true,
          model: 'claude-sonnet-4-20250514',
        };
      case 'openai':
        if (!process.env.OPENAI_API_KEY) {
          return { provider: 'none', configured: false };
        }
        return {
          provider: 'openai',
          configured: true,
          model: process.env.OPENAI_MODEL || 'gpt-4o',
        };
      case 'local':
        if (!process.env.LLM_BASE_URL) {
          return { provider: 'none', configured: false };
        }
        return {
          provider: 'local',
          configured: true,
          endpoint: process.env.LLM_BASE_URL,
          model: process.env.LLM_MODEL || 'gpt-oss-20b',
        };
      default:
        return { provider: 'none', configured: false };
    }
  }

  private static getAutoSelectedProviderInfo(): ProviderInfo {
    if (process.env.CLAUDE_API_KEY) {
      return {
        provider: 'claude',
        configured: true,
        model: 'claude-sonnet-4-20250514',
      };
    }

    if (process.env.OPENAI_API_KEY) {
      return {
        provider: 'openai',
        configured: true,
        model: process.env.OPENAI_MODEL || 'gpt-4o',
      };
    }

    if (process.env.LLM_BASE_URL) {
      return {
        provider: 'local',
        configured: true,
        endpoint: process.env.LLM_BASE_URL,
        model: process.env.LLM_MODEL || 'gpt-oss-20b',
      };
    }

    return {
      provider: 'none',
      configured: false,
    };
  }
}
