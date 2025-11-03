-- =============================================================================
-- COMPREHENSIVE QUESTION SET FOR META & ATLASSIAN SENIOR ML ENGINEER INTERVIEWS
-- 40 LeetCode Questions (Focus: Medium difficulty, Common Interview Problems)
-- 10 ML System Design Questions (Meta/Atlassian relevant)
-- =============================================================================

-- =============================================================================
-- LEETCODE QUESTIONS (40 Total)
-- =============================================================================

-- 1. Two Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Two Sum', 'easy', 
'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.',
'["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9"]',
'[{"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1], "explanation": "nums[0] + nums[1] == 9"}]',
'["array", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass',
'class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};',
'[{"input": [[2,7,11,15], 9], "expectedOutput": [0,1]}, {"input": [[3,2,4], 6], "expectedOutput": [1,2]}, {"input": [[3,3], 6], "expectedOutput": [0,1]}]',
'O(n)', 'O(n)');

-- 2. Valid Parentheses
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Valid Parentheses', 'easy',
'Given a string s containing just the characters ''('', '')'', ''{'', ''}'', ''['' and '']'', determine if the input string is valid.',
'["1 <= s.length <= 10^4"]',
'[{"input": {"s": "()"}, "output": true}, {"input": {"s": "()[]{}"}, "output": true}, {"input": {"s": "(]"}, "output": false}]',
'["string", "stack"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def isValid(self, s: str) -> bool:\n        pass',
'class Solution {\n    public boolean isValid(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool isValid(string s) {\n        \n    }\n};',
'[{"input": ["()"], "expectedOutput": true}, {"input": ["()[]{}"], "expectedOutput": true}, {"input": ["(]"], "expectedOutput": false}]',
'O(n)', 'O(n)');

-- 3. Merge Two Sorted Lists
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Merge Two Sorted Lists', 'easy',
'You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list.',
'["The number of nodes in both lists is in the range [0, 50]", "-100 <= Node.val <= 100"]',
'[{"input": {"list1": [1,2,4], "list2": [1,3,4]}, "output": [1,1,2,3,4,4]}]',
'["linked-list", "recursion"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        \n    }\n};',
'[{"input": [[1,2,4], [1,3,4]], "expectedOutput": [1,1,2,3,4,4]}, {"input": [[], []], "expectedOutput": []}]',
'O(n+m)', 'O(1)');

-- 4. Longest Substring Without Repeating Characters
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Longest Substring Without Repeating Characters', 'medium',
'Given a string s, find the length of the longest substring without repeating characters.',
'["0 <= s.length <= 5 * 10^4"]',
'[{"input": {"s": "abcabcbb"}, "output": 3, "explanation": "The answer is \"abc\""}, {"input": {"s": "bbbbb"}, "output": 1}]',
'["string", "sliding-window", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        pass',
'class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        \n    }\n}',
'class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        \n    }\n};',
'[{"input": ["abcabcbb"], "expectedOutput": 3}, {"input": ["bbbbb"], "expectedOutput": 1}, {"input": ["pwwkew"], "expectedOutput": 3}]',
'O(n)', 'O(min(m,n))');

-- 5. Add Two Numbers
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Add Two Numbers', 'medium',
'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order.',
'["The number of nodes is in the range [1, 100]", "0 <= Node.val <= 9"]',
'[{"input": {"l1": [2,4,3], "l2": [5,6,4]}, "output": [7,0,8], "explanation": "342 + 465 = 807"}]',
'["linked-list", "math"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        \n    }\n};',
'[{"input": [[2,4,3], [5,6,4]], "expectedOutput": [7,0,8]}, {"input": [[9,9,9], [9,9,9,9]], "expectedOutput": [8,9,9,0,1]}]',
'O(max(m,n))', 'O(max(m,n))');

-- 6. 3Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, '3Sum', 'medium',
'Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.',
'["3 <= nums.length <= 3000", "-10^5 <= nums[i] <= 10^5"]',
'[{"input": {"nums": [-1,0,1,2,-1,-4]}, "output": [[-1,-1,2],[-1,0,1]]}]',
'["array", "two-pointers", "sorting"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        pass',
'class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[-1,0,1,2,-1,-4]], "expectedOutput": [[-1,-1,2],[-1,0,1]]}, {"input": [[0,0,0]], "expectedOutput": [[0,0,0]]}]',
'O(n^2)', 'O(n)');

-- 7. Container With Most Water
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Container With Most Water', 'medium',
'You are given an integer array height of length n. Find two lines that together with the x-axis form a container that contains the most water.',
'["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"]',
'[{"input": {"height": [1,8,6,2,5,4,8,3,7]}, "output": 49}]',
'["array", "two-pointers", "greedy"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        pass',
'class Solution {\n    public int maxArea(int[] height) {\n        \n    }\n}',
'class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        \n    }\n};',
'[{"input": [[1,8,6,2,5,4,8,3,7]], "expectedOutput": 49}, {"input": [[1,1]], "expectedOutput": 1}]',
'O(n)', 'O(1)');

-- 8. Letter Combinations of a Phone Number
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Letter Combinations of a Phone Number', 'medium',
'Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.',
'["0 <= digits.length <= 4", "digits[i] is a digit in the range [''2'', ''9'']"]',
'[{"input": {"digits": "23"}, "output": ["ad","ae","af","bd","be","bf","cd","ce","cf"]}]',
'["backtracking", "string", "hash-table"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        pass',
'class Solution {\n    public List<String> letterCombinations(String digits) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<string> letterCombinations(string digits) {\n        \n    }\n};',
'[{"input": ["23"], "expectedOutput": ["ad","ae","af","bd","be","bf","cd","ce","cf"]}, {"input": [""], "expectedOutput": []}]',
'O(4^n)', 'O(n)');

