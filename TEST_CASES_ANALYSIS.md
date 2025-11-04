# Interview Prep Platform: Test Cases Implementation Analysis

## Executive Summary

The Interview Prep Platform implements a comprehensive two-tier test case system for LeetCode questions:
- **Visible Test Cases**: Shown to users during practice, used for "Run Code"
- **Hidden Test Cases**: Used only during submission, not shown to users initially

This document provides a thorough analysis of how test cases are currently stored, used, and executed across the entire system.

---

## 1. DATABASE SCHEMA

### Location
`/database/schema.sql`

### Key Table: `leetcode_questions`

```sql
CREATE TABLE IF NOT EXISTS leetcode_questions (
    question_id INTEGER PRIMARY KEY,
    function_signature_python TEXT,
    function_signature_java TEXT,
    function_signature_cpp TEXT,
    test_cases TEXT NOT NULL,              -- JSON array of VISIBLE test cases
    hidden_test_cases TEXT,                -- JSON array of HIDDEN test cases (run on submission)
    expected_time_complexity TEXT,
    expected_space_complexity TEXT,
    solution_python TEXT,
    solution_java TEXT,
    solution_cpp TEXT,
    solution_explanation TEXT,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);
```

### Test Case Data Structure

Both `test_cases` and `hidden_test_cases` are stored as JSON strings with the following structure:

```json
[
  {
    "input": [2, 7, 11, 15],
    "expectedOutput": [0, 1]
  },
  {
    "input": [3, 2, 4],
    "expectedOutput": [1, 2]
  }
]
```

Where:
- `input`: Can be a single value, list, or dict (depends on function signature)
- `expectedOutput`: The expected return value from the function

---

## 2. QUESTIONS DATA SOURCE

### Location
`/scripts/questions_data_full.py`

### Format
Each question is a Python dictionary with the following test case structure:

```python
{
    "title": "Two Sum",
    "leetcode_url": "https://leetcode.com/problems/two-sum/",
    "difficulty": "easy",
    # ... other fields ...
    "test_cases": [
        {
            "input": [[2, 7, 11, 15], 9],
            "expectedOutput": [0, 1]
        },
        {
            "input": [[3, 2, 4], 6],
            "expectedOutput": [1, 2]
        },
        {
            "input": [[3, 3], 6],
            "expectedOutput": [0, 1]
        }
    ],
    "hidden_test_cases": []  # Currently empty - can be populated manually
}
```

### Current Status
- `test_cases`: Fully populated with 2-4 visible test cases per question
- `hidden_test_cases`: Currently empty arrays (not yet populated)

### Future Usage
To add actual hidden test cases, edit `questions_data_full.py` and add test case objects to the `hidden_test_cases` field for each question.

---

## 3. SQL GENERATION PIPELINE

### Location
`/scripts/generate_seed_sql.py`

### Process

1. **Read Questions Data**
   - Source: `questions_data_full.py` (LEETCODE_QUESTIONS list)
   - Contains 40 LeetCode questions + 10 ML System Design questions

2. **Generate Hints** (if missing)
   - Function: `generate_hints(q)`
   - Creates tag-based and difficulty-based hints
   - Ensures every question has at least one hint
   - Includes LeetCode URL as final hint

3. **Generate Hidden Test Cases** (if missing)
   - Function: `generate_hidden_test_cases(q)`
   - Currently returns empty list (generation not fully implemented)
   - Can be manually specified in `questions_data_full.py`
   - Should contain 3 edge-case test cases per question

4. **Generate SQL INSERT Statements**
   - Converts Python data to SQL
   - Generates `INSERT INTO questions` (base question data)
   - Generates `INSERT INTO leetcode_questions` (test cases + solutions)
   - Creates `/database/seed_complete.sql`

### Usage
```bash
python3 scripts/generate_seed_sql.py  # Regenerates seed_complete.sql
```

---

## 4. TEST CASE FLOW IN FRONTEND

### Location
`/src/pages/Practice.tsx`

### Component State
```typescript
const [selectedQuestion, setSelectedQuestion] = useState<Question | null>(null);
const [testCases, setTestCases] = useState<TestCase[]>([]);  // Visible test cases
const [questionDetails, setQuestionDetails] = useState<LeetCodeQuestion | null>(null);
const [results, setResults] = useState<ExecutionResult | null>(null);
```

### Test Case Loading

When a question is selected:

```typescript
const loadQuestionDetails = async () => {
  const details = await api.getLeetCodeDetails(selectedQuestion.id);
  
  // Parse VISIBLE test cases (shown in UI)
  const cases = JSON.parse(details.test_cases);
  setTestCases(cases);
  
  // Hidden test cases are loaded but not shown in test runner
  // (only shown during submission)
};
```

