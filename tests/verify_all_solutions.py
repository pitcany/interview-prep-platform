#!/usr/bin/env python3
"""
Verification script to test all question solutions against their test cases.
This ensures every provided solution passes ALL test cases.
"""

import sys
import json
from typing import Any, List, Dict
from questions_data_full import LEETCODE_QUESTIONS, ML_QUESTIONS


def list_to_linkedlist(arr, ListNode):
    """Convert a list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """Convert a linked list to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_tree(arr, TreeNode):
    """Convert a list to a binary tree (level-order)."""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    """Convert a binary tree to a list (level-order)."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def run_test_case(solution_code: str, test_case: Dict[str, Any], title: str) -> tuple[bool, str]:
    """
    Execute a solution against a single test case.
    Returns (success, error_message)
    """
    try:
        # Create a namespace for execution with common imports
        from typing import List, Optional

        # Define common data structures
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        class Node:
            def __init__(self, val=0, neighbors=None):
                self.val = val
                self.neighbors = neighbors if neighbors is not None else []

        namespace = {
            'List': List,
            'Optional': Optional,
            'ListNode': ListNode,
            'TreeNode': TreeNode,
            'Node': Node,
        }

        # Execute the solution code to define the Solution class
        exec(solution_code, namespace)

        # Create an instance of the Solution class
        solution_instance = namespace['Solution']()

        # Extract input and expected output
        test_input = test_case['input']
        expected_output = test_case['expectedOutput']

        # Determine the method name from the solution code
        # Most solutions have a method like twoSum, isValid, etc.
        import re
        method_match = re.search(r'def (\w+)\(self', solution_code)
        if not method_match:
            return False, "Could not find method name in solution"

        method_name = method_match.group(1)
        method = getattr(solution_instance, method_name)

        # Call the method with the test input
        if isinstance(test_input, list):
            actual_output = method(*test_input)
        elif isinstance(test_input, dict):
            actual_output = method(**test_input)
        else:
            actual_output = method(test_input)

        # Compare output
        # Handle different types of comparisons
        if isinstance(expected_output, (list, tuple)):
            # For lists, we might need to handle order-independence or nested structures
            if actual_output != expected_output:
                # Try comparing as sets for unordered comparison
                try:
                    if isinstance(actual_output, list) and isinstance(expected_output, list):
                        if len(actual_output) == len(expected_output):
                            # For nested lists, try sorting
                            sorted_actual = sorted([sorted(x) if isinstance(x, list) else x for x in actual_output])
                            sorted_expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected_output])
                            if sorted_actual == sorted_expected:
                                return True, ""
                except:
                    pass

                return False, f"Expected {expected_output}, got {actual_output}"
        else:
            if actual_output != expected_output:
                return False, f"Expected {expected_output}, got {actual_output}"

        return True, ""

    except Exception as e:
        return False, f"Runtime error: {str(e)}"


def verify_question(question: Dict[str, Any], question_num: int) -> Dict[str, Any]:
    """
    Verify all test cases for a single question.
    Returns a dict with results.
    """
    title = question.get('title', f'Question {question_num}')
    solution = question.get('solution_python', '')
    test_cases = question.get('test_cases', [])

    if not solution:
        return {
            'title': title,
            'status': 'SKIPPED',
            'reason': 'No Python solution provided'
        }

    if not test_cases:
        return {
            'title': title,
            'status': 'SKIPPED',
            'reason': 'No test cases provided'
        }

    failed_tests = []
    passed_tests = 0

    for i, test_case in enumerate(test_cases):
        success, error = run_test_case(solution, test_case, title)
        if success:
            passed_tests += 1
        else:
            failed_tests.append({
                'test_num': i + 1,
                'input': test_case.get('input'),
                'expected': test_case.get('expectedOutput'),
                'error': error
            })

    if failed_tests:
        return {
            'title': title,
            'status': 'FAILED',
            'passed': passed_tests,
            'failed': len(failed_tests),
            'total': len(test_cases),
            'failures': failed_tests
        }
    else:
        return {
            'title': title,
            'status': 'PASSED',
            'passed': passed_tests,
            'total': len(test_cases)
        }


def main():
    """Run verification on all questions."""
    print("=" * 80)
    print("SOLUTION VERIFICATION REPORT")
    print("=" * 80)
    print()

    all_results = []

    # Verify LeetCode questions
    print(f"Verifying {len(LEETCODE_QUESTIONS)} LeetCode questions...")
    print()

    for i, question in enumerate(LEETCODE_QUESTIONS, 1):
        result = verify_question(question, i)
        all_results.append(result)

        # Print result
        status_symbol = "✓" if result['status'] == 'PASSED' else "✗" if result['status'] == 'FAILED' else "○"
        print(f"{status_symbol} [{i:2d}] {result['title']:<50} {result['status']}")

        if result['status'] == 'FAILED':
            print(f"     Failed {result['failed']}/{result['total']} test cases:")
            for failure in result['failures']:
                print(f"     Test {failure['test_num']}: {failure['error']}")
            print()

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    passed = sum(1 for r in all_results if r['status'] == 'PASSED')
    failed = sum(1 for r in all_results if r['status'] == 'FAILED')
    skipped = sum(1 for r in all_results if r['status'] == 'SKIPPED')

    print(f"Total questions: {len(all_results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    print()

    if failed > 0:
        print("⚠️  ATTENTION: Some solutions are failing their test cases!")
        print("   Please fix the following questions:")
        for result in all_results:
            if result['status'] == 'FAILED':
                print(f"   - {result['title']}")
        sys.exit(1)
    else:
        print("✓ All solutions pass their test cases!")
        sys.exit(0)


if __name__ == "__main__":
    main()
