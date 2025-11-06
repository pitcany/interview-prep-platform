#!/usr/bin/env python3
"""Test the complete flow through test_runner.py as Electron would call it."""

import subprocess
import json

# The solution from the database
solution_code = '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next'''

# Test cases from database (format as Electron sends them)
input_data = {
    'code': solution_code,
    'testCases': [
        {'input': [[1, 2, 4], [1, 3, 4]], 'expectedOutput': [1, 1, 2, 3, 4, 4]},
        {'input': [[], []], 'expectedOutput': []},
        {'input': [[], [0]], 'expectedOutput': [0]}
    ],
    'language': 'python',
    'timeout': 10,
    'maxMemory': 512
}

print("=" * 80)
print("Testing complete flow through test_runner.py")
print("=" * 80)
print(f"Test cases: {len(input_data['testCases'])}")
print()

# Call test_runner.py as Electron does
test_runner_path = '/home/yannik/Work/interview-prep-platform/.worktrees/experimental/python-service/test_runner.py'
input_json = json.dumps(input_data)

result = subprocess.run(
    ['python3', test_runner_path],
    input=input_json,
    capture_output=True,
    text=True,
    timeout=15
)

print("Return code:", result.returncode)
print()

if result.returncode == 0:
    print("✓ Process completed successfully")
else:
    print("✗ Process failed with code:", result.returncode)

print()
print("STDOUT:")
print(result.stdout)
print()
print("STDERR:")
print(result.stderr)
print()

if result.stdout:
    try:
        output = json.loads(result.stdout)
        print("Parsed output:")
        print(json.dumps(output, indent=2))
        print()

        if output.get('status') == 'passed':
            print("✓ All tests passed!")
        elif output.get('status') == 'failed':
            print("✗ Some tests failed")
            for i, test_result in enumerate(output.get('test_results', [])):
                print(f"  Test {i+1}:", "PASS" if test_result['passed'] else "FAIL")
                if not test_result['passed']:
                    print(f"    Input: {test_result['input']}")
                    print(f"    Expected: {test_result['expectedOutput']}")
                    print(f"    Actual: {test_result['actualOutput']}")
                    if test_result.get('error'):
                        print(f"    Error: {test_result['error']}")
        else:
            print(f"Status: {output.get('status')}")
            print(f"Error: {output.get('error_message')}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
