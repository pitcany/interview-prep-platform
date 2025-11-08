#!/usr/bin/env python3
"""
Complete database setup script.
Initializes database and populates all test cases in one command.

Usage:
    python3 scripts/setup_database.py
"""

import sqlite3
import json
import sys
import os
from pathlib import Path

# Include all hidden test cases from update_db_with_hidden_tests.py and add_remaining_hidden_tests.py
HIDDEN_TEST_CASES = {'Two Sum': [{'input': [[1, 1], 2], 'expectedOutput': [0, 1]}, {'input': [[0, 4, 3, 0], 0], 'expectedOutput': [0, 3]}, {'input': [[-3, 4, 3, 90], 0], 'expectedOutput': [0, 2]}, {'input': [[1000000000, -1000000000, 999999999, -999999999], 0], 'expectedOutput': [0, 1]}], 'Valid Parentheses': [{'input': ['((()))'], 'expectedOutput': True}, {'input': ['((('], 'expectedOutput': False}, {'input': [')))'], 'expectedOutput': False}, {'input': ['{[(])}'], 'expectedOutput': False}, {'input': ['()()()()()()()()()()()()()()()()()()()()'], 'expectedOutput': True}], 'Merge Two Sorted Lists': [{'input': [[1], []], 'expectedOutput': [1]}, {'input': [[-100], [100]], 'expectedOutput': [-100, 100]}, {'input': [[1, 1, 1], [1, 1, 1]], 'expectedOutput': [1, 1, 1, 1, 1, 1]}, {'input': [[5, 6, 7], [1, 2, 3]], 'expectedOutput': [1, 2, 3, 5, 6, 7]}], 'Best Time to Buy and Sell Stock': [{'input': [[7, 6, 5, 4, 3, 2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 3, 4, 5, 6, 7]], 'expectedOutput': 6}, {'input': [[1]], 'expectedOutput': 0}, {'input': [[3, 3, 3, 3, 3]], 'expectedOutput': 0}, {'input': [[2, 1, 4, 1, 7]], 'expectedOutput': 6}], 'Valid Palindrome': [{'input': [''], 'expectedOutput': True}, {'input': ['a'], 'expectedOutput': True}, {'input': ['aa'], 'expectedOutput': True}, {'input': ['ab'], 'expectedOutput': False}, {'input': ['.,!@#$%^&*()'], 'expectedOutput': True}], 'Maximum Depth of Binary Tree': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[1, None, 2, None, 3, None, 4]], 'expectedOutput': 4}, {'input': [[1, 2, None, 3, None, 4, None]], 'expectedOutput': 4}], 'Climbing Stairs': [{'input': [1], 'expectedOutput': 1}, {'input': [2], 'expectedOutput': 2}, {'input': [10], 'expectedOutput': 89}, {'input': [35], 'expectedOutput': 14930352}], 'Symmetric Tree': [{'input': [[]], 'expectedOutput': True}, {'input': [[1]], 'expectedOutput': True}, {'input': [[1, 2, 2, None, 3, None, 3]], 'expectedOutput': False}, {'input': [[1, 2, 2, 2, None, 2, None]], 'expectedOutput': False}], 'Add Two Numbers': [{'input': [[0], [0]], 'expectedOutput': [0]}, {'input': [[9, 9, 9, 9], [1]], 'expectedOutput': [0, 0, 0, 0, 1]}, {'input': [[1], [9, 9, 9]], 'expectedOutput': [0, 0, 0, 1]}, {'input': [[5], [5]], 'expectedOutput': [0, 1]}], 'Longest Substring Without Repeating Characters': [{'input': [''], 'expectedOutput': 0}, {'input': ['a'], 'expectedOutput': 1}, {'input': ['aaaaaaa'], 'expectedOutput': 1}, {'input': ['abcdefghijklmnopqrstuvwxyz'], 'expectedOutput': 26}, {'input': ['dvdf'], 'expectedOutput': 3}], 'Median of Two Sorted Arrays': [{'input': [[1], [2]], 'expectedOutput': 1.5}, {'input': [[1, 2], []], 'expectedOutput': 1.5}, {'input': [[100], [101]], 'expectedOutput': 100.5}, {'input': [[1, 3, 5], [2, 4, 6]], 'expectedOutput': 3.5}, {'input': [[1], [2, 3, 4, 5, 6, 7]], 'expectedOutput': 4}], 'Container With Most Water': [{'input': [[1, 1]], 'expectedOutput': 1}, {'input': [[1, 2, 1]], 'expectedOutput': 2}, {'input': [[10000, 1, 1, 1, 1, 10000]], 'expectedOutput': 50000}, {'input': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 'expectedOutput': 25}], '3Sum': [{'input': [[0, 0, 0]], 'expectedOutput': [[0, 0, 0]]}, {'input': [[1, 2, -3]], 'expectedOutput': []}, {'input': [[-1, 0, 1, 0]], 'expectedOutput': [[-1, 0, 1]]}, {'input': [[-2, 0, 0, 2, 2]], 'expectedOutput': [[-2, 0, 2]]}], 'Letter Combinations of a Phone Number': [{'input': [''], 'expectedOutput': []}, {'input': ['2'], 'expectedOutput': ['a', 'b', 'c']}, {'input': ['99'], 'expectedOutput': ['ww', 'wx', 'wy', 'wz', 'xw', 'xx', 'xy', 'xz', 'yw', 'yx', 'yy', 'yz', 'zw', 'zx', 'zy', 'zz']}], 'Remove Nth Node From End of List': [{'input': [[1], 1], 'expectedOutput': []}, {'input': [[1, 2], 1], 'expectedOutput': [1]}, {'input': [[1, 2], 2], 'expectedOutput': [2]}, {'input': [[1, 2, 3, 4, 5], 3], 'expectedOutput': [1, 2, 4, 5]}], 'Generate Parentheses': [{'input': [1], 'expectedOutput': ['()']}, {'input': [4], 'expectedOutput': ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']}], 'Swap Nodes in Pairs': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}, {'input': [[1, 2, 3]], 'expectedOutput': [2, 1, 3]}, {'input': [[1, 2, 3, 4, 5, 6]], 'expectedOutput': [2, 1, 4, 3, 6, 5]}], 'Group Anagrams': [{'input': [['']], 'expectedOutput': [['']]}, {'input': [['a']], 'expectedOutput': [['a']]}, {'input': [['abc', 'bca', 'cab', 'xyz', 'zyx']], 'expectedOutput': [['abc', 'bca', 'cab'], ['xyz', 'zyx']]}], 'Maximum Subarray': [{'input': [[1]], 'expectedOutput': 1}, {'input': [[-1]], 'expectedOutput': -1}, {'input': [[5, -3, 5]], 'expectedOutput': 7}, {'input': [[-2, -3, -1, -5]], 'expectedOutput': -1}], 'Spiral Matrix': [{'input': [[[1]]], 'expectedOutput': [1]}, {'input': [[[1, 2, 3]]], 'expectedOutput': [1, 2, 3]}, {'input': [[[1], [2], [3]]], 'expectedOutput': [1, 2, 3]}], 'Merge Intervals': [{'input': [[[1, 3]]], 'expectedOutput': [[1, 3]]}, {'input': [[[1, 10], [2, 3], [4, 5], [6, 7]]], 'expectedOutput': [[1, 10]]}, {'input': [[[1, 2], [3, 4], [5, 6]]], 'expectedOutput': [[1, 2], [3, 4], [5, 6]]}], 'Unique Paths': [{'input': [1, 1], 'expectedOutput': 1}, {'input': [1, 10], 'expectedOutput': 1}, {'input': [10, 1], 'expectedOutput': 1}, {'input': [3, 3], 'expectedOutput': 6}], 'Minimum Path Sum': [{'input': [[[1]]], 'expectedOutput': 1}, {'input': [[[1, 2], [3, 4]]], 'expectedOutput': 7}, {'input': [[[1, 1, 1], [1, 1, 1]]], 'expectedOutput': 4}], 'Subsets': [{'input': [[]], 'expectedOutput': [[]]}, {'input': [[1]], 'expectedOutput': [[], [1]]}, {'input': [[1, 2, 3, 4]], 'expectedOutput': [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]}], 'Word Search': [{'input': [[['A']], 'A'], 'expectedOutput': True}, {'input': [[['A']], 'B'], 'expectedOutput': False}, {'input': [[['A', 'B'], ['C', 'D']], 'ABDC'], 'expectedOutput': True}], 'Validate Binary Search Tree': [{'input': [[]], 'expectedOutput': True}, {'input': [[1]], 'expectedOutput': True}, {'input': [[10, 5, 15, None, None, 6, 20]], 'expectedOutput': False}, {'input': [[5, 3, 8, 1, 4, 7, 9]], 'expectedOutput': True}], 'Binary Tree Level Order Traversal': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [[1]]}, {'input': [[1, None, 2, None, 3]], 'expectedOutput': [[1], [2], [3]]}], 'Construct Binary Tree from Preorder and Inorder Traversal': [{'input': [[1], [1]], 'expectedOutput': [1]}, {'input': [[1, 2], [2, 1]], 'expectedOutput': [1, 2, None]}, {'input': [[1, 2], [1, 2]], 'expectedOutput': [1, None, 2]}], 'Best Time to Buy and Sell Stock II': [{'input': [[1]], 'expectedOutput': 0}, {'input': [[7, 6, 5, 4, 3, 2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 3, 4, 5, 6, 7]], 'expectedOutput': 6}, {'input': [[1, 7, 2, 8]], 'expectedOutput': 12}], 'Longest Consecutive Sequence': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[1, 3, 5, 7, 9]], 'expectedOutput': 1}, {'input': [[100, 1, 200, 2, 3, 4]], 'expectedOutput': 4}], 'Clone Graph': [{'input': [[]], 'expectedOutput': []}, {'input': [[[1, []]]], 'expectedOutput': [[1, []]]}, {'input': [[[1, [2]], [2, [1]]]], 'expectedOutput': [[1, [2]], [2, [1]]]}], 'Gas Station': [{'input': [[5], [4]], 'expectedOutput': 0}, {'input': [[2], [3]], 'expectedOutput': -1}, {'input': [[5, 1, 2, 3, 4], [4, 4, 1, 5, 1]], 'expectedOutput': 4}], 'Word Break': [{'input': ['', []], 'expectedOutput': True}, {'input': ['a', ['a']], 'expectedOutput': True}, {'input': ['abc', ['a', 'b', 'c']], 'expectedOutput': True}, {'input': ['aaaaaaa', ['aaaa', 'aaa']], 'expectedOutput': True}], 'LRU Cache': [{'input': [[['put', 1, 1], ['get', 1]], 1], 'expectedOutput': [None, 1]}, {'input': [[['put', 1, 1], ['put', 2, 2], ['get', 1], ['put', 3, 3], ['get', 2]], 2], 'expectedOutput': [None, None, 1, None, -1]}], 'Evaluate Reverse Polish Notation': [{'input': [['1']], 'expectedOutput': 1}, {'input': [['1', '2', '+']], 'expectedOutput': 3}, {'input': [['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']], 'expectedOutput': 22}], 'Find Peak Element': [{'input': [[1]], 'expectedOutput': 0}, {'input': [[1, 2]], 'expectedOutput': 1}, {'input': [[2, 1]], 'expectedOutput': 0}, {'input': [[1, 2, 1, 3, 5, 6, 4]], 'expectedOutput': 5}], 'Rotate Array': [{'input': [[1], 0], 'expectedOutput': [1]}, {'input': [[1, 2], 3], 'expectedOutput': [2, 1]}, {'input': [[-1], 2], 'expectedOutput': [-1]}], 'Number of Islands': [{'input': [[['0']]], 'expectedOutput': 0}, {'input': [[['1']]], 'expectedOutput': 1}, {'input': [[['1', '0', '1'], ['0', '1', '0'], ['1', '0', '1']]], 'expectedOutput': 5}], 'Course Schedule': [{'input': [1, []], 'expectedOutput': True}, {'input': [2, [[0, 1], [1, 0]]], 'expectedOutput': False}, {'input': [3, [[0, 1], [0, 2], [1, 2]]], 'expectedOutput': True}], 'Binary Tree Inorder Traversal': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}, {'input': [[1, None, 2, None, 3]], 'expectedOutput': [1, 2, 3]}, {'input': [[1, 2, 3, 4, 5]], 'expectedOutput': [4, 2, 5, 1, 3]}], 'Linked List Cycle': [{'input': [[1], -1], 'expectedOutput': False}, {'input': [[1, 2], 0], 'expectedOutput': True}, {'input': [[1, 2, 3, 4], 1], 'expectedOutput': True}, {'input': [[1, 2, 3, 4, 5], -1], 'expectedOutput': False}], 'Longest Palindromic Substring': [{'input': ['a'], 'expectedOutput': 'a'}, {'input': ['aa'], 'expectedOutput': 'aa'}, {'input': ['abc'], 'expectedOutput': 'a'}, {'input': ['racecar'], 'expectedOutput': 'racecar'}], 'Product of Array Except Self': [{'input': [[1]], 'expectedOutput': [1]}, {'input': [[0, 0]], 'expectedOutput': [0, 0]}, {'input': [[1, 2, 3, 4]], 'expectedOutput': [24, 12, 8, 6]}, {'input': [[-1, 1, 0, -3, 3]], 'expectedOutput': [0, 0, 9, 0, 0]}], 'Rotate Image': [{'input': [[[1]]], 'expectedOutput': [[1]]}, {'input': [[[1, 2], [3, 4]]], 'expectedOutput': [[3, 1], [4, 2]]}, {'input': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 'expectedOutput': [[7, 4, 1], [8, 5, 2], [9, 6, 3]]}], 'Set Matrix Zeroes': [{'input': [[[0]]], 'expectedOutput': [[0]]}, {'input': [[[1]]], 'expectedOutput': [[1]]}, {'input': [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]], 'expectedOutput': [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}], 'Subarray Sum Equals K': [{'input': [[1], 1], 'expectedOutput': 1}, {'input': [[1], 0], 'expectedOutput': 0}, {'input': [[1, 1, 1], 2], 'expectedOutput': 2}, {'input': [[1, 2, 3], 3], 'expectedOutput': 2}], 'Reverse Linked List II': [{'input': [[1], 1, 1], 'expectedOutput': [1]}, {'input': [[1, 2], 1, 2], 'expectedOutput': [2, 1]}, {'input': [[1, 2, 3], 2, 3], 'expectedOutput': [1, 3, 2]}, {'input': [[1, 2, 3, 4, 5], 2, 4], 'expectedOutput': [1, 4, 3, 2, 5]}], 'Kth Smallest Element in a BST': [{'input': [[1], 1], 'expectedOutput': 1}, {'input': [[2, 1, 3], 2], 'expectedOutput': 2}, {'input': [[5, 3, 6, 2, 4, None, None, 1], 3], 'expectedOutput': 3}], 'Binary Tree Right Side View': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}, {'input': [[1, None, 3]], 'expectedOutput': [1, 3]}, {'input': [[1, 2, 3, None, 5]], 'expectedOutput': [1, 3, 5]}], 'Path Sum II': [{'input': [[]], 'expectedOutput': []}, {'input': [[1], 1], 'expectedOutput': [[1]]}, {'input': [[1, 2, 3], 3], 'expectedOutput': [[1, 2]]}, {'input': [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], 'expectedOutput': [[5, 4, 11, 2], [5, 8, 4, 5]]}], 'Lowest Common Ancestor of a Binary Tree': [{'input': [[1], 1, 1], 'expectedOutput': 1}, {'input': [[3, 5, 1], 5, 1], 'expectedOutput': 3}, {'input': [[3, 5, 1, 6, 2], 5, 1], 'expectedOutput': 3}, {'input': [[3, 5, 1, 6, 2, 0, 8], 5, 4], 'expectedOutput': 5}], 'Coin Change': [{'input': [[1], 0], 'expectedOutput': 0}, {'input': [[1], 1], 'expectedOutput': 1}, {'input': [[2], 3], 'expectedOutput': -1}, {'input': [[1, 2, 5], 11], 'expectedOutput': 3}], 'Longest Increasing Subsequence': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[1, 2, 3, 4]], 'expectedOutput': 4}, {'input': [[10, 9, 2, 5, 3, 7, 101, 18]], 'expectedOutput': 4}], 'House Robber II': [{'input': [[1]], 'expectedOutput': 1}, {'input': [[1, 2]], 'expectedOutput': 2}, {'input': [[2, 3, 2]], 'expectedOutput': 3}, {'input': [[1, 2, 3, 1]], 'expectedOutput': 4}], 'Decode Ways': [{'input': ['0'], 'expectedOutput': 0}, {'input': ['1'], 'expectedOutput': 1}, {'input': ['12'], 'expectedOutput': 2}, {'input': ['226'], 'expectedOutput': 3}, {'input': ['06'], 'expectedOutput': 0}], 'Permutations': [{'input': [[]], 'expectedOutput': [[]]}, {'input': [[1]], 'expectedOutput': [[1]]}, {'input': [[1, 2]], 'expectedOutput': [[1, 2], [2, 1]]}], 'Trapping Rain Water': [{'input': [[]], 'expectedOutput': 0}, {'input': [[1]], 'expectedOutput': 0}, {'input': [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 'expectedOutput': 6}], 'Binary Tree Maximum Path Sum': [{'input': [[1]], 'expectedOutput': 1}, {'input': [[-3]], 'expectedOutput': -3}, {'input': [[1, 2, 3]], 'expectedOutput': 6}, {'input': [[-10, 9, 20, None, None, 15, 7]], 'expectedOutput': 42}], 'Serialize and Deserialize Binary Tree': [{'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}, {'input': [[1, 2, 3]], 'expectedOutput': [1, 2, 3]}], 'Regular Expression Matching': [{'input': ['', ''], 'expectedOutput': True}, {'input': ['a', 'a'], 'expectedOutput': True}, {'input': ['a', 'b'], 'expectedOutput': False}, {'input': ['aa', 'a*'], 'expectedOutput': True}, {'input': ['ab', '.*'], 'expectedOutput': True}], 'Edit Distance': [{'input': ['', ''], 'expectedOutput': 0}, {'input': ['a', 'a'], 'expectedOutput': 0}, {'input': ['a', 'b'], 'expectedOutput': 1}, {'input': ['horse', 'ros'], 'expectedOutput': 3}], 'Word Ladder': [{'input': ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']], 'expectedOutput': 5}, {'input': ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']], 'expectedOutput': 0}], 'Merge k Sorted Lists': [{'input': [[]], 'expectedOutput': []}, {'input': [[[1, 4, 5], [1, 3, 4], [2, 6]]], 'expectedOutput': [1, 1, 2, 3, 4, 4, 5, 6]}]}

