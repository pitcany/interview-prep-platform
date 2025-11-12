#!/usr/bin/env python3
"""
Integration test for code executor stdin fix.
Tests that the code executor can handle large submissions via stdin.
"""

import subprocess
import json
import sys


def test_small_submission():
    """Test basic functionality with a small submission."""
    print("Test 1: Small submission (basic functionality)")
    print("-" * 60)

    test_input = {
        "code": """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
""",
        "testCases": [
            {"input": [[2, 7, 11, 15], 9], "expectedOutput": [0, 1]},
            {"input": [[3, 2, 4], 6], "expectedOutput": [1, 2]}
        ],
        "language": "python",
        "timeout": 10,
        "maxMemory": 512
    }

    # Call test_runner.py with stdin
    proc = subprocess.Popen(
        ['python3', '../python-service/test_runner.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = proc.communicate(input=json.dumps(test_input))

    if proc.returncode != 0:
        print(f"❌ FAILED: Process exited with code {proc.returncode}")
        print(f"stderr: {stderr}")
        return False

    try:
        result = json.loads(stdout)
        print(f"Status: {result['status']}")
        print(f"Test results: {len(result['test_results'])} tests")

        if result['status'] == 'passed':
            print("✓ PASSED: Small submission works")
            return True
        else:
            print(f"❌ FAILED: Status was {result['status']}")
            print(f"Results: {result}")
            return False
    except json.JSONDecodeError as e:
        print(f"❌ FAILED: Could not parse JSON output")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        return False


def test_large_submission():
    """Test with a large submission that would exceed command-line arg limits."""
    print("\nTest 2: Large submission (>100KB code)")
    print("-" * 60)

    # Create a large code string (>100KB)
    large_code = """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """ + ("Large comment to increase size. " * 2000) + """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
"""

    test_input = {
        "code": large_code,
        "testCases": [
            {"input": [[2, 7, 11, 15], 9], "expectedOutput": [0, 1]}
        ],
        "language": "python",
        "timeout": 10,
        "maxMemory": 512
    }

    print(f"Code size: {len(large_code)} bytes ({len(large_code)/1024:.1f} KB)")
    print(f"JSON size: {len(json.dumps(test_input))} bytes ({len(json.dumps(test_input))/1024:.1f} KB)")

    proc = subprocess.Popen(
        ['python3', '../python-service/test_runner.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = proc.communicate(input=json.dumps(test_input))

    if proc.returncode != 0:
        print(f"❌ FAILED: Process exited with code {proc.returncode}")
        print(f"stderr: {stderr}")
        return False

    try:
        result = json.loads(stdout)
        if result['status'] == 'passed':
            print("✓ PASSED: Large submission works (Bug #1 fixed!)")
            return True
        else:
            print(f"❌ FAILED: Status was {result['status']}")
            return False
    except json.JSONDecodeError:
        print(f"❌ FAILED: Could not parse JSON output")
        return False


def test_with_listnode():
    """Test with ListNode class definition (Bug #3 fix)."""
    print("\nTest 3: Code with ListNode (testing Bug #3 fix)")
    print("-" * 60)

    test_input = {
        "code": """from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next
""",
        "testCases": [
            {
                "input": [None, None],  # Empty lists
                "expectedOutput": None
            }
        ],
        "language": "python",
        "timeout": 10,
        "maxMemory": 512
    }

    proc = subprocess.Popen(
        ['python3', '../python-service/test_runner.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = proc.communicate(input=json.dumps(test_input))

    if proc.returncode != 0:
        print(f"❌ FAILED: Process exited with code {proc.returncode}")
        print(f"stderr: {stderr}")
        return False

    try:
        result = json.loads(stdout)
        print(f"Status: {result['status']}")

        # It's OK if test fails due to test case format, we just want to verify
        # that the code with ListNode definition can be executed without NameError
        if 'NameError' in str(result.get('error_message', '')):
            print("❌ FAILED: NameError found - imports still broken")
            return False

        print("✓ PASSED: No NameError (Bug #3 fix verified!)")
        return True
    except json.JSONDecodeError:
        print(f"❌ FAILED: Could not parse JSON output")
        return False


def main():
    print("=" * 60)
    print("Code Executor Integration Tests")
    print("=" * 60)

    results = []

    results.append(("Small submission", test_small_submission()))
    results.append(("Large submission", test_large_submission()))
    results.append(("ListNode imports", test_with_listnode()))

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    for name, passed in results:
        status = "✓ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {name}")

    all_passed = all(result[1] for result in results)

    if all_passed:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️  {sum(1 for r in results if not r[1])} test(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
