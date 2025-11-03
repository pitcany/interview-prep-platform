#!/usr/bin/env python3
"""
Complete dataset of 40 LeetCode + 10 ML System Design questions
Distribution: 8 Easy, 35 Medium, 8 Hard LeetCode questions (51 total, filter to 40)
"""

# 40 LeetCode Questions - Real problems with complete details
LEETCODE_QUESTIONS = [
    # ============ EASY (8 questions) ============
    {
        "title": "Two Sum",
        "leetcode_url": "https://leetcode.com/problems/two-sum/",
        "difficulty": "easy",
        "description": """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.""",
        "constraints": ["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9", "Only one valid answer exists"],
        "examples": [
            {"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1], "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."},
            {"input": {"nums": [3,2,4], "target": 6}, "output": [1,2], "explanation": "Because nums[1] + nums[2] == 6, we return [1, 2]."}
        ],
        "tags": ["array", "hash-table"],
        "test_cases": [
            {"input": [[2,7,11,15], 9], "expectedOutput": [0,1]},
            {"input": [[3,2,4], 6], "expectedOutput": [1,2]},
            {"input": [[3,3], 6], "expectedOutput": [0,1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};"
    },
    {
        "title": "Valid Parentheses",
        "leetcode_url": "https://leetcode.com/problems/valid-parentheses/",
        "difficulty": "easy",
        "description": """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.""",
        "constraints": ["1 <= s.length <= 10^4", "s consists of parentheses only '()[]{}'"],
        "examples": [
            {"input": {"s": "()"}, "output": True, "explanation": "The string is valid."},
            {"input": {"s": "()[]{}"}, "output": True, "explanation": "All brackets are properly closed."},
            {"input": {"s": "(]"}, "output": False, "explanation": "Mismatched brackets."}
        ],
        "tags": ["string", "stack"],
        "test_cases": [
            {"input": ["()"], "expectedOutput": True},
            {"input": ["()[]{}"], "expectedOutput": True},
            {"input": ["(]"], "expectedOutput": False},
            {"input": ["([)]"], "expectedOutput": False}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def isValid(self, s: str) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean isValid(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool isValid(string s) {\n        \n    }\n};"
    },
    {
        "title": "Merge Two Sorted Lists",
        "leetcode_url": "https://leetcode.com/problems/merge-two-sorted-lists/",
        "difficulty": "easy",
        "description": """You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.""",
        "constraints": ["The number of nodes in both lists is in the range [0, 50]", "-100 <= Node.val <= 100", "Both list1 and list2 are sorted in non-decreasing order"],
        "examples": [
            {"input": {"list1": [1,2,4], "list2": [1,3,4]}, "output": [1,1,2,3,4,4], "explanation": "Merge both sorted lists."},
            {"input": {"list1": [], "list2": []}, "output": [], "explanation": "Both lists are empty."}
        ],
        "tags": ["linked-list", "recursion"],
        "test_cases": [
            {"input": [[1,2,4], [1,3,4]], "expectedOutput": [1,1,2,3,4,4]},
            {"input": [[], []], "expectedOutput": []},
            {"input": [[], [0]], "expectedOutput": [0]}
        ],
        "time_complexity": "O(n+m)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        \n    }\n};"
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "leetcode_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "difficulty": "easy",
        "description": """You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.""",
        "constraints": ["1 <= prices.length <= 10^5", "0 <= prices[i] <= 10^4"],
        "examples": [
            {"input": {"prices": [7,1,5,3,6,4]}, "output": 5, "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5."},
            {"input": {"prices": [7,6,4,3,1]}, "output": 0, "explanation": "In this case, no transactions are done and the max profit = 0."}
        ],
        "tags": ["array", "dynamic-programming"],
        "test_cases": [
            {"input": [[7,1,5,3,6,4]], "expectedOutput": 5},
            {"input": [[7,6,4,3,1]], "expectedOutput": 0}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int maxProfit(int[] prices) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        \n    }\n};"
    },
    {
        "title": "Valid Palindrome",
        "leetcode_url": "https://leetcode.com/problems/valid-palindrome/",
        "difficulty": "easy",
        "description": """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.""",
        "constraints": ["1 <= s.length <= 2 * 10^5", "s consists only of printable ASCII characters"],
        "examples": [
            {"input": {"s": "A man, a plan, a canal: Panama"}, "output": True, "explanation": "After cleaning: amanaplanacanalpanama which is a palindrome."},
            {"input": {"s": "race a car"}, "output": False, "explanation": "After cleaning: raceacar which is not a palindrome."}
        ],
        "tags": ["two-pointers", "string"],
        "test_cases": [
            {"input": ["A man, a plan, a canal: Panama"], "expectedOutput": True},
            {"input": ["race a car"], "expectedOutput": False},
            {"input": [" "], "expectedOutput": True}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean isPalindrome(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool isPalindrome(string s) {\n        \n    }\n};"
    },
    {
        "title": "Climbing Stairs",
        "leetcode_url": "https://leetcode.com/problems/climbing-stairs/",
        "difficulty": "easy",
        "description": """You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?""",
        "constraints": ["1 <= n <= 45"],
        "examples": [
            {"input": {"n": 2}, "output": 2, "explanation": "There are two ways: 1. 1 step + 1 step, 2. 2 steps"},
            {"input": {"n": 3}, "output": 3, "explanation": "There are three ways: 1. 1+1+1, 2. 1+2, 3. 2+1"}
        ],
        "tags": ["dynamic-programming", "math"],
        "test_cases": [
            {"input": [2], "expectedOutput": 2},
            {"input": [3], "expectedOutput": 3},
            {"input": [4], "expectedOutput": 5}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def climbStairs(self, n: int) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int climbStairs(int n) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int climbStairs(int n) {\n        \n    }\n};"
    },
    {
        "title": "Binary Tree Inorder Traversal",
        "leetcode_url": "https://leetcode.com/problems/binary-tree-inorder-traversal/",
        "difficulty": "easy",
        "description": """Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal: Left -> Root -> Right""",
        "constraints": ["The number of nodes in the tree is in the range [0, 100]", "-100 <= Node.val <= 100"],
        "examples": [
            {"input": {"root": [1,None,2,3]}, "output": [1,3,2], "explanation": "Inorder traversal of the tree."},
            {"input": {"root": []}, "output": [], "explanation": "Empty tree."}
        ],
        "tags": ["tree", "depth-first-search", "stack"],
        "test_cases": [
            {"input": [[1,None,2,3]], "expectedOutput": [1,3,2]},
            {"input": [[]], "expectedOutput": []},
            {"input": [[1]], "expectedOutput": [1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public List<Integer> inorderTraversal(TreeNode root) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        \n    }\n};"
    },
    {
        "title": "Linked List Cycle",
        "leetcode_url": "https://leetcode.com/problems/linked-list-cycle/",
        "difficulty": "easy",
        "description": """Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.""",
        "constraints": ["The number of the nodes in the list is in the range [0, 10^4]", "-10^5 <= Node.val <= 10^5", "pos is -1 or a valid index in the linked-list"],
        "examples": [
            {"input": {"head": [3,2,0,-4], "pos": 1}, "output": True, "explanation": "There is a cycle where the tail connects to the 1st node."},
            {"input": {"head": [1], "pos": -1}, "output": False, "explanation": "There is no cycle in the linked list."}
        ],
        "tags": ["linked-list", "two-pointers", "hash-table"],
        "test_cases": [
            {"input": [[3,2,0,-4], 1], "expectedOutput": True},
            {"input": [[1,2], 0], "expectedOutput": True},
            {"input": [[1], -1], "expectedOutput": False}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean hasCycle(ListNode head) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool hasCycle(ListNode *head) {\n        \n    }\n};"
    },
    
    # ============ MEDIUM (25 questions) ============
    {
        "title": "Longest Substring Without Repeating Characters",
        "leetcode_url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "difficulty": "medium",
        "description": """Given a string s, find the length of the longest substring without repeating characters.""",
        "constraints": ["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"],
        "examples": [
            {"input": {"s": "abcabcbb"}, "output": 3, "explanation": "The answer is 'abc', with the length of 3."},
            {"input": {"s": "bbbbb"}, "output": 1, "explanation": "The answer is 'b', with the length of 1."}
        ],
        "tags": ["string", "sliding-window", "hash-table"],
        "test_cases": [
            {"input": ["abcabcbb"], "expectedOutput": 3},
            {"input": ["bbbbb"], "expectedOutput": 1},
            {"input": ["pwwkew"], "expectedOutput": 3}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(min(m,n))",
        "python_sig": "class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        \n    }\n};"
    },
    {
        "title": "Add Two Numbers",
        "leetcode_url": "https://leetcode.com/problems/add-two-numbers/",
        "difficulty": "medium",
        "description": """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.""",
        "constraints": ["The number of nodes in each linked list is in the range [1, 100]", "0 <= Node.val <= 9", "It is guaranteed that the list represents a number that does not have leading zeros"],
        "examples": [
            {"input": {"l1": [2,4,3], "l2": [5,6,4]}, "output": [7,0,8], "explanation": "342 + 465 = 807."},
            {"input": {"l1": [0], "l2": [0]}, "output": [0], "explanation": "0 + 0 = 0."}
        ],
        "tags": ["linked-list", "math", "recursion"],
        "test_cases": [
            {"input": [[2,4,3], [5,6,4]], "expectedOutput": [7,0,8]},
            {"input": [[0], [0]], "expectedOutput": [0]},
            {"input": [[9,9,9], [9,9,9,9]], "expectedOutput": [8,9,9,0,1]}
        ],
        "time_complexity": "O(max(m,n))",
        "space_complexity": "O(max(m,n))",
        "python_sig": "class Solution:\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        \n    }\n};"
    },
    {
        "title": "Container With Most Water",
        "leetcode_url": "https://leetcode.com/problems/container-with-most-water/",
        "difficulty": "medium",
        "description": """You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.""",
        "constraints": ["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"],
        "examples": [
            {"input": {"height": [1,8,6,2,5,4,8,3,7]}, "output": 49, "explanation": "The max area is between index 1 (height 8) and index 8 (height 7)."}
        ],
        "tags": ["array", "two-pointers", "greedy"],
        "test_cases": [
            {"input": [[1,8,6,2,5,4,8,3,7]], "expectedOutput": 49},
            {"input": [[1,1]], "expectedOutput": 1},
            {"input": [[4,3,2,1,4]], "expectedOutput": 16}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int maxArea(int[] height) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        \n    }\n};"
    },
    {
        "title": "3Sum",
        "leetcode_url": "https://leetcode.com/problems/3sum/",
        "difficulty": "medium",
        "description": """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.""",
        "constraints": ["3 <= nums.length <= 3000", "-10^5 <= nums[i] <= 10^5"],
        "examples": [
            {"input": {"nums": [-1,0,1,2,-1,-4]}, "output": [[-1,-1,2],[-1,0,1]], "explanation": "The distinct triplets are [-1,0,1] and [-1,-1,2]."},
            {"input": {"nums": [0,1,1]}, "output": [], "explanation": "The only possible triplet does not sum up to 0."}
        ],
        "tags": ["array", "two-pointers", "sorting"],
        "test_cases": [
            {"input": [[-1,0,1,2,-1,-4]], "expectedOutput": [[-1,-1,2],[-1,0,1]]},
            {"input": [[0,1,1]], "expectedOutput": []},
            {"input": [[0,0,0]], "expectedOutput": [[0,0,0]]}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        pass",
        "java_sig": "class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        \n    }\n};"
    },
    {
        "title": "Group Anagrams",
        "leetcode_url": "https://leetcode.com/problems/group-anagrams/",
        "difficulty": "medium",
        "description": """Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.""",
        "constraints": ["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100", "strs[i] consists of lowercase English letters"],
        "examples": [
            {"input": {"strs": ["eat","tea","tan","ate","nat","bat"]}, "output": [["bat"],["nat","tan"],["ate","eat","tea"]], "explanation": "Group words that are anagrams."}
        ],
        "tags": ["array", "hash-table", "string", "sorting"],
        "test_cases": [
            {"input": [["eat","tea","tan","ate","nat","bat"]], "expectedOutput": [["bat"],["nat","tan"],["ate","eat","tea"]]},
            {"input": [[""]], "expectedOutput": [[""]]},
            {"input": [["a"]], "expectedOutput": [["a"]]}
        ],
        "time_complexity": "O(n*k)",
        "space_complexity": "O(n*k)",
        "python_sig": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        pass",
        "java_sig": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        \n    }\n};"
    },
    {
        "title": "Longest Palindromic Substring",
        "leetcode_url": "https://leetcode.com/problems/longest-palindromic-substring/",
        "difficulty": "medium",
        "description": """Given a string s, return the longest palindromic substring in s.""",
        "constraints": ["1 <= s.length <= 1000", "s consist of only digits and English letters"],
        "examples": [
            {"input": {"s": "babad"}, "output": "bab", "explanation": "Note: 'aba' is also a valid answer."},
            {"input": {"s": "cbbd"}, "output": "bb", "explanation": "The longest palindrome is 'bb'."}
        ],
        "tags": ["string", "dynamic-programming"],
        "test_cases": [
            {"input": ["babad"], "expectedOutput": "bab"},
            {"input": ["cbbd"], "expectedOutput": "bb"},
            {"input": ["a"], "expectedOutput": "a"}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        pass",
        "java_sig": "class Solution {\n    public String longestPalindrome(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    string longestPalindrome(string s) {\n        \n    }\n};"
    },
    {
        "title": "Product of Array Except Self",
        "leetcode_url": "https://leetcode.com/problems/product-of-array-except-self/",
        "difficulty": "medium",
        "description": """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.""",
        "constraints": ["2 <= nums.length <= 10^5", "-30 <= nums[i] <= 30", "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer"],
        "examples": [
            {"input": {"nums": [1,2,3,4]}, "output": [24,12,8,6], "explanation": "answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, etc."}
        ],
        "tags": ["array", "prefix-sum"],
        "test_cases": [
            {"input": [[1,2,3,4]], "expectedOutput": [24,12,8,6]},
            {"input": [[-1,1,0,-3,3]], "expectedOutput": [0,0,9,0,0]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> productExceptSelf(vector<int>& nums) {\n        \n    }\n};"
    },
    {
        "title": "Spiral Matrix",
        "leetcode_url": "https://leetcode.com/problems/spiral-matrix/",
        "difficulty": "medium",
        "description": """Given an m x n matrix, return all elements of the matrix in spiral order.""",
        "constraints": ["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 10", "-100 <= matrix[i][j] <= 100"],
        "examples": [
            {"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "output": [1,2,3,6,9,8,7,4,5], "explanation": "Traverse the matrix in spiral order."}
        ],
        "tags": ["array", "matrix", "simulation"],
        "test_cases": [
            {"input": [[[1,2,3],[4,5,6],[7,8,9]]], "expectedOutput": [1,2,3,6,9,8,7,4,5]},
            {"input": [[[1,2,3,4],[5,6,7,8],[9,10,11,12]]], "expectedOutput": [1,2,3,4,8,12,11,10,9,5,6,7]}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        \n    }\n};"
    },
    {
        "title": "Rotate Image",
        "leetcode_url": "https://leetcode.com/problems/rotate-image/",
        "difficulty": "medium",
        "description": """You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.""",
        "constraints": ["n == matrix.length == matrix[i].length", "1 <= n <= 20", "-1000 <= matrix[i][j] <= 1000"],
        "examples": [
            {"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "output": [[7,4,1],[8,5,2],[9,6,3]], "explanation": "Rotate 90 degrees clockwise."}
        ],
        "tags": ["array", "matrix"],
        "test_cases": [
            {"input": [[[1,2,3],[4,5,6],[7,8,9]]], "expectedOutput": [[7,4,1],[8,5,2],[9,6,3]]},
            {"input": [[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]], "expectedOutput": [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n        pass",
        "java_sig": "class Solution {\n    public void rotate(int[][] matrix) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) {\n        \n    }\n};"
    },
    {
        "title": "Set Matrix Zeroes",
        "leetcode_url": "https://leetcode.com/problems/set-matrix-zeroes/",
        "difficulty": "medium",
        "description": """Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.""",
        "constraints": ["m == matrix.length", "n == matrix[0].length", "1 <= m, n <= 200", "-2^31 <= matrix[i][j] <= 2^31 - 1"],
        "examples": [
            {"input": {"matrix": [[1,1,1],[1,0,1],[1,1,1]]}, "output": [[1,0,1],[0,0,0],[1,0,1]], "explanation": "Mark row and column of 0s."}
        ],
        "tags": ["array", "matrix", "hash-table"],
        "test_cases": [
            {"input": [[[1,1,1],[1,0,1],[1,1,1]]], "expectedOutput": [[1,0,1],[0,0,0],[1,0,1]]},
            {"input": [[[0,1,2,0],[3,4,5,2],[1,3,1,5]]], "expectedOutput": [[0,0,0,0],[0,4,5,0],[0,3,1,0]]}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def setZeroes(self, matrix: List[List[int]]) -> None:\n        pass",
        "java_sig": "class Solution {\n    public void setZeroes(int[][] matrix) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    void setZeroes(vector<vector<int>>& matrix) {\n        \n    }\n};"
    },
    {
        "title": "Subarray Sum Equals K",
        "leetcode_url": "https://leetcode.com/problems/subarray-sum-equals-k/",
        "difficulty": "medium",
        "description": """Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.""",
        "constraints": ["1 <= nums.length <= 2 * 10^4", "-1000 <= nums[i] <= 1000", "-10^7 <= k <= 10^7"],
        "examples": [
            {"input": {"nums": [1,1,1], "k": 2}, "output": 2, "explanation": "Subarrays [1,1] and [1,1] sum to 2."},
            {"input": {"nums": [1,2,3], "k": 3}, "output": 2, "explanation": "Subarrays [1,2] and [3] sum to 3."}
        ],
        "tags": ["array", "hash-table", "prefix-sum"],
        "test_cases": [
            {"input": [[1,1,1], 2], "expectedOutput": 2},
            {"input": [[1,2,3], 3], "expectedOutput": 2}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int subarraySum(int[] nums, int k) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        \n    }\n};"
    },
    {
        "title": "Maximum Subarray",
        "leetcode_url": "https://leetcode.com/problems/maximum-subarray/",
        "difficulty": "medium",
        "description": """Given an integer array nums, find the subarray with the largest sum, and return its sum.""",
        "constraints": ["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4"],
        "examples": [
            {"input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]}, "output": 6, "explanation": "The subarray [4,-1,2,1] has the largest sum 6."},
            {"input": {"nums": [1]}, "output": 1, "explanation": "The subarray [1] has the largest sum 1."}
        ],
        "tags": ["array", "divide-and-conquer", "dynamic-programming"],
        "test_cases": [
            {"input": [[-2,1,-3,4,-1,2,1,-5,4]], "expectedOutput": 6},
            {"input": [[1]], "expectedOutput": 1},
            {"input": [[5,4,-1,7,8]], "expectedOutput": 23}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int maxSubArray(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        \n    }\n};"
    },
    {
        "title": "Remove Nth Node From End of List",
        "leetcode_url": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
        "difficulty": "medium",
        "description": """Given the head of a linked list, remove the nth node from the end of the list and return its head.""",
        "constraints": ["The number of nodes in the list is sz", "1 <= sz <= 30", "0 <= Node.val <= 100", "1 <= n <= sz"],
        "examples": [
            {"input": {"head": [1,2,3,4,5], "n": 2}, "output": [1,2,3,5], "explanation": "Remove 2nd node from end."}
        ],
        "tags": ["linked-list", "two-pointers"],
        "test_cases": [
            {"input": [[1,2,3,4,5], 2], "expectedOutput": [1,2,3,5]},
            {"input": [[1], 1], "expectedOutput": []},
            {"input": [[1,2], 1], "expectedOutput": [1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode removeNthFromEnd(ListNode head, int n) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* removeNthFromEnd(ListNode* head, int n) {\n        \n    }\n};"
    },
    {
        "title": "Reverse Linked List II",
        "leetcode_url": "https://leetcode.com/problems/reverse-linked-list-ii/",
        "difficulty": "medium",
        "description": """Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.""",
        "constraints": ["The number of nodes in the list is n", "1 <= n <= 500", "-500 <= Node.val <= 500", "1 <= left <= right <= n"],
        "examples": [
            {"input": {"head": [1,2,3,4,5], "left": 2, "right": 4}, "output": [1,4,3,2,5], "explanation": "Reverse nodes from position 2 to 4."}
        ],
        "tags": ["linked-list"],
        "test_cases": [
            {"input": [[1,2,3,4,5], 2, 4], "expectedOutput": [1,4,3,2,5]},
            {"input": [[5], 1, 1], "expectedOutput": [5]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode reverseBetween(ListNode head, int left, int right) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* reverseBetween(ListNode* head, int left, int right) {\n        \n    }\n};"
    },
    {
        "title": "Swap Nodes in Pairs",
        "leetcode_url": "https://leetcode.com/problems/swap-nodes-in-pairs/",
        "difficulty": "medium",
        "description": """Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.""",
        "constraints": ["The number of nodes in the list is in the range [0, 100]", "0 <= Node.val <= 100"],
        "examples": [
            {"input": {"head": [1,2,3,4]}, "output": [2,1,4,3], "explanation": "Swap adjacent pairs."}
        ],
        "tags": ["linked-list", "recursion"],
        "test_cases": [
            {"input": [[1,2,3,4]], "expectedOutput": [2,1,4,3]},
            {"input": [[]], "expectedOutput": []},
            {"input": [[1]], "expectedOutput": [1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode swapPairs(ListNode head) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* swapPairs(ListNode* head) {\n        \n    }\n};"
    },
    {
        "title": "Binary Tree Level Order Traversal",
        "leetcode_url": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
        "difficulty": "medium",
        "description": """Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).""",
        "constraints": ["The number of nodes in the tree is in the range [0, 2000]", "-1000 <= Node.val <= 1000"],
        "examples": [
            {"input": {"root": [3,9,20,None,None,15,7]}, "output": [[3],[9,20],[15,7]], "explanation": "Level by level traversal."}
        ],
        "tags": ["tree", "breadth-first-search"],
        "test_cases": [
            {"input": [[3,9,20,None,None,15,7]], "expectedOutput": [[3],[9,20],[15,7]]},
            {"input": [[1]], "expectedOutput": [[1]]},
            {"input": [[]], "expectedOutput": []}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        pass",
        "java_sig": "class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        \n    }\n};"
    },
    {
        "title": "Validate Binary Search Tree",
        "leetcode_url": "https://leetcode.com/problems/validate-binary-search-tree/",
        "difficulty": "medium",
        "description": """Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.""",
        "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"],
        "examples": [
            {"input": {"root": [2,1,3]}, "output": True, "explanation": "Valid BST."},
            {"input": {"root": [5,1,4,None,None,3,6]}, "output": False, "explanation": "Node 4 in right subtree of 5 violates BST property."}
        ],
        "tags": ["tree", "depth-first-search", "binary-search-tree"],
        "test_cases": [
            {"input": [[2,1,3]], "expectedOutput": True},
            {"input": [[5,1,4,None,None,3,6]], "expectedOutput": False}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean isValidBST(TreeNode root) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        \n    }\n};"
    },
    {
        "title": "Kth Smallest Element in a BST",
        "leetcode_url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
        "difficulty": "medium",
        "description": """Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.""",
        "constraints": ["The number of nodes in the tree is n", "1 <= k <= n <= 10^4", "0 <= Node.val <= 10^4"],
        "examples": [
            {"input": {"root": [3,1,4,None,2], "k": 1}, "output": 1, "explanation": "The smallest element is 1."},
            {"input": {"root": [5,3,6,2,4,None,None,1], "k": 3}, "output": 3, "explanation": "The 3rd smallest is 3."}
        ],
        "tags": ["tree", "depth-first-search", "binary-search-tree"],
        "test_cases": [
            {"input": [[3,1,4,None,2], 1], "expectedOutput": 1},
            {"input": [[5,3,6,2,4,None,None,1], 3], "expectedOutput": 3}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        \n    }\n};"
    },
    {
        "title": "Binary Tree Right Side View",
        "leetcode_url": "https://leetcode.com/problems/binary-tree-right-side-view/",
        "difficulty": "medium",
        "description": """Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.""",
        "constraints": ["The number of nodes in the tree is in the range [0, 100]", "-100 <= Node.val <= 100"],
        "examples": [
            {"input": {"root": [1,2,3,None,5,None,4]}, "output": [1,3,4], "explanation": "Right side view shows nodes 1, 3, 4."}
        ],
        "tags": ["tree", "depth-first-search", "breadth-first-search"],
        "test_cases": [
            {"input": [[1,2,3,None,5,None,4]], "expectedOutput": [1,3,4]},
            {"input": [[1,None,3]], "expectedOutput": [1,3]},
            {"input": [[]], "expectedOutput": []}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public List<Integer> rightSideView(TreeNode root) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> rightSideView(TreeNode* root) {\n        \n    }\n};"
    },
    {
        "title": "Path Sum II",
        "leetcode_url": "https://leetcode.com/problems/path-sum-ii/",
        "difficulty": "medium",
        "description": """Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.""",
        "constraints": ["The number of nodes in the tree is in the range [0, 5000]", "-1000 <= Node.val <= 1000", "-1000 <= targetSum <= 1000"],
        "examples": [
            {"input": {"root": [5,4,8,11,None,13,4,7,2,None,None,5,1], "targetSum": 22}, "output": [[5,4,11,2],[5,8,4,5]], "explanation": "Two paths sum to 22."}
        ],
        "tags": ["tree", "backtracking", "depth-first-search"],
        "test_cases": [
            {"input": [[5,4,8,11,None,13,4,7,2,None,None,5,1], 22], "expectedOutput": [[5,4,11,2],[5,8,4,5]]},
            {"input": [[1,2,3], 5], "expectedOutput": []},
            {"input": [[1,2], 0], "expectedOutput": []}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:\n        pass",
        "java_sig": "class Solution {\n    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {\n        \n    }\n};"
    },
    {
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "leetcode_url": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
        "difficulty": "medium",
        "description": """Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.""",
        "constraints": ["1 <= preorder.length <= 3000", "inorder.length == preorder.length", "-3000 <= preorder[i], inorder[i] <= 3000", "preorder and inorder consist of unique values"],
        "examples": [
            {"input": {"preorder": [3,9,20,15,7], "inorder": [9,3,15,20,7]}, "output": [3,9,20,None,None,15,7], "explanation": "Construct tree from traversals."}
        ],
        "tags": ["tree", "array", "hash-table", "divide-and-conquer"],
        "test_cases": [
            {"input": [[3,9,20,15,7], [9,3,15,20,7]], "expectedOutput": [3,9,20,None,None,15,7]},
            {"input": [[-1], [-1]], "expectedOutput": [-1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:\n        pass",
        "java_sig": "class Solution {\n    public TreeNode buildTree(int[] preorder, int[] inorder) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {\n        \n    }\n};"
    },
    {
        "title": "Lowest Common Ancestor of a Binary Tree",
        "leetcode_url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
        "difficulty": "medium",
        "description": """Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).""",
        "constraints": ["The number of nodes in the tree is in the range [2, 10^5]", "-10^9 <= Node.val <= 10^9", "All Node.val are unique", "p != q", "p and q exist in the tree"],
        "examples": [
            {"input": {"root": [3,5,1,6,2,0,8,None,None,7,4], "p": 5, "q": 1}, "output": 3, "explanation": "The LCA of nodes 5 and 1 is 3."}
        ],
        "tags": ["tree", "depth-first-search", "binary-tree"],
        "test_cases": [
            {"input": [[3,5,1,6,2,0,8,None,None,7,4], 5, 1], "expectedOutput": 3},
            {"input": [[3,5,1,6,2,0,8,None,None,7,4], 5, 4], "expectedOutput": 5}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:\n        pass",
        "java_sig": "class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n        \n    }\n};"
    },
    {
        "title": "Number of Islands",
        "leetcode_url": "https://leetcode.com/problems/number-of-islands/",
        "difficulty": "medium",
        "description": """Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.""",
        "constraints": ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 300", "grid[i][j] is '0' or '1'"],
        "examples": [
            {"input": {"grid": [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]}, "output": 1, "explanation": "One connected island."}
        ],
        "tags": ["array", "depth-first-search", "breadth-first-search", "union-find", "matrix"],
        "test_cases": [
            {"input": [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]], "expectedOutput": 1},
            {"input": [[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]], "expectedOutput": 3}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(m*n)",
        "python_sig": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int numIslands(char[][] grid) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int numIslands(vector<vector<char>>& grid) {\n        \n    }\n};"
    },
    {
        "title": "Course Schedule",
        "leetcode_url": "https://leetcode.com/problems/course-schedule/",
        "difficulty": "medium",
        "description": """There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.""",
        "constraints": ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000", "prerequisites[i].length == 2", "0 <= ai, bi < numCourses", "All the pairs prerequisites[i] are unique"],
        "examples": [
            {"input": {"numCourses": 2, "prerequisites": [[1,0]]}, "output": True, "explanation": "Take course 0 first, then course 1."},
            {"input": {"numCourses": 2, "prerequisites": [[1,0],[0,1]]}, "output": False, "explanation": "Circular dependency."}
        ],
        "tags": ["graph", "topological-sort", "depth-first-search", "breadth-first-search"],
        "test_cases": [
            {"input": [2, [[1,0]]], "expectedOutput": True},
            {"input": [2, [[1,0],[0,1]]], "expectedOutput": False}
        ],
        "time_complexity": "O(V+E)",
        "space_complexity": "O(V+E)",
        "python_sig": "class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        \n    }\n};"
    },
    {
        "title": "Clone Graph",
        "leetcode_url": "https://leetcode.com/problems/clone-graph/",
        "difficulty": "medium",
        "description": """Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.""",
        "constraints": ["The number of nodes in the graph is in the range [0, 100]", "1 <= Node.val <= 100", "Node.val is unique for each node", "There are no repeated edges and no self-loops"],
        "examples": [
            {"input": {"adjList": [[2,4],[1,3],[2,4],[1,3]]}, "output": [[2,4],[1,3],[2,4],[1,3]], "explanation": "Clone the graph."}
        ],
        "tags": ["hash-table", "depth-first-search", "breadth-first-search", "graph"],
        "test_cases": [
            {"input": [[[2,4],[1,3],[2,4],[1,3]]], "expectedOutput": [[2,4],[1,3],[2,4],[1,3]]},
            {"input": [[[]]], "expectedOutput": [[]]},
            {"input": [[]], "expectedOutput": []}
        ],
        "time_complexity": "O(N+M)",
        "space_complexity": "O(N)",
        "python_sig": "class Solution:\n    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:\n        pass",
        "java_sig": "class Solution {\n    public Node cloneGraph(Node node) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    Node* cloneGraph(Node* node) {\n        \n    }\n};"
    },
    {
        "title": "Word Search",
        "leetcode_url": "https://leetcode.com/problems/word-search/",
        "difficulty": "medium",
        "description": """Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.""",
        "constraints": ["m == board.length", "n = board[i].length", "1 <= m, n <= 6", "1 <= word.length <= 15", "board and word consists of only lowercase and uppercase English letters"],
        "examples": [
            {"input": {"board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "word": "ABCCED"}, "output": True, "explanation": "Word found in board."}
        ],
        "tags": ["array", "backtracking", "matrix"],
        "test_cases": [
            {"input": [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"], "expectedOutput": True},
            {"input": [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"], "expectedOutput": True},
            {"input": [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"], "expectedOutput": False}
        ],
        "time_complexity": "O(m*n*4^L)",
        "space_complexity": "O(L)",
        "python_sig": "class Solution:\n    def exist(self, board: List[List[str]], word: str) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean exist(char[][] board, String word) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool exist(vector<vector<char>>& board, string word) {\n        \n    }\n};"
    },
    {
        "title": "Coin Change",
        "leetcode_url": "https://leetcode.com/problems/coin-change/",
        "difficulty": "medium",
        "description": """You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.""",
        "constraints": ["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"],
        "examples": [
            {"input": {"coins": [1,2,5], "amount": 11}, "output": 3, "explanation": "11 = 5 + 5 + 1"},
            {"input": {"coins": [2], "amount": 3}, "output": -1, "explanation": "Cannot make amount 3."}
        ],
        "tags": ["array", "dynamic-programming", "breadth-first-search"],
        "test_cases": [
            {"input": [[1,2,5], 11], "expectedOutput": 3},
            {"input": [[2], 3], "expectedOutput": -1},
            {"input": [[1], 0], "expectedOutput": 0}
        ],
        "time_complexity": "O(amount * n)",
        "space_complexity": "O(amount)",
        "python_sig": "class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int coinChange(int[] coins, int amount) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        \n    }\n};"
    },
    {
        "title": "Longest Increasing Subsequence",
        "leetcode_url": "https://leetcode.com/problems/longest-increasing-subsequence/",
        "difficulty": "medium",
        "description": """Given an integer array nums, return the length of the longest strictly increasing subsequence.""",
        "constraints": ["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"],
        "examples": [
            {"input": {"nums": [10,9,2,5,3,7,101,18]}, "output": 4, "explanation": "The longest increasing subsequence is [2,3,7,101]."},
            {"input": {"nums": [0,1,0,3,2,3]}, "output": 4, "explanation": "The longest increasing subsequence is [0,1,2,3]."}
        ],
        "tags": ["array", "binary-search", "dynamic-programming"],
        "test_cases": [
            {"input": [[10,9,2,5,3,7,101,18]], "expectedOutput": 4},
            {"input": [[0,1,0,3,2,3]], "expectedOutput": 4},
            {"input": [[7,7,7,7,7,7,7]], "expectedOutput": 1}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int lengthOfLIS(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        \n    }\n};"
    },
    {
        "title": "Unique Paths",
        "leetcode_url": "https://leetcode.com/problems/unique-paths/",
        "difficulty": "medium",
        "description": """There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.""",
        "constraints": ["1 <= m, n <= 100"],
        "examples": [
            {"input": {"m": 3, "n": 7}, "output": 28, "explanation": "There are 28 unique paths."},
            {"input": {"m": 3, "n": 2}, "output": 3, "explanation": "From top-left: right->down->down, down->down->right, down->right->down"}
        ],
        "tags": ["math", "dynamic-programming", "combinatorics"],
        "test_cases": [
            {"input": [3, 7], "expectedOutput": 28},
            {"input": [3, 2], "expectedOutput": 3}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(m*n)",
        "python_sig": "class Solution:\n    def uniquePaths(self, m: int, n: int) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int uniquePaths(int m, int n) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        \n    }\n};"
    },
    {
        "title": "Word Break",
        "leetcode_url": "https://leetcode.com/problems/word-break/",
        "difficulty": "medium",
        "description": """Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.""",
        "constraints": ["1 <= s.length <= 300", "1 <= wordDict.length <= 1000", "1 <= wordDict[i].length <= 20", "s and wordDict[i] consist of only lowercase English letters", "All strings in wordDict are unique"],
        "examples": [
            {"input": {"s": "leetcode", "wordDict": ["leet","code"]}, "output": True, "explanation": "'leetcode' can be segmented as 'leet code'."},
            {"input": {"s": "applepenapple", "wordDict": ["apple","pen"]}, "output": True, "explanation": "'applepenapple' can be segmented as 'apple pen apple'."}
        ],
        "tags": ["hash-table", "string", "dynamic-programming", "trie", "memoization"],
        "test_cases": [
            {"input": ["leetcode", ["leet","code"]], "expectedOutput": True},
            {"input": ["applepenapple", ["apple","pen"]], "expectedOutput": True},
            {"input": ["catsandog", ["cats","dog","sand","and","cat"]], "expectedOutput": False}
        ],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean wordBreak(String s, List<String> wordDict) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool wordBreak(string s, vector<string>& wordDict) {\n        \n    }\n};"
    },
    {
        "title": "House Robber II",
        "leetcode_url": "https://leetcode.com/problems/house-robber-ii/",
        "difficulty": "medium",
        "description": """You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.""",
        "constraints": ["1 <= nums.length <= 100", "0 <= nums[i] <= 1000"],
        "examples": [
            {"input": {"nums": [2,3,2]}, "output": 3, "explanation": "You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent."},
            {"input": {"nums": [1,2,3,1]}, "output": 4, "explanation": "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4."}
        ],
        "tags": ["array", "dynamic-programming"],
        "test_cases": [
            {"input": [[2,3,2]], "expectedOutput": 3},
            {"input": [[1,2,3,1]], "expectedOutput": 4},
            {"input": [[1,2,3]], "expectedOutput": 3}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def rob(self, nums: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int rob(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int rob(vector<int>& nums) {\n        \n    }\n};"
    },
    {
        "title": "Decode Ways",
        "leetcode_url": "https://leetcode.com/problems/decode-ways/",
        "difficulty": "medium",
        "description": """A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above. Given a string s containing only digits, return the number of ways to decode it.""",
        "constraints": ["1 <= s.length <= 100", "s contains only digits and may contain leading zero(s)"],
        "examples": [
            {"input": {"s": "12"}, "output": 2, "explanation": "It could be decoded as 'AB' (1 2) or 'L' (12)."},
            {"input": {"s": "226"}, "output": 3, "explanation": "It could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6)."}
        ],
        "tags": ["string", "dynamic-programming"],
        "test_cases": [
            {"input": ["12"], "expectedOutput": 2},
            {"input": ["226"], "expectedOutput": 3},
            {"input": ["06"], "expectedOutput": 0}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def numDecodings(self, s: str) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int numDecodings(String s) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int numDecodings(string s) {\n        \n    }\n};"
    },
    {
        "title": "Letter Combinations of a Phone Number",
        "leetcode_url": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/",
        "difficulty": "medium",
        "description": """Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz""",
        "constraints": ["0 <= digits.length <= 4", "digits[i] is a digit in the range ['2', '9']"],
        "examples": [
            {"input": {"digits": "23"}, "output": ["ad","ae","af","bd","be","bf","cd","ce","cf"], "explanation": "All possible combinations."},
            {"input": {"digits": ""}, "output": [], "explanation": "Empty input."}
        ],
        "tags": ["hash-table", "string", "backtracking"],
        "test_cases": [
            {"input": ["23"], "expectedOutput": ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
            {"input": [""], "expectedOutput": []},
            {"input": ["2"], "expectedOutput": ["a","b","c"]}
        ],
        "time_complexity": "O(4^n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        pass",
        "java_sig": "class Solution {\n    public List<String> letterCombinations(String digits) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<string> letterCombinations(string digits) {\n        \n    }\n};"
    },
    {
        "title": "Generate Parentheses",
        "leetcode_url": "https://leetcode.com/problems/generate-parentheses/",
        "difficulty": "medium",
        "description": """Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.""",
        "constraints": ["1 <= n <= 8"],
        "examples": [
            {"input": {"n": 3}, "output": ["((()))","(()())","(())()","()(())","()()()"], "explanation": "All valid combinations of 3 pairs."},
            {"input": {"n": 1}, "output": ["()"], "explanation": "Only one combination."}
        ],
        "tags": ["string", "dynamic-programming", "backtracking"],
        "test_cases": [
            {"input": [3], "expectedOutput": ["((()))","(()())","(())()","()(())","()()()"]},
            {"input": [1], "expectedOutput": ["()"]}
        ],
        "time_complexity": "O(4^n/sqrt(n))",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def generateParenthesis(self, n: int) -> List[str]:\n        pass",
        "java_sig": "class Solution {\n    public List<String> generateParenthesis(int n) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<string> generateParenthesis(int n) {\n        \n    }\n};"
    },
    {
        "title": "Permutations",
        "leetcode_url": "https://leetcode.com/problems/permutations/",
        "difficulty": "medium",
        "description": """Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.""",
        "constraints": ["1 <= nums.length <= 6", "-10 <= nums[i] <= 10", "All the integers of nums are unique"],
        "examples": [
            {"input": {"nums": [1,2,3]}, "output": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "explanation": "All permutations."},
            {"input": {"nums": [0,1]}, "output": [[0,1],[1,0]], "explanation": "Two permutations."}
        ],
        "tags": ["array", "backtracking"],
        "test_cases": [
            {"input": [[1,2,3]], "expectedOutput": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]},
            {"input": [[0,1]], "expectedOutput": [[0,1],[1,0]]},
            {"input": [[1]], "expectedOutput": [[1]]}
        ],
        "time_complexity": "O(n!)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def permute(self, nums: List[int]) -> List[List[int]]:\n        pass",
        "java_sig": "class Solution {\n    public List<List<Integer>> permute(int[] nums) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<vector<int>> permute(vector<int>& nums) {\n        \n    }\n};"
    },
    
    # ============ HARD (7 questions) ============
    {
        "title": "Trapping Rain Water",
        "leetcode_url": "https://leetcode.com/problems/trapping-rain-water/",
        "difficulty": "hard",
        "description": """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.""",
        "constraints": ["n == height.length", "1 <= n <= 2 * 10^4", "0 <= height[i] <= 10^5"],
        "examples": [
            {"input": {"height": [0,1,0,2,1,0,1,3,2,1,2,1]}, "output": 6, "explanation": "The elevation map can trap 6 units of rain water."}
        ],
        "tags": ["array", "two-pointers", "dynamic-programming", "stack", "monotonic-stack"],
        "test_cases": [
            {"input": [[0,1,0,2,1,0,1,3,2,1,2,1]], "expectedOutput": 6},
            {"input": [[4,2,0,3,2,5]], "expectedOutput": 9}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def trap(self, height: List[int]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int trap(int[] height) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int trap(vector<int>& height) {\n        \n    }\n};"
    },
    {
        "title": "Median of Two Sorted Arrays",
        "leetcode_url": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "difficulty": "hard",
        "description": """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).""",
        "constraints": ["nums1.length == m", "nums2.length == n", "0 <= m <= 1000", "0 <= n <= 1000", "1 <= m + n <= 2000", "-10^6 <= nums1[i], nums2[i] <= 10^6"],
        "examples": [
            {"input": {"nums1": [1,3], "nums2": [2]}, "output": 2.0, "explanation": "Merged array = [1,2,3], median = 2."},
            {"input": {"nums1": [1,2], "nums2": [3,4]}, "output": 2.5, "explanation": "Merged array = [1,2,3,4], median = (2+3)/2 = 2.5."}
        ],
        "tags": ["array", "binary-search", "divide-and-conquer"],
        "test_cases": [
            {"input": [[1,3], [2]], "expectedOutput": 2.0},
            {"input": [[1,2], [3,4]], "expectedOutput": 2.5}
        ],
        "time_complexity": "O(log(min(m,n)))",
        "space_complexity": "O(1)",
        "python_sig": "class Solution:\n    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\n        pass",
        "java_sig": "class Solution {\n    public double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n        \n    }\n};"
    },
    {
        "title": "Binary Tree Maximum Path Sum",
        "leetcode_url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
        "difficulty": "hard",
        "description": """A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.""",
        "constraints": ["The number of nodes in the tree is in the range [1, 3 * 10^4]", "-1000 <= Node.val <= 1000"],
        "examples": [
            {"input": {"root": [1,2,3]}, "output": 6, "explanation": "The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6."},
            {"input": {"root": [-10,9,20,None,None,15,7]}, "output": 42, "explanation": "The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42."}
        ],
        "tags": ["tree", "depth-first-search", "dynamic-programming", "binary-tree"],
        "test_cases": [
            {"input": [[1,2,3]], "expectedOutput": 6},
            {"input": [[-10,9,20,None,None,15,7]], "expectedOutput": 42}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(h)",
        "python_sig": "class Solution:\n    def maxPathSum(self, root: Optional[TreeNode]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int maxPathSum(TreeNode root) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int maxPathSum(TreeNode* root) {\n        \n    }\n};"
    },
    {
        "title": "Serialize and Deserialize Binary Tree",
        "leetcode_url": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
        "difficulty": "hard",
        "description": """Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.""",
        "constraints": ["The number of nodes in the tree is in the range [0, 10^4]", "-1000 <= Node.val <= 1000"],
        "examples": [
            {"input": {"root": [1,2,3,None,None,4,5]}, "output": [1,2,3,None,None,4,5], "explanation": "Serialize then deserialize the tree."}
        ],
        "tags": ["string", "tree", "depth-first-search", "breadth-first-search", "design", "binary-tree"],
        "test_cases": [
            {"input": [[1,2,3,None,None,4,5]], "expectedOutput": [1,2,3,None,None,4,5]},
            {"input": [[]], "expectedOutput": []}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Codec:\n    def serialize(self, root: Optional[TreeNode]) -> str:\n        pass\n    \n    def deserialize(self, data: str) -> Optional[TreeNode]:\n        pass",
        "java_sig": "public class Codec {\n    public String serialize(TreeNode root) {\n        \n    }\n    \n    public TreeNode deserialize(String data) {\n        \n    }\n}",
        "cpp_sig": "class Codec {\npublic:\n    string serialize(TreeNode* root) {\n        \n    }\n    \n    TreeNode* deserialize(string data) {\n        \n    }\n};"
    },
    {
        "title": "Regular Expression Matching",
        "leetcode_url": "https://leetcode.com/problems/regular-expression-matching/",
        "difficulty": "hard",
        "description": """Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).""",
        "constraints": ["1 <= s.length <= 20", "1 <= p.length <= 20", "s contains only lowercase English letters", "p contains only lowercase English letters, '.', and '*'"],
        "examples": [
            {"input": {"s": "aa", "p": "a"}, "output": False, "explanation": "a does not match the entire string aa."},
            {"input": {"s": "aa", "p": "a*"}, "output": True, "explanation": "* means zero or more of the preceding element, a. Therefore, by repeating a once, it becomes aa."}
        ],
        "tags": ["string", "dynamic-programming", "recursion"],
        "test_cases": [
            {"input": ["aa", "a"], "expectedOutput": False},
            {"input": ["aa", "a*"], "expectedOutput": True},
            {"input": ["ab", ".*"], "expectedOutput": True}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(m*n)",
        "python_sig": "class Solution:\n    def isMatch(self, s: str, p: str) -> bool:\n        pass",
        "java_sig": "class Solution {\n    public boolean isMatch(String s, String p) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    bool isMatch(string s, string p) {\n        \n    }\n};"
    },
    {
        "title": "Edit Distance",
        "leetcode_url": "https://leetcode.com/problems/edit-distance/",
        "difficulty": "hard",
        "description": """Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character""",
        "constraints": ["0 <= word1.length, word2.length <= 500", "word1 and word2 consist of lowercase English letters"],
        "examples": [
            {"input": {"word1": "horse", "word2": "ros"}, "output": 3, "explanation": "horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e')"},
            {"input": {"word1": "intention", "word2": "execution"}, "output": 5, "explanation": "intention -> inention (remove 't') -> enention (replace 'i' with 'e') -> exention (replace 'n' with 'x') -> exection (replace 'n' with 'c') -> execution (insert 'u')"}
        ],
        "tags": ["string", "dynamic-programming"],
        "test_cases": [
            {"input": ["horse", "ros"], "expectedOutput": 3},
            {"input": ["intention", "execution"], "expectedOutput": 5}
        ],
        "time_complexity": "O(m*n)",
        "space_complexity": "O(m*n)",
        "python_sig": "class Solution:\n    def minDistance(self, word1: str, word2: str) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int minDistance(String word1, String word2) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int minDistance(string word1, string word2) {\n        \n    }\n};"
    },
    {
        "title": "Word Ladder",
        "leetcode_url": "https://leetcode.com/problems/word-ladder/",
        "difficulty": "hard",
        "description": """A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.""",
        "constraints": ["1 <= beginWord.length <= 10", "endWord.length == beginWord.length", "1 <= wordList.length <= 5000", "wordList[i].length == beginWord.length", "All strings consist of lowercase English letters", "beginWord != endWord", "All the words in wordList are unique"],
        "examples": [
            {"input": {"beginWord": "hit", "endWord": "cog", "wordList": ["hot","dot","dog","lot","log","cog"]}, "output": 5, "explanation": "One shortest transformation sequence is 'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog', which is 5 words long."},
            {"input": {"beginWord": "hit", "endWord": "cog", "wordList": ["hot","dot","dog","lot","log"]}, "output": 0, "explanation": "The endWord 'cog' is not in wordList, therefore there is no valid transformation sequence."}
        ],
        "tags": ["hash-table", "string", "breadth-first-search"],
        "test_cases": [
            {"input": ["hit", "cog", ["hot","dot","dog","lot","log","cog"]], "expectedOutput": 5},
            {"input": ["hit", "cog", ["hot","dot","dog","lot","log"]], "expectedOutput": 0}
        ],
        "time_complexity": "O(M^2 * N)",
        "space_complexity": "O(M^2 * N)",
        "python_sig": "class Solution:\n    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:\n        pass",
        "java_sig": "class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n        \n    }\n};"
    },
    {
        "title": "Merge k Sorted Lists",
        "leetcode_url": "https://leetcode.com/problems/merge-k-sorted-lists/",
        "difficulty": "hard",
        "description": """You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.""",
        "constraints": ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500", "-10^4 <= lists[i][j] <= 10^4", "lists[i] is sorted in ascending order", "The sum of lists[i].length will not exceed 10^4"],
        "examples": [
            {"input": {"lists": [[1,4,5],[1,3,4],[2,6]]}, "output": [1,1,2,3,4,4,5,6], "explanation": "Merging all lists: [1,4,5], [1,3,4], and [2,6] into one sorted list."},
            {"input": {"lists": []}, "output": [], "explanation": "Empty input."},
            {"input": {"lists": [[]]}, "output": [], "explanation": "Single empty list."}
        ],
        "tags": ["linked-list", "divide-and-conquer", "heap", "merge-sort"],
        "test_cases": [
            {"input": [[[1,4,5],[1,3,4],[2,6]]], "expectedOutput": [1,1,2,3,4,4,5,6]},
            {"input": [[]], "expectedOutput": []},
            {"input": [[[]]], "expectedOutput": []}
        ],
        "time_complexity": "O(N log k) where N is total number of nodes",
        "space_complexity": "O(k) for heap or O(log k) for divide-and-conquer",
        "python_sig": "class Solution:\n    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        pass",
        "java_sig": "class Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        \n    }\n};"
    }
]

# 10 ML System Design Questions
# Meta/Atlassian Senior ML Engineer - ML System Design Questions
# Replace the ML_QUESTIONS section in questions_data_full.py with this

ML_QUESTIONS = [
    {
        "title": "Design Facebook News Feed Ranking System",
        "difficulty": "hard",
        "description": "Design the ML ranking system for Facebook's News Feed that serves 3B+ users, deciding which posts to show and in what order to maximize meaningful user engagement.",
        "scenario": """Facebook's News Feed is the core product serving 3B+ users daily. The ML system must:
- Rank posts from friends, pages, groups, and ads
- Process millions of candidate posts per user
- Predict multiple engagement types (likes, comments, shares, time spent, hide/report)
- Optimize for "meaningful social interactions" not just clicks
- Handle diverse content types (text, photo, video, link, live)
- Serve feeds in <500ms while making complex ML predictions
- Combat engagement bait, clickbait, and misinformation
- Balance organic content with ads (revenue optimization)

The system processes billions of posts daily, makes trillions of predictions, and directly impacts Meta's $100B+ revenue.""",
        "requirements": [
            "Rank feeds for 3B+ users in real-time (<500ms latency)",
            "Multi-task prediction: likes, comments, shares, time spent, hide",
            "Multi-objective optimization (engagement + quality + revenue)",
            "Handle multiple content types with different engagement patterns",
            "Lightweight models for edge devices (mobile)",
            "Feature freshness (recent interactions matter)",
            "Virality modeling (predict shares/spread)",
            "Counter-abuse: clickbait, engagement bait, misinformation",
            "Personalization at scale with privacy constraints",
            "Seamless A/B testing infrastructure"
        ],
        "evaluation_criteria": {
            "architecture": "Two-stage: candidate generation + heavy ranking",
            "model_design": "Multi-task learning for different engagement types",
            "feature_engineering": "User features, post features, social graph, temporal",
            "training_pipeline": "Distributed training, online learning",
            "serving_infra": "Low-latency prediction serving at scale",
            "multi_objective": "Balancing engagement, quality, revenue, user satisfaction",
            "counter_abuse": "Strategies to detect and demote low-quality content",
            "evaluation": "Online metrics (time spent, DAU), offline metrics (AUC, calibration)"
        },
        "key_components": [
            "Candidate Generation (filter from millions to thousands)",
            "Heavy Ranker (GBDT or Deep Neural Network)",
            "Multi-task Head (predict likes, comments, shares, time, hide)",
            "Post-ranking Filters (diversity, freshness, ads insertion)",
            "Real-time Feature Store",
            "Online Learning Pipeline",
            "Counter-abuse Models (clickbait, misinformation)",
            "A/B Testing Platform",
            "Metrics Dashboard (time spent, meaningful interactions)"
        ],
        "tags": ["ranking", "multi-task-learning", "news-feed", "meta", "scale", "personalization"]
    },
    {
        "title": "Design Instagram Reels Recommendation System",
        "difficulty": "hard",
        "description": "Design the ML system powering Instagram Reels recommendations - a TikTok competitor serving short-form video to 2B+ users with multi-modal understanding.",
        "scenario": """Instagram Reels competes with TikTok by recommending engaging short-form videos. The system must:
- Understand video content (visual, audio, text, music)
- Cold start: recommend videos to new users and new videos to users
- Optimize for watch time and completion rate
- Handle the \"creator economy\" (help creators grow)
- Prevent filter bubbles while maximizing engagement
- Support audio trends (viral sounds)
- Real-time: new videos should surface quickly
- Multi-modal: video, audio, captions, hashtags, music

Key challenge: Unlike Feed (friends/following), Reels is discovery-based like TikTok.""",
        "requirements": [
            "Multi-modal understanding (video, audio, text, music)",
            "Real-time recommendations (<100ms)",
            "Cold start for new users and new content",
            "Optimize for watch time and completion rate",
            "Surface trending content quickly (viral detection)",
            "Creator growth (help small creators get discovered)",
            "Audio-based features (trending sounds)",
            "Prevent filter bubbles (content diversity)",
            "Handle billions of videos",
            "Mobile-first (lightweight models)"
        ],
        "evaluation_criteria": {
            "multi_modal": "How video, audio, text signals are combined",
            "cold_start": "Strategy for new users and new content",
            "viral_detection": "Identifying trending content early",
            "model_architecture": "Two-tower, transformers, or hybrid approach",
            "feature_engineering": "Video embeddings, audio features, engagement signals",
            "training": "Handling data skew (power law distribution)",
            "serving": "Low-latency multi-modal inference",
            "metrics": "Watch time, completion rate, user retention"
        },
        "key_components": [
            "Video Understanding (frame-level embeddings)",
            "Audio Understanding (music/sound embeddings)",
            "Text Understanding (captions, hashtags)",
            "Two-Tower Model (user tower + video tower)",
            "Candidate Retrieval (ANN search)",
            "Ranking Model (watch time prediction)",
            "Trending Detection System",
            "Creator Recommendation Engine",
            "Real-time Feature Pipeline",
            "A/B Testing for Reels"
        ],
        "tags": ["recommendation", "multi-modal", "video", "meta", "instagram", "reels", "cold-start"]
    },
    {
        "title": "Design Real-time Ad Targeting & Ranking System",
        "difficulty": "hard",
        "description": "Design Meta's ad targeting and ranking system that serves personalized ads to 3B+ users, generating $100B+ annual revenue while balancing user experience.",
        "scenario": """Meta's ad system is critical infrastructure generating $100B+ revenue. The ML system must:
- Target: Find right users for each ad campaign (audience selection)
- Rank: Order ads by expected value (bid × pCTR × pConversion)
- Auction: Run real-time ad auction for each impression
- Budget: Manage advertiser budgets and pacing
- Quality: Maintain user experience (not too many ads)
- Privacy: Work with limited data (iOS privacy, GDPR)
- Scale: Billions of users, millions of advertisers, trillions of impressions

Revenue equation: eCPM = bid × pCTR × pConversion
Goal: Maximize revenue while maintaining user satisfaction.""",
        "requirements": [
            "Real-time ad auction (<50ms per impression)",
            "Predict CTR (click-through rate)",
            "Predict conversion probability",
            "Budget pacing (spend advertiser budgets evenly)",
            "Audience targeting (find right users for ads)",
            "Frequency capping (don't show same ad too much)",
            "Ad quality scoring (prevent low-quality ads)",
            "Privacy-preserving (limited tracking)",
            "Handle billions of users, millions of advertisers",
            "Revenue optimization vs user experience"
        ],
        "evaluation_criteria": {
            "auction_mechanism": "Second-price auction, VCG, or generalized second price",
            "pCTR_model": "Model for click prediction",
            "pConversion_model": "Model for conversion prediction",
            "targeting": "How to match ads to users",
            "budget_pacing": "Algorithm to spend budgets over time",
            "calibration": "Are predicted probabilities accurate?",
            "privacy": "How to work with limited data",
            "revenue_metrics": "eCPM, revenue lift, advertiser ROI"
        },
        "key_components": [
            "Ad Retrieval (find candidate ads)",
            "CTR Prediction Model",
            "Conversion Prediction Model",
            "Ad Auction System",
            "Budget Pacing Algorithm",
            "Frequency Capping",
            "Ad Quality Classifier",
            "Targeting Engine (lookalike audiences)",
            "Attribution System (track conversions)",
            "Real-time Bidding Infrastructure"
        ],
        "tags": ["ads", "ranking", "auction", "revenue", "meta", "ctr-prediction", "conversion"]
    },
    {
        "title": "Design AI Content Moderation System for Meta",
        "difficulty": "hard",
        "description": "Design Meta's content moderation system that detects and removes harmful content (hate speech, violence, spam, misinformation) across Facebook, Instagram, WhatsApp at scale.",
        "scenario": """Meta's content moderation is critical for platform safety. The system must:
- Detect multiple violation types: hate speech, violence, nudity, spam, misinformation, bullying
- Multi-modal: text, images, videos, audio
- Real-time: flag content within seconds
- Multi-language: 100+ languages
- Precision is critical: false positives remove legitimate content
- Recall is critical: false negatives allow harmful content
- Human review: queue borderline content for human moderators
- Adversarial: bad actors constantly try to evade detection
- Scale: billions of posts/day

This is a high-stakes system with regulatory, legal, and ethical implications.""",
        "requirements": [
            "Multi-modal detection (text, image, video, audio)",
            "Real-time inference (<1s for text, <10s for video)",
            "Multi-class: hate speech, violence, nudity, spam, etc.",
            "Multi-language support (100+ languages)",
            "High precision (>95%) to avoid removing legitimate content",
            "High recall (>98%) for severe violations",
            "Human-in-the-loop for borderline cases",
            "Explainability for appeals",
            "Adversarial robustness",
            "Regional policy differences"
        ],
        "evaluation_criteria": {
            "model_architecture": "Multi-modal models (CLIP, ViT, transformers)",
            "data_pipeline": "How to get labeled data (human labeling, active learning)",
            "precision_recall": "Strategy to balance false positives vs false negatives",
            "adversarial": "Handling adversarial attacks (typos, obfuscation)",
            "human_loop": "Queue design, reviewer workflow",
            "explainability": "SHAP, attention, or rule-based explanations",
            "scaling": "Distributed inference for billions of items",
            "metrics": "Precision, recall, proactive rate, human review queue size"
        },
        "key_components": [
            "Text Classification (hate speech, spam)",
            "Image Classification (nudity, violence)",
            "Video Understanding (frame + audio analysis)",
            "Multi-modal Fusion",
            "Human Review Queue",
            "Active Learning Pipeline",
            "Adversarial Detection",
            "Explanation Generator",
            "Appeal System",
            "Policy Engine (region-specific rules)"
        ],
        "tags": ["content-moderation", "classification", "multi-modal", "safety", "meta", "nlp", "computer-vision"]
    },
    {
        "title": "Design Spam Detection System for Messaging",
        "difficulty": "medium",
        "description": "Design a real-time spam detection system for Meta Messenger/WhatsApp that identifies and blocks spam, scams, and phishing at scale while preserving user privacy.",
        "scenario": """Meta's messaging platforms (Messenger, WhatsApp, Instagram DMs) need spam detection:
- Billions of messages daily
- Real-time detection (<100ms)
- Privacy: End-to-end encrypted (WhatsApp)
- Multi-type: spam, scams, phishing, malware links
- Low false positive rate (legitimate messages blocked)
- Handle adversarial attackers (constantly evolving tactics)
- Multi-language support
- On-device ML (for encrypted messages)

Challenge: Balance spam detection with privacy (can't read WhatsApp messages).""",
        "requirements": [
            "Real-time detection (<100ms per message)",
            "Privacy-preserving (work with encrypted messages)",
            "Multi-type: spam, scams, phishing, malware",
            "Low false positive rate (<0.1%)",
            "High recall for dangerous scams (>95%)",
            "On-device models (for WhatsApp)",
            "Handle text, images, links, files",
            "Adversarial robustness",
            "Multi-language support",
            "Scale to billions of messages/day"
        ],
        "evaluation_criteria": {
            "privacy": "How to detect spam without reading content",
            "on_device": "Lightweight models for mobile devices",
            "features": "Metadata vs content features",
            "adversarial": "Handling typos, obfuscation, zero-day attacks",
            "false_positives": "Strategy to minimize blocking legitimate messages",
            "link_scanning": "Detecting malicious URLs",
            "user_reports": "Incorporating user feedback",
            "metrics": "Precision, recall, proactive detection rate"
        },
        "key_components": [
            "Message Classifier (spam vs ham)",
            "URL Scanner (malware/phishing detection)",
            "Image OCR + Classification",
            "Behavioral Signals (message patterns)",
            "On-device Model (for WhatsApp)",
            "Server-side Model (for Messenger)",
            "User Report System",
            "Challenge Flows (CAPTCHA for suspected spam)",
            "Adversarial Detection",
            "Feedback Loop"
        ],
        "tags": ["spam-detection", "classification", "privacy", "meta", "messaging", "adversarial"]
    },
    {
        "title": "Design A/B Testing Platform for ML Experiments",
        "difficulty": "medium",
        "description": "Design Meta/Atlassian's ML experimentation platform that enables safe, fast, statistically rigorous A/B testing of ML models in production.",
        "scenario": """Large tech companies run thousands of A/B tests. The platform must:
- Enable data scientists to run ML experiments easily
- Random assignment (users to treatment/control)
- Metric computation (online + offline metrics)
- Statistical testing (p-values, confidence intervals)
- Heterogeneous treatment effects (does it work for all users?)
- Interference handling (network effects, spillover)
- Multi-armed bandits (explore/exploit)
- Staged rollouts (1% → 10% → 100%)
- Automated monitoring (metric guardrails)

Meta runs 1000s of experiments concurrently. Atlassian tests product changes.""",
        "requirements": [
            "Support 1000s of concurrent experiments",
            "Random assignment with stratification",
            "Real-time metric computation",
            "Statistical testing (t-test, bootstrap)",
            "Heterogeneous treatment effects",
            "Network effect handling",
            "Multi-armed bandits",
            "Automated rollout (gradual)",
            "Metric guardrails (auto-disable bad experiments)",
            "Experiment analysis dashboard"
        ],
        "evaluation_criteria": {
            "randomization": "Proper random assignment, avoiding bias",
            "metrics": "How to compute online and offline metrics",
            "statistics": "Statistical rigor, multiple testing correction",
            "interference": "Handling network effects, spillover",
            "bandits": "Explore/exploit strategies",
            "infrastructure": "Scalable, low-latency",
            "usability": "Easy for data scientists to use",
            "safety": "Guardrails to prevent bad launches"
        },
        "key_components": [
            "Randomization Service",
            "Experiment Configuration System",
            "Metric Computation Pipeline",
            "Statistical Testing Engine",
            "Bandit Algorithm",
            "Staged Rollout Controller",
            "Metric Guardrails",
            "Experiment Dashboard",
            "Heterogeneous Treatment Effect Analysis",
            "Interference Detection"
        ],
        "tags": ["ab-testing", "experimentation", "infrastructure", "statistics", "meta", "atlassian"]
    },
    {
        "title": "Design Search Ranking for Atlassian Products",
        "difficulty": "medium",
        "description": "Design an ML-powered search system for Atlassian products (Jira, Confluence) that helps users find relevant issues, pages, and projects using natural language queries.",
        "scenario": """Atlassian's products (Jira, Confluence) have extensive search needs:
- Jira: Search issues, projects, filters, boards
- Confluence: Search pages, spaces, attachments, comments
- Cross-product search: Find related items across products
- Natural language: Understand user intent (\"bugs from last sprint about login\")
- Personalization: Rank based on user's role, projects, history
- Structured data (Jira fields) + unstructured data (Confluence pages)
- Enterprise scale: 100K+ issues, 50K+ pages per workspace
- Permission-aware (only show what user can access)

Key: Work with limited data (Atlassian is B2B, not consumer scale like Google).""",
        "requirements": [
            "Natural language query understanding",
            "Multi-source search (Jira, Confluence, comments, attachments)",
            "Semantic search (beyond keyword matching)",
            "Personalized ranking",
            "Permission-aware results",
            "Sub-second latency",
            "Handle structured + unstructured data",
            "Cross-product search",
            "Auto-complete and suggestions",
            "Work with limited data (B2B, not web-scale)"
        ],
        "evaluation_criteria": {
            "query_understanding": "NLP for intent extraction, entity recognition",
            "semantic_search": "Embeddings for semantic similarity",
            "ranking": "Learning-to-rank with personalization",
            "indexing": "Efficient indexing for mixed data types",
            "permissions": "Secure, fast permission filtering",
            "personalization": "User context, project access, search history",
            "limited_data": "How to work with limited training data",
            "metrics": "Search success rate, CTR, time to find"
        },
        "key_components": [
            "Query Parser (NLP, intent classification)",
            "Document Indexing (Elasticsearch)",
            "Semantic Embedding Models (sentence transformers)",
            "Hybrid Search (keyword + semantic)",
            "Ranking Model (LambdaMART or neural ranker)",
            "Permission Filter",
            "Personalization Layer",
            "Auto-complete Service",
            "Cross-product Aggregator",
            "Click-through Rate Tracker"
        ],
        "tags": ["search", "ranking", "nlp", "semantic-search", "atlassian", "enterprise", "jira", "confluence"]
    },
    {
        "title": "Design Real-time Fraud Detection System",
        "difficulty": "hard",
        "description": "Design a real-time fraud detection system for Meta's payment products (Meta Pay, WhatsApp Pay) that identifies fraudulent transactions with <100ms latency.",
        "scenario": """Meta's payment products need fraud detection:
- Real-time: Score transactions in <100ms
- Multi-type fraud: stolen cards, account takeover, fake accounts, money laundering
- Class imbalance: fraud rate <1%
- False positives are costly: block legitimate transactions
- False negatives are costly: allow fraud, chargebacks
- Adversarial: fraudsters constantly adapt
- Explainability: Why was this transaction blocked?
- Regulatory compliance: PCI-DSS, AML, KYC

The system processes millions of transactions daily, losing millions to fraud if ineffective.""",
        "requirements": [
            "Real-time scoring (<100ms per transaction)",
            "Multi-type fraud detection",
            "High recall for fraud (>90%)",
            "Low false positive rate (<2%)",
            "Handle severe class imbalance (<1% fraud)",
            "Adversarial robustness",
            "Explainability for compliance",
            "Online learning (adapt to new fraud patterns)",
            "Scale to millions of transactions/day",
            "Multi-stage: real-time → post-transaction analysis"
        ],
        "evaluation_criteria": {
            "model": "Gradient boosting, neural networks, or ensemble",
            "features": "Transaction, user, device, behavioral features",
            "imbalance": "Handling class imbalance (SMOTE, class weights)",
            "adversarial": "Detecting novel fraud patterns",
            "latency": "Sub-100ms inference",
            "explainability": "SHAP, rule-based explanations",
            "online_learning": "Continuous model updates",
            "metrics": "Precision, recall, F1, fraud loss, false positive rate"
        },
        "key_components": [
            "Real-time Transaction Scorer",
            "Feature Engineering Pipeline",
            "Fraud Detection Model (GBDT or NN)",
            "Rule Engine (known fraud patterns)",
            "Anomaly Detector (novel fraud)",
            "Device Fingerprinting",
            "Behavioral Analytics (velocity checks)",
            "Post-transaction Analysis",
            "Explainability Module",
            "Feedback Loop (confirmed fraud cases)"
        ],
        "tags": ["fraud-detection", "classification", "real-time", "payments", "meta", "imbalanced-data"]
    },
    {
        "title": "Design Video Understanding System for Meta",
        "difficulty": "hard",
        "description": "Design Meta's video understanding system that analyzes billions of videos to enable search, recommendations, content moderation, and monetization.",
        "scenario": """Meta processes billions of videos (Facebook, Instagram, Reels, Stories). The system must:
- Understand video content: objects, actions, scenes, audio, text
- Enable video search (\"find videos of surfing in Hawaii\")
- Power recommendations (similar videos)
- Content moderation (detect violations)
- Ad placement (find ad-safe content)
- Thumbnail selection (pick engaging frame)
- Auto-captions (accessibility)
- Copyright detection (match against known content)

Challenge: Video processing is expensive (compute, storage). Need efficient models.""",
        "requirements": [
            "Multi-modal understanding (visual, audio, text)",
            "Scale to billions of videos",
            "Real-time for short videos (<10s)",
            "Batch processing for long videos",
            "Frame-level analysis (scene detection)",
            "Audio understanding (speech, music, sounds)",
            "Text extraction (OCR on video)",
            "Efficient inference (cost-effective)",
            "Enable search, recommendations, moderation",
            "Copyright detection"
        ],
        "evaluation_criteria": {
            "model_architecture": "Video transformers, 3D CNNs, or frame sampling",
            "multi_modal": "How to fuse visual, audio, text signals",
            "efficiency": "Cost-effective processing at scale",
            "embeddings": "Quality of video embeddings for search/recommendations",
            "scene_detection": "Identifying scene boundaries",
            "audio_processing": "Speech recognition, music detection",
            "ocr": "Text extraction from video frames",
            "metrics": "Video search quality, recommendation CTR, moderation accuracy"
        },
        "key_components": [
            "Video Encoder (frame embeddings)",
            "Audio Encoder (audio embeddings)",
            "Text Encoder (captions, OCR)",
            "Multi-modal Fusion",
            "Scene Detection",
            "Object/Action Recognition",
            "Speech-to-Text",
            "Thumbnail Selector",
            "Copyright Matcher",
            "Video Search Index"
        ],
        "tags": ["video-understanding", "multi-modal", "computer-vision", "meta", "reels", "deep-learning"]
    },
    {
        "title": "Design Real-time Personalization Engine",
        "difficulty": "medium",
        "description": "Design a real-time personalization system that adapts Meta/Atlassian products to individual users based on their behavior, preferences, and context.",
        "scenario": """Modern products need personalization at scale:
- Meta: Personalize Feed, Reels, notifications, ads
- Atlassian: Personalize Jira dashboards, Confluence recommendations
- Real-time: Update preferences as user interacts
- Cold start: New users have no history
- Context: Time of day, device, location matter
- Privacy: Limited data collection
- Scale: Billions of users
- Latency: <50ms per request

Goal: Show the right content to the right user at the right time.""",
        "requirements": [
            "Real-time preference updates (<50ms)",
            "Handle billions of users",
            "Cold start for new users",
            "Context-aware (time, device, location)",
            "Privacy-preserving",
            "Multi-product personalization",
            "Efficient user representation (embeddings)",
            "Online learning (user preferences change)",
            "A/B testing integration",
            "Explainability (why this recommendation?)"
        ],
        "evaluation_criteria": {
            "user_modeling": "How to represent users (embeddings, features)",
            "real_time": "Low-latency updates and inference",
            "cold_start": "Strategy for new users",
            "context": "Incorporating temporal, device, location signals",
            "online_learning": "Continuous preference updates",
            "privacy": "Working with limited data",
            "scalability": "Handling billions of users efficiently",
            "metrics": "Engagement lift, user satisfaction, CTR"
        },
        "key_components": [
            "User Profile Store (preferences, embeddings)",
            "Real-time Event Stream (user actions)",
            "User Embedding Model",
            "Context Feature Service",
            "Personalization API",
            "Cold Start Solver",
            "Online Learning Pipeline",
            "A/B Testing Integration",
            "Privacy Controls",
            "Explainability Module"
        ],
        "tags": ["personalization", "user-modeling", "real-time", "meta", "atlassian", "recommendations"]
    }
]