# Python imports from the second script
PYTHON_IMPORTS = {'Clone Graph': 'from typing import Optional\n\n# Definition for a Node.\nclass Node:\n    def __init__(self, val = 0, neighbors = None):\n        self.val = val\n        self.neighbors = neighbors if neighbors is not None else []', 'Lowest Common Ancestor of a Binary Tree': 'from typing import Optional\n\n# Definition for a binary tree node.\nclass TreeNode:\n    def __init__(self, x):\n        self.val = x\n        self.left = None\n        self.right = None'}

def get_db_path():
    """Get the database path based on OS"""
    if os.name == 'nt':  # Windows
        db_path = Path(os.environ.get('APPDATA', '')) / 'interview-prep-platform' / 'interview-prep.db'
    elif sys.platform == 'darwin':  # macOS
        db_path = Path.home() / 'Library' / 'Application Support' / 'interview-prep-platform' / 'interview-prep.db'
    else:  # Linux
        db_path = Path.home() / '.config' / 'interview-prep-platform' / 'interview-prep.db'
    return db_path

def main():
    print("=" * 70)
    print("Complete Database Setup")
    print("=" * 70)
    print()

    db_path = get_db_path()

    if not db_path.exists():
        print(f"❌ Database not found at: {db_path}")
        print("   Please run the application first to create the database.")
        print("   Or run: npm run db:init")
        sys.exit(1)

    print(f"📂 Database: {db_path}")
    print()

    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Update hidden test cases
        print("📝 Updating hidden test cases...")
        updated_count = 0
        for title, hidden_tests in HIDDEN_TEST_CASES.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET hidden_test_cases = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (json.dumps(hidden_tests), title))

            if cursor.rowcount > 0:
                updated_count += 1
                print(f"   ✅ {title}")

        print(f"\n✅ Updated hidden test cases for {updated_count} questions")

        # Update Python imports
        print("\n📝 Updating Python imports...")
        imports_count = 0
        for title, imports in PYTHON_IMPORTS.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET function_signature_python = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (imports, title))

            if cursor.rowcount > 0:
                imports_count += 1
                print(f"   ✅ {title}")

        print(f"\n✅ Updated imports for {imports_count} questions")

        # Commit changes
        conn.commit()

        # Verify setup
        print("\n🔍 Verifying setup...")
        cursor.execute("""
            SELECT COUNT(*) as total,
                   SUM(CASE WHEN json_array_length(hidden_test_cases) > 0 THEN 1 ELSE 0 END) as with_hidden
            FROM leetcode_questions
        """)

        total, with_hidden = cursor.fetchone()

        print(f"   Total questions: {total}")
        print(f"   With hidden tests: {with_hidden}")

        if with_hidden == total and total > 0:
            print("\n" + "=" * 70)
            print("✅ Database setup complete!")
            print("=" * 70)
            print("\n📊 Summary:")
            print(f"   • {total} LeetCode questions")
            print(f"   • {with_hidden} questions with hidden tests")
            print(f"   • ~{with_hidden * 3} visible test cases")
            print(f"   • ~{with_hidden * 4} hidden test cases")
            print(f"   • ~{with_hidden * 7} total test cases")
            print("\n🚀 Next steps:")
            print("   1. Set execution mode in .env (SANDBOX_MODE=local or docker)")
            print("   2. Start the app: npm run dev")
            print("   3. Try submitting a solution!")
            sys.exit(0)
        else:
            print("\n❌ Some questions missing hidden tests")
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