-- 9. Remove Nth Node From End of List
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Remove Nth Node From End of List', 'medium',
'Given the head of a linked list, remove the nth node from the end of the list and return its head.',
'["The number of nodes in the list is sz", "1 <= sz <= 30", "0 <= Node.val <= 100", "1 <= n <= sz"]',
'[{"input": {"head": [1,2,3,4,5], "n": 2}, "output": [1,2,3,5]}]',
'["linked-list", "two-pointers"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode removeNthFromEnd(ListNode head, int n) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* removeNthFromEnd(ListNode* head, int n) {\n        \n    }\n};',
'[{"input": [[1,2,3,4,5], 2], "expectedOutput": [1,2,3,5]}, {"input": [[1], 1], "expectedOutput": []}]',
'O(n)', 'O(1)');

-- 10. Valid Sudoku
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Valid Sudoku', 'medium',
'Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the rules.',
'["board.length == 9", "board[i].length == 9"]',
'[{"input": {"board": [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."]]}, "output": true}]',
'["array", "hash-table", "matrix"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def isValidSudoku(self, board: List[List[str]]) -> bool:\n        pass',
'class Solution {\n    public boolean isValidSudoku(char[][] board) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool isValidSudoku(vector<vector<char>>& board) {\n        \n    }\n};',
'[{"input": [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."]]], "expectedOutput": true}]',
'O(1)', 'O(1)');

-- 11. Group Anagrams
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Group Anagrams', 'medium',
'Given an array of strings strs, group the anagrams together. You can return the answer in any order.',
'["1 <= strs.length <= 10^4", "0 <= strs[i].length <= 100"]',
'[{"input": {"strs": ["eat","tea","tan","ate","nat","bat"]}, "output": [["bat"],["nat","tan"],["ate","eat","tea"]]}]',
'["array", "hash-table", "string", "sorting"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        pass',
'class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        \n    }\n};',
'[{"input": [["eat","tea","tan","ate","nat","bat"]], "expectedOutput": [["bat"],["nat","tan"],["ate","eat","tea"]]}]',
'O(n*k*log(k))', 'O(n*k)');

-- 12. Maximum Subarray
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Maximum Subarray', 'medium',
'Given an integer array nums, find the subarray with the largest sum, and return its sum.',
'["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4"]',
'[{"input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]}, "output": 6, "explanation": "The subarray [4,-1,2,1] has the largest sum 6"}]',
'["array", "divide-and-conquer", "dynamic-programming"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        pass',
'class Solution {\n    public int maxSubArray(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[-2,1,-3,4,-1,2,1,-5,4]], "expectedOutput": 6}, {"input": [[1]], "expectedOutput": 1}]',
'O(n)', 'O(1)');

-- 13. Spiral Matrix
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Spiral Matrix', 'medium',
'Given an m x n matrix, return all elements of the matrix in spiral order.',
'["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 10"]',
'[{"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "output": [1,2,3,6,9,8,7,4,5]}]',
'["array", "matrix", "simulation"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:\n        pass',
'class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        \n    }\n};',
'[{"input": [[[1,2,3],[4,5,6],[7,8,9]]], "expectedOutput": [1,2,3,6,9,8,7,4,5]}]',
'O(m*n)', 'O(1)');

-- 14. Rotate Image
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Rotate Image', 'medium',
'You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).',
'["n == matrix.length == matrix[i].length", "1 <= n <= 20"]',
'[{"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "output": [[7,4,1],[8,5,2],[9,6,3]]}]',
'["array", "matrix"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n        pass',
'class Solution {\n    public void rotate(int[][] matrix) {\n        \n    }\n}',
'class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) {\n        \n    }\n};',
'[{"input": [[[1,2,3],[4,5,6],[7,8,9]]], "expectedOutput": [[7,4,1],[8,5,2],[9,6,3]]}]',
'O(n^2)', 'O(1)');

-- 15. Permutations
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Permutations', 'medium',
'Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.',
'["1 <= nums.length <= 6", "-10 <= nums[i] <= 10", "All integers of nums are unique"]',
'[{"input": {"nums": [1,2,3]}, "output": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]}]',
'["array", "backtracking"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def permute(self, nums: List[int]) -> List[List[int]]:\n        pass',
'class Solution {\n    public List<List<Integer>> permute(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<int>> permute(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[1,2,3]], "expectedOutput": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]}]',
'O(n!)', 'O(n)');

-- 16. Subarray Sum Equals K
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Subarray Sum Equals K', 'medium',
'Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.',
'["1 <= nums.length <= 2 * 10^4", "-1000 <= nums[i] <= 1000", "-10^7 <= k <= 10^7"]',
'[{"input": {"nums": [1,1,1], "k": 2}, "output": 2}, {"input": {"nums": [1,2,3], "k": 3}, "output": 2}]',
'["array", "hash-table", "prefix-sum"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        pass',
'class Solution {\n    public int subarraySum(int[] nums, int k) {\n        \n    }\n}',
'class Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        \n    }\n};',
'[{"input": [[1,1,1], 2], "expectedOutput": 2}, {"input": [[1,2,3], 3], "expectedOutput": 2}]',
'O(n)', 'O(n)');

-- 17. Merge Intervals
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Merge Intervals', 'medium',
'Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.',
'["1 <= intervals.length <= 10^4", "intervals[i].length == 2"]',
'[{"input": {"intervals": [[1,3],[2,6],[8,10],[15,18]]}, "output": [[1,6],[8,10],[15,18]]}]',
'["array", "sorting"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n        pass',
'class Solution {\n    public int[][] merge(int[][] intervals) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        \n    }\n};',
'[{"input": [[[1,3],[2,6],[8,10],[15,18]]], "expectedOutput": [[1,6],[8,10],[15,18]]}]',
'O(n*log(n))', 'O(n)');

