# Hidden test cases to be added to questions_data_full.py

# Copy these into the appropriate questions in LEETCODE_QUESTIONS


# Two Sum

'hidden_test_cases': [
    {
        "input": [
            [
                1,
                1
            ],
            2
        ],
        "expectedOutput": [
            0,
            1
        ]
    },
    {
        "input": [
            [
                0,
                4,
                3,
                0
            ],
            0
        ],
        "expectedOutput": [
            0,
            3
        ]
    },
    {
        "input": [
            [
                -3,
                4,
                3,
                90
            ],
            0
        ],
        "expectedOutput": [
            0,
            2
        ]
    },
    {
        "input": [
            [
                1000000000,
                -1000000000,
                999999999,
                -999999999
            ],
            0
        ],
        "expectedOutput": [
            0,
            1
        ]
    }
],

'python_imports': '''from typing import List''',



# Valid Parentheses

'hidden_test_cases': [
    {
        "input": [
            "((()))"
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "((("
        ],
        "expectedOutput": false
    },
    {
        "input": [
            ")))"
        ],
        "expectedOutput": false
    },
    {
        "input": [
            "{[(])}"
        ],
        "expectedOutput": false
    },
    {
        "input": [
            "()()()()()()()()()()()()()()()()()()()()"
        ],
        "expectedOutput": true
    }
],



# Merge Two Sorted Lists

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ],
            []
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                -100
            ],
            [
                100
            ]
        ],
        "expectedOutput": [
            -100,
            100
        ]
    },
    {
        "input": [
            [
                1,
                1,
                1
            ],
            [
                1,
                1,
                1
            ]
        ],
        "expectedOutput": [
            1,
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "input": [
            [
                5,
                6,
                7
            ],
            [
                1,
                2,
                3
            ]
        ],
        "expectedOutput": [
            1,
            2,
            3,
            5,
            6,
            7
        ]
    }
],

'python_imports': '''from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next''',



# Best Time to Buy and Sell Stock

'hidden_test_cases': [
    {
        "input": [
            [
                7,
                6,
                5,
                4,
                3,
                2,
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7
            ]
        ],
        "expectedOutput": 6
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                3,
                3,
                3,
                3,
                3
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                2,
                1,
                4,
                1,
                7
            ]
        ],
        "expectedOutput": 6
    }
],

'python_imports': '''from typing import List''',



# Valid Palindrome

'hidden_test_cases': [
    {
        "input": [
            ""
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "a"
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "aa"
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "ab"
        ],
        "expectedOutput": false
    },
    {
        "input": [
            ".,!@#$%^&*()"
        ],
        "expectedOutput": true
    }
],



# Maximum Depth of Binary Tree

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                1,
                null,
                2,
                null,
                3,
                null,
                4
            ]
        ],
        "expectedOutput": 4
    },
    {
        "input": [
            [
                1,
                2,
                null,
                3,
                null,
                4,
                null
            ]
        ],
        "expectedOutput": 4
    }
],

'python_imports': '''from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right''',



# Climbing Stairs

'hidden_test_cases': [
    {
        "input": [
            1
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            2
        ],
        "expectedOutput": 2
    },
    {
        "input": [
            10
        ],
        "expectedOutput": 89
    },
    {
        "input": [
            35
        ],
        "expectedOutput": 14930352
    }
],



# Symmetric Tree

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": true
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": true
    },
    {
        "input": [
            [
                1,
                2,
                2,
                null,
                3,
                null,
                3
            ]
        ],
        "expectedOutput": false
    },
    {
        "input": [
            [
                1,
                2,
                2,
                2,
                null,
                2,
                null
            ]
        ],
        "expectedOutput": false
    }
],

'python_imports': '''from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right''',



# Add Two Numbers

'hidden_test_cases': [
    {
        "input": [
            [
                0
            ],
            [
                0
            ]
        ],
        "expectedOutput": [
            0
        ]
    },
    {
        "input": [
            [
                9,
                9,
                9,
                9
            ],
            [
                1
            ]
        ],
        "expectedOutput": [
            0,
            0,
            0,
            0,
            1
        ]
    },
    {
        "input": [
            [
                1
            ],
            [
                9,
                9,
                9
            ]
        ],
        "expectedOutput": [
            0,
            0,
            0,
            1
        ]
    },
    {
        "input": [
            [
                5
            ],
            [
                5
            ]
        ],
        "expectedOutput": [
            0,
            1
        ]
    }
],

'python_imports': '''from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next''',



# Longest Substring Without Repeating Characters

'hidden_test_cases': [
    {
        "input": [
            ""
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            "a"
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            "aaaaaaa"
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            "abcdefghijklmnopqrstuvwxyz"
        ],
        "expectedOutput": 26
    },
    {
        "input": [
            "dvdf"
        ],
        "expectedOutput": 3
    }
],



