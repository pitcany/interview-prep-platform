/**
 * Environment Variable Validation Utility
 * Validates all required environment variables at startup
 */

interface ValidationError {
  variable: string;
  error: string;
}

interface ValidationResult {
  isValid: boolean;
  errors: ValidationError[];
  warnings: string[];
}

/**
 * Validates URL format
 */
function isValidUrl(url: string): boolean {
  try {
    const parsed = new URL(url);
    return parsed.protocol === 'http:' || parsed.protocol === 'https:';
  } catch {
    return false;
  }
}

/**
 * Validates Claude API key format (starts with sk-ant-)
 */
function isValidClaudeApiKey(key: string): boolean {
  return key.startsWith('sk-ant-') && key.length > 20;
}

/**
 * Validates OpenAI API key format (starts with sk-)
 */
function isValidOpenAIApiKey(key: string): boolean {
  return key.startsWith('sk-') && key.length > 20;
}

/**
 * Validates all environment variables
 */
export function validateEnvironmentVariables(): ValidationResult {
  const errors: ValidationError[] = [];
  const warnings: string[] = [];

  // Get environment variables
  const llmProvider = process.env.LLM_PROVIDER?.toLowerCase();
  const claudeApiKey = process.env.CLAUDE_API_KEY;
  const openaiApiKey = process.env.OPENAI_API_KEY;
  const llmBaseUrl = process.env.LLM_BASE_URL;
  const llmModel = process.env.LLM_MODEL;
  const openaiModel = process.env.OPENAI_MODEL;
  const sandboxMode = process.env.SANDBOX_MODE;
  const maxExecutionTime = process.env.MAX_EXECUTION_TIME;
  const maxMemory = process.env.MAX_MEMORY;

  // Validate LLM Provider configuration
  if (llmProvider) {
    const validProviders = ['claude', 'openai', 'local'];
    if (!validProviders.includes(llmProvider)) {
      errors.push({
        variable: 'LLM_PROVIDER',
        error: `Invalid provider "${llmProvider}". Must be one of: ${validProviders.join(', ')}`,
      });
    }

    // Check that required env vars for the provider are set
    if (llmProvider === 'claude' && !claudeApiKey) {
      errors.push({
        variable: 'CLAUDE_API_KEY',
        error: 'Required when LLM_PROVIDER=claude',
      });
    } else if (llmProvider === 'openai' && !openaiApiKey) {
      errors.push({
        variable: 'OPENAI_API_KEY',
        error: 'Required when LLM_PROVIDER=openai',
      });
    } else if (llmProvider === 'local' && !llmBaseUrl) {
      errors.push({
        variable: 'LLM_BASE_URL',
        error: 'Required when LLM_PROVIDER=local',
      });
    }
  }

  // Validate Claude API Key format
  if (claudeApiKey) {
    if (!isValidClaudeApiKey(claudeApiKey)) {
      errors.push({
        variable: 'CLAUDE_API_KEY',
        error: 'Invalid format. Must start with "sk-ant-" and be at least 20 characters',
      });
    }
  }

  // Validate OpenAI API Key format
  if (openaiApiKey) {
    if (!isValidOpenAIApiKey(openaiApiKey)) {
      errors.push({
        variable: 'OPENAI_API_KEY',
        error: 'Invalid format. Must start with "sk-" and be at least 20 characters',
      });
    }
  }

  // Validate LLM Base URL format
  if (llmBaseUrl) {
    if (!isValidUrl(llmBaseUrl)) {
      errors.push({
        variable: 'LLM_BASE_URL',
        error: 'Invalid URL format. Must be a valid HTTP or HTTPS URL',
      });
    }
  }

  // Validate local LLM configuration
  if (llmBaseUrl && !llmModel) {
    warnings.push('LLM_MODEL not set. Using default: gpt-oss-20b');
  }

  // Validate OpenAI model
  if (openaiApiKey && openaiModel) {
    const validOpenAIModels = [
      'gpt-4o',
      'gpt-4o-mini',
      'gpt-4-turbo',
      'gpt-4',
      'gpt-3.5-turbo',
    ];
    if (!validOpenAIModels.includes(openaiModel)) {
      warnings.push(
        `OPENAI_MODEL="${openaiModel}" is not a known model. Valid models: ${validOpenAIModels.join(', ')}`
      );
    }
  }

  // Validate sandbox mode
  if (sandboxMode) {
    const validModes = ['local', 'docker'];
    if (!validModes.includes(sandboxMode)) {
      errors.push({
        variable: 'SANDBOX_MODE',
        error: `Invalid mode "${sandboxMode}". Must be one of: ${validModes.join(', ')}`,
      });
    }

    if (sandboxMode === 'docker') {
      warnings.push(
        'SANDBOX_MODE=docker is set but Docker execution is not fully implemented yet'
      );
    }
  }

  // Validate execution time
  if (maxExecutionTime) {
    const time = parseInt(maxExecutionTime, 10);
    if (isNaN(time) || time < 1000 || time > 60000) {
      errors.push({
        variable: 'MAX_EXECUTION_TIME',
        error: 'Must be a number between 1000 and 60000 (milliseconds)',
      });
    }
  }

  // Validate memory limit
  if (maxMemory) {
    const memory = parseInt(maxMemory, 10);
    if (isNaN(memory) || memory < 128 || memory > 2048) {
      errors.push({
        variable: 'MAX_MEMORY',
        error: 'Must be a number between 128 and 2048 (MB)',
      });
    }
  }

  // Check if at least one LLM provider is configured
  if (!claudeApiKey && !openaiApiKey && !llmBaseUrl) {
    warnings.push(
      'No LLM provider configured. AI feedback generation will be disabled. ' +
        'Set CLAUDE_API_KEY, OPENAI_API_KEY, or LLM_BASE_URL to enable feedback.'
    );
  }

  return {
    isValid: errors.length === 0,
    errors,
    warnings,
  };
}

/**
 * Throws an error if environment variables are invalid
 * Use this at app startup to fail fast
 */
export function validateOrThrow(): void {
  const result = validateEnvironmentVariables();

  if (!result.isValid) {
    const errorMessages = result.errors
      .map((e) => `  - ${e.variable}: ${e.error}`)
      .join('\n');

    throw new Error(
      `Environment variable validation failed:\n${errorMessages}\n\n` +
        'Please check your .env file and correct the invalid values.'
    );
  }

  // Log warnings to stderr (not console.log for production)
  if (result.warnings.length > 0) {
    result.warnings.forEach((warning) => {
      process.stderr.write(`Warning: ${warning}\n`);
    });
  }
}

/**
 * Returns a user-friendly validation report
 */
export function getValidationReport(): string {
  const result = validateEnvironmentVariables();
  let report = '=== Environment Variable Validation ===\n\n';

  if (result.isValid) {
    report += '✓ All environment variables are valid\n\n';
  } else {
    report += '✗ Validation failed with the following errors:\n\n';
    result.errors.forEach((error) => {
      report += `  ${error.variable}:\n    ${error.error}\n\n`;
    });
  }

  if (result.warnings.length > 0) {
    report += 'Warnings:\n\n';
    result.warnings.forEach((warning) => {
      report += `  - ${warning}\n\n`;
    });
  }

  return report;
}
