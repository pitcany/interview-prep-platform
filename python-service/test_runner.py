#!/usr/bin/env python3
"""
Test Runner Service
Runs multiple test cases against submitted code and reports results.
"""

import sys
import json
import time
from typing import List, Dict, Any
from sandbox import Sandbox


class TestRunner:
    """
    Manages execution of multiple test cases against code submissions.
    """

    def __init__(self, max_memory_mb: int = 512, timeout_seconds: int = 10):
        self.max_memory_mb = max_memory_mb
        self.timeout_seconds = timeout_seconds

    def run_tests(self, code: str, test_cases: List[Dict[str, Any]], language: str = 'python') -> Dict[str, Any]:
        """
        Run all test cases against the provided code.

        Args:
            code: Source code to test
            test_cases: List of test cases with 'input' and 'expectedOutput'
            language: Programming language

        Returns:
            Complete test results with pass/fail status
        """
        results = {
            'status': 'passed',
            'test_results': [],
            'execution_time': 0,
            'memory_used': 0,
            'error_message': None
        }

        start_time = time.time()
        total_memory = 0
        memory_count = 0

        with Sandbox(self.max_memory_mb, self.timeout_seconds) as sandbox:
            for i, test_case in enumerate(test_cases):
                test_input = test_case.get('input')
                expected_output = test_case.get('expectedOutput')

                # Execute test case
                test_start = time.time()
                execution_result = sandbox.execute(code, test_input, language)
                test_duration = (time.time() - test_start) * 1000  # Convert to ms

                # Build test result
                test_result = {
                    'passed': False,
                    'input': test_input,
                    'expectedOutput': expected_output,
                    'actualOutput': None,
                    'executionTime': test_duration,
                    'error': None
                }

                if execution_result.get('success'):
                    actual_output = execution_result.get('output')
                    test_result['actualOutput'] = actual_output

                    # Compare outputs
                    test_result['passed'] = self._compare_outputs(expected_output, actual_output)

                    # Track memory (estimate based on output size)
                    if isinstance(actual_output, str):
                        memory_count += 1
                        total_memory += len(actual_output) * 2  # Rough estimate in bytes

                else:
                    # Test failed with error
                    test_result['error'] = execution_result.get('error', 'Unknown error')
                    test_result['actualOutput'] = execution_result.get('stdout', '')
                    results['status'] = 'failed'

                    if execution_result.get('error_type') == 'timeout':
                        results['status'] = 'timeout'
                        results['error_message'] = 'Code execution timed out'
                    elif execution_result.get('error_type') == 'memory_error':
                        results['status'] = 'error'
                        results['error_message'] = 'Memory limit exceeded'
                    else:
                        results['error_message'] = test_result['error']

                results['test_results'].append(test_result)

                # If any test fails, mark overall status as failed
                if not test_result['passed'] and results['status'] == 'passed':
                    results['status'] = 'failed'

        # Calculate total execution time
        results['execution_time'] = (time.time() - start_time) * 1000  # ms

        # Calculate average memory usage (rough estimate)
        if memory_count > 0:
            results['memory_used'] = int(total_memory / memory_count / 1024)  # KB
        else:
            results['memory_used'] = 0

        return results

    def _compare_outputs(self, expected: Any, actual: Any) -> bool:
        """
        Compare expected and actual outputs with tolerance for floating point.

        Args:
            expected: Expected output value
            actual: Actual output value

        Returns:
            True if outputs match
        """
        # Handle None
        if expected is None and actual is None:
            return True
        if expected is None or actual is None:
            return False

        # Handle floats with tolerance
        if isinstance(expected, float) and isinstance(actual, (int, float)):
            return abs(expected - actual) < 1e-9

        # Handle lists of floats
        if isinstance(expected, list) and isinstance(actual, list):
            if len(expected) != len(actual):
                return False

            for exp_item, act_item in zip(expected, actual):
                if isinstance(exp_item, float) and isinstance(act_item, (int, float)):
                    if abs(exp_item - act_item) >= 1e-9:
                        return False
                elif isinstance(exp_item, list):
                    if not self._compare_outputs(exp_item, act_item):
                        return False
                else:
                    if exp_item != act_item:
                        return False
            return True

        # Direct comparison for everything else
        return expected == actual


def main():
    """CLI interface for test runner."""
    try:
        # Parse input from stdin (avoids command line arg size limits)
        input_json = sys.stdin.read()
        if not input_json:
            print(json.dumps({
                'status': 'error',
                'error_message': 'No input provided on stdin',
                'test_results': []
            }))
            sys.exit(1)

        input_data = json.loads(input_json)
        code = input_data.get('code', '')
        test_cases = input_data.get('testCases', [])
        language = input_data.get('language', 'python')
        timeout = input_data.get('timeout', 10)
        max_memory = input_data.get('maxMemory', 512)

        # Run tests
        runner = TestRunner(max_memory, timeout)
        results = runner.run_tests(code, test_cases, language)

        # Output results
        print(json.dumps(results))

    except Exception as e:
        print(json.dumps({
            'status': 'error',
            'error_message': str(e),
            'test_results': []
        }))
        sys.exit(1)


if __name__ == '__main__':
    main()