-- 18. Unique Paths
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Unique Paths', 'medium',
'There is a robot on an m x n grid. The robot can only move either down or right. How many possible unique paths are there?',
'["1 <= m, n <= 100"]',
'[{"input": {"m": 3, "n": 7}, "output": 28}, {"input": {"m": 3, "n": 2}, "output": 3}]',
'["math", "dynamic-programming", "combinatorics"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def uniquePaths(self, m: int, n: int) -> int:\n        pass',
'class Solution {\n    public int uniquePaths(int m, int n) {\n        \n    }\n}',
'class Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        \n    }\n};',
'[{"input": [3, 7], "expectedOutput": 28}, {"input": [3, 2], "expectedOutput": 3}]',
'O(m*n)', 'O(m*n)');

-- 19. Climbing Stairs
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Climbing Stairs', 'easy',
'You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?',
'["1 <= n <= 45"]',
'[{"input": {"n": 2}, "output": 2}, {"input": {"n": 3}, "output": 3}]',
'["math", "dynamic-programming"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def climbStairs(self, n: int) -> int:\n        pass',
'class Solution {\n    public int climbStairs(int n) {\n        \n    }\n}',
'class Solution {\npublic:\n    int climbStairs(int n) {\n        \n    }\n};',
'[{"input": [2], "expectedOutput": 2}, {"input": [3], "expectedOutput": 3}, {"input": [5], "expectedOutput": 8}]',
'O(n)', 'O(1)');

-- 20. Minimum Path Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Minimum Path Sum', 'medium',
'Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.',
'["m == grid.length", "n == grid[i].length", "1 <= m, n <= 200"]',
'[{"input": {"grid": [[1,3,1],[1,5,1],[4,2,1]]}, "output": 7}]',
'["array", "dynamic-programming", "matrix"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def minPathSum(self, grid: List[List[int]]) -> int:\n        pass',
'class Solution {\n    public int minPathSum(int[][] grid) {\n        \n    }\n}',
'class Solution {\npublic:\n    int minPathSum(vector<vector<int>>& grid) {\n        \n    }\n};',
'[{"input": [[[1,3,1],[1,5,1],[4,2,1]]], "expectedOutput": 7}]',
'O(m*n)', 'O(1)');

-- 21. Set Matrix Zeroes
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Set Matrix Zeroes', 'medium',
'Given an m x n integer matrix, if an element is 0, set its entire row and column to 0''s. You must do it in place.',
'["m == matrix.length", "n == matrix[0].length", "1 <= m, n <= 200"]',
'[{"input": {"matrix": [[1,1,1],[1,0,1],[1,1,1]]}, "output": [[1,0,1],[0,0,0],[1,0,1]]}]',
'["array", "hash-table", "matrix"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def setZeroes(self, matrix: List[List[int]]) -> None:\n        pass',
'class Solution {\n    public void setZeroes(int[][] matrix) {\n        \n    }\n}',
'class Solution {\npublic:\n    void setZeroes(vector<vector<int>>& matrix) {\n        \n    }\n};',
'[{"input": [[[1,1,1],[1,0,1],[1,1,1]]], "expectedOutput": [[1,0,1],[0,0,0],[1,0,1]]}]',
'O(m*n)', 'O(1)');

-- 22. Search in Rotated Sorted Array
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Search in Rotated Sorted Array', 'medium',
'There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated. Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.',
'["1 <= nums.length <= 5000", "-10^4 <= nums[i] <= 10^4", "All values of nums are unique"]',
'[{"input": {"nums": [4,5,6,7,0,1,2], "target": 0}, "output": 4}]',
'["array", "binary-search"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        pass',
'class Solution {\n    public int search(int[] nums, int target) {\n        \n    }\n}',
'class Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        \n    }\n};',
'[{"input": [[4,5,6,7,0,1,2], 0], "expectedOutput": 4}, {"input": [[4,5,6,7,0,1,2], 3], "expectedOutput": -1}]',
'O(log n)', 'O(1)');

-- 23. Combination Sum
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Combination Sum', 'medium',
'Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.',
'["1 <= candidates.length <= 30", "2 <= candidates[i] <= 40", "1 <= target <= 40"]',
'[{"input": {"candidates": [2,3,6,7], "target": 7}, "output": [[2,2,3],[7]]}]',
'["array", "backtracking"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:\n        pass',
'class Solution {\n    public List<List<Integer>> combinationSum(int[] candidates, int target) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n        \n    }\n};',
'[{"input": [[2,3,6,7], 7], "expectedOutput": [[2,2,3],[7]]}]',
'O(n^target)', 'O(target)');

-- 24. Jump Game
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Jump Game', 'medium',
'You are given an integer array nums. You are initially positioned at the array''s first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.',
'["1 <= nums.length <= 10^4", "0 <= nums[i] <= 10^5"]',
'[{"input": {"nums": [2,3,1,1,4]}, "output": true}, {"input": {"nums": [3,2,1,0,4]}, "output": false}]',
'["array", "dynamic-programming", "greedy"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def canJump(self, nums: List[int]) -> bool:\n        pass',
'class Solution {\n    public boolean canJump(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool canJump(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[2,3,1,1,4]], "expectedOutput": true}, {"input": [[3,2,1,0,4]], "expectedOutput": false}]',
'O(n)', 'O(1)');

-- 25. Merge K Sorted Lists
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Merge K Sorted Lists', 'hard',
'You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.',
'["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500"]',
'[{"input": {"lists": [[1,4,5],[1,3,4],[2,6]]}, "output": [1,1,2,3,4,4,5,6]}]',
'["linked-list", "divide-and-conquer", "heap", "merge-sort"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        \n    }\n};',
'[{"input": [[[1,4,5],[1,3,4],[2,6]]], "expectedOutput": [1,1,2,3,4,4,5,6]}]',
'O(n*log(k))', 'O(k)');

