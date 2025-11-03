#!/usr/bin/env python3
"""
Code Executor Service
Executes Python code safely with resource limits and timeout.
"""

import sys
import json
import traceback
import resource
import signal
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
from typing import Any, Dict, List


class TimeoutException(Exception):
    """Raised when code execution exceeds time limit."""
    pass


def timeout_handler(signum, frame):
    """Signal handler for execution timeout."""
    raise TimeoutException("Code execution exceeded time limit")


def set_resource_limits(max_memory_mb: int = 512):
    """Set resource limits for code execution."""
    try:
        # Set memory limit (in bytes)
        max_memory = max_memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (max_memory, max_memory))

        # Set CPU time limit (in seconds)
        resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    except Exception as e:
        print(f"Warning: Could not set resource limits: {e}", file=sys.stderr)


def execute_code(code: str, test_input: Any, timeout_seconds: int = 10) -> Dict[str, Any]:
    """
    Execute Python code with a single test input.

    Args:
        code: Python code to execute
        test_input: Input value to pass to the function
        timeout_seconds: Maximum execution time in seconds

    Returns:
        Dict with execution results
    """
    # Set up timeout alarm
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)

    # Capture stdout and stderr
    stdout_capture = StringIO()
    stderr_capture = StringIO()

    result = {
        'success': False,
        'output': None,
        'stdout': '',
        'stderr': '',
        'error': None,
        'error_type': None
    }

    try:
        # Create restricted execution environment
        exec_globals = {
            '__builtins__': __builtins__,
            'input_value': test_input
        }

        # Redirect output streams
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            # Execute the code
            exec(code, exec_globals)

            # Try to find and call the solution function
            # Look for common function names
            func_names = ['solution', 'solve', 'twoSum', 'threeSum', 'maxProfit',
                         'findMedianSortedArrays', 'lengthOfLongestSubstring',
                         'longestPalindrome', 'reverse', 'myAtoi', 'isMatch',
                         'maxArea', 'intToRoman', 'romanToInt', 'longestCommonPrefix']

            solution_func = None
            for func_name in func_names:
                if func_name in exec_globals and callable(exec_globals[func_name]):
                    solution_func = exec_globals[func_name]
                    break

            # If no standard function found, look for any callable
            if solution_func is None:
                for name, obj in exec_globals.items():
                    if callable(obj) and not name.startswith('_'):
                        solution_func = obj
                        break

            if solution_func is None:
                raise ValueError("No callable function found in code")

            # Execute the function with test input
            if isinstance(test_input, dict):
                output = solution_func(**test_input)
            elif isinstance(test_input, (list, tuple)):
                output = solution_func(*test_input)
            else:
                output = solution_func(test_input)

            result['success'] = True
            result['output'] = output

    except TimeoutException as e:
        result['error'] = str(e)
        result['error_type'] = 'timeout'

    except MemoryError as e:
        result['error'] = "Memory limit exceeded"
        result['error_type'] = 'memory_error'

    except Exception as e:
        result['error'] = str(e)
        result['error_type'] = type(e).__name__
        result['traceback'] = traceback.format_exc()

    finally:
        # Cancel the alarm
        signal.alarm(0)

        # Capture output
        result['stdout'] = stdout_capture.getvalue()
        result['stderr'] = stderr_capture.getvalue()

    return result


def main():
    """Main entry point for the executor service."""
    if len(sys.argv) < 2:
        print(json.dumps({
            'error': 'Usage: executor.py <input_json>',
            'success': False
        }))
        sys.exit(1)

    try:
        # Parse input JSON
        input_data = json.loads(sys.argv[1])
        code = input_data.get('code', '')
        test_input = input_data.get('input')
        timeout = input_data.get('timeout', 10)
        max_memory = input_data.get('max_memory', 512)

        # Set resource limits
        set_resource_limits(max_memory)

        # Execute code
        result = execute_code(code, test_input, timeout)

        # Output result as JSON
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__,
            'traceback': traceback.format_exc()
        }))
        sys.exit(1)


if __name__ == '__main__':
    main()
