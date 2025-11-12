#!/usr/bin/env python3
"""
Verify that code execution is working correctly.
Run this AFTER restarting the app to ensure Python service works.
"""

import json
import subprocess
import sys
from pathlib import Path

def test_python_service():
    """Test the Python service directly"""
    print("🧪 Testing Python service...")

    test_data = {
        "code": """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []""",
        "testCases": [
            {"input": [[2, 7, 11, 15], 9], "expectedOutput": [0, 1]},
            {"input": [[3, 2, 4], 6], "expectedOutput": [1, 2]},
            {"input": [[3, 3], 6], "expectedOutput": [0, 1]}
        ],
        "language": "python",
        "timeout": 10,
        "maxMemory": 512
    }

    # Find python-service directory
    project_root = Path(__file__).parent.parent
    test_runner = project_root / "python-service" / "test_runner.py"

    if not test_runner.exists():
        print(f"❌ Python service not found at: {test_runner}")
        return False

    try:
        result = subprocess.run(
            ["python3", str(test_runner)],
            input=json.dumps(test_data),
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            print(f"❌ Python service failed with exit code {result.returncode}")
            print(f"   stderr: {result.stderr}")
            return False

        output = json.loads(result.stdout)

        if output.get("status") != "passed":
            print(f"❌ Tests failed: {output.get('error_message', 'Unknown error')}")
            return False

        passed_count = sum(1 for test in output.get("test_results", []) if test.get("passed"))
        total_count = len(output.get("test_results", []))

        print(f"✅ Python service working correctly!")
        print(f"   Tests passed: {passed_count}/{total_count}")
        return True

    except subprocess.TimeoutExpired:
        print("❌ Python service timed out")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse output: {e}")
        print(f"   stdout: {result.stdout[:200]}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_environment():
    """Check environment configuration"""
    print("\n🔍 Checking environment configuration...")

    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"

    if not env_file.exists():
        print("❌ .env file not found")
        return False

    with open(env_file) as f:
        env_content = f.read()

    # Check for SANDBOX_MODE=local
    if "SANDBOX_MODE=local" in env_content:
        print("✅ SANDBOX_MODE=local configured correctly")
        return True
    elif "SANDBOX_MODE=docker" in env_content:
        print("⚠️  SANDBOX_MODE=docker (requires Docker running)")
        return False
    else:
        print("❌ SANDBOX_MODE not configured in .env")
        return False

def main():
    print("=" * 60)
    print("Code Execution Verification")
    print("=" * 60)

    env_ok = check_environment()
    python_ok = test_python_service()

    print("\n" + "=" * 60)
    if env_ok and python_ok:
        print("✅ All checks passed!")
        print("\n📝 Next steps:")
        print("   1. Make sure the app is stopped (Ctrl+C)")
        print("   2. Restart: npm run dev")
        print("   3. Try submitting a solution in the app")
        print("   4. Should see '7/7 tests passed' for Two Sum")
        sys.exit(0)
    else:
        print("❌ Some checks failed")
        print("\n🔧 Troubleshooting:")
        if not env_ok:
            print("   - Set SANDBOX_MODE=local in .env")
            print("   - Restart the app after changing .env")
        if not python_ok:
            print("   - Check that python3 is installed")
            print("   - Verify python-service/ directory exists")
        sys.exit(1)

if __name__ == "__main__":
    main()
