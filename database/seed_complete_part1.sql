-- Complete Question Set: 50 LeetCode + 15 ML Design Questions

-- =============================================================================
-- LEETCODE QUESTIONS (50 total: 8 Easy, 35 Medium, 7 Hard)
-- =============================================================================

-- EASY QUESTIONS (8)

-- 1. Two Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Two Sum', 'easy', 
'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.',
'["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9", "Only one valid answer exists"]',
'[{"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1], "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."}]',
'["array", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(1, 
'class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass',
'class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};',
'[{"input": [[2,7,11,15], 9], "expectedOutput": [0,1]}, {"input": [[3,2,4], 6], "expectedOutput": [1,2]}, {"input": [[3,3], 6], "expectedOutput": [0,1]}]',
'O(n)', 'O(n)');

-- 2. Valid Parentheses
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Valid Parentheses', 'easy',
'Given a string s containing just the characters ''('', '')'', ''{'', ''}'', ''['' and '']'', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.',
'["1 <= s.length <= 10^4", "s consists of parentheses only ''()[]{}''"]',
'[{"input": {"s": "()"}, "output": true}, {"input": {"s": "()[]{}"}, "output": true}, {"input": {"s": "(]"}, "output": false}]',
'["string", "stack"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(2,
'class Solution:\n    def isValid(self, s: str) -> bool:\n        pass',
'class Solution {\n    public boolean isValid(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool isValid(string s) {\n        \n    }\n};',
'[{"input": ["()"], "expectedOutput": true}, {"input": ["()[]{}"], "expectedOutput": true}, {"input": ["(]"], "expectedOutput": false}, {"input": ["([)]"], "expectedOutput": false}]',
'O(n)', 'O(n)');

-- 3. Merge Two Sorted Lists
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Merge Two Sorted Lists', 'easy',
'You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.',
'["The number of nodes in both lists is in the range [0, 50]", "-100 <= Node.val <= 100", "Both list1 and list2 are sorted in non-decreasing order"]',
'[{"input": {"list1": [1,2,4], "list2": [1,3,4]}, "output": [1,1,2,3,4,4]}]',
'["linked-list", "recursion"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(3,
'class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        \n    }\n};',
'[{"input": [[1,2,4], [1,3,4]], "expectedOutput": [1,1,2,3,4,4]}, {"input": [[], []], "expectedOutput": []}, {"input": [[], [0]], "expectedOutput": [0]}]',
'O(n+m)', 'O(1)');

-- 4. Best Time to Buy and Sell Stock
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Best Time to Buy and Sell Stock', 'easy',
'You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.',
'["1 <= prices.length <= 10^5", "0 <= prices[i] <= 10^4"]',
'[{"input": {"prices": [7,1,5,3,6,4]}, "output": 5, "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5."}]',
'["array", "dynamic-programming"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(4,
'class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        pass',
'class Solution {\n    public int maxProfit(int[] prices) {\n        \n    }\n}',
'class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        \n    }\n};',
'[{"input": [[7,1,5,3,6,4]], "expectedOutput": 5}, {"input": [[7,6,4,3,1]], "expectedOutput": 0}]',
'O(n)', 'O(1)');

-- 5. Valid Palindrome
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Valid Palindrome', 'easy',
'A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.',
'["1 <= s.length <= 2 * 10^5", "s consists only of printable ASCII characters"]',
'[{"input": {"s": "A man, a plan, a canal: Panama"}, "output": true}, {"input": {"s": "race a car"}, "output": false}]',
'["two-pointers", "string"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(5,
'class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        pass',
'class Solution {\n    public boolean isPalindrome(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool isPalindrome(string s) {\n        \n    }\n};',
'[{"input": ["A man, a plan, a canal: Panama"], "expectedOutput": true}, {"input": ["race a car"], "expectedOutput": false}, {"input": [" "], "expectedOutput": true}]',
'O(n)', 'O(1)');

