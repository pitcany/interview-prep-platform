#!/usr/bin/env python3
"""
Add hidden test cases for the 24 remaining LeetCode questions.
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

# Hidden test cases for the remaining 24 questions
ADDITIONAL_HIDDEN_TESTS = {
    'Binary Tree Inorder Traversal': [
        {"input": [[]], "expectedOutput": []},  # Empty tree
        {"input": [[1]], "expectedOutput": [1]},  # Single node
        {"input": [[1, None, 2, None, 3]], "expectedOutput": [1, 2, 3]},  # Right skewed
        {"input": [[1, 2, None, 3, None]], "expectedOutput": [3, 2, 1]},  # Left skewed
    ],
    'Linked List Cycle': [
        {"input": [[1], -1], "expectedOutput": False},  # Single node no cycle
        {"input": [[1, 2], 0], "expectedOutput": True},  # Two nodes cycle at head
        {"input": [[1, 2, 3, 4], 1], "expectedOutput": True},  # Cycle in middle
        {"input": [[1, 2, 3, 4], -1], "expectedOutput": False},  # No cycle
    ],
    'Longest Palindromic Substring': [
        {"input": ["a"], "expectedOutput": "a"},  # Single character
        {"input": ["aa"], "expectedOutput": "aa"},  # Two same chars
        {"input": ["abc"], "expectedOutput": "a"},  # No palindrome
        {"input": ["racecar"], "expectedOutput": "racecar"},  # Whole string palindrome
        {"input": ["abcdefgfedcba"], "expectedOutput": "abcdefgfedcba"},  # Long palindrome
    ],
    'Product of Array Except Self': [
        {"input": [[1]], "expectedOutput": [1]},  # Single element
        {"input": [[1, 2]], "expectedOutput": [2, 1]},  # Two elements
        {"input": [[0, 0]], "expectedOutput": [0, 0]},  # All zeros
        {"input": [[1, 0]], "expectedOutput": [0, 1]},  # One zero
        {"input": [[-1, 1, 0, -3, 3]], "expectedOutput": [0, 0, 9, 0, 0]},  # With zero and negatives
    ],
    'Rotate Image': [
        {"input": [[[1]]], "expectedOutput": [[1]]},  # 1x1 matrix
        {"input": [[[1, 2], [3, 4]]], "expectedOutput": [[3, 1], [4, 2]]},  # 2x2 matrix
        {"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expectedOutput": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},  # 3x3
        {"input": [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]], "expectedOutput": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]},  # 4x4
    ],
    'Set Matrix Zeroes': [
        {"input": [[[0]]], "expectedOutput": [[0]]},  # 1x1 zero
        {"input": [[[1]]], "expectedOutput": [[1]]},  # 1x1 non-zero
        {"input": [[[1, 0]]], "expectedOutput": [[0, 0]]},  # Single row with zero
        {"input": [[[0, 1], [1, 1]]], "expectedOutput": [[0, 0], [0, 1]]},  # First column zero
        {"input": [[[1, 1, 1], [0, 1, 2]]], "expectedOutput": [[0, 1, 1], [0, 0, 0]]},  # 2x3 matrix
    ],
    'Subarray Sum Equals K': [
        {"input": [[1], 1], "expectedOutput": 1},  # Single element match
        {"input": [[1], 0], "expectedOutput": 0},  # Single element no match
        {"input": [[1, 1, 1], 2], "expectedOutput": 2},  # Multiple subarrays
        {"input": [[1, -1, 0], 0], "expectedOutput": 3},  # With negatives and zero
        {"input": [[1, 2, 3, 4, 5], 9], "expectedOutput": 2},  # Multiple combinations
    ],
    'Reverse Linked List II': [
        {"input": [[1], 1, 1], "expectedOutput": [1]},  # Single node reverse itself
        {"input": [[1, 2], 1, 2], "expectedOutput": [2, 1]},  # Reverse entire list
        {"input": [[1, 2, 3], 2, 3], "expectedOutput": [1, 3, 2]},  # Reverse tail
        {"input": [[1, 2, 3, 4, 5], 2, 4], "expectedOutput": [1, 4, 3, 2, 5]},  # Reverse middle
    ],
    'Kth Smallest Element in a BST': [
        {"input": [[1], 1], "expectedOutput": 1},  # Single node
        {"input": [[2, 1], 1], "expectedOutput": 1},  # Two nodes k=1
        {"input": [[2, 1], 2], "expectedOutput": 2},  # Two nodes k=2
        {"input": [[5, 3, 6, 2, 4, None, None, 1], 3], "expectedOutput": 3},  # Complex tree
    ],
    'Binary Tree Right Side View': [
        {"input": [[]], "expectedOutput": []},  # Empty tree
        {"input": [[1]], "expectedOutput": [1]},  # Single node
        {"input": [[1, 2, None]], "expectedOutput": [1, 2]},  # Left child only
        {"input": [[1, None, 3]], "expectedOutput": [1, 3]},  # Right child only
        {"input": [[1, 2, 3, None, 5, None, 4]], "expectedOutput": [1, 3, 4]},  # Complex
    ],
    'Path Sum II': [
        {"input": [[]], "expectedOutput": []},  # Empty tree
        {"input": [[1], 1], "expectedOutput": [[1]]},  # Single node match
        {"input": [[1], 0], "expectedOutput": []},  # Single node no match
        {"input": [[1, 2, 3], 3], "expectedOutput": [[1, 2]]},  # Left path
        {"input": [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], "expectedOutput": [[5, 4, 11, 2], [5, 8, 4, 5]]},  # Multiple paths
    ],
    'Lowest Common Ancestor of a Binary Tree': [
        {"input": [[1], 1, 1], "expectedOutput": 1},  # Single node
        {"input": [[3, 5, 1], 5, 1], "expectedOutput": 3},  # Root is LCA
        {"input": [[3, 5, 1, 6, 2, 0, 8], 6, 2], "expectedOutput": 5},  # Left subtree LCA
        {"input": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 4], "expectedOutput": 2},  # Deep nodes
    ],
    'Coin Change': [
        {"input": [[1], 0], "expectedOutput": 0},  # Zero amount
        {"input": [[1], 1], "expectedOutput": 1},  # Exact match
        {"input": [[2], 3], "expectedOutput": -1},  # Impossible
        {"input": [[1, 2, 5], 11], "expectedOutput": 3},  # Standard case
        {"input": [[2, 5, 10, 1], 27], "expectedOutput": 4},  # Greedy fails, DP works
    ],
    'Longest Increasing Subsequence': [
        {"input": [[]], "expectedOutput": 0},  # Empty array
        {"input": [[1]], "expectedOutput": 1},  # Single element
        {"input": [[3, 2, 1]], "expectedOutput": 1},  # Decreasing
        {"input": [[1, 2, 3, 4, 5]], "expectedOutput": 5},  # All increasing
        {"input": [[10, 9, 2, 5, 3, 7, 101, 18]], "expectedOutput": 4},  # Complex
    ],
    'House Robber II': [
        {"input": [[1]], "expectedOutput": 1},  # Single house
        {"input": [[1, 2]], "expectedOutput": 2},  # Two houses
        {"input": [[1, 2, 3]], "expectedOutput": 3},  # Three houses
        {"input": [[2, 3, 2]], "expectedOutput": 3},  # First and last adjacent
        {"input": [[1, 2, 3, 1]], "expectedOutput": 4},  # Four houses
    ],
    'Decode Ways': [
        {"input": ["0"], "expectedOutput": 0},  # Invalid single zero
        {"input": ["1"], "expectedOutput": 1},  # Single digit
        {"input": ["10"], "expectedOutput": 1},  # One way (10)
        {"input": ["27"], "expectedOutput": 1},  # One way (2,7)
        {"input": ["12"], "expectedOutput": 2},  # Two ways (1,2) or (12)
        {"input": ["226"], "expectedOutput": 3},  # Three ways
    ],
    'Permutations': [
        {"input": [[]], "expectedOutput": [[]]},  # Empty array
        {"input": [[1]], "expectedOutput": [[1]]},  # Single element
        {"input": [[1, 2]], "expectedOutput": [[1, 2], [2, 1]]},  # Two elements
        {"input": [[1, 2, 3]], "expectedOutput": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]},  # Three elements
    ],
    'Trapping Rain Water': [
        {"input": [[]], "expectedOutput": 0},  # Empty
        {"input": [[3]], "expectedOutput": 0},  # Single bar
        {"input": [[3, 0, 2]], "expectedOutput": 2},  # Simple valley
        {"input": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "expectedOutput": 6},  # Standard
        {"input": [[4, 2, 0, 3, 2, 5]], "expectedOutput": 9},  # Complex
    ],
    'Binary Tree Maximum Path Sum': [
        {"input": [[1]], "expectedOutput": 1},  # Single node
        {"input": [[-10]], "expectedOutput": -10},  # Single negative
        {"input": [[2, -1]], "expectedOutput": 2},  # Ignore negative child
        {"input": [[1, 2, 3]], "expectedOutput": 6},  # All three nodes
        {"input": [[-10, 9, 20, None, None, 15, 7]], "expectedOutput": 42},  # Right subtree path
    ],
    'Serialize and Deserialize Binary Tree': [
        {"input": [[]], "expectedOutput": []},  # Empty tree
        {"input": [[1]], "expectedOutput": [1]},  # Single node
        {"input": [[1, 2, 3]], "expectedOutput": [1, 2, 3]},  # Three nodes
        {"input": [[1, 2, 3, None, None, 4, 5]], "expectedOutput": [1, 2, 3, None, None, 4, 5]},  # Complex
    ],
    'Regular Expression Matching': [
        {"input": ["", ""], "expectedOutput": True},  # Both empty
        {"input": ["a", "a"], "expectedOutput": True},  # Exact match
        {"input": ["a", "."], "expectedOutput": True},  # Dot wildcard
        {"input": ["aa", "a"], "expectedOutput": False},  # No match
        {"input": ["aa", "a*"], "expectedOutput": True},  # Star match
        {"input": ["ab", ".*"], "expectedOutput": True},  # Dot star matches all
    ],
    'Edit Distance': [
        {"input": ["", ""], "expectedOutput": 0},  # Both empty
        {"input": ["a", ""], "expectedOutput": 1},  # Delete one
        {"input": ["", "a"], "expectedOutput": 1},  # Insert one
        {"input": ["horse", "ros"], "expectedOutput": 3},  # Standard case
        {"input": ["intention", "execution"], "expectedOutput": 5},  # Complex
    ],
    'Word Ladder': [
        {"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expectedOutput": 5},  # Standard
        {"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "expectedOutput": 0},  # No path
        {"input": ["a", "c", ["a", "b", "c"]], "expectedOutput": 2},  # Simple path
        {"input": ["hot", "dog", ["hot", "dog"]], "expectedOutput": 0},  # Direct but different
    ],
    'Merge k Sorted Lists': [
        {"input": [[]], "expectedOutput": []},  # Empty lists
        {"input": [[[1]]], "expectedOutput": [1]},  # Single list single element
        {"input": [[[1], [2], [3]]], "expectedOutput": [1, 2, 3]},  # Three single-element lists
        {"input": [[[1, 4, 5], [1, 3, 4], [2, 6]]], "expectedOutput": [1, 1, 2, 3, 4, 4, 5, 6]},  # Standard
    ],
}

# Additional Python imports
ADDITIONAL_IMPORTS = {
    'Binary Tree Inorder Traversal': 'from typing import Optional, List\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Linked List Cycle': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Longest Palindromic Substring': '',
    'Product of Array Except Self': 'from typing import List',
    'Rotate Image': 'from typing import List',
    'Set Matrix Zeroes': 'from typing import List',
    'Subarray Sum Equals K': 'from typing import List',
    'Reverse Linked List II': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
    'Kth Smallest Element in a BST': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Binary Tree Right Side View': 'from typing import Optional, List\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Path Sum II': 'from typing import Optional, List\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Lowest Common Ancestor of a Binary Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Coin Change': 'from typing import List',
    'Longest Increasing Subsequence': 'from typing import List',
    'House Robber II': 'from typing import List',
    'Decode Ways': '',
    'Permutations': 'from typing import List',
    'Trapping Rain Water': 'from typing import List',
    'Binary Tree Maximum Path Sum': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Serialize and Deserialize Binary Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right',
    'Regular Expression Matching': '',
    'Edit Distance': '',
    'Word Ladder': 'from typing import List',
    'Merge k Sorted Lists': 'from typing import List, Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next',
}

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
        updated_count = 0
        import_count = 0

        # Update each question with hidden test cases
        for title, hidden_tests in ADDITIONAL_HIDDEN_TESTS.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET hidden_test_cases = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (json.dumps(hidden_tests), title))

            if cursor.rowcount > 0:
                print(f"✅ Updated hidden test cases for: {title}")
                updated_count += 1
            else:
                print(f"⚠️  Question not found: {title}")

        # Update Python signatures with imports
        for title, imports in ADDITIONAL_IMPORTS.items():
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
                    # Add imports before the class definition if not already present
                    if not current_sig.startswith('from typing'):
                        new_sig = imports + '\n\n' + current_sig

                        cursor.execute("""
                            UPDATE leetcode_questions
                            SET function_signature_python = ?
                            WHERE question_id IN (
                                SELECT id FROM questions WHERE title = ?
                            )
                        """, (new_sig, title))

                        print(f"✅ Updated imports for: {title}")
                        import_count += 1

        conn.commit()
        print(f"\n✅ Database updated successfully!")
        print(f"   Hidden tests: {updated_count} questions")
        print(f"   Imports: {import_count} questions")

    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
