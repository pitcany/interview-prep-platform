#!/usr/bin/env python3
"""
Security Sandbox Wrapper
Provides additional security layers for code execution.
"""

import sys
import os
import subprocess
import json
import tempfile
from pathlib import Path
from typing import Dict, Any


class Sandbox:
    """
    Sandbox for executing untrusted code with security restrictions.
    """

    def __init__(self, max_memory_mb: int = 512, timeout_seconds: int = 10):
        self.max_memory_mb = max_memory_mb
        self.timeout_seconds = timeout_seconds
        self.temp_dir = tempfile.mkdtemp(prefix='interview-prep-')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup temp directory
        self._cleanup()

    def _cleanup(self):
        """Remove temporary files."""
        try:
            import shutil
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Warning: Could not clean up temp directory: {e}", file=sys.stderr)

    def execute(self, code: str, test_input: Any, language: str = 'python') -> Dict[str, Any]:
        """
        Execute code in sandboxed environment.

        Args:
            code: Source code to execute
            test_input: Input for the test case
            language: Programming language (python, java, cpp)

        Returns:
            Execution result dictionary
        """
        if language == 'python':
            return self._execute_python(code, test_input)
        elif language == 'java':
            return self._execute_java(code, test_input)
        elif language == 'cpp':
            return self._execute_cpp(code, test_input)
        else:
            return {
                'success': False,
                'error': f'Unsupported language: {language}',
                'error_type': 'UnsupportedLanguage'
            }

    def _execute_python(self, code: str, test_input: Any) -> Dict[str, Any]:
        """Execute Python code using executor.py."""
        executor_path = Path(__file__).parent / 'executor.py'

        input_data = {
            'code': code,
            'input': test_input,
            'timeout': self.timeout_seconds,
            'max_memory': self.max_memory_mb
        }

        try:
            result = subprocess.run(
                [sys.executable, str(executor_path), json.dumps(input_data)],
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds + 2  # Extra buffer for subprocess
            )

            if result.returncode != 0 and not result.stdout:
                return {
                    'success': False,
                    'error': result.stderr or 'Execution failed',
                    'error_type': 'ExecutionError',
                    'returncode': result.returncode
                }

            # Parse JSON output
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return {
                    'success': False,
                    'error': f'Invalid JSON output: {result.stdout}',
                    'error_type': 'JSONDecodeError',
                    'stdout': result.stdout,
                    'stderr': result.stderr
                }

        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Code execution timed out',
                'error_type': 'timeout'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'error_type': type(e).__name__
            }

    def _execute_java(self, code: str, test_input: Any) -> Dict[str, Any]:
        """Execute Java code (placeholder for future implementation)."""
        return {
            'success': False,
            'error': 'Java execution not yet implemented',
            'error_type': 'NotImplemented'
        }

    def _execute_cpp(self, code: str, test_input: Any) -> Dict[str, Any]:
        """Execute C++ code (placeholder for future implementation)."""
        return {
            'success': False,
            'error': 'C++ execution not yet implemented',
            'error_type': 'NotImplemented'
        }


def main():
    """CLI interface for sandbox."""
    if len(sys.argv) < 4:
        print("Usage: sandbox.py <code_file> <input_json> <language>")
        sys.exit(1)

    code_file = sys.argv[1]
    input_json = sys.argv[2]
    language = sys.argv[3]

    # Read code from file
    with open(code_file, 'r') as f:
        code = f.read()

    # Parse input
    test_input = json.loads(input_json)

    # Execute in sandbox
    with Sandbox() as sandbox:
        result = sandbox.execute(code, test_input, language)
        print(json.dumps(result))


if __name__ == '__main__':
    main()