### "Run Code" vs "Submit" Behavior

#### Run Code
- Uses VISIBLE test cases only
- Tests shown in real-time
- User can see all test cases
- Located in `TestRunner` component

#### Submit Code
- Combines VISIBLE + HIDDEN test cases
- Executes all tests
- Returns pass/fail status
- Shows only visible test case results

```typescript
const handleSubmit = async () => {
  // Parse visible test cases
  let visibleTestCases: TestCase[] = [];
  try {
    visibleTestCases = JSON.parse(questionDetails.test_cases);
  } catch (e) {
    visibleTestCases = testCases;  // Fallback
  }

  // Parse hidden test cases
  let hiddenTestCases: TestCase[] = [];
  if (questionDetails.hidden_test_cases) {
    try {
      hiddenTestCases = JSON.parse(questionDetails.hidden_test_cases);
    } catch (e) {
      console.error('Failed to parse hidden test cases');
    }
  }

  // Combine for submission
  const allTestCases = [...visibleTestCases, ...hiddenTestCases];
};
```

### TestRunner Component
- Location: `/src/components/TestRunner/index.tsx`
- Displays test case results
- Shows "X / Y passed"
- Allows custom test case addition (user-created)
- Only displays visible test cases

---

## 5. CODE EXECUTION FLOW

### Visible Test Cases (Run Code)
- Called via: `api.executeCode()`
- IPC Handler: `code:execute` → `CodeExecutorService.executeCode()`
- Runs only visible test cases
- Results displayed in real-time

### Hidden + Visible Test Cases (Submit)
- Called via: `api.submitCode()`
- IPC Handler: `code:submit` → `CodeExecutorService.executeCode()`
- Receives combined test cases (visible + hidden)
- All tests executed in one batch

---

## 6. CODE EXECUTION SERVICE

### Location
`/electron/services/codeExecutor.ts`

### Main Method
```typescript
async executeCode(
  code: string,
  language: string,
  testCases: TestCase[]
): Promise<ExecutionResult>
```

### Execution Flow

1. **For Python (SANDBOX_MODE = 'local')**
   - Delegates to Python service: `executeWithPythonService()`
   - Spawns child process: `python3 python-service/test_runner.py`
   - Passes code + test cases as JSON
   - Returns JSON result

2. **For Other Languages (Docker)**
   - Creates temp file
   - Mounts Docker volume
   - Executes in container
   - Cleans up temp file

### Method Extraction
```typescript
private extractMethodName(code: string, language: string): string {
  // For Python:
  // 1. Try regex: class Solution(...): ... def methodName(self,
  // 2. Fallback: Look for common LeetCode method names
  // 3. Last resort: Find ANY method in Solution class
  // 4. Return empty string if not found (wrapper code will introspect)
}
```

### Code Wrapper (Python)
The service wraps user code with test execution logic:

```python
import json
import sys

${code}  # User's code inserted here

test_input = json.loads('${inputStr}')

try:
    sol = Solution()
    
    # Get all callable methods
    all_methods = [m for m in dir(sol) if not m.startswith('_') and callable(getattr(sol, m))]
    
    # Try extracted method name
    method_name = '${methodName}' if '${methodName}' else all_methods[0]
    
    # Call the method with test input
    method = getattr(sol, method_name)
    if isinstance(test_input, list):
        result = method(*test_input)
    else:
        result = method(test_input)
    
    print(json.dumps(result))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
```

---

## 7. PYTHON EXECUTION SERVICE

### Location
`/python-service/`

#### Files
1. **test_runner.py** - Main test runner
2. **executor.py** - Individual code executor
3. **sandbox.py** - Security wrapper

### test_runner.py
```python
class TestRunner:
    def run_tests(self, code: str, test_cases: List[Dict], language: str = 'python'):
        """Run all test cases against code"""
        results = {
            'status': 'passed',
            'test_results': [],
            'execution_time': 0,
            'memory_used': 0,
            'error_message': None
        }
        
        for i, test_case in enumerate(test_cases):
            test_input = test_case.get('input')
            expected_output = test_case.get('expectedOutput')
            
            # Execute via Sandbox
            execution_result = sandbox.execute(code, test_input, language)
            
            # Compare outputs
            test_result['passed'] = self._compare_outputs(expected_output, actual_output)
            results['test_results'].append(test_result)
```

### executor.py
```python
def execute_code(code: str, test_input: Any, timeout_seconds: int = 10):
    """Execute Python code with single test input"""
    
    # Uses multiprocessing for timeout control
    # Sets resource limits (memory, CPU time)
    
    # Executes code and finds callable method:
    # 1. Look for Solution class
    # 2. Find first non-__init__ method
    # 3. Call with test_input
    # 4. Return result
```

