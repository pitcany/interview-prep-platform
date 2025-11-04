#!/usr/bin/env python3
"""
Code Executor Service
Executes Python code safely with resource limits and timeout.
"""

import sys
import json
import traceback
import signal
import threading
import multiprocessing
import queue
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
from typing import Any, Dict

try:
    import resource
except ImportError:  # pragma: no cover - not available on Windows
    resource = None


TIMEOUT_ERROR_MSG = "Code execution exceeded time limit"


class TimeoutException(Exception):
    """Raised when code execution exceeds time limit."""


def timeout_handler(signum, frame):
    """Signal handler for execution timeout."""
    raise TimeoutException(TIMEOUT_ERROR_MSG)


SUPPORTS_SIGALRM = hasattr(signal, "SIGALRM")

if SUPPORTS_SIGALRM:
    signal.signal(signal.SIGALRM, timeout_handler)


def set_resource_limits(max_memory_mb: int = 512):
    """Set resource limits for code execution."""
    if resource is None:
        warning = (
            "Warning: Resource module not available; "
            "skipping resource limits."
        )
        print(warning, file=sys.stderr)
        return

    try:
        # Set memory limit (in bytes)
        max_memory = max_memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (max_memory, max_memory))

        # Set CPU time limit (in seconds)
        resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    except Exception as e:
        print(f"Warning: Could not set resource limits: {e}", file=sys.stderr)


def _initialize_result() -> Dict[str, Any]:
    return {
        'success': False,
        'output': None,
        'stdout': '',
        'stderr': '',
        'error': None,
        'error_type': None
    }


def _timeout_result() -> Dict[str, Any]:
    result = _initialize_result()
    result['error'] = TIMEOUT_ERROR_MSG
    result['error_type'] = 'timeout'
    return result


def _execution_error_result(message: str) -> Dict[str, Any]:
    result = _initialize_result()
    result['error'] = message
    result['error_type'] = 'execution_error'
    return result


