#!/usr/bin/env python3
"""
Test Java Code Execution
Tests the Java code executor with various LeetCode-style problems.
"""

import sys
import os
import json

# Add python-service to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python-service'))

from sandbox import Sandbox


def test_java_two_sum():
    """Test Java execution with Two Sum problem."""
    print("Testing Java Two Sum...")

    java_code = """
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
"""

    test_input = [[2, 7, 11, 15], 9]
    expected_output = [0, 1]

    with Sandbox() as sandbox:
        result = sandbox.execute(java_code, test_input, 'java')

        if result.get('success'):
            output = result.get('output')
            print(f"✓ Java Two Sum executed successfully")
            print(f"  Input: {test_input}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected_output}")

            if output == expected_output:
                print("✓ Output matches expected!")
                return True
            else:
                print("✗ Output does not match expected")
                return False
        else:
            error = result.get('error')
            error_type = result.get('error_type')
            print(f"✗ Java execution failed: {error_type} - {error}")

            if error_type == 'DockerNotAvailable':
                print("  Note: Docker is not available. Build images with:")
                print("    cd docker/java && docker build -t interview-prep-java .")

            return False


def test_java_reverse_integer():
    """Test Java execution with Reverse Integer problem."""
    print("\nTesting Java Reverse Integer...")

    java_code = """
public class Solution {
    public int reverse(int x) {
        long result = 0;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }

        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
            return 0;
        }

        return (int) result;
    }
}
"""

    test_input = [123]
    expected_output = 321

    with Sandbox() as sandbox:
        result = sandbox.execute(java_code, test_input, 'java')

        if result.get('success'):
            output = result.get('output')
            print(f"✓ Java Reverse Integer executed successfully")
            print(f"  Input: {test_input}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected_output}")

            if output == expected_output:
                print("✓ Output matches expected!")
                return True
            else:
                print("✗ Output does not match expected")
                return False
        else:
            error = result.get('error')
            error_type = result.get('error_type')
            print(f"✗ Java execution failed: {error_type} - {error}")
            return False


def test_java_compilation_error():
    """Test Java compilation error handling."""
    print("\nTesting Java Compilation Error Handling...")

    java_code = """
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Intentional syntax error
        return new int[] {0, 1}  // Missing semicolon
    }
}
"""

    test_input = [[2, 7, 11, 15], 9]

    with Sandbox() as sandbox:
        result = sandbox.execute(java_code, test_input, 'java')

        if not result.get('success'):
            error_type = result.get('error_type')
            print(f"✓ Compilation error detected: {error_type}")

            if error_type == 'CompilationError':
                print("✓ Error type is correct!")
                return True
            else:
                print(f"✗ Expected CompilationError, got {error_type}")
                return False
        else:
            print("✗ Expected compilation error but code executed successfully")
            return False


def main():
    """Run all Java tests."""
    print("=" * 60)
    print("Java Code Execution Tests")
    print("=" * 60)

    tests = [
        test_java_two_sum,
        test_java_reverse_integer,
        test_java_compilation_error,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ Test raised exception: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