-- 26. Binary Tree Level Order Traversal
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Binary Tree Level Order Traversal', 'medium',
'Given the root of a binary tree, return the level order traversal of its nodes'' values. (i.e., from left to right, level by level).',
'["The number of nodes in the tree is in the range [0, 2000]", "-1000 <= Node.val <= 1000"]',
'[{"input": {"root": [3,9,20,null,null,15,7]}, "output": [[3],[9,20],[15,7]]}]',
'["tree", "breadth-first-search"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        pass',
'class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        \n    }\n};',
'[{"input": [[3,9,20,null,null,15,7]], "expectedOutput": [[3],[9,20],[15,7]]}]',
'O(n)', 'O(n)');

-- 27. Validate Binary Search Tree
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Validate Binary Search Tree', 'medium',
'Given the root of a binary tree, determine if it is a valid binary search tree (BST).',
'["The number of nodes in the tree is in the range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"]',
'[{"input": {"root": [2,1,3]}, "output": true}, {"input": {"root": [5,1,4,null,null,3,6]}, "output": false}]',
'["tree", "depth-first-search", "binary-search-tree"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        pass',
'class Solution {\n    public boolean isValidBST(TreeNode root) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        \n    }\n};',
'[{"input": [[2,1,3]], "expectedOutput": true}, {"input": [[5,1,4,null,null,3,6]], "expectedOutput": false}]',
'O(n)', 'O(n)');

-- 28. Kth Smallest Element in a BST
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Kth Smallest Element in a BST', 'medium',
'Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.',
'["The number of nodes in the tree is n", "1 <= k <= n <= 10^4"]',
'[{"input": {"root": [3,1,4,null,2], "k": 1}, "output": 1}]',
'["tree", "depth-first-search", "binary-search-tree"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:\n        pass',
'class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        \n    }\n}',
'class Solution {\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        \n    }\n};',
'[{"input": [[3,1,4,null,2], 1], "expectedOutput": 1}, {"input": [[5,3,6,2,4,null,null,1], 3], "expectedOutput": 3}]',
'O(n)', 'O(n)');

-- 29. Lowest Common Ancestor of a Binary Tree
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Lowest Common Ancestor of a Binary Tree', 'medium',
'Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.',
'["The number of nodes in the tree is in the range [2, 10^5]", "All Node.val are unique"]',
'[{"input": {"root": [3,5,1,6,2,0,8,null,null,7,4], "p": 5, "q": 1}, "output": 3}]',
'["tree", "depth-first-search", "binary-tree"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:\n        pass',
'class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        \n    }\n}',
'class Solution {\npublic:\n    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n        \n    }\n};',
'[{"input": [[3,5,1,6,2,0,8,null,null,7,4], 5, 1], "expectedOutput": 3}]',
'O(n)', 'O(n)');

-- 30. Number of Islands
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Number of Islands', 'medium',
'Given an m x n 2D binary grid which represents a map of ''1''s (land) and ''0''s (water), return the number of islands.',
'["m == grid.length", "n == grid[i].length", "1 <= m, n <= 300"]',
'[{"input": {"grid": [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]}, "output": 1}]',
'["array", "depth-first-search", "breadth-first-search", "union-find", "matrix"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        pass',
'class Solution {\n    public int numIslands(char[][] grid) {\n        \n    }\n}',
'class Solution {\npublic:\n    int numIslands(vector<vector<char>>& grid) {\n        \n    }\n};',
'[{"input": [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]], "expectedOutput": 1}]',
'O(m*n)', 'O(m*n)');

-- 31. Clone Graph
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Clone Graph', 'medium',
'Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.',
'["The number of nodes in the graph is in the range [0, 100]", "1 <= Node.val <= 100"]',
'[{"input": {"adjList": [[2,4],[1,3],[2,4],[1,3]]}, "output": [[2,4],[1,3],[2,4],[1,3]]}]',
'["hash-table", "depth-first-search", "breadth-first-search", "graph"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:\n        pass',
'class Solution {\n    public Node cloneGraph(Node node) {\n        \n    }\n}',
'class Solution {\npublic:\n    Node* cloneGraph(Node* node) {\n        \n    }\n};',
'[{"input": [[[2,4],[1,3],[2,4],[1,3]]], "expectedOutput": [[2,4],[1,3],[2,4],[1,3]]}]',
'O(n)', 'O(n)');

-- 32. Course Schedule
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Course Schedule', 'medium',
'There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses.',
'["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000"]',
'[{"input": {"numCourses": 2, "prerequisites": [[1,0]]}, "output": true}]',
'["depth-first-search", "breadth-first-search", "graph", "topological-sort"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        pass',
'class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        \n    }\n};',
'[{"input": [2, [[1,0]]], "expectedOutput": true}, {"input": [2, [[1,0],[0,1]]], "expectedOutput": false}]',
'O(V+E)', 'O(V+E)');

-- 33. Word Break
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Word Break', 'medium',
'Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.',
'["1 <= s.length <= 300", "1 <= wordDict.length <= 1000", "1 <= wordDict[i].length <= 20"]',
'[{"input": {"s": "leetcode", "wordDict": ["leet","code"]}, "output": true}]',
'["hash-table", "string", "dynamic-programming", "trie"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n        pass',
'class Solution {\n    public boolean wordBreak(String s, List<String> wordDict) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool wordBreak(string s, vector<string>& wordDict) {\n        \n    }\n};',
'[{"input": ["leetcode", ["leet","code"]], "expectedOutput": true}, {"input": ["applepenapple", ["apple","pen"]], "expectedOutput": true}]',
'O(n^2)', 'O(n)');

