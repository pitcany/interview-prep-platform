#!/usr/bin/env python3
"""
Comprehensive verification script for both Local and Docker execution modes.
Tests that both modes work correctly with the same code and test cases.
"""

import json
import subprocess
import sys
import tempfile
import os
from pathlib import Path

def test_local_python():
    """Test local Python service"""
    print("🧪 Testing Local Python Mode...")

    project_root = Path(__file__).parent.parent
    test_runner = project_root / "python-service" / "test_runner.py"

    if not test_runner.exists():
        print(f"❌ Python service not found at: {test_runner}")
        return False

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

    try:
        result = subprocess.run(
            ["python3", str(test_runner)],
            input=json.dumps(test_data),
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            print(f"❌ Python service failed")
            print(f"   stderr: {result.stderr}")
            return False

        output = json.loads(result.stdout)

        if output.get("status") != "passed":
            print(f"❌ Tests failed: {output.get('error_message', 'Unknown')}")
            return False

        passed = sum(1 for t in output.get("test_results", []) if t.get("passed"))
        total = len(output.get("test_results", []))

        print(f"✅ Local Python mode working!")
        print(f"   Tests passed: {passed}/{total}")
        print(f"   Execution time: {output.get('execution_time', 0):.0f}ms")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_docker_mode():
    """Test Docker execution"""
    print("\n🐳 Testing Docker Mode...")

    # Check Docker is running
    try:
        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            timeout=5
        )
        if result.returncode != 0:
            print("❌ Docker daemon not running")
            print("   Start Docker Desktop and try again")
            return False
    except Exception:
        print("❌ Docker not available")
        return False

    # Check image exists
    result = subprocess.run(
        ["docker", "images", "-q", "interview-prep-python:latest"],
        capture_output=True,
        text=True
    )
    if not result.stdout.strip():
        print("❌ Docker image not built")
        print("   Run: cd docker && docker build -t interview-prep-python:latest -f python.Dockerfile python/")
        return False

    # Create test code with wrapper
    user_code = """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []"""

    test_input = [[2, 7, 11, 15], 9]
    expected_output = [0, 1]

    input_str = json.dumps(test_input)

    full_code = f'''
import json
import sys
from typing import List

{user_code}

test_input = json.loads('{input_str}')
sol = Solution()
result = sol.twoSum(*test_input)
print(json.dumps(result))
'''

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(full_code)
        temp_file = f.name

    try:
        # Run in Docker
        cmd = [
            'docker', 'run', '--rm',
            '-v', f'{os.path.dirname(temp_file)}:/code',
            '--memory', '512m',
            '--cpus', '1',
            '--network', 'none',
            'interview-prep-python:latest',
            'python3', f'/code/{os.path.basename(temp_file)}'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if result.returncode != 0:
            print(f"❌ Docker execution failed")
            print(f"   stderr: {result.stderr}")
            return False

        output = json.loads(result.stdout.strip())

        if output == expected_output:
            print(f"✅ Docker mode working!")
            print(f"   Test passed: {test_input} → {output}")
            return True
        else:
            print(f"❌ Output mismatch")
            print(f"   Expected: {expected_output}")
            print(f"   Got: {output}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)

def check_database():
    """Check database has hidden test cases"""
    print("\n💾 Checking Database...")

    try:
        project_root = Path(__file__).parent.parent
        db_path = Path.home() / "Library" / "Application Support" / "interview-prep-platform" / "interview-prep.db"

        if not db_path.exists():
            print("❌ Database not found")
            return False

        result = subprocess.run(
            ["sqlite3", str(db_path),
             "SELECT COUNT(*) as total, "
             "SUM(CASE WHEN json_array_length(hidden_test_cases) > 0 THEN 1 ELSE 0 END) as with_hidden "
             "FROM leetcode_questions;"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("❌ Failed to query database")
            return False

        total, with_hidden = map(int, result.stdout.strip().split('|'))

        if with_hidden == total and total > 0:
            print(f"✅ Database configured correctly!")
            print(f"   Questions with hidden tests: {with_hidden}/{total}")
            return True
        else:
            print(f"❌ Missing hidden test cases")
            print(f"   Questions with hidden tests: {with_hidden}/{total}")
            print("   Run: python3 scripts/update_db_with_hidden_tests.py")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 70)
    print("Comprehensive Verification: Local + Docker + Database")
    print("=" * 70)

    results = {
        "Database": check_database(),
        "Local Python": test_local_python(),
        "Docker": test_docker_mode()
    }

    print("\n" + "=" * 70)
    print("Summary:")
    print("=" * 70)

    for name, status in results.items():
        symbol = "✅" if status else "❌"
        print(f"{symbol} {name}: {'PASSED' if status else 'FAILED'}")

    all_passed = all(results.values())

    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 All systems operational!")
        print("\n📝 Both execution modes work correctly:")
        print("   • Local mode: Fast, for development")
        print("   • Docker mode: Secure, for production")
        print("\n🚀 Next steps:")
        print("   1. Choose mode in .env: SANDBOX_MODE=local or docker")
        print("   2. Restart app: npm run dev")
        print("   3. Submit a solution")
        print("   4. Should see '7/7 tests passed' for Two Sum")
        sys.exit(0)
    else:
        print("❌ Some systems need attention")
        print("\n🔧 Troubleshooting:")
        if not results["Database"]:
            print("   • Run: python3 scripts/update_db_with_hidden_tests.py")
        if not results["Local Python"]:
            print("   • Check python-service/ directory exists")
        if not results["Docker"]:
            print("   • Start Docker Desktop")
            print("   • Build images: cd docker && docker build -t interview-prep-python:latest -f python.Dockerfile python/")
        sys.exit(1)

if __name__ == "__main__":
    main()
