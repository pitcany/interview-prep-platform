# Key Files Reference

This document lists all critical files for understanding test case implementation.

## Database & Schema
- `/database/schema.sql` - Database schema with `test_cases` and `hidden_test_cases` columns
- `/database/seed_complete.sql` - Generated SQL INSERT statements (auto-generated)

## Questions Data (Source of Truth)
- `/scripts/questions_data_full.py` - All 50 questions with test cases and solutions
  - Contains 40 LeetCode questions (empty `hidden_test_cases`)
  - Contains 10 ML System Design questions
  - Each question has visible `test_cases` with 2-4 examples

## Script Pipeline
- `/scripts/generate_seed_sql.py` - Converts Python questions data to SQL
  - `generate_hints(q)` - Generates hints if missing
  - `generate_hidden_test_cases(q)` - Currently returns empty list
  - `generate_leetcode_insert(q, question_id)` - Creates SQL INSERT for LeetCode

- `/scripts/add_hidden_test_cases.py` - Adds hidden test cases to DB
  - `generate_hidden_test_cases_for_question()` - Stub for future use
  - `ensure_hints_exist()` - Adds default hints if missing

## Backend Services
- `/electron/main.ts` - Electron main process
  - `ipcMain.handle('code:execute', ...)` - Run visible test cases only
  - `ipcMain.handle('code:submit', ...)` - Run visible + hidden test cases

- `/electron/services/database.ts` - SQLite database operations
  - `getLeetCodeQuestionDetails(questionId)` - Retrieves test cases + hidden test cases
  - `createCodeSubmission(data)` - Saves submission with all test results
  - `updateProgress(userId, questionId, solved)` - Updates user progress

- `/electron/services/codeExecutor.ts` - Code execution orchestration
  - `executeCode(code, language, testCases)` - Main execution method
  - `extractMethodName(code, language)` - Finds method to call
  - `prepareCodeWithTestCase(code, language, testCase)` - Wraps code for execution
  - `compareOutputs(actual, expected)` - JSON string comparison

## Python Execution Service
- `/python-service/test_runner.py` - Main test runner
  - `TestRunner.run_tests(code, test_cases, language)` - Runs multiple test cases
  - `_compare_outputs(expected, actual)` - Compares with float tolerance

- `/python-service/executor.py` - Single test case executor
  - `execute_code(code, test_input, timeout_seconds)` - Executes one test
  - Method introspection: finds and calls callable methods
  - Handles Solution class and standalone functions

- `/python-service/sandbox.py` - Security wrapper
  - `Sandbox.execute(code, test_input, language)` - Executes in sandbox
  - Resource limits: memory and timeout
  - Spawns executor.py for Python code

## Frontend Components
- `/src/pages/Practice.tsx` - Main practice page
  - Loads question details (test cases + hidden test cases)
  - `handleRunCode()` - Sends visible test cases only
  - `handleSubmit()` - Sends visible + hidden test cases combined

- `/src/components/TestRunner/index.tsx` - Display test results
  - Shows "X / Y passed"
  - Displays only visible test cases (not hidden)
  - Allows custom test case creation

- `/src/services/api.ts` - IPC wrapper
  - `executeCode(data)` - Calls `code:execute`
  - `submitCode(data)` - Calls `code:submit`
  - `getLeetCodeDetails(questionId)` - Gets question with test cases

## TypeScript Types
- `/src/types/index.ts` - All type definitions
  - `TestCase` - Single test case (input + expectedOutput)
  - `TestResult` - Result from running a test case
  - `ExecutionResult` - Results from all test cases
  - `LeetCodeQuestion` - Question with test_cases + hidden_test_cases (JSON strings)

## Preload & IPC
- `/electron/preload.ts` - IPC bridge
  - Exposes `window.electronAPI` methods
  - Type-safe wrappers for all handlers

---

# Critical Code Paths

## Test Case Storage (Database)
```
questions_data_full.py (source)
    ↓
generate_seed_sql.py (converts to SQL)
    ↓
seed_complete.sql (INSERT statements)
    ↓
SQLite database (leetcode_questions table)
```

## Test Case Execution (Run)
```
Practice.tsx (handleRunCode)
    ↓
api.executeCode({code, language, testCases: [visible]})
    ↓
main.ts ipcMain.handle('code:execute')
    ↓
CodeExecutorService.executeCode()
    ↓
For Python: test_runner.py → executor.py → Solution class
For Docker: Create file → Docker run → Compare results
    ↓
Return ExecutionResult with test results
```

## Test Case Execution (Submit)
```
Practice.tsx (handleSubmit)
    ↓
Combine: JSON.parse(test_cases) + JSON.parse(hidden_test_cases)
    ↓
api.submitCode({code, language, customTestCases: [visible + hidden]})
    ↓
main.ts ipcMain.handle('code:submit')
    ↓
CodeExecutorService.executeCode() [same as above, but more tests]
    ↓
DatabaseService.createCodeSubmission()
    ↓
DatabaseService.updateProgress(solved = all_passed)
    ↓
Return submission + ExecutionResult
```