-- 34. Longest Increasing Subsequence
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Longest Increasing Subsequence', 'medium',
'Given an integer array nums, return the length of the longest strictly increasing subsequence.',
'["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"]',
'[{"input": {"nums": [10,9,2,5,3,7,101,18]}, "output": 4, "explanation": "The longest increasing subsequence is [2,3,7,101]"}]',
'["array", "binary-search", "dynamic-programming"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        pass',
'class Solution {\n    public int lengthOfLIS(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[10,9,2,5,3,7,101,18]], "expectedOutput": 4}, {"input": [[0,1,0,3,2,3]], "expectedOutput": 4}]',
'O(n*log(n))', 'O(n)');

-- 35. Coin Change
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Coin Change', 'medium',
'You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount.',
'["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"]',
'[{"input": {"coins": [1,2,5], "amount": 11}, "output": 3, "explanation": "11 = 5 + 5 + 1"}]',
'["array", "dynamic-programming", "breadth-first-search"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        pass',
'class Solution {\n    public int coinChange(int[] coins, int amount) {\n        \n    }\n}',
'class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        \n    }\n};',
'[{"input": [[1,2,5], 11], "expectedOutput": 3}, {"input": [[2], 3], "expectedOutput": -1}]',
'O(amount * n)', 'O(amount)');

-- 36. Product of Array Except Self
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Product of Array Except Self', 'medium',
'Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].',
'["2 <= nums.length <= 10^5", "-30 <= nums[i] <= 30"]',
'[{"input": {"nums": [1,2,3,4]}, "output": [24,12,8,6]}]',
'["array", "prefix-sum"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        pass',
'class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        \n    }\n}',
'class Solution {\npublic:\n    vector<int> productExceptSelf(vector<int>& nums) {\n        \n    }\n};',
'[{"input": [[1,2,3,4]], "expectedOutput": [24,12,8,6]}, {"input": [[-1,1,0,-3,3]], "expectedOutput": [0,0,9,0,0]}]',
'O(n)', 'O(1)');

-- 37. Linked List Cycle
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Linked List Cycle', 'easy',
'Given head, the head of a linked list, determine if the linked list has a cycle in it.',
'["The number of nodes in the list is in the range [0, 10^4]"]',
'[{"input": {"head": [3,2,0,-4], "pos": 1}, "output": true}]',
'["hash-table", "linked-list", "two-pointers"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        pass',
'class Solution {\n    public boolean hasCycle(ListNode head) {\n        \n    }\n}',
'class Solution {\npublic:\n    bool hasCycle(ListNode *head) {\n        \n    }\n};',
'[{"input": [[3,2,0,-4], 1], "expectedOutput": true}, {"input": [[1,2], 0], "expectedOutput": true}, {"input": [[1], -1], "expectedOutput": false}]',
'O(n)', 'O(1)');

-- 38. Reverse Linked List
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Reverse Linked List', 'easy',
'Given the head of a singly linked list, reverse the list, and return the reversed list.',
'["The number of nodes in the list is the range [0, 5000]", "-5000 <= Node.val <= 5000"]',
'[{"input": {"head": [1,2,3,4,5]}, "output": [5,4,3,2,1]}]',
'["linked-list", "recursion"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Solution:\n    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
'class Solution {\n    public ListNode reverseList(ListNode head) {\n        \n    }\n}',
'class Solution {\npublic:\n    ListNode* reverseList(ListNode* head) {\n        \n    }\n};',
'[{"input": [[1,2,3,4,5]], "expectedOutput": [5,4,3,2,1]}, {"input": [[1,2]], "expectedOutput": [2,1]}]',
'O(n)', 'O(1)');

-- 39. LRU Cache
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'LRU Cache', 'medium',
'Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.',
'["1 <= capacity <= 3000", "0 <= key <= 10^4", "0 <= value <= 10^5"]',
'[{"input": {"operations": ["LRUCache","put","put","get","put","get","put","get","get","get"], "values": [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]}, "output": [null,null,null,1,null,-1,null,-1,3,4]}]',
'["hash-table", "linked-list", "design", "doubly-linked-list"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class LRUCache:\n    def __init__(self, capacity: int):\n        pass\n    def get(self, key: int) -> int:\n        pass\n    def put(self, key: int, value: int) -> None:\n        pass',
'class LRUCache {\n    public LRUCache(int capacity) {\n    }\n    public int get(int key) {\n        return 0;\n    }\n    public void put(int key, int value) {\n    }\n}',
'class LRUCache {\npublic:\n    LRUCache(int capacity) {\n    }\n    int get(int key) {\n        return 0;\n    }\n    void put(int key, int value) {\n    }\n};',
'[{"input": [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]], "expectedOutput": [null,null,null,1,null,-1,null,-1,3,4]}]',
'O(1)', 'O(capacity)');

-- 40. Implement Trie (Prefix Tree)
INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags) VALUES
(1, 'Implement Trie (Prefix Tree)', 'medium',
'A trie (prefix tree) is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Implement the Trie class.',
'["1 <= word.length, prefix.length <= 2000", "word and prefix consist only of lowercase English letters"]',
'[{"input": {"operations": ["Trie","insert","search","search","startsWith","insert","search"], "values": [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]}, "output": [null,null,true,false,true,null,true]}]',
'["hash-table", "string", "design", "trie"]');

INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, expected_time_complexity, expected_space_complexity) VALUES
(last_insert_rowid(),
'class Trie:\n    def __init__(self):\n        pass\n    def insert(self, word: str) -> None:\n        pass\n    def search(self, word: str) -> bool:\n        pass\n    def startsWith(self, prefix: str) -> bool:\n        pass',
'class Trie {\n    public Trie() {\n    }\n    public void insert(String word) {\n    }\n    public boolean search(String word) {\n        return false;\n    }\n    public boolean startsWith(String prefix) {\n        return false;\n    }\n}',
'class Trie {\npublic:\n    Trie() {\n    }\n    void insert(string word) {\n    }\n    bool search(string word) {\n        return false;\n    }\n    bool startsWith(string prefix) {\n        return false;\n    }\n};',
'[{"input": [[],["apple"],["apple"],["app"],["app"],["app"],["app"]], "expectedOutput": [null,null,true,false,true,null,true]}]',
'O(n)', 'O(n)');