# Median of Two Sorted Arrays

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ],
            [
                2
            ]
        ],
        "expectedOutput": 1.5
    },
    {
        "input": [
            [
                1,
                2
            ],
            []
        ],
        "expectedOutput": 1.5
    },
    {
        "input": [
            [
                100
            ],
            [
                101
            ]
        ],
        "expectedOutput": 100.5
    },
    {
        "input": [
            [
                1,
                3,
                5
            ],
            [
                2,
                4,
                6
            ]
        ],
        "expectedOutput": 3.5
    },
    {
        "input": [
            [
                1
            ],
            [
                2,
                3,
                4,
                5,
                6,
                7
            ]
        ],
        "expectedOutput": 4
    }
],

'python_imports': '''from typing import List''',



# Container With Most Water

'hidden_test_cases': [
    {
        "input": [
            [
                1,
                1
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                1,
                2,
                1
            ]
        ],
        "expectedOutput": 2
    },
    {
        "input": [
            [
                10000,
                1,
                1,
                1,
                1,
                10000
            ]
        ],
        "expectedOutput": 50000
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ]
        ],
        "expectedOutput": 25
    }
],

'python_imports': '''from typing import List''',



# 3Sum

'hidden_test_cases': [
    {
        "input": [
            [
                0,
                0,
                0
            ]
        ],
        "expectedOutput": [
            [
                0,
                0,
                0
            ]
        ]
    },
    {
        "input": [
            [
                1,
                2,
                -3
            ]
        ],
        "expectedOutput": []
    },
    {
        "input": [
            [
                -1,
                0,
                1,
                0
            ]
        ],
        "expectedOutput": [
            [
                -1,
                0,
                1
            ]
        ]
    },
    {
        "input": [
            [
                -2,
                0,
                0,
                2,
                2
            ]
        ],
        "expectedOutput": [
            [
                -2,
                0,
                2
            ]
        ]
    }
],

'python_imports': '''from typing import List''',



# Letter Combinations of a Phone Number

'hidden_test_cases': [
    {
        "input": [
            ""
        ],
        "expectedOutput": []
    },
    {
        "input": [
            "2"
        ],
        "expectedOutput": [
            "a",
            "b",
            "c"
        ]
    },
    {
        "input": [
            "99"
        ],
        "expectedOutput": [
            "ww",
            "wx",
            "wy",
            "wz",
            "xw",
            "xx",
            "xy",
            "xz",
            "yw",
            "yx",
            "yy",
            "yz",
            "zw",
            "zx",
            "zy",
            "zz"
        ]
    }
],

'python_imports': '''from typing import List''',



# Remove Nth Node From End of List

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ],
            1
        ],
        "expectedOutput": []
    },
    {
        "input": [
            [
                1,
                2
            ],
            1
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                1,
                2
            ],
            2
        ],
        "expectedOutput": [
            2
        ]
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4,
                5
            ],
            3
        ],
        "expectedOutput": [
            1,
            2,
            4,
            5
        ]
    }
],

'python_imports': '''from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next''',



# Generate Parentheses

'hidden_test_cases': [
    {
        "input": [
            1
        ],
        "expectedOutput": [
            "()"
        ]
    },
    {
        "input": [
            4
        ],
        "expectedOutput": [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()"
        ]
    }
],

'python_imports': '''from typing import List''',



# Swap Nodes in Pairs

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": []
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                1,
                2,
                3
            ]
        ],
        "expectedOutput": [
            2,
            1,
            3
        ]
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4,
                5,
                6
            ]
        ],
        "expectedOutput": [
            2,
            1,
            4,
            3,
            6,
            5
        ]
    }
],

'python_imports': '''from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next''',



# Group Anagrams

'hidden_test_cases': [
    {
        "input": [
            [
                ""
            ]
        ],
        "expectedOutput": [
            [
                ""
            ]
        ]
    },
    {
        "input": [
            [
                "a"
            ]
        ],
        "expectedOutput": [
            [
                "a"
            ]
        ]
    },
    {
        "input": [
            [
                "abc",
                "bca",
                "cab",
                "xyz",
                "zyx"
            ]
        ],
        "expectedOutput": [
            [
                "abc",
                "bca",
                "cab"
            ],
            [
                "xyz",
                "zyx"
            ]
        ]
    }
],

'python_imports': '''from typing import List''',



# Maximum Subarray

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                -1
            ]
        ],
        "expectedOutput": -1
    },
    {
        "input": [
            [
                5,
                -3,
                5
            ]
        ],
        "expectedOutput": 7
    },
    {
        "input": [
            [
                -2,
                -3,
                -1,
                -5
            ]
        ],
        "expectedOutput": -1
    }
],

