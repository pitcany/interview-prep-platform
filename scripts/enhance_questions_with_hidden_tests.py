#!/usr/bin/env python3
"""
Enhance questions_data_full.py with hidden test cases and proper imports for type hints.

This script:
1. Adds comprehensive hidden test cases for all 40 LeetCode questions
2. Adds proper Python import statements for type hints
3. Tests edge cases, boundary conditions, and performance scenarios
"""

import json

# Define hidden test cases for each problem
HIDDEN_TEST_CASES = {
    'Two Sum': [
        {"input": [[1, 1], 2], "expectedOutput": [0, 1]},  # Duplicates that sum to target
        {"input": [[0, 4, 3, 0], 0], "expectedOutput": [0, 3]},  # Target is 0
        {"input": [[-3, 4, 3, 90], 0], "expectedOutput": [0, 2]},  # Negative numbers
        {"input": [[1000000000, -1000000000, 999999999, -999999999], 0], "expectedOutput": [0, 1]},  # Large values
    ],
    'Valid Parentheses': [
        {"input": ["((()))"], "expectedOutput": True},  # Deeply nested
        {"input": ["((("], "expectedOutput": False},  # All opening
        {"input": [")))"], "expectedOutput": False},  # All closing
        {"input": ["{[(])}"], "expectedOutput": False},  # Wrong order
        {"input": ["()()()()()()()()()()()()()()()()()()()()"], "expectedOutput": True},  # Many valid pairs
    ],
    'Merge Two Sorted Lists': [
        {"input": [[1], []], "expectedOutput": [1]},  # One empty list
        {"input": [[-100], [100]], "expectedOutput": [-100, 100]},  # Extreme values
        {"input": [[1, 1, 1], [1, 1, 1]], "expectedOutput": [1, 1, 1, 1, 1, 1]},  # All duplicates
        {"input": [[5, 6, 7], [1, 2, 3]], "expectedOutput": [1, 2, 3, 5, 6, 7]},  # No overlap
    ],
    'Best Time to Buy and Sell Stock': [
        {"input": [[7, 6, 5, 4, 3, 2, 1]], "expectedOutput": 0},  # Strictly decreasing
        {"input": [[1, 2, 3, 4, 5, 6, 7]], "expectedOutput": 6},  # Strictly increasing
        {"input": [[1]], "expectedOutput": 0},  # Single element
        {"input": [[3, 3, 3, 3, 3]], "expectedOutput": 0},  # All same values
        {"input": [[2, 1, 4, 1, 7]], "expectedOutput": 6},  # Multiple valleys and peaks
    ],
    'Valid Palindrome': [
        {"input": [""], "expectedOutput": True},  # Empty string
        {"input": ["a"], "expectedOutput": True},  # Single character
        {"input": ["aa"], "expectedOutput": True},  # Two same characters
        {"input": ["ab"], "expectedOutput": False},  # Two different characters
        {"input": [".,!@#$%^&*()"], "expectedOutput": True},  # Only non-alphanumeric
    ],
    'Maximum Depth of Binary Tree': [
        {"input": [[]], "expectedOutput": 0},  # Empty tree
        {"input": [[1]], "expectedOutput": 1},  # Single node
        {"input": [[1, None, 2, None, 3, None, 4]], "expectedOutput": 4},  # Right skewed
        {"input": [[1, 2, None, 3, None, 4, None]], "expectedOutput": 4},  # Left skewed
    ],
    'Climbing Stairs': [
        {"input": [1], "expectedOutput": 1},  # Base case
        {"input": [2], "expectedOutput": 2},  # Base case
        {"input": [10], "expectedOutput": 89},  # Moderate size
        {"input": [35], "expectedOutput": 14930352},  # Large Fibonacci number
    ],
    'Symmetric Tree': [
        {"input": [[]], "expectedOutput": True},  # Empty tree
        {"input": [[1]], "expectedOutput": True},  # Single node
        {"input": [[1, 2, 2, None, 3, None, 3]], "expectedOutput": False},  # Asymmetric structure
        {"input": [[1, 2, 2, 2, None, 2, None]], "expectedOutput": False},  # Values match but not symmetric
    ],
    'Add Two Numbers': [
        {"input": [[0], [0]], "expectedOutput": [0]},  # Zero + Zero
        {"input": [[9, 9, 9, 9], [1]], "expectedOutput": [0, 0, 0, 0, 1]},  # Carry propagation
        {"input": [[1], [9, 9, 9]], "expectedOutput": [0, 0, 0, 1]},  # Different lengths
        {"input": [[5], [5]], "expectedOutput": [0, 1]},  # Simple carry
    ],
    'Longest Substring Without Repeating Characters': [
        {"input": [""], "expectedOutput": 0},  # Empty string
        {"input": ["a"], "expectedOutput": 1},  # Single character
        {"input": ["aaaaaaa"], "expectedOutput": 1},  # All same
        {"input": ["abcdefghijklmnopqrstuvwxyz"], "expectedOutput": 26},  # All unique
        {"input": ["dvdf"], "expectedOutput": 3},  # Tricky case
    ],
    'Median of Two Sorted Arrays': [
        {"input": [[1], [2]], "expectedOutput": 1.5},  # Two single elements
        {"input": [[1, 2], []], "expectedOutput": 1.5},  # One empty array
        {"input": [[100], [101]], "expectedOutput": 100.5},  # Close values
        {"input": [[1, 3, 5], [2, 4, 6]], "expectedOutput": 3.5},  # Interleaved
        {"input": [[1], [2, 3, 4, 5, 6, 7]], "expectedOutput": 4},  # Very different sizes
    ],
    'Container With Most Water': [
        {"input": [[1, 1]], "expectedOutput": 1},  # Two elements same height
        {"input": [[1, 2, 1]], "expectedOutput": 2},  # Triangle
        {"input": [[10000, 1, 1, 1, 1, 10000]], "expectedOutput": 50000},  # Tall edges
        {"input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], "expectedOutput": 25},  # Ascending
    ],
    '3Sum': [
        {"input": [[0, 0, 0]], "expectedOutput": [[0, 0, 0]]},  # All zeros
        {"input": [[1, 2, -3]], "expectedOutput": []},  # No solution
        {"input": [[-1, 0, 1, 0]], "expectedOutput": [[-1, 0, 1]]},  # Duplicate zeros
        {"input": [[-2, 0, 0, 2, 2]], "expectedOutput": [[-2, 0, 2]]},  # Multiple duplicates
    ],
    'Letter Combinations of a Phone Number': [
        {"input": [""], "expectedOutput": []},  # Empty input
        {"input": ["2"], "expectedOutput": ["a", "b", "c"]},  # Single digit
        {"input": ["99"], "expectedOutput": ["ww", "wx", "wy", "wz", "xw", "xx", "xy", "xz", "yw", "yx", "yy", "yz", "zw", "zx", "zy", "zz"]},  # Same digit repeated
    ],
    'Remove Nth Node From End of List': [
        {"input": [[1], 1], "expectedOutput": []},  # Remove only node
        {"input": [[1, 2], 1], "expectedOutput": [1]},  # Remove last
        {"input": [[1, 2], 2], "expectedOutput": [2]},  # Remove first
        {"input": [[1, 2, 3, 4, 5], 3], "expectedOutput": [1, 2, 4, 5]},  # Remove middle
    ],
    'Generate Parentheses': [
        {"input": [1], "expectedOutput": ["()"]},  # n=1
        {"input": [4], "expectedOutput": ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]},  # n=4
    ],
    'Swap Nodes in Pairs': [
        {"input": [[]], "expectedOutput": []},  # Empty list
        {"input": [[1]], "expectedOutput": [1]},  # Single node
        {"input": [[1, 2, 3]], "expectedOutput": [2, 1, 3]},  # Odd number
        {"input": [[1, 2, 3, 4, 5, 6]], "expectedOutput": [2, 1, 4, 3, 6, 5]},  # Multiple pairs
    ],
    'Group Anagrams': [
        {"input": [[""]], "expectedOutput": [[""]]},  # Empty string
        {"input": [["a"]], "expectedOutput": [["a"]]},  # Single character
        {"input": [["abc", "bca", "cab", "xyz", "zyx"]], "expectedOutput": [["abc", "bca", "cab"], ["xyz", "zyx"]]},  # Multiple groups
    ],
    'Maximum Subarray': [
        {"input": [[1]], "expectedOutput": 1},  # Single element
        {"input": [[-1]], "expectedOutput": -1},  # Single negative
        {"input": [[5, -3, 5]], "expectedOutput": 7},  # Cross middle negative
        {"input": [[-2, -3, -1, -5]], "expectedOutput": -1},  # All negative
    ],
    'Spiral Matrix': [
        {"input": [[[1]]], "expectedOutput": [1]},  # 1x1 matrix
        {"input": [[[1, 2, 3]]], "expectedOutput": [1, 2, 3]},  # Single row
        {"input": [[[1], [2], [3]]], "expectedOutput": [1, 2, 3]},  # Single column
    ],
    'Merge Intervals': [
        {"input": [[[1, 3]]], "expectedOutput": [[1, 3]]},  # Single interval
        {"input": [[[1, 10], [2, 3], [4, 5], [6, 7]]], "expectedOutput": [[1, 10]]},  # All contained
        {"input": [[[1, 2], [3, 4], [5, 6]]], "expectedOutput": [[1, 2], [3, 4], [5, 6]]},  # No overlap
    ],
    'Unique Paths': [
        {"input": [1, 1], "expectedOutput": 1},  # 1x1 grid
        {"input": [1, 10], "expectedOutput": 1},  # Single row
        {"input": [10, 1], "expectedOutput": 1},  # Single column
        {"input": [3, 3], "expectedOutput": 6},  # 3x3 grid
    ],
    'Minimum Path Sum': [
        {"input": [[[1]]], "expectedOutput": 1},  # 1x1 grid
        {"input": [[[1, 2], [3, 4]]], "expectedOutput": 7},  # 2x2 grid
        {"input": [[[1, 1, 1], [1, 1, 1]]], "expectedOutput": 4},  # All same values
    ],
    'Subsets': [
        {"input": [[]], "expectedOutput": [[]]},  # Empty set
        {"input": [[1]], "expectedOutput": [[], [1]]},  # Single element
        {"input": [[1, 2, 3, 4]], "expectedOutput": [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3], [4], [1,4], [2,4], [1,2,4], [3,4], [1,3,4], [2,3,4], [1,2,3,4]]},  # 4 elements
    ],
    'Word Search': [
        {"input": [[["A"]], "A"], "expectedOutput": True},  # 1x1 grid match
        {"input": [[["A"]], "B"], "expectedOutput": False},  # 1x1 grid no match
        {"input": [[["A", "B"], ["C", "D"]], "ABDC"], "expectedOutput": True},  # Circular path
    ],
    'Validate Binary Search Tree': [
        {"input": [[]], "expectedOutput": True},  # Empty tree
        {"input": [[1]], "expectedOutput": True},  # Single node
        {"input": [[10, 5, 15, None, None, 6, 20]], "expectedOutput": False},  # Right subtree violation
        {"input": [[5, 3, 8, 1, 4, 7, 9]], "expectedOutput": True},  # Perfect BST
    ],
    'Binary Tree Level Order Traversal': [
        {"input": [[]], "expectedOutput": []},  # Empty tree
        {"input": [[1]], "expectedOutput": [[1]]},  # Single node
        {"input": [[1, None, 2, None, 3]], "expectedOutput": [[1], [2], [3]]},  # Right skewed
    ],
    'Construct Binary Tree from Preorder and Inorder Traversal': [
        {"input": [[1], [1]], "expectedOutput": [1]},  # Single node
        {"input": [[1, 2], [2, 1]], "expectedOutput": [1, 2, None]},  # Two nodes left child
        {"input": [[1, 2], [1, 2]], "expectedOutput": [1, None, 2]},  # Two nodes right child
    ],
    'Best Time to Buy and Sell Stock II': [
        {"input": [[1]], "expectedOutput": 0},  # Single price
        {"input": [[7, 6, 5, 4, 3, 2, 1]], "expectedOutput": 0},  # Decreasing
        {"input": [[1, 2, 3, 4, 5, 6, 7]], "expectedOutput": 6},  # Increasing
        {"input": [[1, 7, 2, 8]], "expectedOutput": 12},  # Two transactions
    ],
    'Longest Consecutive Sequence': [
        {"input": [[]], "expectedOutput": 0},  # Empty array
        {"input": [[1]], "expectedOutput": 1},  # Single element
        {"input": [[1, 3, 5, 7, 9]], "expectedOutput": 1},  # No consecutive
        {"input": [[100, 1, 200, 2, 3, 4]], "expectedOutput": 4},  # Unsorted consecutive
    ],
    'Clone Graph': [
        {"input": [[]], "expectedOutput": []},  # Empty graph
        {"input": [[[1, []]]], "expectedOutput": [[1, []]]},  # Single node no neighbors
        {"input": [[[1, [2]], [2, [1]]]], "expectedOutput": [[1, [2]], [2, [1]]]},  # Two nodes connected
    ],
    'Gas Station': [
        {"input": [[5], [4]], "expectedOutput": 0},  # Single station valid
        {"input": [[2], [3]], "expectedOutput": -1},  # Single station invalid
        {"input": [[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]], "expectedOutput": 4},  # Start from end
    ],
    'Word Break': [
        {"input": ["", []], "expectedOutput": True},  # Empty string
        {"input": ["a", ["a"]], "expectedOutput": True},  # Single char match
        {"input": ["abc", ["a", "b", "c"]], "expectedOutput": True},  # All single chars
        {"input": ["aaaaaaa", ["aaaa", "aaa"]], "expectedOutput": True},  # Overlapping words
    ],
    'LRU Cache': [
        {"input": [[["put", 1, 1], ["get", 1]], 1], "expectedOutput": [None, 1]},  # Single item
        {"input": [[["put", 1, 1], ["put", 2, 2], ["get", 1], ["put", 3, 3], ["get", 2]], 2], "expectedOutput": [None, None, 1, None, -1]},  # Eviction
    ],
    'Evaluate Reverse Polish Notation': [
        {"input": [["1"]], "expectedOutput": 1},  # Single number
        {"input": [["1", "2", "+"]], "expectedOutput": 3},  # Simple addition
        {"input": [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], "expectedOutput": 22},  # Complex
    ],
    'Find Peak Element': [
        {"input": [[1]], "expectedOutput": 0},  # Single element
        {"input": [[1, 2]], "expectedOutput": 1},  # Two increasing
        {"input": [[2, 1]], "expectedOutput": 0},  # Two decreasing
        {"input": [[1, 2, 1, 3, 5, 6, 4]], "expectedOutput": 5},  # Multiple peaks
    ],
    'Rotate Array': [
        {"input": [[1], 0], "expectedOutput": [1]},  # No rotation
        {"input": [[1, 2], 3], "expectedOutput": [2, 1]},  # k > length
        {"input": [[-1], 2], "expectedOutput": [-1]},  # Single element
    ],
    'Number of Islands': [
        {"input": [[["0"]]], "expectedOutput": 0},  # Single water
        {"input": [[["1"]]], "expectedOutput": 1},  # Single land
        {"input": [[["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]], "expectedOutput": 5},  # Checkerboard
    ],
    'Course Schedule': [
        {"input": [1, []], "expectedOutput": True},  # No prerequisites
        {"input": [2, [[0, 1], [1, 0]]], "expectedOutput": False},  # Circular dependency
        {"input": [3, [[0, 1], [0, 2], [1, 2]]], "expectedOutput": True},  # Diamond dependency
    ]
}

# Define import statements for Python type hints
PYTHON_IMPORTS = {
    'Two Sum': 'from typing import List',
    'Valid Parentheses': '',
    'Merge Two Sorted Lists': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Best Time to Buy and Sell Stock': 'from typing import List',
    'Valid Palindrome': '',
    'Maximum Depth of Binary Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Climbing Stairs': '',
    'Symmetric Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Add Two Numbers': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Longest Substring Without Repeating Characters': '',
    'Median of Two Sorted Arrays': 'from typing import List',
    'Container With Most Water': 'from typing import List',
    '3Sum': 'from typing import List',
    'Letter Combinations of a Phone Number': 'from typing import List',
    'Remove Nth Node From End of List': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Generate Parentheses': 'from typing import List',
    'Swap Nodes in Pairs': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Group Anagrams': 'from typing import List',
    'Maximum Subarray': 'from typing import List',
    'Spiral Matrix': 'from typing import List',
    'Merge Intervals': 'from typing import List',
    'Unique Paths': '',
    'Minimum Path Sum': 'from typing import List',
    'Subsets': 'from typing import List',
    'Word Search': 'from typing import List',
    'Validate Binary Search Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Binary Tree Level Order Traversal': 'from typing import Optional, List\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Construct Binary Tree from Preorder and Inorder Traversal': 'from typing import List, Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Best Time to Buy and Sell Stock II': 'from typing import List',
    'Longest Consecutive Sequence': 'from typing import List',
    'Clone Graph': 'from typing import Optional\n\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []',
    'Gas Station': 'from typing import List',
    'Word Break': 'from typing import List',
    'LRU Cache': '',
    'Evaluate Reverse Polish Notation': 'from typing import List',
    'Find Peak Element': 'from typing import List',
    'Rotate Array': 'from typing import List',
    'Number of Islands': 'from typing import List',
    'Course Schedule': 'from typing import List'
}

def update_questions_file():
    """Read questions_data_full.py and add hidden test cases and imports"""

    # Read the original file
    with open('questions_data_full.py', 'r') as f:
        content = f.read()

    # Add hidden_test_cases field to each question
    import ast
    import sys

    # Parse the file to extract the questions
    # We'll need to manually update the file since it's a complex structure

    print("Updating questions_data_full.py with hidden test cases and imports...")

    # For now, let's create a new structure that can be manually integrated
    output = []
    output.append("# Hidden test cases to be added to questions_data_full.py\n")
    output.append("# Copy these into the appropriate questions in LEETCODE_QUESTIONS\n\n")

    for title, hidden_tests in HIDDEN_TEST_CASES.items():
        output.append(f"# {title}\n")
        output.append(f"'hidden_test_cases': {json.dumps(hidden_tests, indent=4)},\n")
        if title in PYTHON_IMPORTS and PYTHON_IMPORTS[title]:
            output.append(f"'python_imports': '''{PYTHON_IMPORTS[title]}''',\n")
        output.append("\n")

    # Write to a separate file for manual integration
    with open('hidden_test_cases_to_add.py', 'w') as f:
        f.write('\n'.join(output))

    print("Created hidden_test_cases_to_add.py with test cases to manually add to questions_data_full.py")

    # Also create a script to automatically update the database
    create_db_update_script()

def create_db_update_script():
    """Create a script to update the database with hidden test cases"""

    script = '''#!/usr/bin/env python3
"""
Update the database with hidden test cases and imports for all LeetCode questions.
"""

import json
import sqlite3
import os
import sys
from pathlib import Path

def get_db_path():
    """Get the database path based on OS"""
    if os.name == 'nt':  # Windows
        db_path = Path(os.environ.get('APPDATA', '')) / 'interview-prep-platform' / 'interview-prep.db'
    elif sys.platform == 'darwin':  # macOS
        db_path = Path.home() / 'Library' / 'Application Support' / 'interview-prep-platform' / 'interview-prep.db'
    else:  # Linux
        db_path = Path.home() / '.config' / 'interview-prep-platform' / 'interview-prep.db'
    return db_path

# Hidden test cases data
HIDDEN_TEST_CASES = ''' + str(HIDDEN_TEST_CASES) + '''

# Python imports data
PYTHON_IMPORTS = ''' + str(PYTHON_IMPORTS) + '''

def main():
    db_path = get_db_path()

    if not db_path.exists():
        print(f"❌ Database not found at: {db_path}")
        print("   Please run the application first to create the database.")
        sys.exit(1)

    print(f"📂 Opening database: {db_path}")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()

    try:
        # Update each question with hidden test cases
        for title, hidden_tests in HIDDEN_TEST_CASES.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET hidden_test_cases = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (json.dumps(hidden_tests), title))

            print(f"✅ Updated hidden test cases for: {title}")

        # Update Python signatures with imports
        for title, imports in PYTHON_IMPORTS.items():
            if imports:
                # Get current signature
                cursor.execute("""
                    SELECT lq.function_signature_python
                    FROM leetcode_questions lq
                    JOIN questions q ON lq.question_id = q.id
                    WHERE q.title = ?
                """, (title,))

                result = cursor.fetchone()
                if result and result[0]:
                    current_sig = result[0]
                    # Add imports before the class definition
                    if not current_sig.startswith('from typing'):
                        new_sig = imports + '\\n\\n' + current_sig

                        cursor.execute("""
                            UPDATE leetcode_questions
                            SET function_signature_python = ?
                            WHERE question_id IN (
                                SELECT id FROM questions WHERE title = ?
                            )
                        """, (new_sig, title))

                        print(f"✅ Updated imports for: {title}")

        conn.commit()
        print("\\n✅ Database updated successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
'''

    with open('update_db_with_hidden_tests.py', 'w') as f:
        f.write(script)

    # Make the script executable
    import os
    os.chmod('update_db_with_hidden_tests.py', 0o755)

    print("Created update_db_with_hidden_tests.py to update the database")

if __name__ == '__main__':
    update_questions_file()
    print("\nTo apply these changes:")
    print("1. Review hidden_test_cases_to_add.py for the test cases to add")
    print("2. Run: python3 update_db_with_hidden_tests.py to update the database")
    print("3. Or manually add the hidden test cases to questions_data_full.py and regenerate")