# Testing Guide

This document describes the testing strategy and how to run tests for the Interview Prep Platform.

## Test Framework

We use **Vitest** as our test framework, which provides:
- Fast test execution with smart caching
- Compatible with Vit's development environment
- TypeScript support out of the box
- Vi test mocking utilities
- Code coverage reporting

## Test Structure

```
interview-prep-platform/
├── src/
│   └── utils/
│       └── __tests__/
│           └── validation.test.ts          # Frontend validation tests
├── electron/
│   ├── utils/
│   │   └── __tests__/
│   │       └── envValidation.test.ts       # Environment validation tests
│   └── services/
│       ├── __tests__/
│       │   ├── database.test.ts            # Database service tests
│       │   └── codeExecutor.test.ts        # Code executor tests
│       └── llmProviderFactory.test.ts      # LLM provider tests
```

## Running Tests

### Run All Tests
```bash
npm test
```

### Run Tests in Watch Mode
```bash
npm test -- --watch
```

### Run Tests with Coverage
```bash
npm test -- --coverage
```

### Run Specific Test File
```bash
npm test -- validation.test.ts
```

### Run Tests Matching Pattern
```bash
npm test -- --grep "database"
```

## Test Suites

### 1. Validation Utilities (48 tests)
**File:** `src/utils/__tests__/validation.test.ts`

Tests all input validation functions:
- `validateUsername` - Username format and length validation
- `validateEmail` - Email format validation
- `validateCode` - Code size and content validation
- `validateTestCaseJSON` - JSON format validation
- `validateExplanation` - Minimum length validation
- `validateQuestionSelection` - Mock interview question selection
- `validateDuration` - Time duration validation
- `validateNumberRange` - Generic number range validation
- `validateFileName` - File name validation
- `validateTestCases` - Comprehensive test case structure validation

**Coverage:** 100% of validation utilities

### 2. Environment Validation (24 tests)
**File:** `electron/utils/__tests__/envValidation.test.ts`

Tests environment variable validation:
- API key format validation (Claude, OpenAI)
- URL format validation (LLM_BASE_URL)
- Provider configuration validation
- Execution parameter validation (timeout, memory)
- Sandbox mode validation
- Error reporting and warnings

**Coverage:** 100% of environment validation logic

### 3. LLM Provider Factory (22 tests)
**File:** `electron/services/llmProviderFactory.test.ts`

Tests LLM provider selection logic:
- Auto-selection based on environment variables
- Explicit provider override with LLM_PROVIDER
- Provider priority: Claude > OpenAI > Local
- Error handling for missing credentials
- Provider information reporting
- Case-insensitive provider names
- Default model selection

**Coverage:** 100% of provider factory logic

### 4. Database Service (60+ tests)
**File:** `electron/services/__tests__/database.test.ts`

Tests all database operations:
- **User Management:** Create, login, get all, delete, preferences
- **Question Management:** Get questions, filter by category/difficulty, get details
- **Code Submissions:** Create, retrieve, execution metrics
- **Design Submissions:** Create, retrieve
- **Progress Tracking:** Update progress, get stats, reset
- **Mock Interviews:** Create, complete, add questions
- **Feedback:** Create, retrieve user feedback
- **Submission History:** Combined history, sorting, limits

**Setup:** Each test uses a temporary SQLite database that is cleaned up after the test.

**Coverage:** All database methods tested with real database operations

### 5. Code Executor (30+ tests)
**File:** `electron/services/__tests__/codeExecutor.test.ts`

Tests code execution with mocked subprocess:
- **Input Validation:** Language, code size, empty code
- **Test Case Execution:** Success, timeout, errors
- **Docker Execution:** Resource limits, network isolation
- **Security:** Crypto-random filenames, path traversal prevention, cleanup
- **Language Support:** Python execution, method extraction
- **Error Handling:** Process errors, invalid JSON, multiple test cases

**Mocking:** Uses Vitest's `vi.mock()` to mock `child_process.spawn` for isolated testing

**Coverage:** All execution paths including error scenarios

## Test Coverage Goals

