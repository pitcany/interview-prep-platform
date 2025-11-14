# IPC API Documentation

This document describes all Inter-Process Communication (IPC) channels between the Electron main process and renderer process. Use this as a reference for understanding existing APIs or adding new features.

## Table of Contents

- [Architecture](#architecture)
- [User Management](#user-management)
- [Question Management](#question-management)
- [Code Execution](#code-execution)
- [Submissions](#submissions)
- [Mock Interviews](#mock-interviews)
- [Feedback](#feedback)
- [Progress & Analytics](#progress--analytics)
- [Adding New IPC Channels](#adding-new-ipc-channels)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)

## Architecture

### IPC Flow

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  React (UI)     │         │  Preload Script  │         │  Main Process   │
│                 │         │                  │         │                 │
│  api.ts         │ ──────> │  preload.ts      │ ──────> │  main.ts        │
│  (Frontend)     │ <────── │  contextBridge   │ <────── │  ipcMain        │
└─────────────────┘         └──────────────────┘         └─────────────────┘
       │                                                          │
       │                                                          │
       └──────────────────────────────────────────────────────────┘
                         IPC Communication
```

### Components

1. **React Components** (`src/`)
   - Call methods on `window.electronAPI`
   - Handle responses and errors

2. **API Service** (`src/services/api.ts`)
   - Wraps `window.electronAPI` with TypeScript types
   - Adds retry logic for resilience
   - Singleton export: `export const api = new APIService()`

3. **Preload Script** (`electron/preload.ts`)
   - Exposes safe IPC methods via `contextBridge`
   - Validates and sanitizes data
   - Security boundary between renderer and main

4. **Main Process** (`electron/main.ts`)
   - Registers IPC handlers with `ipcMain.handle()`
   - Orchestrates backend services
   - Returns results or throws errors

5. **Backend Services** (`electron/services/`)
   - Database operations (SQLite)
   - Code execution
   - LLM feedback generation

## User Management

### Create User

Creates a new user account.

**IPC Channel:** `user:create`

**Request:**
```typescript
{
  username: string;      // 3-50 characters
  email: string;         // Valid email format
  preferredLanguage?: 'python' | 'java' | 'cpp';
}
```

**Response:**
```typescript
{
  id: number;
  username: string;
  email: string;
  preferred_language: 'python' | 'java' | 'cpp';
  created_at: string;    // ISO 8601 timestamp
  last_login: string;    // ISO 8601 timestamp
}
```

**Usage:**
```typescript
const user = await api.createUser({
  username: 'john_doe',
  email: 'john@example.com',
  preferredLanguage: 'python'
});
```

**Errors:**
- User with username or email already exists
- Invalid email format
- Username too short/long

---

### Login User

Logs in an existing user and updates last_login timestamp.

**IPC Channel:** `user:login`

**Request:**
```typescript
username: string
```

**Response:**
```typescript
User  // Same as create user response
```

**Usage:**
```typescript
const user = await api.loginUser('john_doe');
```

**Errors:**
- User not found

---

### Get All Users

Retrieves all registered users.

**IPC Channel:** `user:getAll`

**Request:** None

**Response:**
```typescript
User[]
```

**Usage:**
```typescript
const users = await api.getAllUsers();
```

---

### Delete User

Permanently deletes a user and all associated data.

**IPC Channel:** `user:delete`

**Request:**
```typescript
userId: number
```

**Response:**
```typescript
{
  success: boolean;
  deletedId: number;
}
```

**Usage:**
```typescript
const result = await api.deleteUser(userId);
```

**Errors:**
- User not found

---

### Update User Preferences

Updates user preferences (theme, font size, etc.).

**IPC Channel:** `user:updatePreferences`

**Request:**
```typescript
userId: number
preferences: {
  editor_theme?: 'vs-dark' | 'vs-light' | 'hc-black';
  editor_font_size?: number;  // 10-24
  auto_run_code?: boolean;
}
```

**Response:**
```typescript
void
```

**Usage:**
```typescript
await api.updateUserPreferences(userId, {
  editor_theme: 'vs-dark',
  editor_font_size: 16
});
```

## Question Management

### Get Questions

Retrieves questions with optional filtering.

**IPC Channel:** `questions:getAll`

**Request:**
```typescript
category?: 'leetcode' | 'ml_system_design'
difficulty?: 'easy' | 'medium' | 'hard'
```

**Response:**
```typescript
Question[]

interface Question {
  id: number;
  title: string;
  category_name: string;
  difficulty: 'easy' | 'medium' | 'hard';
  tags: string;  // JSON array
  created_at: string;
}
```

**Usage:**
```typescript
// All questions
const all = await api.getQuestions();

// LeetCode medium questions only
const mediumLeetCode = await api.getQuestions('leetcode', 'medium');
```

---

### Get Question By ID

Retrieves basic question information.

**IPC Channel:** `questions:getById`

**Request:**
```typescript
questionId: number
```

**Response:**
```typescript
Question
```

---

### Get LeetCode Details

Retrieves full details for a LeetCode question.

**IPC Channel:** `questions:leetcode:getDetails`

**Request:**
```typescript
questionId: number
```

**Response:**
```typescript
{
  ...Question,
  description: string;
  function_signature_python: string;
  function_signature_java: string;
  function_signature_cpp: string;
  test_cases: string;  // JSON array
  hidden_test_cases: string;  // JSON array
  expected_time_complexity: string;
  expected_space_complexity: string;
  hints: string[];  // JSON array
  leetcode_url: string;
  solution_approach: string;
}
```

**Usage:**
```typescript
const details = await api.getLeetCodeDetails(questionId);
const testCases = JSON.parse(details.test_cases);
```

---

### Get ML Design Details

Retrieves full details for an ML System Design question.

**IPC Channel:** `questions:mldesign:getDetails`

**Request:**
```typescript
questionId: number
```

**Response:**
```typescript
{
  ...Question,
  scenario: string;
  requirements: string;  // JSON array
  constraints: string;   // JSON array
  key_components: string;  // JSON array
  evaluation_criteria: string;  // JSON array
  sample_architecture_image: string | null;
  reference_links: string;  // JSON array
}
```

**Usage:**
```typescript
const details = await api.getMLDesignDetails(questionId);
const requirements = JSON.parse(details.requirements);
```

---

### Get Question Hints

Retrieves hints for a question.

**IPC Channel:** `questions:hints`

**Request:**
```typescript
questionId: number
```

**Response:**
```typescript
string[]  // Array of hint strings
```

**Usage:**
```typescript
const hints = await api.getQuestionHints(questionId);
```

## Code Execution

### Execute Code

Runs code against test cases without saving submission.

**IPC Channel:** `code:execute`

**Request:**
```typescript
{
  code: string;
  language: 'python' | 'java' | 'cpp';
  testCases: TestCase[];
  questionId: number;
}

interface TestCase {
  input: unknown;
  expectedOutput: unknown;
}
```

**Response:**
```typescript
{
  status: 'passed' | 'failed' | 'error' | 'timeout';
  test_results: TestResult[];
  execution_time_ms: number;
  memory_used_kb: number;
  error_message?: string;
}

interface TestResult {
  passed: boolean;
  input: unknown;
  expected: unknown;
  actual: unknown;
  error?: string;
  execution_time_ms?: number;
}
```

**Usage:**
```typescript
const result = await api.executeCode({
  code: 'def twoSum(nums, target): ...',
  language: 'python',
  testCases: [
    { input: [[2,7,11,15], 9], expectedOutput: [0,1] }
  ],
  questionId: 1
});

if (result.status === 'passed') {
  console.log('All tests passed!');
}
```

**Errors:**
- Code execution timeout (>10s)
- Memory limit exceeded (>512MB)
- Compilation error
- Runtime error

---

### Submit Code

Executes code and saves submission to database.

**IPC Channel:** `code:submit`

**Request:**
```typescript
{
  userId: number;
  questionId: number;
  code: string;
  language: 'python' | 'java' | 'cpp';
  customTestCases: TestCase[];
}
```

**Response:**
```typescript
{
  submission: CodeSubmission;
  executionResult: ExecutionResult;
}

interface CodeSubmission {
  id: number;
  user_id: number;
  question_id: number;
  code: string;
  language: string;
  status: string;
  execution_time_ms: number;
  memory_used_kb: number;
  test_results: string;  // JSON
  submitted_at: string;
}
```

**Usage:**
```typescript
const { submission, executionResult } = await api.submitCode({
  userId: 1,
  questionId: 1,
  code: 'def twoSum...',
  language: 'python',
  customTestCases: []
});
```

## Submissions

### Submit Design

Submits ML system design diagram and explanation.

**IPC Channel:** `design:submit`

**Request:**
```typescript
{
  userId: number;
  questionId: number;
  diagramData: DiagramData;
  writtenExplanation: string;
  timeSpent: number;  // seconds
}

interface DiagramData {
  nodes: Node[];
  edges: Edge[];
}
```

**Response:**
```typescript
{
  id: number;
  user_id: number;
  question_id: number;
  diagram_data: string;  // JSON
  written_explanation: string;
  time_spent_seconds: number;
  submitted_at: string;
}
```

**Usage:**
```typescript
const submission = await api.submitDesign({
  userId: 1,
  questionId: 10,
  diagramData: { nodes: [...], edges: [...] },
  writtenExplanation: 'My design approach...',
  timeSpent: 1800  // 30 minutes
});
```

## Mock Interviews

### Start Mock Interview

Creates a new mock interview session.

**IPC Channel:** `mock:start`

**Request:**
```typescript
{
  userId: number;
  interviewType: 'leetcode' | 'ml_design';
}
```

**Response:**
```typescript
{
  id: number;
  user_id: number;
  interview_type: string;
  status: 'in_progress' | 'completed';
  started_at: string;
  completed_at: string | null;
  duration_minutes: number;
}
```

**Usage:**
```typescript
const mock = await api.startMockInterview({
  userId: 1,
  interviewType: 'leetcode'
});
```

---

### Complete Mock Interview

Marks a mock interview as completed.

**IPC Channel:** `mock:complete`

**Request:**
```typescript
mockId: number
```

**Response:**
```typescript
MockInterview  // Updated with completed_at
```

---

### Get Mock Interview Questions

Retrieves questions assigned to a mock interview.

**IPC Channel:** `mock:getQuestions`

**Request:**
```typescript
mockId: number
```

**Response:**
```typescript
Array<{
  mock_interview_id: number;
  question_id: number;
  order_index: number;
  question?: Question;
}>
```

---

### Add Question to Mock

Associates a question with a mock interview.

**IPC Channel:** `mock:addQuestion`

**Request:**
```typescript
mockId: number
questionId: number
orderIndex: number
```

**Response:**
```typescript
void
```

## Feedback

### Generate Feedback

Generates AI feedback for a code or design submission.

**IPC Channel:** `feedback:generate`

**Request:**
```typescript
{
  userId: number;
  submissionId: number;
  submissionType: 'code' | 'design';
  mockInterviewId?: number;
}
```

**Response:**
```typescript
{
  id: number;
  user_id: number;
  submission_id: number;
  submission_type: string;
  mock_interview_id: number | null;
  feedback_text: string;  // Markdown formatted
  scores: string;  // JSON
  strengths: string;  // JSON array
  improvements: string;  // JSON array
  generated_at: string;
}
```

**Usage:**
```typescript
const feedback = await api.generateFeedback({
  userId: 1,
  submissionId: 42,
  submissionType: 'code'
});

const scores = JSON.parse(feedback.scores);
console.log('Correctness:', scores.correctness);
```

**Special Cases:**
- If LLM service unavailable, returns feedback with setup instructions
- If generation fails, returns feedback with error and retry instructions
- Never throws errors - gracefully degrades

## Progress & Analytics

### Get User Progress

Retrieves progress for all questions attempted by user.

**IPC Channel:** `progress:getByUser`

**Request:**
```typescript
userId: number
```

**Response:**
```typescript
Array<{
  id: number;
  user_id: number;
  question_id: number;
  times_attempted: number;
  times_solved: number;
  best_execution_time_ms: number | null;
  last_attempted_at: string;
}>
```

**Usage:**
```typescript
const progress = await api.getUserProgress(userId);
const solved = progress.filter(p => p.times_solved > 0);
```

---

### Get User Stats

Retrieves aggregate statistics for a user.

**IPC Channel:** `stats:getByUser`

**Request:**
```typescript
userId: number
```

**Response:**
```typescript
{
  totalQuestions: number;
  solvedQuestions: number;
  attemptedQuestions: number;

  leetcode: {
    total: number;
    solved: number;
    easy: number;
    medium: number;
    hard: number;
  };

  mlDesign: {
    total: number;
    solved: number;
    easy: number;
    medium: number;
    hard: number;
  };

  recentActivity: Array<{
    date: string;  // YYYY-MM-DD
    submissionsCount: number;
  }>;
}
```

**Usage:**
```typescript
const stats = await api.getUserStats(userId);
console.log(`Solved ${stats.solvedQuestions}/${stats.totalQuestions}`);
```

---

### Get Submission History

Retrieves recent submissions (code + design).

**IPC Channel:** `submissions:history`

**Request:**
```typescript
userId: number
limit?: number  // Default: 20
```

**Response:**
```typescript
Array<CodeSubmission | DesignSubmission>
```

---

### Get User Feedback

Retrieves all feedback received by user.

**IPC Channel:** `feedback:getByUser`

**Request:**
```typescript
userId: number
limit?: number
```

**Response:**
```typescript
Feedback[]
```

---

### Reset User Progress

Deletes all progress, submissions, and feedback for a user.

**IPC Channel:** `progress:reset`

**Request:**
```typescript
userId: number
```

**Response:**
```typescript
{
  success: boolean;
}
```

**Warning:** This is irreversible!

## Adding New IPC Channels

### Step 1: Define Types

Add TypeScript interfaces in `src/types/index.ts`:

```typescript
export interface MyNewData {
  field1: string;
  field2: number;
}
```

### Step 2: Add Handler in Main Process

In `electron/main.ts`:

```typescript
ipcMain.handle('my:newChannel', async (_, arg1, arg2) => {
  try {
    // Validate input
    if (!arg1) {
      throw new Error('arg1 is required');
    }

    // Process request (call services)
    const result = await someService.doSomething(arg1, arg2);

    // Return result
    return result;
  } catch (error: any) {
    console.error('[IPC] my:newChannel error:', error);
    throw error;  // Propagates to renderer
  }
});
```

### Step 3: Expose in Preload

In `electron/preload.ts`:

```typescript
contextBridge.exposeInMainWorld('electronAPI', {
  // ... existing methods

  myNewMethod: (arg1: string, arg2: number): Promise<MyNewData> =>
    ipcRenderer.invoke('my:newChannel', arg1, arg2),
});

// Update ElectronAPI interface
interface ElectronAPI {
  // ... existing methods
  myNewMethod: (arg1: string, arg2: number) => Promise<MyNewData>;
}
```

### Step 4: Add API Wrapper

In `src/services/api.ts`:

```typescript
async myNewMethod(arg1: string, arg2: number): Promise<MyNewData> {
  return this.withRetry(() => this.api.myNewMethod(arg1, arg2));
}
```

### Step 5: Use in Components

```typescript
import { api } from '../services/api';

const result = await api.myNewMethod('test', 42);
```

## Error Handling

### Error Types

All IPC methods can throw errors. Use try-catch:

```typescript
try {
  const result = await api.someMethod();
} catch (error) {
  console.error('Failed:', error.message);
  // Show error to user
}
```

### Error Classification

The app includes error classification (see `src/utils/errorHandling.ts`):

```typescript
import { classifyError } from '../utils/errorHandling';

try {
  const result = await api.someMethod();
} catch (error) {
  const classified = classifyError(error);

  // Show user-friendly message
  showToast(classified.userMessage, 'error');

  // Log technical details
  console.error(classified.technicalMessage);

  // Show recovery suggestions
  if (classified.recoverySuggestions.length > 0) {
    console.log('Try:', classified.recoverySuggestions);
  }
}
```

### Retry Logic

API methods automatically retry on transient failures (network, timeout, IPC errors):

```typescript
// Automatic retry (up to 3 attempts with exponential backoff)
const questions = await api.getQuestions();
```

Customize retry behavior:

```typescript
import { retryWithBackoff } from '../utils/retry';

const result = await retryWithBackoff(
  () => api.someMethod(),
  {
    maxRetries: 5,
    baseDelay: 2000,
    maxDelay: 20000
  }
);
```

## Best Practices

### Security

1. **Never expose Node.js APIs directly to renderer**
   - Use preload script with contextBridge
   - Validate all inputs in main process

2. **Sanitize user input**
   - Use validation utilities (see `src/utils/validation.ts`)
   - Prevent SQL injection (use parameterized queries)
   - Prevent command injection (in code execution)

3. **Use contextIsolation**
   - Already enabled in `electron/main.ts`
   - Prevents renderer from accessing Node.js

### Performance

1. **Batch operations when possible**
   ```typescript
   // Bad: Multiple IPC calls
   for (const id of ids) {
     await api.getQuestionById(id);
   }

   // Good: Single IPC call
   const questions = await api.getQuestionsByIds(ids);
   ```

2. **Use pagination for large datasets**
   ```typescript
   const history = await api.getSubmissionHistory(userId, 20);
   ```

3. **Cache static data**
   ```typescript
   // Cache questions in component state
   const [questions, setQuestions] = useState([]);

   useEffect(() => {
     api.getQuestions().then(setQuestions);
   }, []);  // Only fetch once
   ```

### Error Handling

1. **Always handle errors**
   ```typescript
   try {
     await api.someMethod();
   } catch (error) {
     // Show user feedback
     showToast(getUserMessage(error), 'error');
   }
   ```

2. **Provide fallbacks**
   ```typescript
   try {
     const feedback = await api.generateFeedback(...);
   } catch (error) {
     // Fallback: allow user to continue without feedback
     console.warn('Feedback unavailable:', error);
   }
   ```

3. **Log errors appropriately**
   ```typescript
   // Development
   console.error('Full error:', error);

   // Production
   // Send to error tracking service (Sentry, etc.)
   ```

### TypeScript

1. **Define types for all IPC data**
   - Add to `src/types/index.ts`
   - Share types between main and renderer

2. **Use type guards**
   ```typescript
   function isCodeSubmission(sub: any): sub is CodeSubmission {
     return 'code' in sub;
   }
   ```

3. **Avoid `any`**
   ```typescript
   // Bad
   const data: any = await api.someMethod();

   // Good
   const data: MyType = await api.someMethod();
   ```

## Testing IPC

### Unit Tests

Mock the IPC API:

```typescript
import { vi } from 'vitest';

// Mock window.electronAPI
global.window.electronAPI = {
  getQuestions: vi.fn().mockResolvedValue([]),
  // ... other methods
};
```

### Integration Tests

Test full IPC flow:

```typescript
import { app, ipcMain } from 'electron';

describe('IPC Integration', () => {
  it('should handle questions:getAll', async () => {
    const result = await ipcMain.handleOnce('questions:getAll', async () => {
      return [{ id: 1, title: 'Test' }];
    });

    expect(result).toHaveLength(1);
  });
});
```

## Further Reading

- [Electron IPC](https://www.electronjs.org/docs/latest/tutorial/ipc)
- [Context Isolation](https://www.electronjs.org/docs/latest/tutorial/context-isolation)
- [Security Best Practices](https://www.electronjs.org/docs/latest/tutorial/security)
- [Error Handling Guide](./ERROR_HANDLING.md)