-- =============================================================================
-- ML SYSTEM DESIGN QUESTIONS (10 Total - Optimized for Meta/Atlassian)
-- =============================================================================

-- 1. Design Facebook News Feed Ranking System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Facebook News Feed Ranking System', 'hard',
'Design a personalized news feed ranking system for Facebook/Meta with billions of users. The system must rank posts from friends, pages, and groups to maximize user engagement while considering recency, relevance, and content diversity.

Context:
- 3 billion+ monthly active users
- Millions of posts per second
- Must handle real-time updates and personalization
- Balance engagement, user satisfaction, and platform health
- Support multiple content types (text, images, videos, links)

Your Task:
Design an ML system that ranks posts in a user''s news feed. Consider data collection, feature engineering, model architecture, training pipeline, serving infrastructure, and evaluation metrics. Discuss trade-offs between accuracy, latency, and computational cost.',
'["recommendation", "ranking", "real-time-ml", "distributed-systems", "personalization"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Meta needs a scalable news feed ranking system that personalizes content for billions of users while maintaining sub-100ms latency and maximizing long-term user engagement.',
'["Handle 3B+ users with real-time personalization", "Latency < 100ms for ranking", "Process millions of posts per second", "Multi-objective optimization (engagement, diversity, quality)", "Handle cold start for new users/content", "A/B testing infrastructure", "Content moderation integration", "Support for multiple content types"]',
'{"problem_understanding": "Understood scale, latency, and multi-objective nature", "data_pipeline": "Comprehensive feature engineering including user, content, and context features", "model_architecture": "Two-tower or multi-stage ranking with appropriate models", "scalability": "Distributed training and serving architecture", "evaluation": "Offline metrics (AUC, NDCG) and online metrics (CTR, dwell time)", "cold_start": "Strategies for new users and content", "tradeoffs": "Discussion of accuracy vs latency, exploration vs exploitation"}',
'["Candidate Generation (Retrieval)", "Feature Engineering", "Ranking Models (L2R)", "Multi-objective Optimization", "Real-time Serving", "A/B Testing", "Monitoring & Feedback Loops", "Cold Start Handling"]');

-- 2. Design Instagram Recommendation System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Instagram Reels/Explore Recommendation System', 'hard',
'Design a recommendation system for Instagram Reels and Explore page that maximizes user engagement through personalized video and image recommendations.

Context:
- 2 billion+ monthly active users
- Short-form video content (Reels)
- Diverse content discovery (Explore)
- Need to balance viral content with personalization
- Must handle rapid content velocity

Your Task:
Design an ML system for recommending content. Consider content understanding (computer vision, NLP), user modeling, candidate generation, ranking, and real-time updates. Discuss how to handle trending content while maintaining personalization.',
'["recommendation", "computer-vision", "nlp", "real-time-ml", "content-understanding"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Instagram needs a recommendation system for Reels and Explore that discovers relevant content for users while promoting creator discovery and platform growth.',
'["Real-time content recommendations", "Multi-modal content understanding (vision + audio + text)", "Balance personalization with discovery", "Handle trending/viral content", "Support creator growth objectives", "Low latency inference (<50ms)", "Handle billions of daily recommendations"]',
'{"problem_understanding": "Understood multi-modal nature and discovery vs personalization", "content_understanding": "Computer vision and NLP for content features", "model_architecture": "Candidate generation and ranking approach", "real_time_updates": "Handling new content and trending signals", "evaluation": "Engagement metrics and user satisfaction", "creator_economy": "Balancing user experience with creator growth"}',
'["Content Understanding (Vision, Audio, Text)", "User Interest Modeling", "Candidate Generation", "Ranking System", "Trending Signal Integration", "Serving Infrastructure", "Evaluation Metrics", "Cold Start for New Content"]');

-- 3. Design Real-time Fraud Detection System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Real-time Payment Fraud Detection System', 'hard',
'Design a real-time fraud detection system for payment transactions that can detect fraudulent activity with high precision while minimizing false positives.

Context:
- Process millions of transactions per day
- Need real-time decision making (<50ms)
- Class imbalance (fraud is rare ~0.1%)
- Fraud patterns evolve rapidly
- High cost of false positives and false negatives
- Regulatory compliance requirements

Your Task:
Design an ML system for fraud detection. Consider feature engineering, model selection for imbalanced data, real-time inference, model updating, explainability for compliance, and handling concept drift.',
'["fraud-detection", "real-time-ml", "imbalanced-data", "anomaly-detection", "explainability"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design a payment fraud detection system that identifies fraudulent transactions in real-time while maintaining low false positive rates and providing explainable decisions for compliance.',
'["Real-time inference (<50ms)", "Handle extreme class imbalance", "Minimize false positives (customer friction)", "Adapt to evolving fraud patterns", "Provide explainability for decisions", "Process millions of transactions daily", "Regulatory compliance (audit trail)"]',
'{"problem_understanding": "Understood real-time constraints and class imbalance", "feature_engineering": "Transaction, user, and contextual features", "model_selection": "Appropriate models for imbalanced data", "real_time_serving": "Low-latency architecture", "handling_imbalance": "Sampling, weighting, or ensemble strategies", "concept_drift": "Model updating and monitoring", "explainability": "SHAP, LIME, or rule-based explanations"}',
'["Feature Engineering", "Handling Class Imbalance", "Model Selection", "Real-time Inference", "Concept Drift Detection", "Model Updating", "Explainability", "Monitoring & Alerting"]');

-- 4. Design Search Ranking System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design E-commerce Search Ranking System', 'hard',
'Design a search ranking system for an e-commerce platform (like Amazon) that returns relevant product results for user queries with personalization.

