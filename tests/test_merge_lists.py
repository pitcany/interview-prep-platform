#!/usr/bin/env python3
"""Test script to reproduce Merge Two Sorted Lists execution."""

import sys
import json

# Add python-service to path
sys.path.insert(0, '/home/yannik/Work/interview-prep-platform/.worktrees/experimental/python-service')

from executor import execute_code

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

# Test case from database
test_input = [[1, 2, 4], [1, 3, 4]]
expected_output = [1, 1, 2, 3, 4, 4]

print("=" * 80)
print("Testing Merge Two Sorted Lists")
print("=" * 80)
print(f"Input: {test_input}")
print(f"Expected: {expected_output}")
print()

# Execute
result = execute_code(solution_code, test_input, timeout_seconds=5)

print("Result:")
print(json.dumps(result, indent=2))
print()

if result['success']:
    print(f"✓ Execution successful")
    print(f"  Output: {result['output']}")
    if result['output'] == expected_output:
        print(f"  ✓ Output matches expected!")
    else:
        print(f"  ✗ Output mismatch!")
        print(f"    Expected: {expected_output}")
        print(f"    Got:      {result['output']}")
else:
    print(f"✗ Execution failed")
    print(f"  Error: {result.get('error')}")
    print(f"  Error type: {result.get('error_type')}")
    if 'traceback' in result:
        print(f"  Traceback:")
        print(result['traceback'])

print()
print("stdout:", result.get('stdout', ''))
print("stderr:", result.get('stderr', ''))