'python_imports': '''from typing import List''',



# Spiral Matrix

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    1
                ]
            ]
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                [
                    1,
                    2,
                    3
                ]
            ]
        ],
        "expectedOutput": [
            1,
            2,
            3
        ]
    },
    {
        "input": [
            [
                [
                    1
                ],
                [
                    2
                ],
                [
                    3
                ]
            ]
        ],
        "expectedOutput": [
            1,
            2,
            3
        ]
    }
],

'python_imports': '''from typing import List''',



# Merge Intervals

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    1,
                    3
                ]
            ]
        ],
        "expectedOutput": [
            [
                1,
                3
            ]
        ]
    },
    {
        "input": [
            [
                [
                    1,
                    10
                ],
                [
                    2,
                    3
                ],
                [
                    4,
                    5
                ],
                [
                    6,
                    7
                ]
            ]
        ],
        "expectedOutput": [
            [
                1,
                10
            ]
        ]
    },
    {
        "input": [
            [
                [
                    1,
                    2
                ],
                [
                    3,
                    4
                ],
                [
                    5,
                    6
                ]
            ]
        ],
        "expectedOutput": [
            [
                1,
                2
            ],
            [
                3,
                4
            ],
            [
                5,
                6
            ]
        ]
    }
],

'python_imports': '''from typing import List''',



# Unique Paths

'hidden_test_cases': [
    {
        "input": [
            1,
            1
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            1,
            10
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            10,
            1
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            3,
            3
        ],
        "expectedOutput": 6
    }
],



# Minimum Path Sum

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    1
                ]
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                [
                    1,
                    2
                ],
                [
                    3,
                    4
                ]
            ]
        ],
        "expectedOutput": 7
    },
    {
        "input": [
            [
                [
                    1,
                    1,
                    1
                ],
                [
                    1,
                    1,
                    1
                ]
            ]
        ],
        "expectedOutput": 4
    }
],

'python_imports': '''from typing import List''',



# Subsets

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": [
            []
        ]
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": [
            [],
            [
                1
            ]
        ]
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4
            ]
        ],
        "expectedOutput": [
            [],
            [
                1
            ],
            [
                2
            ],
            [
                1,
                2
            ],
            [
                3
            ],
            [
                1,
                3
            ],
            [
                2,
                3
            ],
            [
                1,
                2,
                3
            ],
            [
                4
            ],
            [
                1,
                4
            ],
            [
                2,
                4
            ],
            [
                1,
                2,
                4
            ],
            [
                3,
                4
            ],
            [
                1,
                3,
                4
            ],
            [
                2,
                3,
                4
            ],
            [
                1,
                2,
                3,
                4
            ]
        ]
    }
],

'python_imports': '''from typing import List''',



# Word Search

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    "A"
                ]
            ],
            "A"
        ],
        "expectedOutput": true
    },
    {
        "input": [
            [
                [
                    "A"
                ]
            ],
            "B"
        ],
        "expectedOutput": false
    },
    {
        "input": [
            [
                [
                    "A",
                    "B"
                ],
                [
                    "C",
                    "D"
                ]
            ],
            "ABDC"
        ],
        "expectedOutput": true
    }
],

'python_imports': '''from typing import List''',



# Validate Binary Search Tree

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": true
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": true
    },
    {
        "input": [
            [
                10,
                5,
                15,
                null,
                null,
                6,
                20
            ]
        ],
        "expectedOutput": false
    },
    {
        "input": [
            [
                5,
                3,
                8,
                1,
                4,
                7,
                9
            ]
        ],
        "expectedOutput": true
    }
],

'python_imports': '''from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right''',



# Binary Tree Level Order Traversal

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": []
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": [
            [
                1
            ]
        ]
    },
    {
        "input": [
            [
                1,
                null,
                2,
                null,
                3
            ]
        ],
        "expectedOutput": [
            [
                1
            ],
            [
                2
            ],
            [
                3
            ]
        ]
    }
],

'python_imports': '''from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right''',



# Construct Binary Tree from Preorder and Inorder Traversal

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ],
            [
                1
            ]
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                1,
                2
            ],
            [
                2,
                1
            ]
        ],
        "expectedOutput": [
            1,
            2,
            null
        ]
    },
    {
        "input": [
            [
                1,
                2
            ],
            [
                1,
                2
            ]
        ],
        "expectedOutput": [
            1,
            null,
            2
        ]
    }
],

'python_imports': '''from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right''',



# Best Time to Buy and Sell Stock II

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                7,
                6,
                5,
                4,
                3,
                2,
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7
            ]
        ],
        "expectedOutput": 6
    },
    {
        "input": [
            [
                1,
                7,
                2,
                8
            ]
        ],
        "expectedOutput": 12
    }
],

