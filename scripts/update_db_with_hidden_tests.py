#!/usr/bin/env python3
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
HIDDEN_TEST_CASES = {'Two Sum': [{'input': [[1, 1], 2], 'expectedOutput': [0, 1]}, {'input': [[0, 4, 3, 0], 0], 'expectedOutput': [0, 3]}, {'input': [[-3, 4, 3, 90], 0], 'expectedOutput': [0, 2]}, {'input': [[1000000000, -1000000000, 999999999, -999999999], 0], 'expectedOutput': [0, 1]}], 'Valid Parentheses': [{'input': ['((()))'], 'expectedOutput': True}, {'input': ['((('], 'expectedOutput': False}, {'input': [')))'], 'expectedOutput': False}, {'input': ['{[(])}'], 'expectedOutput': False}, {'input': ['()()()()()()()()()()()()()()()()()()()()'], 'expectedOutput': True}], 'Merge Two Sorted Lists': [{'input': [[1], []], 'expectedOutput': [1]}, {'input': [[-100], [100]], 'expectedOutput': [-100, 100]}, {'input': [[1, 1, 1], [1, 1, 1]], 'expectedOutput': [1, 1, 1, 1, 1, 1]}, {'input': [[5, 6, 7], [1, 2, 3]], 'expectedOutput': [1, 2, 3, 5, 6, 7]}], 'Best Time to Buy and Sell Stock': [{'input': [[7, 6, 5, 4, 3, 2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 3, 4, 5, 6, 7]], 'expectedOutput': 6}, {'input': [[1]], 'expectedOutput': 0}, {'input': [[3, 3, 3, 3, 3]], 'expectedOutput': 0}, {'input': [[2, 1, 4, 1, 7]], 'expectedOutput': 6}], 'Valid Palindrome': [{'input': [''], 'expectedOutput': True}, {'input': ['a'], 'expectedOutput': True}, {'input': ['aa'], 'expectedOutput': True}, {'input': ['ab'], 'expectedOutput': False}, {'input': ['.,!@#$%^&*()'], 'expectedOutput': True}], 'Maximum Depth of Binary Tree': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[1, None, 2, None, 3, None, 4]], 'expectedOutput': 4}, {'input': [[1, 2, None, 3, None, 4, None]], 'expectedOutput': 4}], 'Climbing Stairs': [{'input': [1], 'expectedOutput': 1}, {'input': [2], 'expectedOutput': 2}, {'input': [10], 'expectedOutput': 89}, {'input': [35], 'expectedOutput': 14930352}], 'Symmetric Tree': [{'input': [[]], 'expectedOutput': True}, {'input': [[1]], 'expectedOutput': True}, {'input': [[1, 2, 2, None, 3, None, 3]], 'expectedOutput': False}, {'input': [[1, 2, 2, 2, None, 2, None]], 'expectedOutput': False}], 'Add Two Numbers': [{'input': [[0], [0]], 'expectedOutput': [0]}, {'input': [[9, 9, 9, 9], [1]], 'expectedOutput': [0, 0, 0, 0, 1]}, {'input': [[1], [9, 9, 9]], 'expectedOutput': [0, 0, 0, 1]}, {'input': [[5], [5]], 'expectedOutput': [0, 1]}], 'Longest Substring Without Repeating Characters': [{'input': [''], 'expectedOutput': 0}, {'input': ['a'], 'expectedOutput': 1}, {'input': ['aaaaaaa'], 'expectedOutput': 1}, {'input': ['abcdefghijklmnopqrstuvwxyz'], 'expectedOutput': 26}, {'input': ['dvdf'], 'expectedOutput': 3}], 'Median of Two Sorted Arrays': [{'input': [[1], [2]], 'expectedOutput': 1.5}, {'input': [[1, 2], []], 'expectedOutput': 1.5}, {'input': [[100], [101]], 'expectedOutput': 100.5}, {'input': [[1, 3, 5], [2, 4, 6]], 'expectedOutput': 3.5}, {'input': [[1], [2, 3, 4, 5, 6, 7]], 'expectedOutput': 4}], 'Container With Most Water': [{'input': [[1, 1]], 'expectedOutput': 1}, {'input': [[1, 2, 1]], 'expectedOutput': 2}, {'input': [[10000, 1, 1, 1, 1, 10000]], 'expectedOutput': 50000}, {'input': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 'expectedOutput': 25}], '3Sum': [{'input': [[0, 0, 0]], 'expectedOutput': [[0, 0, 0]]}, {'input': [[1, 2, -3]], 'expectedOutput': []}, {'input': [[-1, 0, 1, 0]], 'expectedOutput': [[-1, 0, 1]]}, {'input': [[-2, 0, 0, 2, 2]], 'expectedOutput': [[-2, 0, 2]]}], 'Letter Combinations of a Phone Number': [{'input': [''], 'expectedOutput': []}, {'input': ['2'], 'expectedOutput': ['a', 'b', 'c']}, {'input': ['99'], 'expectedOutput': ['ww', 'wx', 'wy', 'wz', 'xw', 'xx', 'xy', 'xz', 'yw', 'yx', 'yy', 'yz', 'zw', 'zx', 'zy', 'zz']}], 'Remove Nth Node From End of List': [{'input': [[1], 1], 'expectedOutput': []}, {'input': [[1, 2], 1], 'expectedOutput': [1]}, {'input': [[1, 2], 2], 'expectedOutput': [2]}, {'input': [[1, 2, 3, 4, 5], 3], 'expectedOutput': [1, 2, 4, 5]}], 'Generate Parentheses': [{'input': [1], 'expectedOutput': ['()']}, {'input': [4], 'expectedOutput': ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']}], 'Swap Nodes in Pairs': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}, {'input': [[1, 2, 3]], 'expectedOutput': [2, 1, 3]}, {'input': [[1, 2, 3, 4, 5, 6]], 'expectedOutput': [2, 1, 4, 3, 6, 5]}], 'Group Anagrams': [{'input': [['']], 'expectedOutput': [['']]}, {'input': [['a']], 'expectedOutput': [['a']]}, {'input': [['abc', 'bca', 'cab', 'xyz', 'zyx']], 'expectedOutput': [['abc', 'bca', 'cab'], ['xyz', 'zyx']]}], 'Maximum Subarray': [{'input': [[1]], 'expectedOutput': 1}, {'input': [[-1]], 'expectedOutput': -1}, {'input': [[5, -3, 5]], 'expectedOutput': 7}, {'input': [[-2, -3, -1, -5]], 'expectedOutput': -1}], 'Spiral Matrix': [{'input': [[[1]]], 'expectedOutput': [1]}, {'input': [[[1, 2, 3]]], 'expectedOutput': [1, 2, 3]}, {'input': [[[1], [2], [3]]], 'expectedOutput': [1, 2, 3]}], 'Merge Intervals': [{'input': [[[1, 3]]], 'expectedOutput': [[1, 3]]}, {'input': [[[1, 10], [2, 3], [4, 5], [6, 7]]], 'expectedOutput': [[1, 10]]}, {'input': [[[1, 2], [3, 4], [5, 6]]], 'expectedOutput': [[1, 2], [3, 4], [5, 6]]}], 'Unique Paths': [{'input': [1, 1], 'expectedOutput': 1}, {'input': [1, 10], 'expectedOutput': 1}, {'input': [10, 1], 'expectedOutput': 1}, {'input': [3, 3], 'expectedOutput': 6}], 'Minimum Path Sum': [{'input': [[[1]]], 'expectedOutput': 1}, {'input': [[[1, 2], [3, 4]]], 'expectedOutput': 7}, {'input': [[[1, 1, 1], [1, 1, 1]]], 'expectedOutput': 4}], 'Subsets': [{'input': [[]], 'expectedOutput': [[]]}, {'input': [[1]], 'expectedOutput': [[], [1]]}, {'input': [[1, 2, 3, 4]], 'expectedOutput': [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]}], 'Word Search': [{'input': [[['A']], 'A'], 'expectedOutput': True}, {'input': [[['A']], 'B'], 'expectedOutput': False}, {'input': [[['A', 'B'], ['C', 'D']], 'ABDC'], 'expectedOutput': True}], 'Validate Binary Search Tree': [{'input': [[]], 'expectedOutput': True}, {'input': [[1]], 'expectedOutput': True}, {'input': [[10, 5, 15, None, None, 6, 20]], 'expectedOutput': False}, {'input': [[5, 3, 8, 1, 4, 7, 9]], 'expectedOutput': True}], 'Binary Tree Level Order Traversal': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [[1]]}, {'input': [[1, None, 2, None, 3]], 'expectedOutput': [[1], [2], [3]]}], 'Construct Binary Tree from Preorder and Inorder Traversal': [{'input': [[1], [1]], 'expectedOutput': [1]}, {'input': [[1, 2], [2, 1]], 'expectedOutput': [1, 2, None]}, {'input': [[1, 2], [1, 2]], 'expectedOutput': [1, None, 2]}], 'Best Time to Buy and Sell Stock II': [{'input': [[1]], 'expectedOutput': 0}, {'input': [[7, 6, 5, 4, 3, 2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 3, 4, 5, 6, 7]], 'expectedOutput': 6}, {'input': [[1, 7, 2, 8]], 'expectedOutput': 12}], 'Longest Consecutive Sequence': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[1, 3, 5, 7, 9]], 'expectedOutput': 1}, {'input': [[100, 1, 200, 2, 3, 4]], 'expectedOutput': 4}], 'Clone Graph': [{'input': [[]], 'expectedOutput': []}, {'input': [[[1, []]]], 'expectedOutput': [[1, []]]}, {'input': [[[1, [2]], [2, [1]]]], 'expectedOutput': [[1, [2]], [2, [1]]]}], 'Gas Station': [{'input': [[5], [4]], 'expectedOutput': 0}, {'input': [[2], [3]], 'expectedOutput': -1}, {'input': [[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]], 'expectedOutput': 4}], 'Word Break': [{'input': ['', []], 'expectedOutput': True}, {'input': ['a', ['a']], 'expectedOutput': True}, {'input': ['abc', ['a', 'b', 'c']], 'expectedOutput': True}, {'input': ['aaaaaaa', ['aaaa', 'aaa']], 'expectedOutput': True}], 'LRU Cache': [{'input': [[['put', 1, 1], ['get', 1]], 1], 'expectedOutput': [None, 1]}, {'input': [[['put', 1, 1], ['put', 2, 2], ['get', 1], ['put', 3, 3], ['get', 2]], 2], 'expectedOutput': [None, None, 1, None, -1]}], 'Evaluate Reverse Polish Notation': [{'input': [['1']], 'expectedOutput': 1}, {'input': [['1', '2', '+']], 'expectedOutput': 3}, {'input': [['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']], 'expectedOutput': 22}], 'Find Peak Element': [{'input': [[1]], 'expectedOutput': 0}, {'input': [[1, 2]], 'expectedOutput': 1}, {'input': [[2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 1, 3, 5, 6, 4]], 'expectedOutput': 5}], 'Rotate Array': [{'input': [[1], 0], 'expectedOutput': [1]}, {'input': [[1, 2], 3], 'expectedOutput': [2, 1]}, {'input': [[-1], 2], 'expectedOutput': [-1]}], 'Number of Islands': [{'input': [[['0']]], 'expectedOutput': 0}, {'input': [[['1']]], 'expectedOutput': 1}, {'input': [[['1', '0', '1'], ['0', '1', '0'], ['1', '0', '1']]], 'expectedOutput': 5}], 'Course Schedule': [{'input': [1, []], 'expectedOutput': True}, {'input': [2, [[0, 1], [1, 0]]], 'expectedOutput': False}, {'input': [3, [[0, 1], [0, 2], [1, 2]]], 'expectedOutput': True}]}

# Python imports data
PYTHON_IMPORTS = {'Two Sum': 'from typing import List', 'Valid Parentheses': '', 'Merge Two Sorted Lists': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next', 'Best Time to Buy and Sell Stock': 'from typing import List', 'Valid Palindrome': '', 'Maximum Depth of Binary Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right', 'Climbing Stairs': '', 'Symmetric Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right', 'Add Two Numbers': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next', 'Longest Substring Without Repeating Characters': '', 'Median of Two Sorted Arrays': 'from typing import List', 'Container With Most Water': 'from typing import List', '3Sum': 'from typing import List', 'Letter Combinations of a Phone Number': 'from typing import List', 'Remove Nth Node From End of List': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next', 'Generate Parentheses': 'from typing import List', 'Swap Nodes in Pairs': 'from typing import Optional\n\n# Definition for singly-linked list.\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next', 'Group Anagrams': 'from typing import List', 'Maximum Subarray': 'from typing import List', 'Spiral Matrix': 'from typing import List', 'Merge Intervals': 'from typing import List', 'Unique Paths': '', 'Minimum Path Sum': 'from typing import List', 'Subsets': 'from typing import List', 'Word Search': 'from typing import List', 'Validate Binary Search Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right', 'Binary Tree Level Order Traversal': 'from typing import Optional, List\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right', 'Construct Binary Tree from Preorder and Inorder Traversal': 'from typing import List, Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right', 'Best Time to Buy and Sell Stock II': 'from typing import List', 'Longest Consecutive Sequence': 'from typing import List', 'Clone Graph': 'from typing import Optional\n\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []', 'Gas Station': 'from typing import List', 'Word Break': 'from typing import List', 'LRU Cache': '', 'Evaluate Reverse Polish Notation': 'from typing import List', 'Find Peak Element': 'from typing import List', 'Rotate Array': 'from typing import List', 'Number of Islands': 'from typing import List', 'Course Schedule': 'from typing import List'}

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
                        new_sig = imports + '\n\n' + current_sig

                        cursor.execute("""
                            UPDATE leetcode_questions
                            SET function_signature_python = ?
                            WHERE question_id IN (
                                SELECT id FROM questions WHERE title = ?
                            )
                        """, (new_sig, title))

                        print(f"✅ Updated imports for: {title}")

        conn.commit()
        print("\n✅ Database updated successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