-- 6. Climbing Stairs
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Climbing Stairs', 'easy',
'You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?',
'["1 <= n <= 45"]',
'[{"input": {"n": 2}, "output": 2, "explanation": "There are two ways: 1. 1 step + 1 step, 2. 2 steps"}, {"input": {"n": 3}, "output": 3}]',
'["dynamic-programming", "math"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(6,
'class Solution:\n    def climbStairs(self, n: int) -> int:\n        pass',
'class Solution {\n    public int climbStairs(int n) {\n        \n    }\n}',
'class Solution {\npublic:\n    int climbStairs(int n) {\n        \n    }\n};',
'[{"input": [2], "expectedOutput": 2}, {"input": [3], "expectedOutput": 3}, {"input": [5], "expectedOutput": 8}]',
'O(n)', 'O(1)');

-- 7. Binary Tree Inorder Traversal
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Binary Tree Inorder Traversal', 'easy',
'Given the root of a binary tree, return the inorder traversal of its nodes'' values.',
'["The number of nodes in the tree is in the range [0, 100]", "-100 <= Node.val <= 100"]',
'[{"input": {"root": [1,null,2,3]}, "output": [1,3,2]}]',
'["tree", "depth-first-search", "stack"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(7,
'class Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        pass',
'class Solution {\n    public List<Integer> inorderTraversal(TreeNode root) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        \n    }\n};',
'[{"input": [[1,null,2,3]], "expectedOutput": [1,3,2]}, {"input": [[]], "expectedOutput": []}, {"input": [[1]], "expectedOutput": [1]}]',
'O(n)', 'O(n)');

-- 8. Linked List Cycle
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Linked List Cycle', 'easy',
'Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.',
'["The number of the nodes in the list is in the range [0, 10^4]", "-10^5 <= Node.val <= 10^5"]',
'[{"input": {"head": [3,2,0,-4], "pos": 1}, "output": true}, {"input": {"head": [1,2], "pos": 0}, "output": true}]',
'["linked-list", "two-pointers"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(8,
'class Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        pass',
'class Solution {\n    public boolean hasCycle(ListNode head) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool hasCycle(ListNode *head) {\n        \n    }\n};',
'[{"input": [[3,2,0,-4], 1], "expectedOutput": true}, {"input": [[1,2], 0], "expectedOutput": true}, {"input": [[1], -1], "expectedOutput": false}]',
'O(n)', 'O(1)');

-- MEDIUM QUESTIONS (35)

-- 9. Longest Substring Without Repeating Characters
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Longest Substring Without Repeating Characters', 'medium',
'Given a string s, find the length of the longest substring without repeating characters.',
'["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"]',
'[{"input": {"s": "abcabcbb"}, "output": 3, "explanation": "The answer is abc, with the length of 3."}, {"input": {"s": "bbbbb"}, "output": 1}]',
'["string", "sliding-window", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(9,
'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        pass',
'class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        \n    }\n};',
'[{"input": ["abcabcbb"], "expectedOutput": 3}, {"input": ["bbbbb"], "expectedOutput": 1}, {"input": ["pwwkew"], "expectedOutput": 3}]',
'O(n)', 'O(min(m,n))');

-- 10. Add Two Numbers
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Add Two Numbers', 'medium',
'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.',
'["The number of nodes in each linked list is in the range [1, 100]", "0 <= Node.val <= 9"]',
'[{"input": {"l1": [2,4,3], "l2": [5,6,4]}, "output": [7,0,8], "explanation": "342 + 465 = 807"}]',
'["linked-list", "math", "recursion"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(10,
'class Solution:\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        \n    }\n};',
'[{"input": [[2,4,3], [5,6,4]], "expectedOutput": [7,0,8]}, {"input": [[0], [0]], "expectedOutput": [0]}, {"input": [[9,9,9], [9,9,9,9]], "expectedOutput": [8,9,9,0,1]}]',
'O(max(m,n))', 'O(max(m,n))');

-- Continue with more medium questions...
-- (Due to length constraints, I'll create a more complete version in the next file)
