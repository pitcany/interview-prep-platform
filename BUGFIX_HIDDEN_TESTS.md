# Bug Fix: Hidden Test Cases Not Running

## Problem
- Solutions were not being tested against hidden test cases
- All submissions only ran against visible test cases (3-4 tests)
- Hidden test cases existed in codebase but were NOT in the database

## Root Cause
Database had `hidden_test_cases = []` (empty array) for all questions, even though:
1. The schema supported it (`hidden_test_cases TEXT` column)
2. Scripts existed to populate the data (`update_db_with_hidden_tests.py`)
3. Frontend code correctly combined visible + hidden test cases
4. Python executor properly ran all provided test cases

**The scripts were simply never executed during setup.**

## Solution
Ran the database update scripts to populate hidden test cases:

```bash
# Updated 39 core questions
python3 scripts/update_db_with_hidden_tests.py

# Updated remaining 24 questions
python3 scripts/add_remaining_hidden_tests.py
```

## Verification

### Database Status
- **Before:** 0/51 questions had hidden test cases
- **After:** 51/51 questions have hidden test cases ✅

### Test Case Counts
```
Total questions: 51
Questions with hidden tests: 51
Questions without hidden tests: 0
```

### Example Questions
- Two Sum: 3 visible + 4 hidden = 7 total tests
- Valid Parentheses: 4 visible + 5 hidden = 9 total tests
- Best Time to Buy and Sell Stock: 2 visible + 5 hidden = 7 total tests

## How It Works

### Data Flow
1. **Frontend (Practice.tsx:168-180):**
   - Fetches question details including `hidden_test_cases`
   - Parses both visible and hidden test cases
   - Combines into `allTestCases` array
   - Passes to `api.submitCode()`

2. **IPC Handler (electron/main.ts:194-221):**
   - Receives `customTestCases` from submission
   - Passes ALL test cases to `codeExecutor.executeCode()`

3. **Code Executor (electron/services/codeExecutor.ts):**
   - Runs Python service with ALL test cases
   - Returns results for each test

4. **Python Service (python-service/test_runner.py):**
   - Executes code against each test case
   - Returns pass/fail for all tests

## Testing Instructions

### Manual Test
1. Start the application: `npm run dev`
2. Select a question (e.g., "Two Sum")
3. Write a correct solution
4. Click "Submit" (NOT "Run")
5. **Expected:** Should see "X/Y tests passed" where Y > visible test count
6. Example: "Two Sum" should show "7/7 tests passed" (3 visible + 4 hidden)

### Verify Hidden Tests Don't Leak
- Hidden test case inputs/outputs should NOT be shown to users
- Only pass/fail status for the total count

## Files Modified
- Database: `~/Library/Application Support/interview-prep-platform/interview-prep.db`

## Files Involved (No code changes needed)
- ✅ `database/schema.sql` - Schema already supported hidden tests
- ✅ `src/pages/Practice.tsx` - Already combined visible + hidden
- ✅ `electron/main.ts` - Already passed all test cases
- ✅ `electron/services/codeExecutor.ts` - Already ran all tests
- ✅ `python-service/test_runner.py` - Already executed all tests
- ✅ `scripts/update_db_with_hidden_tests.py` - Had all the data
- ✅ `scripts/add_remaining_hidden_tests.py` - Had remaining data

**The entire system was already built correctly - just needed data!**

## Prevention
Add to setup instructions in CLAUDE.md:
```bash
# After database initialization
python3 scripts/update_db_with_hidden_tests.py
python3 scripts/add_remaining_hidden_tests.py
```

Or combine into a single setup script that runs all database initialization steps.
