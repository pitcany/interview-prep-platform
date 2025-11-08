# Bug Fix: Code Execution Returning Null Values

## Problem
- Solutions were failing on all test cases
- All test results showed `actualOutput: null`
- Error: "docker: Cannot connect to the Docker daemon..."

## Root Cause Analysis

### Evidence from Database
Recent submission (ID: 1) shows:
```json
{
  "status": "failed",
  "test_results": [
    {
      "passed": false,
      "actualOutput": null,
      "error": "docker: Cannot connect to the Docker daemon at unix:///Users/yannik/.docker/run/docker.sock. Is the docker daemon running?"
    }
  ]
}
```

### Root Cause
The application was trying to use **Docker** for code execution even though:
1. `.env` file has `SANDBOX_MODE=local`
2. Python service exists and works correctly
3. Docker is not running

**Why:** Environment variables are loaded when Electron starts. Changes to `.env` require app restart.

## Solution

### Immediate Fix
**Restart the application** to load the updated environment variables:

```bash
# Stop the app (Ctrl+C if running)
# Then restart:
npm run dev
```

### Verification Steps

1. **Check environment is loaded correctly:**
   - Look for console output: `SANDBOX_MODE: local`
   - Look for: `CodeExecutor mode: Local Python`
   - Look for: `Execution mode: Python Service (local)`

2. **Test code execution:**
   - Open the app
   - Select "Two Sum" question
   - Paste this solution:
   ```python
   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           hashmap = {}
           for i, num in enumerate(nums):
               complement = target - num
               if complement in hashmap:
                   return [hashmap[complement], i]
               hashmap[num] = i
           return []
   ```
   - Click "Submit"
   - **Expected:** "7/7 tests passed" (3 visible + 4 hidden)

## Technical Details

### Execution Flow (When Working)
1. **Frontend** sends code + test cases via IPC
2. **Main Process** (electron/main.ts:194) receives submission
3. **CodeExecutorService** checks `SANDBOX_MODE` environment variable:
   - If `'local'` → use Python service (fast, local execution)
   - Otherwise → use Docker (secure but requires Docker daemon)
4. **Python Service** (python-service/test_runner.py):
   - Receives code + test cases via stdin
   - Executes code in sandbox
   - Returns results as JSON

### Why Docker Mode Failed
- `SANDBOX_MODE` wasn't set to `'local'` when app started
- CodeExecutorService defaulted to Docker mode
- Docker daemon not running → all executions failed

### Why Python Service Works
Verified independently:
```bash
echo '{"code": "...", "testCases": [...]}' | python3 python-service/test_runner.py
# ✅ Returns: {"status": "passed", "test_results": [...]}
```

## Environment Configuration

### Current .env Settings
```bash
SANDBOX_MODE=local          # ✅ Correct
LLM_PROVIDER=local          # For AI feedback
LLM_BASE_URL=http://localhost:11434/v1
LLM_MODEL=llama3.1:8b-instruct-q4_K_M
```

### When to Use Docker Mode
Docker mode provides better security but requires:
1. Docker Desktop installed and running
2. Docker images built: `cd docker && ./build-images.sh`
3. `.env` setting: `SANDBOX_MODE=docker`

For local development, `SANDBOX_MODE=local` is recommended (faster, no Docker required).

## Prevention

### For Users
**After modifying `.env` file, always restart the application:**
```bash
# Stop the app (Ctrl+C)
# Restart:
npm run dev
```

### For Developers
Add validation on startup to warn if configuration is problematic:
```typescript
// In electron/main.ts, after loadEnvironmentVariables()
if (!process.env.SANDBOX_MODE) {
  console.warn('⚠️  SANDBOX_MODE not set, defaulting to Docker');
  console.warn('   Set SANDBOX_MODE=local in .env for local Python execution');
}
```

## Related Issues

This fix complements the hidden test cases fix:
1. **Hidden tests fix:** Added test data to database
2. **This fix:** Ensured code execution works at all

Both were needed for submissions to work correctly.

## Files Involved

- ✅ `.env` - Already configured correctly
- ✅ `electron/main.ts:10-51` - Environment loading (works correctly)
- ✅ `electron/services/codeExecutor.ts:35-64` - Checks SANDBOX_MODE
- ✅ `python-service/test_runner.py` - Executes code (works correctly)

**No code changes needed - just restart the app!**