Current coverage:
- ✅ **Validation utilities:** 100%
- ✅ **Environment validation:** 100%
- ✅ **LLM provider factory:** 100%
- ✅ **Database service:** ~95% (all CRUD operations)
- ✅ **Code executor:** ~90% (all major paths)

**Total: 184+ test cases**

## Writing New Tests

### Test File Naming
- Place tests in `__tests__/` directory next to the code being tested
- Name test files with `.test.ts` suffix
- Example: `validation.ts` → `__tests__/validation.test.ts`

### Test Structure
```typescript
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { functionToTest } from '../moduleToTest';

describe('Module Name', () => {
  beforeEach(() => {
    // Setup before each test
  });

  afterEach(() => {
    // Cleanup after each test
  });

  describe('Feature Group', () => {
    it('should do something specific', () => {
      const result = functionToTest(input);
      expect(result).toBe(expected);
    });

    it('should handle edge case', () => {
      expect(() => functionToTest(badInput)).toThrow();
    });
  });
});
```

### Mocking

For external dependencies (filesystem, network, subprocess):

```typescript
import { vi } from 'vitest';

// Mock a module
vi.mock('child_process', () => ({
  spawn: vi.fn(),
}));

// Mock implementation
const mockSpawn = spawn as unknown as ReturnType<typeof vi.fn>;
mockSpawn.mockReturnValue(mockProcess);
```

### Testing Async Code

```typescript
it('should handle async operations', async () => {
  const result = await asyncFunction();
  expect(result).toBeDefined();
});

it('should handle async errors', async () => {
  await expect(async () => {
    await functionThatThrows();
  }).rejects.toThrow('Expected error');
});
```

### Testing Database Code

```typescript
beforeEach(async () => {
  // Create temp database
  testDbPath = path.join(os.tmpdir(), `test-${Date.now()}.db`);
  dbService = new DatabaseService(testDbPath);
  await dbService.initialize();
});

afterEach(() => {
  // Clean up
  dbService.close();
  fs.unlinkSync(testDbPath);
});
```

## Continuous Integration

Tests should be run:
1. Before committing code (pre-commit hook)
2. On pull requests (CI pipeline)
3. Before releasing (pre-release checks)

### Pre-commit Hook (Recommended)
```bash
# .git/hooks/pre-commit
#!/bin/sh
npm test
if [ $? -ne 0 ]; then
  echo "Tests failed. Commit aborted."
  exit 1
fi
```

## Debugging Tests

### Run Single Test in Debug Mode
```bash
npm test -- --reporter=verbose validation.test.ts
```

### Enable Debug Logging
```bash
DEBUG=* npm test
```

### Use Vitest UI (Interactive)
```bash
npm test -- --ui
```

## Best Practices

1. **Test Isolation:** Each test should be independent
2. **Clean Up:** Always clean up resources (files, databases) in `afterEach`
3. **Descriptive Names:** Test names should describe the expected behavior
4. **Arrange-Act-Assert:** Structure tests with clear setup, execution, and verification
5. **Edge Cases:** Test boundary conditions and error scenarios
6. **Fast Tests:** Keep unit tests fast by mocking external dependencies
7. **Coverage:** Aim for high coverage but focus on critical paths

## Common Issues

### Database Locked
If you get "database is locked" errors:
- Ensure `dbService.close()` is called in `afterEach`
- Check that no other processes are accessing the test database

### Timeout Errors
If tests timeout:
- Increase timeout: `it('test', async () => {...}, 10000)` (10 seconds)
- Check for unresolved promises
- Ensure mocked processes emit 'close' event

### Module Not Found
If imports fail:
- Check TypeScript configuration in `tsconfig.json`
- Ensure paths are relative to the test file
- Verify Vitest configuration in `vite.config.ts`

## Next Steps

### Planned Test Coverage
- [ ] IPC integration tests (main ↔ renderer communication)
- [ ] React component tests (using @testing-library/react)
- [ ] E2E tests for critical user flows (using Playwright)
- [ ] Performance benchmarks for code execution
- [ ] LLM service integration tests (with API mocking)

## Resources

- [Vitest Documentation](https://vitest.dev/)
- [Testing Best Practices](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
- [Mocking with Vitest](https://vitest.dev/guide/mocking.html)
