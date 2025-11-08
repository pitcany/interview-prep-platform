#!/usr/bin/env python3
"""
Test Docker execution with the same wrapper code that codeExecutor.ts uses.
This simulates exactly what happens when Docker mode is enabled.
"""

import subprocess
import json
import tempfile
import os

def test_docker_execution():
    """Test Docker execution end-to-end"""

    # User's solution code
    user_code = '''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []'''

    # Test case
    test_case = {
        "input": [[2, 7, 11, 15], 9],
        "expectedOutput": [0, 1]
    }

    # This is the wrapper code that codeExecutor.ts generates
    input_str = json.dumps(test_case["input"])
    escaped_code = user_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

    full_code = f'''
import json
import sys
from typing import List, Optional, Dict, Set, Tuple

# Define common data structures used in LeetCode problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

{user_code}

# Test case input
test_input = json.loads('{input_str.replace("'", "\\'")}')

# Execute the solution
try:
    sol = Solution()

    # Get all available methods from Solution class
    all_methods = [m for m in dir(sol) if not m.startswith('_') and callable(getattr(sol, m))]

    if not all_methods:
        raise AttributeError("Solution class has no callable methods")

    method_name = 'twoSum'  # For this test

    # Prepare input
    processed_input = test_input

    # Call the method
    method = getattr(sol, method_name)
    if isinstance(processed_input, list) and len(processed_input) > 0:
        result = method(*processed_input)
    else:
        result = method(processed_input)

    print(json.dumps(result))
except Exception as e:
    import traceback
    print(json.dumps({{"error": str(e), "error_type": type(e).__name__, "traceback": traceback.format_exc()}}))
    sys.exit(1)
'''

    print("🧪 Testing Docker execution...")
    print(f"   User code length: {len(user_code)} chars")
    print(f"   Wrapper code length: {len(full_code)} chars")

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(full_code)
        temp_file = f.name

    try:
        # Run in Docker (same command as codeExecutor.ts)
        cmd = [
            'docker', 'run', '--rm',
            '-v', f'{os.path.dirname(temp_file)}:/code',
            '--memory', '512m',
            '--cpus', '1',
            '--network', 'none',
            'interview-prep-python:latest',
            'python3', f'/code/{os.path.basename(temp_file)}'
        ]

        print(f"   Docker command: {' '.join(cmd[:4])} ...")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            print(f"❌ Docker execution failed!")
            print(f"   Exit code: {result.returncode}")
            print(f"   stderr: {result.stderr}")
            return False

        output = json.loads(result.stdout.strip())
        expected = test_case["expectedOutput"]

        if output == expected:
            print(f"✅ Docker execution successful!")
            print(f"   Input: {test_case['input']}")
            print(f"   Expected: {expected}")
            print(f"   Got: {output}")
            return True
        else:
            print(f"❌ Output mismatch!")
            print(f"   Expected: {expected}")
            print(f"   Got: {output}")
            return False

    except subprocess.TimeoutExpired:
        print("❌ Docker execution timed out")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse output: {e}")
        print(f"   stdout: {result.stdout[:200]}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    finally:
        # Cleanup
        if os.path.exists(temp_file):
            os.unlink(temp_file)

if __name__ == "__main__":
    print("=" * 60)
    print("Docker Execution Test")
    print("=" * 60)
    print()

    success = test_docker_execution()

    print()
    print("=" * 60)
    if success:
        print("✅ Docker mode is working correctly!")
        print()
        print("📝 To use Docker mode:")
        print("   1. Set SANDBOX_MODE=docker in .env")
        print("   2. Restart the app: npm run dev")
        print("   3. Docker will be used for code execution")
        exit(0)
    else:
        print("❌ Docker mode test failed")
        exit(1)