Context:
- Millions of products in catalog
- Natural language search queries
- Need to handle typos, synonyms, multi-lingual
- Personalization based on user history
- Business objectives (relevance, revenue, diversity)
- Latency requirement <200ms

Your Task:
Design an ML-powered search ranking system. Consider query understanding, candidate generation, ranking models, personalization, and evaluation. Discuss trade-offs between relevance and business metrics.',
'["search", "ranking", "nlp", "information-retrieval", "personalization"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design a search ranking system for e-commerce that balances relevance, personalization, and business objectives while maintaining low latency.',
'["Return results in <200ms", "Handle millions of products", "Query understanding (typos, synonyms)", "Personalization based on user history", "Multi-objective ranking (relevance + revenue)", "Support filters and facets", "Handle long-tail queries"]',
'{"problem_understanding": "Understood search vs recommendation differences", "query_processing": "Typo correction, synonym expansion, intent detection", "candidate_generation": "Efficient retrieval from large catalog", "ranking_model": "Learning to rank with personalization", "multi_objective": "Balancing relevance, revenue, diversity", "evaluation": "NDCG, MRR, conversion rate", "system_design": "Scalable architecture"}',
'["Query Understanding", "Candidate Generation (Retrieval)", "Feature Engineering", "Learning to Rank", "Personalization", "Multi-objective Optimization", "Serving Architecture", "Evaluation Metrics"]');

-- 5. Design Content Moderation System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design AI Content Moderation System', 'hard',
'Design an automated content moderation system for a social media platform to detect and remove harmful content (hate speech, violence, spam, misinformation).

Context:
- Billions of posts/comments daily
- Multiple content types (text, images, videos)
- Multiple violation categories
- Need high recall to catch violations
- Minimize false positives (over-moderation)
- Handle adversarial attacks
- Support human review queue

Your Task:
Design an ML system for content moderation. Consider multi-modal models, violation categories, confidence thresholds, human-in-the-loop, handling adversarial content, and evaluation metrics.',
'["content-moderation", "computer-vision", "nlp", "multi-modal", "classification"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design a content moderation system that automatically detects policy violations across multiple content types while minimizing false positives and supporting human review.',
'["Multi-modal content (text, image, video)", "Multiple violation categories", "High recall for harmful content", "Low false positive rate", "Real-time and batch processing", "Support human review workflow", "Handle adversarial attacks", "Explainability for moderation decisions"]',
'{"problem_understanding": "Understood multi-modal and multi-class nature", "model_architecture": "Appropriate models for text, images, videos", "precision_recall_tradeoff": "Balancing over and under moderation", "human_in_loop": "Review queue design and active learning", "adversarial_robustness": "Handling evasion techniques", "evaluation": "Precision, recall, F1 per category", "ethical_considerations": "Bias, fairness, transparency"}',
'["Multi-modal Models (Text, Vision, Audio)", "Multi-label Classification", "Confidence Calibration", "Human Review Queue", "Active Learning", "Adversarial Robustness", "Model Interpretability", "Evaluation & Fairness"]');

-- 6. Design Recommendation System for Video Platform
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design YouTube Video Recommendation System', 'hard',
'Design a video recommendation system for YouTube that maximizes watch time while considering user satisfaction and content diversity.

Context:
- Billions of users watching billions of hours
- Millions of videos uploaded daily
- Need to recommend next videos and homepage
- Balance watch time, user satisfaction, and creator ecosystem
- Handle diverse content (length, topic, quality)
- Cold start for new videos and users

Your Task:
Design an ML system for video recommendations. Consider candidate generation, ranking, multi-objective optimization, handling video features (thumbnails, titles, metadata), and balancing short-term engagement with long-term satisfaction.',
'["recommendation", "ranking", "video-understanding", "multi-objective", "user-modeling"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'YouTube needs a recommendation system that maximizes watch time and user satisfaction while supporting the creator ecosystem and maintaining content diversity.',
'["Personalized recommendations at scale", "Multi-objective optimization (watch time, satisfaction, diversity)", "Handle diverse video features", "Cold start for new videos/creators", "Real-time updates based on viewing", "Homepage and next video recommendations", "Support different user contexts"]',
'{"problem_understanding": "Understood scale and multi-objective nature", "candidate_generation": "Efficient retrieval from massive catalog", "ranking_model": "Multi-objective ranking approach", "video_features": "Thumbnail, title, metadata, engagement signals", "user_modeling": "Short-term and long-term interests", "evaluation": "Watch time, CTR, satisfaction surveys", "diversity": "Exploration vs exploitation"}',
'["Candidate Generation", "Video Understanding", "User Interest Modeling", "Multi-objective Ranking", "Cold Start Strategies", "Real-time Personalization", "Diversity & Exploration", "Evaluation Metrics"]');

-- 7. Design Ad Targeting and Ranking System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Ad Targeting and Ranking System', 'hard',
'Design an ad targeting and ranking system for a social media platform that maximizes advertiser ROI while maintaining user experience.

Context:
- Billions of users, millions of advertisers
- Real-time ad auction and ranking
- Need to predict ad engagement and conversion
- Balance advertiser goals with user experience
- Multiple ad formats and placements
- Privacy considerations (limited data)