def _execute_user_code(code: str, test_input: Any) -> Dict[str, Any]:
    stdout_capture = StringIO()
    stderr_capture = StringIO()
    result = _initialize_result()

    try:
        exec_globals = {
            '__builtins__': __builtins__,
            'input_value': test_input
        }

        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code, exec_globals)

            # First, check if there's a Solution class (LeetCode style)
            solution_class = exec_globals.get('Solution')
            solution_func = None
            
            if solution_class and isinstance(solution_class, type):
                # Get all methods from the Solution class
                # In Python, instance methods are stored as functions in the class __dict__
                method_names = [
                    name for name, method in solution_class.__dict__.items()
                    if callable(method) and not name.startswith('_')
                ]
                
                # Common LeetCode method names to try
                # Note: 'solve' is NOT included here - LeetCode solutions don't use 'solve'
                common_methods = [
                    'twoSum', 'threeSum', 'maxProfit', 'findMedianSortedArrays',
                    'lengthOfLongestSubstring', 'longestPalindrome', 'reverse',
                    'myAtoi', 'isMatch', 'maxArea', 'intToRoman', 'romanToInt',
                    'longestCommonPrefix', 'isValid', 'mergeTwoLists', 'removeDuplicates',
                    'search', 'searchInsert', 'plusOne', 'addBinary', 'mySqrt',
                    'climbStairs', 'deleteDuplicates', 'merge', 'isSameTree',
                    'isSymmetric', 'maxDepth', 'levelOrder', 'sortedArrayToBST',
                    'inorderTraversal', 'preorderTraversal', 'postorderTraversal',
                    'hasPathSum', 'minDepth', 'isBalanced', 'flatten', 'connect',
                    'buildTree', 'numIslands', 'cloneGraph', 'canFinish', 'findOrder'
                ]
                
                # Try to find a method name in order of preference
                method_name = None
                for method in common_methods:
                    if method in method_names:
                        method_name = method
                        break
                
                # If no common method found, use the first method (excluding __init__)
                if method_name is None and method_names:
                    # Filter out __init__ if present
                    non_init_methods = [m for m in method_names if m != '__init__']
                    if non_init_methods:
                        method_name = non_init_methods[0]
                
                if method_name:
                    # Instantiate Solution class and get the method
                    try:
                        solution_instance = solution_class()
                        solution_func = getattr(solution_instance, method_name)
                        # Verify it's actually callable
                        if not callable(solution_func):
                            solution_func = None
                            method_name = None
                    except AttributeError:
                        # Method doesn't exist, reset and try fallback
                        solution_func = None
                        method_name = None
                
                # If we still don't have a method, try to use any available method
                if solution_func is None and method_names:
                    non_init_methods = [m for m in method_names if m != '__init__']
                    if non_init_methods:
                        try:
                            solution_instance = solution_class()
                            method_name = non_init_methods[0]
                            solution_func = getattr(solution_instance, method_name)
                            if not callable(solution_func):
                                solution_func = None
                        except AttributeError:
                            solution_func = None
            
            # If no Solution class found, look for standalone functions
            # Only do this if we didn't find a Solution class
            if solution_func is None and not (solution_class and isinstance(solution_class, type)):
                func_names = [
                    'solution', 'twoSum', 'threeSum', 'maxProfit',
                    'findMedianSortedArrays', 'lengthOfLongestSubstring',
                    'longestPalindrome', 'reverse', 'myAtoi', 'isMatch',
                    'maxArea', 'intToRoman', 'romanToInt', 'longestCommonPrefix'
                    # Note: 'solve' removed from here to avoid calling non-existent methods
                ]

                for func_name in func_names:
                    if (
                        func_name in exec_globals
                        and callable(exec_globals[func_name])
                    ):
                        solution_func = exec_globals[func_name]
                        break

                if solution_func is None:
                    for name, obj in exec_globals.items():
                        if callable(obj) and not name.startswith('_'):
                            solution_func = obj
                            break

            # Final check - if we still don't have a function, raise an error
            if solution_func is None:
                if solution_class and isinstance(solution_class, type):
                    # Try to get any method from Solution class as last resort
                    try:
                        solution_instance = solution_class()
                        # Get all methods using dir() and introspection
                        all_methods = [m for m in dir(solution_instance) 
                                     if not m.startswith('_') 
                                     and callable(getattr(solution_instance, m))]
                        if all_methods:
                            solution_func = getattr(solution_instance, all_methods[0])
                        else:
                            raise ValueError(
                                f"Solution class found but no callable methods found. "
                                f"Available attributes: {[m for m in dir(solution_instance) if not m.startswith('__')]}"
                            )
                    except Exception as e:
                        raise ValueError(
                            f"Solution class found but could not find or call any method. "
                            f"Error: {str(e)}"
                        )
                else:
                    raise ValueError("No callable function or Solution class method found in code")

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

    except MemoryError:
        result['error'] = "Memory limit exceeded"
        result['error_type'] = 'memory_error'

    except Exception as e:
        result['error'] = str(e)
        result['error_type'] = type(e).__name__
        result['traceback'] = traceback.format_exc()

    finally:
        result['stdout'] = stdout_capture.getvalue()
        result['stderr'] = stderr_capture.getvalue()

    return result


def _execution_worker(
    code: str,
    test_input: Any,
    result_queue: multiprocessing.Queue,
) -> None:
    try:
        result = _execute_user_code(code, test_input)
    except Exception as exc:  # pragma: no cover - defensive programming
        result = _execution_error_result(f"Executor worker failed: {exc}")
        result['traceback'] = traceback.format_exc()
    result_queue.put(result)


def _execute_code_in_subprocess(
    code: str,
    test_input: Any,
    timeout_seconds: int,
) -> Dict[str, Any]:
    result_queue: multiprocessing.Queue = multiprocessing.Queue()
    process = multiprocessing.Process(
        target=_execution_worker,
        args=(code, test_input, result_queue),
    )

    try:
        process.start()
        process.join(timeout_seconds)

        if process.is_alive():
            process.terminate()
            process.join()
            result = _timeout_result()
        else:
            try:
                result = result_queue.get_nowait()
            except queue.Empty:
                result = _execution_error_result(
                    "No result returned from execution process."
                )
    finally:
        result_queue.close()
        result_queue.join_thread()

    return result


def _can_use_unix_alarm() -> bool:
    return (
        SUPPORTS_SIGALRM
        and threading.current_thread() is threading.main_thread()
    )


def execute_code(
    code: str,
    test_input: Any,
    timeout_seconds: int = 10,
) -> Dict[str, Any]:
    """
    Execute Python code with a single test input.

    Args:
        code: Python code to execute
        test_input: Input value to pass to the function
        timeout_seconds: Maximum execution time in seconds

    Returns:
        Dict with execution results
    """
    if _can_use_unix_alarm():
        signal.alarm(timeout_seconds)
        try:
            return _execute_user_code(code, test_input)
        finally:
            signal.alarm(0)

    return _execute_code_in_subprocess(code, test_input, timeout_seconds)


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