### sandbox.py
```python
class Sandbox:
    def execute(self, code: str, test_input: Any, language: str = 'python'):
        """Execute code in sandboxed environment"""
        # - Creates temp directory
        # - Sets memory/timeout limits
        # - Executes via Sandbox.execute() wrapper
        # - Cleans up temp files
        # - For Python: calls executor.py
        # - For Java/C++: placeholders (not implemented)
```

---

## 8. TYPESCRIPT TYPES

### Location
`/src/types/index.ts`

```typescript
export interface TestCase {
  input: any;
  expectedOutput: any;
  explanation?: string;
}

export interface TestResult {
  passed: boolean;
  input: any;
  expectedOutput: any;
  actualOutput: any;
  executionTime: number;
  error?: string;
}

export interface ExecutionResult {
  status: 'passed' | 'failed' | 'error' | 'timeout';
  testResults: TestResult[];
  executionTime: number;
  memoryUsed: number;
  errorMessage?: string;
}

export interface LeetCodeQuestion extends Omit<Question, 'hints'> {
  test_cases: string;              // JSON string (visible test cases)
  hidden_test_cases?: string;      // JSON string (hidden test cases)
  function_signature_python?: string;
  function_signature_java?: string;
  function_signature_cpp?: string;
  expected_time_complexity?: string;
  expected_space_complexity?: string;
  solution_python?: string;
  solution_java?: string;
  solution_cpp?: string;
  solution_explanation?: string;
  hints?: string[];                // Parsed hints array
}
```

---

## 9. DATABASE SERVICE

### Location
`/electron/services/database.ts`

### Method: getLeetCodeQuestionDetails
```typescript
getLeetCodeQuestionDetails(questionId: number) {
  const result = this.db.prepare(`
    SELECT 
      lq.*,
      q.hints
    FROM leetcode_questions lq
    JOIN questions q ON lq.question_id = q.id
    WHERE lq.question_id = ?
  `).get(questionId);

  // Parse hints
  let hints: string[] = [];
  if (result.hints) {
    try {
      hints = JSON.parse(result.hints);
    } catch {
      hints = [];
    }
  }

  // Return with all fields
  return {
    ...result,
    test_cases: result.test_cases || '[]',
    hidden_test_cases: result.hidden_test_cases || '[]',
    hints: hints,
    solution_python: result.solution_python || '',
    solution_java: result.solution_java || '',
    solution_cpp: result.solution_cpp || ''
  };
}
```

---

## 10. IPC COMMUNICATION

### Electron Main Process
```typescript
// code:execute - Run code with visible test cases
ipcMain.handle('code:execute', async (_, executionData) => {
  const { code, language, testCases } = executionData;
  return await codeExecutor.executeCode(code, language, testCases);
});

// code:submit - Submit with visible + hidden test cases
ipcMain.handle('code:submit', async (_, submissionData) => {
  const { userId, questionId, code, language, customTestCases } = submissionData;
  
  // customTestCases = visible + hidden test cases combined
  const executionResult = await codeExecutor.executeCode(
    code,
    language,
    customTestCases
  );

  // Save submission with all test results
  const submission = await dbService.createCodeSubmission({
    userId,
    questionId,
    code,
    language,
    customTestCases: JSON.stringify(customTestCases),
    executionTimeMs: executionResult.executionTime,
    memoryUsedKb: executionResult.memoryUsed,
    testResults: JSON.stringify(executionResult.testResults),
    status: executionResult.status,
  });

  // Update progress
  await dbService.updateProgress(userId, questionId, executionResult.status === 'passed');

  return { submission, executionResult };
});
```

### Frontend API Service
```typescript
async executeCode(data: any): Promise<ExecutionResult> {
  return await window.electronAPI.executeCode({
    code: data.code,
    language: data.language,
    testCases: data.testCases  // Only visible
  });
}

async submitCode(data: any): Promise<any> {
  return await window.electronAPI.submitCode({
    userId: data.userId,
    questionId: data.questionId,
    code: data.code,
    language: data.language,
    customTestCases: data.customTestCases  // Visible + hidden
  });
}
```

---

## 11. HELPER SCRIPTS

### add_hidden_test_cases.py
- Location: `/scripts/add_hidden_test_cases.py`
- Purpose: Add hidden test cases to existing database
- Currently: Just initializes empty arrays
- Future: Can manually add test cases or use more sophisticated generation