---

# File Dependencies

```
Practice.tsx
├── api.ts (API calls)
├── types/index.ts (TypeScript types)
├── TestRunner/index.tsx (Display results)
└── SolutionViewer (Show solutions)

codeExecutor.ts
├── child_process (spawn Python)
├── docker (run containers)
└── fs (temp file management)

test_runner.py
├── executor.py (execute single test)
├── sandbox.py (security wrapper)
└── json (I/O)

executor.py
├── multiprocessing (timeout control)
├── signal (timeout handler)
└── resource (memory limits)

database.ts
├── better-sqlite3 (sync SQLite)
├── fs (read schema)
└── schema.sql (table definitions)

generate_seed_sql.py
├── questions_data_full.py (source)
└── json (parse/serialize)
```

---

# Important Constants & Settings

## Timeouts
- CodeExecutor: 10 seconds (TypeScript)
- Python service: 10 seconds
- Extra buffer: 2 seconds

## Memory Limits
- Default: 512 MB
- Set via: `SANDBOX_MODE=local` environment variable

## Test Case Limits
- Visible: 2-4 per question
- Hidden: 0-5 per question (not yet populated)
- Custom: Unlimited (user-created, not persisted)

## Method Name Extraction (Python)
### Common LeetCode Methods (fallback list)
twoSum, threeSum, maxProfit, findMedianSortedArrays,
lengthOfLongestSubstring, longestPalindrome, reverse,
myAtoi, isMatch, maxArea, intToRoman, romanToInt,
longestCommonPrefix, isValid, mergeTwoLists, removeDuplicates,
search, searchInsert, plusOne, addBinary, mySqrt,
climbStairs, deleteDuplicates, merge, isSameTree,
isSymmetric, maxDepth, levelOrder, sortedArrayToBST,
inorderTraversal, preorderTraversal, postorderTraversal,
hasPathSum, minDepth, isBalanced, flatten, connect,
buildTree, numIslands, cloneGraph, canFinish, findOrder

## Output Comparison
- TypeScript: JSON string equality (exact match)
- Python: Deep comparison with float tolerance (1e-9)

---

# Test Case Data Format

## Input Format
Single value or list (depends on function):
```json
{
  "input": [2, 7, 11, 15],           // Array input
  "expectedOutput": [0, 1]
}
```

or

```json
{
  "input": ["hello", 2],             // Multiple args
  "expectedOutput": "HEHE"
}
```

or

```json
{
  "input": 5,                        // Single arg
  "expectedOutput": 120
}
```

## How Arguments Are Passed
```python
if isinstance(test_input, list):
    result = method(*test_input)     # Unpack: method(arg1, arg2, ...)
elif isinstance(test_input, dict):
    result = method(**test_input)    # Kwargs: method(key=value, ...)
else:
    result = method(test_input)      # Single: method(arg)
```

---

# Environment Variables

```bash
# Execution mode
SANDBOX_MODE=local                   # 'local' for Python service, else Docker

# LLM Configuration
LLM_BASE_URL=http://localhost:8000  # Local LLM API
LLM_MODEL=gpt-oss-20b              # Model name

# Database Path (auto-determined by OS)
# Linux: ~/.config/interview-prep-platform/interview-prep.db
# macOS: ~/Library/Application Support/interview-prep-platform/interview-prep.db
# Windows: %APPDATA%\interview-prep-platform\interview-prep.db
```

---

# How to Add/Modify Hidden Test Cases

### Option 1: Edit questions_data_full.py
```python
{
    "title": "Two Sum",
    "test_cases": [...],
    "hidden_test_cases": [
        {"input": [[1, 2], 3], "expectedOutput": [0, 1]},
        {"input": [[2, 2], 4], "expectedOutput": [0, 1]},
        {"input": [[1, 2, 3], 5], "expectedOutput": [1, 2]}
    ]
}
```

### Option 2: Run generation scripts
```bash
python3 scripts/generate_seed_sql.py
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

### Option 3: Direct database update
```sql
sqlite3 ~/.config/interview-prep-platform/interview-prep.db
UPDATE leetcode_questions 
SET hidden_test_cases = '[{"input": ..., "expectedOutput": ...}]'
WHERE question_id = 1;
```

---

# Debugging Tips

1. Check if test cases parsed correctly:
   - `questionDetails.test_cases` (JSON string)
   - `JSON.parse(questionDetails.test_cases)` (array)

2. Check method extraction:
   - Add console.log in `extractMethodName()`
   - Check if Solution class exists in code

3. Check Python execution:
   - Run test_runner.py manually with JSON input
   - Check executor.py for method introspection issues

4. Check database:
   - Query: `SELECT test_cases, hidden_test_cases FROM leetcode_questions WHERE question_id = 1;`
   - Verify JSON format

5. Check IPC:
   - Verify handler name matches in main.ts, preload.ts, api.ts
   - Check console for IPC errors

