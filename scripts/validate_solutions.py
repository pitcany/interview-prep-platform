#!/usr/bin/env python3
"""
Validation script for LeetCode solutions
Executes solutions against test cases and reports results
"""

import os
import re
import sys
from typing import List, Optional, Any


def extract_method_name(python_sig: str) -> str:
    """Extract method name from python signature string."""
    # Pattern: def methodName(self, ...
    match = re.search(r'def\s+(\w+)\s*\(', python_sig)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract method name from: {python_sig}")


def validate_solution(question: dict) -> tuple[bool, list[str]]:
    """
    Validate a single question's solution against its test cases.

    Returns:
        (all_passed, error_messages)
    """
    title = question['title']
    solution_code = question.get('solution_python', '')
    python_sig = question.get('python_sig', '')
    test_cases = question.get('test_cases', [])

    # Skip if placeholder solution
    if 'TODO: Implement solution' in solution_code:
        return False, [f"Skipped - placeholder solution"]

    errors = []

    try:
        # Extract method name
        method_name = extract_method_name(python_sig)

        # Execute solution code in isolated namespace
        namespace = {}
        exec(solution_code, namespace)

        # Create instance from isolated namespace
        solution = namespace['Solution']()

        # Verify method exists
        if not hasattr(solution, method_name):
            return False, [f"Method '{method_name}' not found in solution"]

        # Run test cases
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case['input']
            expected = test_case['expectedOutput']

            # Call the method with unpacked inputs
            method = getattr(solution, method_name)
            actual = method(*test_input)

            # Compare results
            if actual != expected:
                errors.append(
                    f"  Test {i} FAILED:\n"
                    f"    Input: {test_input}\n"
                    f"    Expected: {expected}\n"
                    f"    Got: {actual}"
                )

        return len(errors) == 0, errors

    except Exception as e:
        return False, [f"  Error: {str(e)}"]


def main():
    """Main validation entry point."""
    # Import questions data - use dynamic path resolution
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)
    from questions_data_full import LEETCODE_QUESTIONS

    # Questions to validate
    target_questions = [
        'Product of Array Except Self',
        'Maximum Subarray',
        'Number of Islands',
        'Coin Change',
        'Binary Tree Level Order Traversal',
        'Validate Binary Search Tree',
        'Longest Increasing Subsequence',
        'Course Schedule',
        'Clone Graph',
        'Trapping Rain Water'
    ]

    print("=" * 60)
    print("LeetCode Solutions Validation")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    for question in LEETCODE_QUESTIONS:
        if question['title'] not in target_questions:
            continue

        title = question['title']
        print(f"Testing: {title}")

        success, errors = validate_solution(question)

        if success:
            num_tests = len(question.get('test_cases', []))
            print(f"  ✓ All {num_tests} test cases passed")
            passed += 1
        else:
            print(f"  ✗ FAILED")
            for error in errors:
                print(error)
            failed += 1

        print()

    print("=" * 60)
    print(f"Summary: {passed}/{passed + failed} solutions passing")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