```python
def generate_hidden_test_cases_for_question(title, test_cases, tags, difficulty):
    """Generate hidden test cases based on question characteristics"""
    # Currently returns empty - should be customized per question
    hidden = []
    return hidden
```

---

## 12. CURRENT IMPLEMENTATION STATUS

### What's Working
✅ Database schema supports hidden test cases
✅ Test cases stored as JSON in database
✅ Frontend loads visible test cases
✅ Frontend loads hidden test cases
✅ Submission runs visible + hidden together
✅ Code execution service handles test arrays
✅ Python execution with method introspection
✅ Results comparison (exact match)
✅ Test results saved to database

### What Needs Work
❌ Hidden test cases not yet populated in questions_data_full.py
❌ No automatic generation of hidden test cases
❌ Java/C++ execution not implemented (Docker only)
❌ Float comparison tolerance only in Python service
❌ No special display for hidden test case failures

---

## 13. HANDLING TYPE HINTS AND IMPORTS

### Current State
- Type hints included in function signatures
- NOT automatically imported
- User code must handle imports

### Example
Question with type hints in signature:
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    pass
```

User must provide:
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # implementation
```

### Execution Wrapper
The wrapper code does NOT add imports. User code must include all necessary imports.

```python
# What gets executed:
import json
import sys

${code}  # User's code - must include its own imports

test_input = json.loads('${inputStr}')
# ...
```

### Future Enhancement
Could pre-inject common imports in wrapper:
```python
from typing import List, Dict, Optional, Tuple, Set
from collections import defaultdict, deque, Counter
```

---

## 14. FILE STRUCTURE SUMMARY

```
interview-prep-platform/
├── database/
│   ├── schema.sql              # Database schema (defines test_cases, hidden_test_cases columns)
│   └── seed_complete.sql       # Generated SQL INSERT statements
├── scripts/
│   ├── questions_data_full.py  # SOURCE OF TRUTH for test cases
│   ├── generate_seed_sql.py    # Generates seed_complete.sql
│   └── add_hidden_test_cases.py # Adds hidden test cases to DB
├── electron/
│   ├── main.ts                 # IPC handlers: code:execute, code:submit
│   ├── preload.ts              # Exposes API to renderer
│   └── services/
│       ├── database.ts         # getLeetCodeQuestionDetails()
│       └── codeExecutor.ts     # executeCode() for all languages
├── python-service/
│   ├── test_runner.py          # Main test runner (runs test cases)
│   ├── executor.py             # Executes single test case
│   └── sandbox.py              # Security wrapper
└── src/
    ├── pages/Practice.tsx      # Test case loading and submission
    ├── components/TestRunner/index.tsx  # Display test results
    ├── services/api.ts         # IPC wrapper
    └── types/index.ts          # TypeScript definitions
```

---

## 15. HOW TO ADD HIDDEN TEST CASES

### Method 1: Edit questions_data_full.py
```python
{
    "title": "Two Sum",
    "test_cases": [...],  # Visible
    "hidden_test_cases": [
        {
            "input": [[1000000, -1000000], 0],
            "expectedOutput": [0, 1]
        },
        {
            "input": [[2, 2], 4],
            "expectedOutput": [0, 1]
        },
        {
            "input": [[1, 2, 3, 4, 5], 9],
            "expectedOutput": [3, 4]
        }
    ]
}
```

### Method 2: Regenerate Database
```bash
python3 scripts/generate_seed_sql.py
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

### Method 3: Manual Database Update
```sql
UPDATE leetcode_questions 
SET hidden_test_cases = '[
  {"input": [[...], ...], "expectedOutput": [...]}
]'
WHERE question_id = 1;
```

---

## 16. FLOW DIAGRAMS

### Test Case Parsing and Execution

```
Practice.tsx (Load Question)
    ↓
getLeetCodeDetails() [IPC]
    ↓
DatabaseService.getLeetCodeQuestionDetails()
    ↓
JSON.parse(test_cases)          ← Visible
JSON.parse(hidden_test_cases)   ← Hidden (not shown initially)

----- User clicks "Run Code" -----

Practice.tsx
    ↓
executeCode() [IPC] with visible test cases only
    ↓
CodeExecutorService.executeCode()
    ↓
For Python: executeWithPythonService()
    └→ Spawn: python test_runner.py
    └→ test_runner.run_tests()
    └→ For each test: Sandbox.execute() → executor.py
    └→ Extract method name, call with input
    └→ Compare output with expectedOutput

----- User clicks "Submit" -----

Practice.tsx (combine visible + hidden)
    ↓
submitCode() [IPC] with ALL test cases
    ↓
CodeExecutorService.executeCode()
    ↓