'python_imports': '''from typing import List''',



# Longest Consecutive Sequence

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                1,
                3,
                5,
                7,
                9
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                100,
                1,
                200,
                2,
                3,
                4
            ]
        ],
        "expectedOutput": 4
    }
],

'python_imports': '''from typing import List''',



# Clone Graph

'hidden_test_cases': [
    {
        "input": [
            []
        ],
        "expectedOutput": []
    },
    {
        "input": [
            [
                [
                    1,
                    []
                ]
            ]
        ],
        "expectedOutput": [
            [
                1,
                []
            ]
        ]
    },
    {
        "input": [
            [
                [
                    1,
                    [
                        2
                    ]
                ],
                [
                    2,
                    [
                        1
                    ]
                ]
            ]
        ],
        "expectedOutput": [
            [
                1,
                [
                    2
                ]
            ],
            [
                2,
                [
                    1
                ]
            ]
        ]
    }
],

'python_imports': '''from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []''',



# Gas Station

'hidden_test_cases': [
    {
        "input": [
            [
                5
            ],
            [
                4
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                2
            ],
            [
                3
            ]
        ],
        "expectedOutput": -1
    },
    {
        "input": [
            [
                5,
                1,
                2,
                3,
                4
            ],
            [
                4,
                4,
                1,
                5,
                1
            ]
        ],
        "expectedOutput": 4
    }
],

'python_imports': '''from typing import List''',



# Word Break

'hidden_test_cases': [
    {
        "input": [
            "",
            []
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "a",
            [
                "a"
            ]
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "abc",
            [
                "a",
                "b",
                "c"
            ]
        ],
        "expectedOutput": true
    },
    {
        "input": [
            "aaaaaaa",
            [
                "aaaa",
                "aaa"
            ]
        ],
        "expectedOutput": true
    }
],

'python_imports': '''from typing import List''',



# LRU Cache

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    "put",
                    1,
                    1
                ],
                [
                    "get",
                    1
                ]
            ],
            1
        ],
        "expectedOutput": [
            null,
            1
        ]
    },
    {
        "input": [
            [
                [
                    "put",
                    1,
                    1
                ],
                [
                    "put",
                    2,
                    2
                ],
                [
                    "get",
                    1
                ],
                [
                    "put",
                    3,
                    3
                ],
                [
                    "get",
                    2
                ]
            ],
            2
        ],
        "expectedOutput": [
            null,
            null,
            1,
            null,
            -1
        ]
    }
],



# Evaluate Reverse Polish Notation

'hidden_test_cases': [
    {
        "input": [
            [
                "1"
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                "1",
                "2",
                "+"
            ]
        ],
        "expectedOutput": 3
    },
    {
        "input": [
            [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+"
            ]
        ],
        "expectedOutput": 22
    }
],

'python_imports': '''from typing import List''',



# Find Peak Element

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1,
                2
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                2,
                1
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                1,
                2,
                1,
                3,
                5,
                6,
                4
            ]
        ],
        "expectedOutput": 5
    }
],

'python_imports': '''from typing import List''',



# Rotate Array

'hidden_test_cases': [
    {
        "input": [
            [
                1
            ],
            0
        ],
        "expectedOutput": [
            1
        ]
    },
    {
        "input": [
            [
                1,
                2
            ],
            3
        ],
        "expectedOutput": [
            2,
            1
        ]
    },
    {
        "input": [
            [
                -1
            ],
            2
        ],
        "expectedOutput": [
            -1
        ]
    }
],

'python_imports': '''from typing import List''',



# Number of Islands

'hidden_test_cases': [
    {
        "input": [
            [
                [
                    "0"
                ]
            ]
        ],
        "expectedOutput": 0
    },
    {
        "input": [
            [
                [
                    "1"
                ]
            ]
        ],
        "expectedOutput": 1
    },
    {
        "input": [
            [
                [
                    "1",
                    "0",
                    "1"
                ],
                [
                    "0",
                    "1",
                    "0"
                ],
                [
                    "1",
                    "0",
                    "1"
                ]
            ]
        ],
        "expectedOutput": 5
    }
],

'python_imports': '''from typing import List''',



# Course Schedule

'hidden_test_cases': [
    {
        "input": [
            1,
            []
        ],
        "expectedOutput": true
    },
    {
        "input": [
            2,
            [
                [
                    0,
                    1
                ],
                [
                    1,
                    0
                ]
            ]
        ],
        "expectedOutput": false
    },
    {
        "input": [
            3,
            [
                [
                    0,
                    1
                ],
                [
                    0,
                    2
                ],
                [
                    1,
                    2
                ]
            ]
        ],
        "expectedOutput": true
    }
],

'python_imports': '''from typing import List''',