Your Task:
Design an ML system for ad ranking and targeting. Consider CTR/CVR prediction, bid optimization, auction mechanism, serving latency, handling cold start ads, and evaluation metrics.',
'["ad-ranking", "ctr-prediction", "auction-mechanism", "personalization", "optimization"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design an ad system that ranks and targets ads to users to maximize advertiser ROI (clicks, conversions) while maintaining positive user experience.',
'["Real-time ad ranking (<100ms)", "CTR and CVR prediction", "Auction mechanism (second-price)", "Personalization at scale", "Multiple ad formats", "Cold start for new ads/advertisers", "Privacy-preserving features", "Revenue optimization"]',
'{"problem_understanding": "Understood auction mechanism and multi-stakeholder", "prediction_models": "CTR and CVR models", "auction_design": "Second-price auction integration", "personalization": "User targeting features", "cold_start": "New ad/advertiser handling", "evaluation": "AUC, calibration, revenue metrics", "privacy": "Privacy-preserving ML techniques"}',
'["CTR/CVR Prediction", "User Targeting", "Auction Mechanism", "Bid Optimization", "Ad Quality Scoring", "Serving Infrastructure", "Privacy-Preserving ML", "Evaluation & Metrics"]');

-- 8. Design Spam Detection System
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Email/Message Spam Detection System', 'medium',
'Design a spam detection system for email or messaging platform that identifies spam, phishing, and malicious content while minimizing false positives.

Context:
- Process millions of messages daily
- Multiple spam types (promotional, phishing, malware)
- Spammers constantly evolve techniques
- Need high precision (minimize false positives)
- Real-time and batch processing
- Multiple languages

Your Task:
Design an ML system for spam detection. Consider feature engineering, model selection, handling concept drift, adversarial robustness, real-time inference, and evaluation metrics.',
'["spam-detection", "nlp", "classification", "anomaly-detection", "adversarial-ml"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design a spam detection system that identifies spam, phishing, and malicious messages with high precision while adapting to evolving spam techniques.',
'["High precision (low false positives)", "Multiple spam categories", "Real-time inference for urgent cases", "Batch processing for scale", "Handle adversarial attacks", "Multi-language support", "Adaptive to evolving patterns"]',
'{"problem_understanding": "Understood precision importance and adversarial nature", "feature_engineering": "Text features, sender features, metadata", "model_selection": "Appropriate classification models", "adversarial_robustness": "Handling evasion techniques", "concept_drift": "Model updating strategies", "evaluation": "Precision, recall, F1 per category", "system_design": "Real-time and batch architecture"}',
'["Feature Engineering", "Text Classification Models", "Adversarial Robustness", "Concept Drift Handling", "Model Updating", "Real-time & Batch Processing", "Multi-language Support", "Evaluation Metrics"]');

-- 9. Design A/B Testing Platform for ML
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design A/B Testing Platform for ML Models', 'medium',
'Design an A/B testing and experimentation platform specifically for ML models that enables data scientists to safely test model changes in production.

Context:
- Multiple ML models in production
- Need to test model variants with statistical rigor
- Support for multi-armed bandit experiments
- Automatic traffic allocation
- Monitoring and alerting
- Handle interaction effects between experiments

Your Task:
Design an experimentation platform for ML models. Consider experiment design, traffic splitting, metric tracking, statistical analysis, guardrail metrics, and experiment interactions.',
'["experimentation", "ab-testing", "statistics", "ml-infrastructure", "monitoring"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design an experimentation platform that enables safe, statistically rigorous A/B testing of ML models in production at scale.',
'["Support multiple concurrent experiments", "Automated traffic allocation", "Statistical significance testing", "Guardrail metrics to prevent harm", "Handle experiment interactions", "Real-time metric tracking", "Multi-armed bandit support", "Experiment analysis tools"]',
'{"problem_understanding": "Understood experimentation challenges for ML", "experiment_design": "Randomization and stratification strategies", "statistical_methods": "Hypothesis testing, confidence intervals", "guardrails": "Automated quality checks", "interaction_handling": "Detecting experiment interference", "tooling": "Dashboard and analysis features", "scalability": "Supporting many experiments"}',
'["Experiment Design", "Traffic Splitting", "Metric Tracking", "Statistical Analysis", "Guardrail Metrics", "Multi-armed Bandits", "Experiment Interaction Detection", "Monitoring & Alerting"]');

-- 10. Design Real-time Personalization Engine
INSERT INTO questions (category_id, title, difficulty, description, tags) VALUES
(2, 'Design Real-time Personalization Engine', 'hard',
'Design a real-time personalization engine that adapts user experiences based on real-time behavior across a platform (homepage, search, recommendations).

Context:
- Need to personalize multiple surfaces
- Update user models in real-time
- Low latency requirements (<50ms)
- Scale to billions of users
- Privacy considerations
- Consistent experience across devices

Your Task:
Design a real-time personalization system. Consider user state management, feature computation, model serving, caching strategies, privacy, and cross-device consistency.',
'["personalization", "real-time-ml", "user-modeling", "distributed-systems", "privacy"]');

INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components) VALUES
(last_insert_rowid(),
'Design a real-time personalization engine that updates user models based on real-time behavior and serves personalized experiences with low latency.',
'["Real-time user state updates", "Low latency serving (<50ms)", "Personalize multiple surfaces", "Scale to billions of users", "Cross-device consistency", "Privacy-preserving features", "Handle cold start", "Graceful degradation"]',
'{"problem_understanding": "Understood real-time and scale requirements", "user_modeling": "Real-time feature computation", "serving_architecture": "Low-latency distributed system", "caching": "Multi-level caching strategy", "consistency": "Cross-device state management", "privacy": "Privacy-preserving techniques", "evaluation": "Latency, accuracy, engagement lift"}',
'["Real-time Feature Engineering", "User State Management", "Model Serving", "Caching Strategies", "Cross-device Consistency", "Privacy-Preserving ML", "Cold Start Handling", "Monitoring & Observability"]');

-- =============================================================================
-- VERIFICATION
-- =============================================================================

SELECT 'Database seeded successfully!' as status;
SELECT COUNT(*) as total_leetcode FROM questions WHERE category_id = 1;
SELECT COUNT(*) as total_ml_design FROM questions WHERE category_id = 2;
SELECT difficulty, COUNT(*) as count FROM questions WHERE category_id = 1 GROUP BY difficulty;
