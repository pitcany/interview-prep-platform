#!/usr/bin/env python3
"""
Test script to verify hidden test cases work correctly with code execution
"""

import json
import sys
import os
sys.path.append('../python-service')

# Sample Two Sum solution to test
test_solution = """
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
"""

# Test cases from database (visible + hidden)
visible_tests = [
    {"input": [[2, 7, 11, 15], 9], "expectedOutput": [0, 1]},
    {"input": [[3, 2, 4], 6], "expectedOutput": [1, 2]},
    {"input": [[3, 3], 6], "expectedOutput": [0, 1]}
]

hidden_tests = [
    {"input": [[1, 1], 2], "expectedOutput": [0, 1]},
    {"input": [[0, 4, 3, 0], 0], "expectedOutput": [0, 3]},
    {"input": [[-3, 4, 3, 90], 0], "expectedOutput": [0, 2]},
    {"input": [[1000000000, -1000000000, 999999999, -999999999], 0], "expectedOutput": [0, 1]}
]

def run_test(code, test_case):
    """Run a single test case"""
    try:
        # Import typing for the execution context
        from typing import List, Optional

        # Create a namespace for execution with typing available
        namespace = {'List': List, 'Optional': Optional}

        # Execute the solution code
        exec(code, namespace)

        # Get the Solution class
        Solution = namespace.get('Solution')
        if not Solution:
            return False, "Solution class not found"

        # Create instance and run
        sol = Solution()

        # Get the method (twoSum in this case)
        method = getattr(sol, 'twoSum', None)
        if not method:
            return False, "twoSum method not found"

        # Run the test
        inputs = test_case['input']
        expected = test_case['expectedOutput']
        result = method(*inputs)

        # Check result
        if result == expected:
            return True, result
        else:
            # For Two Sum, order might be different but still valid
            if len(result) == 2 and len(expected) == 2:
                if sorted(result) == sorted(expected):
                    return True, result
            return False, f"Expected {expected}, got {result}"

    except Exception as e:
        return False, str(e)

def main():
    print("🧪 Testing Two Sum Solution with Hidden Test Cases\n")
    print("=" * 60)

    # Test visible cases
    print("📋 VISIBLE TEST CASES:")
    visible_passed = 0
    for i, test in enumerate(visible_tests, 1):
        passed, result = run_test(test_solution, test)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  Test {i}: {status} - Input: {test['input'][0][:4]}... Target: {test['input'][1]}")
        if passed:
            visible_passed += 1

    print(f"\nVisible: {visible_passed}/{len(visible_tests)} passed")

    # Test hidden cases
    print("\n🔒 HIDDEN TEST CASES:")
    hidden_passed = 0
    for i, test in enumerate(hidden_tests, 1):
        passed, result = run_test(test_solution, test)
        status = "✅ PASS" if passed else "❌ FAIL"

        # Show limited info for hidden tests (like real system)
        if passed:
            print(f"  Hidden Test {i}: {status}")
            hidden_passed += 1
        else:
            # In production, we wouldn't show details
            print(f"  Hidden Test {i}: {status} (Edge case detected)")

    print(f"\nHidden: {hidden_passed}/{len(hidden_tests)} passed")

    # Final result
    print("\n" + "=" * 60)
    total_passed = visible_passed + hidden_passed
    total_tests = len(visible_tests) + len(hidden_tests)

    if total_passed == total_tests:
        print(f"🎉 SUCCESS: All {total_tests} tests passed!")
        print("✅ Solution would be marked as SOLVED")
    else:
        print(f"❌ FAILED: Only {total_passed}/{total_tests} tests passed")
        print("⚠️  Solution would NOT be marked as solved")

    # Demonstrate import necessity
    print("\n" + "=" * 60)
    print("📝 TYPE HINTS DEMONSTRATION:\n")

    # Test without import
    bad_solution = """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0, 1]
"""

    print("Without import:")
    try:
        exec(bad_solution)
        print("  ❌ Should fail but didn't")
    except NameError as e:
        print(f"  ✅ Correctly fails: {e}")

    print("\nWith import:")
    try:
        from typing import List
        namespace = {'List': List}
        exec(test_solution, namespace)
        print("  ✅ Executes successfully with type hints")
    except Exception as e:
        print(f"  ❌ Failed: {e}")

if __name__ == '__main__':
    main()