[Same execution flow as above, but with more test cases]
    ↓
DatabaseService.createCodeSubmission()
    ↓
Update user_progress (solved = true if all passed)
```

---

## 17. TEST CASE OUTPUT COMPARISON

### Python Service (test_runner.py)
```python
def _compare_outputs(self, expected: Any, actual: Any) -> bool:
    # Handle None
    if expected is None and actual is None:
        return True
    if expected is None or actual is None:
        return False

    # Handle floats with tolerance
    if isinstance(expected, float) and isinstance(actual, (int, float)):
        return abs(expected - actual) < 1e-9

    # Handle lists of floats (recursive)
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return False
        for exp_item, act_item in zip(expected, actual):
            # Recursive check with float tolerance
            ...

    # Direct comparison (exact match)
    return expected == actual
```

### TypeScript Service (codeExecutor.ts)
```typescript
private compareOutputs(actual: any, expected: any): boolean {
    // Deep equality check (JSON string comparison)
    return JSON.stringify(actual) === JSON.stringify(expected);
}
```

**Note**: TypeScript version uses exact JSON string matching, no float tolerance.

---

## 18. KNOWN LIMITATIONS & EDGE CASES

1. **Type Hints Not Auto-Imported**
   - Users must include their own imports
   - Could cause confusion with type-hinted signatures

2. **Hidden Test Cases Empty**
   - Currently no hidden test cases in production
   - Manual addition required

3. **Float Comparison Discrepancy**
   - Python service: Tolerance-based (1e-9)
   - TypeScript service: Exact JSON match
   - Could cause different results for floating-point problems

4. **Java/C++ Not Implemented**
   - Only placeholders in executor.py
   - Only Docker execution available (not local)

5. **Method Name Extraction Fragile**
   - Regex-based parsing of user code
   - May fail on unusual code formatting
   - Fallback uses introspection, but requires Solution class

6. **No Custom Test Case Storage**
   - User-created test cases not persisted
   - Only predefined test cases saved

7. **Test Results All-or-Nothing**
   - No partial credit for partial test cases
   - Either all pass or test fails

---

## 19. EXAMPLES: END-TO-END TEST CASE FLOW

### Example Question: "Two Sum"

#### In Database (leetcode_questions table):

```json
test_cases: [
  {"input": [[2, 7, 11, 15], 9], "expectedOutput": [0, 1]},
  {"input": [[3, 2, 4], 6], "expectedOutput": [1, 2]},
  {"input": [[3, 3], 6], "expectedOutput": [0, 1]}
]

hidden_test_cases: [
  {"input": [[1000000, -1000000], 0], "expectedOutput": [0, 1]},
  {"input": [[2, 2], 4], "expectedOutput": [0, 1]},
  {"input": [[1, 2, 3, 4, 5], 9], "expectedOutput": [3, 4]}
]
```

#### Run Code Flow:

1. User types solution:
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
```

2. Click "Run Code" button
3. Frontend sends: `{ code, language: 'python', testCases: [3 visible test cases] }`
4. Backend executes with test_runner.py
5. For each test case, extracts method `twoSum`, calls with `(*input)`
6. Returns results:
```json
{
  "status": "passed",
  "testResults": [
    {"passed": true, "input": [[2,7,11,15], 9], "actualOutput": [0,1], ...},
    {"passed": true, "input": [[3,2,4], 6], "actualOutput": [1,2], ...},
    {"passed": true, "input": [[3,3], 6], "actualOutput": [0,1], ...}
  ],
  "executionTime": 45,
  "memoryUsed": 256
}
```

#### Submit Code Flow:

1. Same user code
2. Click "Submit" button
3. Frontend combines: visible (3) + hidden (3) = 6 total test cases
4. Sends: `{ userId, questionId, code, language, customTestCases: [6 total] }`
5. Backend executes ALL 6 test cases with same process
6. Returns results with all 6 test cases
7. If status == "passed" (all 6 passed):
   - Save to `code_submissions` table
   - Update `user_progress`: solved = true
   - Generate AI feedback

---

## CONCLUSION

The Interview Prep Platform has a **complete infrastructure for hidden test cases**, but it's not yet in use because:

1. **Database schema**: Ready ✅
2. **Code execution**: Ready ✅
3. **Frontend integration**: Ready ✅
4. **Question data**: Needs population ❌

To activate hidden test cases:
1. Edit `/scripts/questions_data_full.py` 
2. Add `hidden_test_cases` arrays with 3-5 edge-case test cases per question
3. Run `python3 scripts/generate_seed_sql.py`
4. Reimport database: `sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql`

The framework is production-ready; it's just waiting for the hidden test case data.

