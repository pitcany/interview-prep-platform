#!/usr/bin/env python3
"""
Verification script using the actual app's executor service.
This ensures we test solutions exactly as the app does.
"""

import sys
import os

# Add python-service to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python-service'))

from executor import execute_code
from questions_data_full import LEETCODE_QUESTIONS
from typing import List, Dict, Any


def compare_outputs(expected: Any, actual: Any) -> tuple[bool, str]:
    """
    Compare expected and actual outputs.
    Returns (is_equal, error_message)
    """
    # Handle None cases
    if expected is None and actual is None:
        return True, ""
    if expected is None or actual is None:
        return False, f"Expected {expected}, got {actual}"

    # Handle list outputs (including nested lists)
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return False, f"Length mismatch: expected {len(expected)}, got {len(actual)}"

        # For list of lists (like combinations, permutations), try order-independent comparison
        if expected and isinstance(expected[0], list):
            sorted_expected = sorted([sorted(x) if isinstance(x, list) else [x] for x in expected])
            sorted_actual = sorted([sorted(x) if isinstance(x, list) else [x] for x in actual])
            if sorted_expected == sorted_actual:
                return True, ""

        # Try direct comparison
        if expected == actual:
            return True, ""

        return False, f"Expected {expected}, got {actual}"

    # Direct comparison for other types
    if expected == actual:
        return True, ""

    return False, f"Expected {expected}, got {actual}"


def verify_question(question: Dict[str, Any], question_num: int) -> Dict[str, Any]:
    """
    Verify all test cases for a single question using the app's executor.
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
        test_input = test_case.get('input')
        expected_output = test_case.get('expectedOutput')

        # Execute using the app's executor
        result = execute_code(solution, test_input, timeout_seconds=10)

        if not result.get('success'):
            failed_tests.append({
                'test_num': i + 1,
                'input': test_input,
                'expected': expected_output,
                'error': result.get('error', 'Unknown error'),
                'error_type': result.get('error_type', 'unknown')
            })
        else:
            actual_output = result.get('output')
            is_equal, error_msg = compare_outputs(expected_output, actual_output)

            if is_equal:
                passed_tests += 1
            else:
                failed_tests.append({
                    'test_num': i + 1,
                    'input': test_input,
                    'expected': expected_output,
                    'actual': actual_output,
                    'error': error_msg
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
    print("SOLUTION VERIFICATION REPORT (Using App's Executor)")
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
            for failure in result['failures'][:3]:  # Show max 3 failures per question
                if 'actual' in failure:
                    print(f"     Test {failure['test_num']}: {failure['error']}")
                else:
                    error_preview = failure['error'][:100] + '...' if len(failure['error']) > 100 else failure['error']
                    print(f"     Test {failure['test_num']}: {error_preview}")
            if result['failed'] > 3:
                print(f"     ... and {result['failed'] - 3} more failures")
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
