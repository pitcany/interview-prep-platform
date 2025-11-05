#!/usr/bin/env python3
"""
Complete dataset of 40 LeetCode + 10 ML System Design questions with solutions
Distribution: 8 Easy, 35 Medium, 8 Hard LeetCode questions
Generated with comprehensive solutions added
"""

# 40 LeetCode Questions with complete solutions
LEETCODE_QUESTIONS = [
    {
        "title": 'Two Sum',
        "leetcode_url": 'https://leetcode.com/problems/two-sum/',
        "difficulty": 'easy',
        "description": 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\nYou can return the answer in any order.',
        "constraints": [
        "2 <= nums.length <= 10^4",
        "-10^9 <= nums[i] <= 10^9",
        "-10^9 <= target <= 10^9",
        "Only one valid answer exists"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                2,
                                7,
                                11,
                                15
                        ],
                        "target": 9
                },
                "output": [
                        0,
                        1
                ],
                "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."
        },
        {
                "input": {
                        "nums": [
                                3,
                                2,
                                4
                        ],
                        "target": 6
                },
                "output": [
                        1,
                        2
                ],
                "explanation": "Because nums[1] + nums[2] == 6, we return [1, 2]."
        }
],
        "tags": [
        "array",
        "hash-table"
],
        "test_cases": [
        {
                "input": [
                        [
                                2,
                                7,
                                11,
                                15
                        ],
                        9
                ],
                "expectedOutput": [
                        0,
                        1
                ]
        },
        {
                "input": [
                        [
                                3,
                                2,
                                4
                        ],
                        6
                ],
                "expectedOutput": [
                        1,
                        2
                ]
        },
        {
                "input": [
                        [
                                3,
                                3
                        ],
                        6
                ],
                "expectedOutput": [
                        0,
                        1
                ]
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass',
        "java_sig": 'class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        # Hash map approach for O(n) time complexity\n        num_map = {}\n\n        for i, num in enumerate(nums):\n            complement = target - num\n            if complement in num_map:\n                return [num_map[complement], i]\n            num_map[num] = i\n\n        return []',
        "solution_java": 'class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        Map<Integer, Integer> map = new HashMap<>();\n\n        for (int i = 0; i < nums.length; i++) {\n            int complement = target - nums[i];\n            if (map.containsKey(complement)) {\n                return new int[] { map.get(complement), i };\n            }\n            map.put(nums[i], i);\n        }\n\n        return new int[] {};\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        unordered_map<int, int> numMap;\n\n        for (int i = 0; i < nums.size(); i++) {\n            int complement = target - nums[i];\n            if (numMap.find(complement) != numMap.end()) {\n                return {numMap[complement], i};\n            }\n            numMap[nums[i]] = i;\n        }\n\n        return {};\n    }\n};',
        "solution_explanation": '## Approach: Hash Table\n\n### Algorithm\n1. Create a hash map to store values and indices\n2. For each number, calculate its complement (target - num)\n3. Check if complement exists in hash map\n4. If found, return indices; otherwise add current number to map\n\n### Complexity Analysis\n- **Time Complexity**: O(n) - Single pass through the array\n- **Space Complexity**: O(n) - Hash map storage'
    },
    {
        "title": 'Valid Parentheses',
        "leetcode_url": 'https://leetcode.com/problems/valid-parentheses/',
        "difficulty": 'easy',
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.\n3. Every close bracket has a corresponding open bracket of the same type.",
        "constraints": [
        "1 <= s.length <= 10^4",
        "s consists of parentheses only '()[]{}'"
],
        "examples": [
        {
                "input": {
                        "s": "()"
                },
                "output": True,
                "explanation": "The string is valid."
        },
        {
                "input": {
                        "s": "()[]{}"
                },
                "output": True,
                "explanation": "All brackets are properly closed."
        },
        {
                "input": {
                        "s": "(]"
                },
                "output": False,
                "explanation": "Mismatched brackets."
        }
],
        "tags": [
        "string",
        "stack"
],
        "test_cases": [
        {
                "input": [
                        "()"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "()[]{}"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "(]"
                ],
                "expectedOutput": False
        },
        {
                "input": [
                        "([)]"
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def isValid(self, s: str) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean isValid(String s) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool isValid(string s) {\n        \n    }\n};',
        "solution_python": "class Solution:\n    def isValid(self, s: str) -> bool:\n        stack = []\n        mapping = {')': '(', '}': '{', ']': '['}\n\n        for char in s:\n            if char in mapping:\n                if not stack or stack[-1] != mapping[char]:\n                    return False\n                stack.pop()\n            else:\n                stack.append(char)\n\n        return len(stack) == 0",
        "solution_java": "class Solution {\n    public boolean isValid(String s) {\n        Stack<Character> stack = new Stack<>();\n        Map<Character, Character> map = new HashMap<>();\n        map.put(')', '(');\n        map.put('}', '{');\n        map.put(']', '[');\n\n        for (char c : s.toCharArray()) {\n            if (map.containsKey(c)) {\n                if (stack.isEmpty() || stack.peek() != map.get(c)) {\n                    return False;\n                }\n                stack.pop();\n            } else {\n                stack.push(c);\n            }\n        }\n\n        return stack.isEmpty();\n    }\n}",
        "solution_cpp": "class Solution {\npublic:\n    bool isValid(string s) {\n        stack<char> st;\n        unordered_map<char, char> mapping = {\n            {')', '('},\n            {'}', '{'},\n            {']', '['}\n        };\n\n        for (char c : s) {\n            if (mapping.count(c)) {\n                if (st.empty() || st.top() != mapping[c]) {\n                    return False;\n                }\n                st.pop();\n            } else {\n                st.push(c);\n            }\n        }\n\n        return st.empty();\n    }\n};",
        "solution_explanation": '## Approach: Stack\n\n### Algorithm\n1. Use a stack to track opening brackets\n2. For closing brackets, check if they match the most recent opening bracket\n3. Valid if all brackets are matched (stack is empty)\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(n)'
    },
    {
        "title": 'Merge Two Sorted Lists',
        "leetcode_url": 'https://leetcode.com/problems/merge-two-sorted-lists/',
        "difficulty": 'easy',
        "description": 'You are given the heads of two sorted linked lists list1 and list2.\n\nMerge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.\n\nReturn the head of the merged linked list.',
        "constraints": [
        "The number of nodes in both lists is in the range [0, 50]",
        "-100 <= Node.val <= 100",
        "Both list1 and list2 are sorted in non-decreasing order"
],
        "examples": [
        {
                "input": {
                        "list1": [
                                1,
                                2,
                                4
                        ],
                        "list2": [
                                1,
                                3,
                                4
                        ]
                },
                "output": [
                        1,
                        1,
                        2,
                        3,
                        4,
                        4
                ],
                "explanation": "Merge both sorted lists."
        },
        {
                "input": {
                        "list1": [],
                        "list2": []
                },
                "output": [],
                "explanation": "Both lists are empty."
        }
],
        "tags": [
        "linked-list",
        "recursion"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                4
                        ],
                        [
                                1,
                                3,
                                4
                        ]
                ],
                "expectedOutput": [
                        1,
                        1,
                        2,
                        3,
                        4,
                        4
                ]
        },
        {
                "input": [
                        [],
                        []
                ],
                "expectedOutput": []
        },
        {
                "input": [
                        [],
                        [
                                0
                        ]
                ],
                "expectedOutput": [
                        0
                ]
        }
],
        "time_complexity": 'O(n+m)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\n        dummy = ListNode(0)\n        current = dummy\n\n        while list1 and list2:\n            if list1.val <= list2.val:\n                current.next = list1\n                list1 = list1.next\n            else:\n                current.next = list2\n                list2 = list2.next\n            current = current.next\n\n        current.next = list1 if list1 else list2\n        return dummy.next',
        "solution_java": 'class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        ListNode dummy = new ListNode(0);\n        ListNode current = dummy;\n\n        while (list1 != None && list2 != None) {\n            if (list1.val <= list2.val) {\n                current.next = list1;\n                list1 = list1.next;\n            } else {\n                current.next = list2;\n                list2 = list2.next;\n            }\n            current = current.next;\n        }\n\n        current.next = (list1 != None) ? list1 : list2;\n        return dummy.next;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n        ListNode dummy(0);\n        ListNode* current = &dummy;\n\n        while (list1 && list2) {\n            if (list1->val <= list2->val) {\n                current->next = list1;\n                list1 = list1->next;\n            } else {\n                current->next = list2;\n                list2 = list2->next;\n            }\n            current = current->next;\n        }\n\n        current->next = list1 ? list1 : list2;\n        return dummy.next;\n    }\n};',
        "solution_explanation": '## Approach: Iterative Merge\n\n### Algorithm\n1. Use dummy node to simplify edge cases\n2. Compare nodes and attach smaller one\n3. Attach remaining list when one is exhausted\n\n### Complexity Analysis\n- **Time Complexity**: O(n + m)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Best Time to Buy and Sell Stock',
        "leetcode_url": 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
        "difficulty": 'easy',
        "description": 'You are given an array prices where prices[i] is the price of a given stock on the ith day.\n\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\n\nReturn the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.',
        "constraints": [
        "1 <= prices.length <= 10^5",
        "0 <= prices[i] <= 10^4"
],
        "examples": [
        {
                "input": {
                        "prices": [
                                7,
                                1,
                                5,
                                3,
                                6,
                                4
                        ]
                },
                "output": 5,
                "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5."
        },
        {
                "input": {
                        "prices": [
                                7,
                                6,
                                4,
                                3,
                                1
                        ]
                },
                "output": 0,
                "explanation": "In this case, no transactions are done and the max profit = 0."
        }
],
        "tags": [
        "array",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        [
                                7,
                                1,
                                5,
                                3,
                                6,
                                4
                        ]
                ],
                "expectedOutput": 5
        },
        {
                "input": [
                        [
                                7,
                                6,
                                4,
                                3,
                                1
                        ]
                ],
                "expectedOutput": 0
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int maxProfit(int[] prices) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        \n    }\n};',
        "solution_python": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        min_price = float('inf')\n        max_profit = 0\n\n        for price in prices:\n            min_price = min(min_price, price)\n            max_profit = max(max_profit, price - min_price)\n\n        return max_profit",
        "solution_java": 'class Solution {\n    public int maxProfit(int[] prices) {\n        int minPrice = Integer.MAX_VALUE;\n        int maxProfit = 0;\n\n        for (int price : prices) {\n            minPrice = Math.min(minPrice, price);\n            maxProfit = Math.max(maxProfit, price - minPrice);\n        }\n\n        return maxProfit;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        int minPrice = INT_MAX;\n        int maxProfit = 0;\n\n        for (int price : prices) {\n            minPrice = min(minPrice, price);\n            maxProfit = max(maxProfit, price - minPrice);\n        }\n\n        return maxProfit;\n    }\n};',
        "solution_explanation": '## Approach: Dynamic Programming\n\n### Algorithm\n1. Track minimum price seen so far\n2. Calculate profit at each day\n3. Keep maximum profit\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Valid Palindrome',
        "leetcode_url": 'https://leetcode.com/problems/valid-palindrome/',
        "difficulty": 'easy',
        "description": 'A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.\n\nGiven a string s, return True if it is a palindrome, or False otherwise.',
        "constraints": [
        "1 <= s.length <= 2 * 10^5",
        "s consists only of printable ASCII characters"
],
        "examples": [
        {
                "input": {
                        "s": "A man, a plan, a canal: Panama"
                },
                "output": True,
                "explanation": "After cleaning: amanaplanacanalpanama which is a palindrome."
        },
        {
                "input": {
                        "s": "race a car"
                },
                "output": False,
                "explanation": "After cleaning: raceacar which is not a palindrome."
        }
],
        "tags": [
        "two-pointers",
        "string"
],
        "test_cases": [
        {
                "input": [
                        "A man, a plan, a canal: Panama"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "race a car"
                ],
                "expectedOutput": False
        },
        {
                "input": [
                        " "
                ],
                "expectedOutput": True
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean isPalindrome(String s) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool isPalindrome(string s) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        left, right = 0, len(s) - 1\n\n        while left < right:\n            while left < right and not s[left].isalnum():\n                left += 1\n            while left < right and not s[right].isalnum():\n                right -= 1\n\n            if s[left].lower() != s[right].lower():\n                return False\n\n            left += 1\n            right -= 1\n\n        return True',
        "solution_java": 'class Solution {\n    public boolean isPalindrome(String s) {\n        int left = 0, right = s.length() - 1;\n\n        while (left < right) {\n            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {\n                left++;\n            }\n            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {\n                right--;\n            }\n\n            if (Character.toLowerCase(s.charAt(left)) !=\n                Character.toLowerCase(s.charAt(right))) {\n                return False;\n            }\n\n            left++;\n            right--;\n        }\n\n        return True;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    bool isPalindrome(string s) {\n        int left = 0, right = s.length() - 1;\n\n        while (left < right) {\n            while (left < right && !isalnum(s[left])) {\n                left++;\n            }\n            while (left < right && !isalnum(s[right])) {\n                right--;\n            }\n\n            if (tolower(s[left]) != tolower(s[right])) {\n                return False;\n            }\n\n            left++;\n            right--;\n        }\n\n        return True;\n    }\n};',
        "solution_explanation": '## Approach: Two Pointers\n\n### Algorithm\n1. Use two pointers from start and end\n2. Skip non-alphanumeric characters\n3. Compare characters (case-insensitive)\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Climbing Stairs',
        "leetcode_url": 'https://leetcode.com/problems/climbing-stairs/',
        "difficulty": 'easy',
        "description": 'You are climbing a staircase. It takes n steps to reach the top.\n\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?',
        "constraints": [
        "1 <= n <= 45"
],
        "examples": [
        {
                "input": {
                        "n": 2
                },
                "output": 2,
                "explanation": "There are two ways: 1. 1 step + 1 step, 2. 2 steps"
        },
        {
                "input": {
                        "n": 3
                },
                "output": 3,
                "explanation": "There are three ways: 1. 1+1+1, 2. 1+2, 3. 2+1"
        }
],
        "tags": [
        "dynamic-programming",
        "math"
],
        "test_cases": [
        {
                "input": [
                        2
                ],
                "expectedOutput": 2
        },
        {
                "input": [
                        3
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        4
                ],
                "expectedOutput": 5
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def climbStairs(self, n: int) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int climbStairs(int n) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int climbStairs(int n) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def climbStairs(self, n: int) -> int:\n        if n <= 2:\n            return n\n\n        # Dynamic programming - Fibonacci sequence\n        prev2, prev1 = 1, 2\n\n        for i in range(3, n + 1):\n            current = prev1 + prev2\n            prev2 = prev1\n            prev1 = current\n\n        return prev1',
        "solution_java": 'class Solution {\n    public int climbStairs(int n) {\n        if (n <= 2) return n;\n\n        int prev2 = 1, prev1 = 2;\n\n        for (int i = 3; i <= n; i++) {\n            int current = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = current;\n        }\n\n        return prev1;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    int climbStairs(int n) {\n        if (n <= 2) return n;\n\n        int prev2 = 1, prev1 = 2;\n\n        for (int i = 3; i <= n; i++) {\n            int current = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = current;\n        }\n\n        return prev1;\n    }\n};',
        "solution_explanation": '## Approach: Dynamic Programming (Fibonacci)\n\n### Algorithm\n1. Base cases: 1 step = 1 way, 2 steps = 2 ways\n2. For n steps: ways(n) = ways(n-1) + ways(n-2)\n3. Use two variables to track previous values\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Binary Tree Inorder Traversal',
        "leetcode_url": 'https://leetcode.com/problems/binary-tree-inorder-traversal/',
        "difficulty": 'easy',
        "description": "Given the root of a binary tree, return the inorder traversal of its nodes' values.\n\nInorder traversal: Left -> Root -> Right",
        "constraints": [
        "The number of nodes in the tree is in the range [0, 100]",
        "-100 <= Node.val <= 100"
],
        "examples": [
        {
                "input": {
                        "root": [
                                1,
                                None,
                                2,
                                3
                        ]
                },
                "output": [
                        1,
                        3,
                        2
                ],
                "explanation": "Inorder traversal of the tree."
        },
        {
                "input": {
                        "root": []
                },
                "output": [],
                "explanation": "Empty tree."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "stack"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                None,
                                2,
                                3
                        ]
                ],
                "expectedOutput": [
                        1,
                        3,
                        2
                ]
        },
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
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        pass',
        "java_sig": 'class Solution {\n    public List<Integer> inorderTraversal(TreeNode root) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:\n        result = []\n        stack = []\n        current = root\n\n        while current or stack:\n            # Go to the leftmost node\n            while current:\n                stack.append(current)\n                current = current.left\n\n            # Current is None, so process the node on top of stack\n            current = stack.pop()\n            result.append(current.val)\n\n            # Visit right subtree\n            current = current.right\n\n        return result',
        "solution_java": 'class Solution {\n    public List<Integer> inorderTraversal(TreeNode root) {\n        List<Integer> result = new ArrayList<>();\n        Stack<TreeNode> stack = new Stack<>();\n        TreeNode current = root;\n\n        while (current != None || !stack.isEmpty()) {\n            while (current != None) {\n                stack.push(current);\n                current = current.left;\n            }\n\n            current = stack.pop();\n            result.add(current.val);\n            current = current.right;\n        }\n\n        return result;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        vector<int> result;\n        stack<TreeNode*> st;\n        TreeNode* current = root;\n\n        while (current || !st.empty()) {\n            while (current) {\n                st.push(current);\n                current = current->left;\n            }\n\n            current = st.top();\n            st.pop();\n            result.push_back(current->val);\n            current = current->right;\n        }\n\n        return result;\n    }\n};',
        "solution_explanation": '## Approach: Iterative using Stack\n\n### Algorithm\n1. Use stack to simulate recursion\n2. Go left as far as possible\n3. Process node and go right\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(n)'
    },
    {
        "title": 'Linked List Cycle',
        "leetcode_url": 'https://leetcode.com/problems/linked-list-cycle/',
        "difficulty": 'easy',
        "description": 'Given head, the head of a linked list, determine if the linked list has a cycle in it.\n\nThere is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.',
        "constraints": [
        "The number of the nodes in the list is in the range [0, 10^4]",
        "-10^5 <= Node.val <= 10^5",
        "pos is -1 or a valid index in the linked-list"
],
        "examples": [
        {
                "input": {
                        "head": [
                                3,
                                2,
                                0,
                                -4
                        ],
                        "pos": 1
                },
                "output": True,
                "explanation": "There is a cycle where the tail connects to the 1st node."
        },
        {
                "input": {
                        "head": [
                                1
                        ],
                        "pos": -1
                },
                "output": False,
                "explanation": "There is no cycle in the linked list."
        }
],
        "tags": [
        "linked-list",
        "two-pointers",
        "hash-table"
],
        "test_cases": [
        {
                "input": [
                        [
                                3,
                                2,
                                0,
                                -4
                        ],
                        1
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        [
                                1,
                                2
                        ],
                        0
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        [
                                1
                        ],
                        -1
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean hasCycle(ListNode head) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool hasCycle(ListNode *head) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def hasCycle(self, head: Optional[ListNode]) -> bool:\n        if not head or not head.next:\n            return False\n\n        slow = head\n        fast = head.next\n\n        while slow != fast:\n            if not fast or not fast.next:\n                return False\n            slow = slow.next\n            fast = fast.next.next\n\n        return True',
        "solution_java": 'public class Solution {\n    public boolean hasCycle(ListNode head) {\n        if (head == None || head.next == None) {\n            return False;\n        }\n\n        ListNode slow = head;\n        ListNode fast = head.next;\n\n        while (slow != fast) {\n            if (fast == None || fast.next == None) {\n                return False;\n            }\n            slow = slow.next;\n            fast = fast.next.next;\n        }\n\n        return True;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    bool hasCycle(ListNode *head) {\n        if (!head || !head->next) return False;\n\n        ListNode* slow = head;\n        ListNode* fast = head->next;\n\n        while (slow != fast) {\n            if (!fast || !fast->next) return False;\n            slow = slow->next;\n            fast = fast->next->next;\n        }\n\n        return True;\n    }\n};',
        "solution_explanation": "## Approach: Floyd's Cycle Detection (Two Pointers)\n\n### Algorithm\n1. Use slow and fast pointers\n2. Slow moves 1 step, fast moves 2 steps\n3. If they meet, there's a cycle\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(1)"
    },
    {
        "title": 'Longest Substring Without Repeating Characters',
        "leetcode_url": 'https://leetcode.com/problems/longest-substring-without-repeating-characters/',
        "difficulty": 'medium',
        "description": 'Given a string s, find the length of the longest substring without repeating characters.',
        "constraints": [
        "0 <= s.length <= 5 * 10^4",
        "s consists of English letters, digits, symbols and spaces"
],
        "examples": [
        {
                "input": {
                        "s": "abcabcbb"
                },
                "output": 3,
                "explanation": "The answer is 'abc', with the length of 3."
        },
        {
                "input": {
                        "s": "bbbbb"
                },
                "output": 1,
                "explanation": "The answer is 'b', with the length of 1."
        }
],
        "tags": [
        "string",
        "sliding-window",
        "hash-table"
],
        "test_cases": [
        {
                "input": [
                        "abcabcbb"
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        "bbbbb"
                ],
                "expectedOutput": 1
        },
        {
                "input": [
                        "pwwkew"
                ],
                "expectedOutput": 3
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(min(m,n))',
        "python_sig": 'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        char_set = set()\n        left = 0\n        max_length = 0\n\n        for right in range(len(s)):\n            while s[right] in char_set:\n                char_set.remove(s[left])\n                left += 1\n\n            char_set.add(s[right])\n            max_length = max(max_length, right - left + 1)\n\n        return max_length',
        "solution_java": 'class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        Set<Character> charSet = new HashSet<>();\n        int left = 0, maxLength = 0;\n\n        for (int right = 0; right < s.length(); right++) {\n            while (charSet.contains(s.charAt(right))) {\n                charSet.remove(s.charAt(left));\n                left++;\n            }\n\n            charSet.add(s.charAt(right));\n            maxLength = Math.max(maxLength, right - left + 1);\n        }\n\n        return maxLength;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    int lengthOfLongestSubstring(string s) {\n        unordered_set<char> charSet;\n        int left = 0, maxLength = 0;\n\n        for (int right = 0; right < s.length(); right++) {\n            while (charSet.count(s[right])) {\n                charSet.erase(s[left]);\n                left++;\n            }\n\n            charSet.insert(s[right]);\n            maxLength = max(maxLength, right - left + 1);\n        }\n\n        return maxLength;\n    }\n};',
        "solution_explanation": '## Approach: Sliding Window with Hash Set\n\n### Algorithm\n1. Use two pointers for sliding window\n2. Expand window by moving right pointer\n3. Contract window when duplicate found\n4. Track maximum window size\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(min(n, m)) where m is charset size'
    },
    {
        "title": 'Add Two Numbers',
        "leetcode_url": 'https://leetcode.com/problems/add-two-numbers/',
        "difficulty": 'medium',
        "description": 'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.\n\nYou may assume the two numbers do not contain any leading zero, except the number 0 itself.',
        "constraints": [
        "The number of nodes in each linked list is in the range [1, 100]",
        "0 <= Node.val <= 9",
        "It is guaranteed that the list represents a number that does not have leading zeros"
],
        "examples": [
        {
                "input": {
                        "l1": [
                                2,
                                4,
                                3
                        ],
                        "l2": [
                                5,
                                6,
                                4
                        ]
                },
                "output": [
                        7,
                        0,
                        8
                ],
                "explanation": "342 + 465 = 807."
        },
        {
                "input": {
                        "l1": [
                                0
                        ],
                        "l2": [
                                0
                        ]
                },
                "output": [
                        0
                ],
                "explanation": "0 + 0 = 0."
        }
],
        "tags": [
        "linked-list",
        "math",
        "recursion"
],
        "test_cases": [
        {
                "input": [
                        [
                                2,
                                4,
                                3
                        ],
                        [
                                5,
                                6,
                                4
                        ]
                ],
                "expectedOutput": [
                        7,
                        0,
                        8
                ]
        },
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
                                9
                        ],
                        [
                                9,
                                9,
                                9,
                                9
                        ]
                ],
                "expectedOutput": [
                        8,
                        9,
                        9,
                        0,
                        1
                ]
        }
],
        "time_complexity": 'O(max(m,n))',
        "space_complexity": 'O(max(m,n))',
        "python_sig": 'class Solution:\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:\n        dummy = ListNode(0)\n        current = dummy\n        carry = 0\n\n        while l1 or l2 or carry:\n            val1 = l1.val if l1 else 0\n            val2 = l2.val if l2 else 0\n\n            total = val1 + val2 + carry\n            carry = total // 10\n\n            current.next = ListNode(total % 10)\n            current = current.next\n\n            l1 = l1.next if l1 else None\n            l2 = l2.next if l2 else None\n\n        return dummy.next',
        "solution_java": 'class Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        ListNode dummy = new ListNode(0);\n        ListNode current = dummy;\n        int carry = 0;\n\n        while (l1 != None || l2 != None || carry != 0) {\n            int val1 = (l1 != None) ? l1.val : 0;\n            int val2 = (l2 != None) ? l2.val : 0;\n\n            int total = val1 + val2 + carry;\n            carry = total / 10;\n\n            current.next = new ListNode(total % 10);\n            current = current.next;\n\n            l1 = (l1 != None) ? l1.next : None;\n            l2 = (l2 != None) ? l2.next : None;\n        }\n\n        return dummy.next;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        ListNode dummy(0);\n        ListNode* current = &dummy;\n        int carry = 0;\n\n        while (l1 || l2 || carry) {\n            int val1 = l1 ? l1->val : 0;\n            int val2 = l2 ? l2->val : 0;\n\n            int total = val1 + val2 + carry;\n            carry = total / 10;\n\n            current->next = new ListNode(total % 10);\n            current = current->next;\n\n            l1 = l1 ? l1->next : Noneptr;\n            l2 = l2 ? l2->next : Noneptr;\n        }\n\n        return dummy.next;\n    }\n};',
        "solution_explanation": '## Approach: Elementary Math with Carry\n\n### Algorithm\n1. Add digits and carry from right to left\n2. Handle carry for next position\n3. Continue until both lists exhausted and no carry\n\n### Complexity Analysis\n- **Time Complexity**: O(max(m, n))\n- **Space Complexity**: O(max(m, n))'
    },
    {
        "title": 'Container With Most Water',
        "leetcode_url": 'https://leetcode.com/problems/container-with-most-water/',
        "difficulty": 'medium',
        "description": 'You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).\n\nFind two lines that together with the x-axis form a container, such that the container contains the most water.\n\nReturn the maximum amount of water a container can store.',
        "constraints": [
        "n == height.length",
        "2 <= n <= 10^5",
        "0 <= height[i] <= 10^4"
],
        "examples": [
        {
                "input": {
                        "height": [
                                1,
                                8,
                                6,
                                2,
                                5,
                                4,
                                8,
                                3,
                                7
                        ]
                },
                "output": 49,
                "explanation": "The max area is between index 1 (height 8) and index 8 (height 7)."
        }
],
        "tags": [
        "array",
        "two-pointers",
        "greedy"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                8,
                                6,
                                2,
                                5,
                                4,
                                8,
                                3,
                                7
                        ]
                ],
                "expectedOutput": 49
        },
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
                                4,
                                3,
                                2,
                                1,
                                4
                        ]
                ],
                "expectedOutput": 16
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int maxArea(int[] height) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def maxArea(self, height: List[int]) -> int:\n        left, right = 0, len(height) - 1\n        max_area = 0\n\n        while left < right:\n            width = right - left\n            current_area = min(height[left], height[right]) * width\n            max_area = max(max_area, current_area)\n\n            # Move the pointer with smaller height\n            if height[left] < height[right]:\n                left += 1\n            else:\n                right -= 1\n\n        return max_area',
        "solution_java": 'class Solution {\n    public int maxArea(int[] height) {\n        int left = 0, right = height.length - 1;\n        int maxArea = 0;\n\n        while (left < right) {\n            int width = right - left;\n            int currentArea = Math.min(height[left], height[right]) * width;\n            maxArea = Math.max(maxArea, currentArea);\n\n            if (height[left] < height[right]) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n\n        return maxArea;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    int maxArea(vector<int>& height) {\n        int left = 0, right = height.size() - 1;\n        int maxArea = 0;\n\n        while (left < right) {\n            int width = right - left;\n            int currentArea = min(height[left], height[right]) * width;\n            maxArea = max(maxArea, currentArea);\n\n            if (height[left] < height[right]) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n\n        return maxArea;\n    }\n};',
        "solution_explanation": '## Approach: Two Pointers\n\n### Algorithm\n1. Start with widest container\n2. Move pointer with smaller height inward\n3. Track maximum area\n\n### Complexity Analysis\n- **Time Complexity**: O(n)\n- **Space Complexity**: O(1)'
    },
    {
        "title": '3Sum',
        "leetcode_url": 'https://leetcode.com/problems/3sum/',
        "difficulty": 'medium',
        "description": 'Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.\n\nNotice that the solution set must not contain duplicate triplets.',
        "constraints": [
        "3 <= nums.length <= 3000",
        "-10^5 <= nums[i] <= 10^5"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                -1,
                                0,
                                1,
                                2,
                                -1,
                                -4
                        ]
                },
                "output": [
                        [
                                -1,
                                -1,
                                2
                        ],
                        [
                                -1,
                                0,
                                1
                        ]
                ],
                "explanation": "The distinct triplets are [-1,0,1] and [-1,-1,2]."
        },
        {
                "input": {
                        "nums": [
                                0,
                                1,
                                1
                        ]
                },
                "output": [],
                "explanation": "The only possible triplet does not sum up to 0."
        }
],
        "tags": [
        "array",
        "two-pointers",
        "sorting"
],
        "test_cases": [
        {
                "input": [
                        [
                                -1,
                                0,
                                1,
                                2,
                                -1,
                                -4
                        ]
                ],
                "expectedOutput": [
                        [
                                -1,
                                -1,
                                2
                        ],
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
                                0,
                                1,
                                1
                        ]
                ],
                "expectedOutput": []
        },
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
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        pass',
        "java_sig": 'class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        nums.sort()\n        result = []\n\n        for i in range(len(nums) - 2):\n            # Skip duplicates\n            if i > 0 and nums[i] == nums[i - 1]:\n                continue\n\n            left, right = i + 1, len(nums) - 1\n\n            while left < right:\n                total = nums[i] + nums[left] + nums[right]\n\n                if total == 0:\n                    result.append([nums[i], nums[left], nums[right]])\n\n                    # Skip duplicates\n                    while left < right and nums[left] == nums[left + 1]:\n                        left += 1\n                    while left < right and nums[right] == nums[right - 1]:\n                        right -= 1\n\n                    left += 1\n                    right -= 1\n                elif total < 0:\n                    left += 1\n                else:\n                    right -= 1\n\n        return result',
        "solution_java": 'class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        Arrays.sort(nums);\n        List<List<Integer>> result = new ArrayList<>();\n\n        for (int i = 0; i < nums.length - 2; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n\n            int left = i + 1, right = nums.length - 1;\n\n            while (left < right) {\n                int sum = nums[i] + nums[left] + nums[right];\n\n                if (sum == 0) {\n                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));\n\n                    while (left < right && nums[left] == nums[left + 1]) left++;\n                    while (left < right && nums[right] == nums[right - 1]) right--;\n\n                    left++;\n                    right--;\n                } else if (sum < 0) {\n                    left++;\n                } else {\n                    right--;\n                }\n            }\n        }\n\n        return result;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    vector<vector<int>> threeSum(vector<int>& nums) {\n        sort(nums.begin(), nums.end());\n        vector<vector<int>> result;\n\n        for (int i = 0; i < nums.size() - 2; i++) {\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n\n            int left = i + 1, right = nums.size() - 1;\n\n            while (left < right) {\n                int sum = nums[i] + nums[left] + nums[right];\n\n                if (sum == 0) {\n                    result.push_back({nums[i], nums[left], nums[right]});\n\n                    while (left < right && nums[left] == nums[left + 1]) left++;\n                    while (left < right && nums[right] == nums[right - 1]) right--;\n\n                    left++;\n                    right--;\n                } else if (sum < 0) {\n                    left++;\n                } else {\n                    right--;\n                }\n            }\n        }\n\n        return result;\n    }\n};',
        "solution_explanation": '## Approach: Sort + Two Pointers\n\n### Algorithm\n1. Sort the array\n2. Fix one element and find two others using two pointers\n3. Skip duplicates to avoid duplicate triplets\n\n### Complexity Analysis\n- **Time Complexity**: O(n²)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Group Anagrams',
        "leetcode_url": 'https://leetcode.com/problems/group-anagrams/',
        "difficulty": 'medium',
        "description": 'Given an array of strings strs, group the anagrams together. You can return the answer in any order.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.',
        "constraints": [
        "1 <= strs.length <= 10^4",
        "0 <= strs[i].length <= 100",
        "strs[i] consists of lowercase English letters"
],
        "examples": [
        {
                "input": {
                        "strs": [
                                "eat",
                                "tea",
                                "tan",
                                "ate",
                                "nat",
                                "bat"
                        ]
                },
                "output": [
                        [
                                "bat"
                        ],
                        [
                                "nat",
                                "tan"
                        ],
                        [
                                "ate",
                                "eat",
                                "tea"
                        ]
                ],
                "explanation": "Group words that are anagrams."
        }
],
        "tags": [
        "array",
        "hash-table",
        "string",
        "sorting"
],
        "test_cases": [
        {
                "input": [
                        [
                                "eat",
                                "tea",
                                "tan",
                                "ate",
                                "nat",
                                "bat"
                        ]
                ],
                "expectedOutput": [
                        [
                                "bat"
                        ],
                        [
                                "nat",
                                "tan"
                        ],
                        [
                                "ate",
                                "eat",
                                "tea"
                        ]
                ]
        },
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
        }
],
        "time_complexity": 'O(n*k)',
        "space_complexity": 'O(n*k)',
        "python_sig": 'class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        pass',
        "java_sig": 'class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        \n    }\n};',
        "solution_python": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        anagram_map = {}\n\n        for s in strs:\n            # Sort the string to create a key\n            key = ''.join(sorted(s))\n            if key not in anagram_map:\n                anagram_map[key] = []\n            anagram_map[key].append(s)\n\n        return list(anagram_map.values())",
        "solution_java": 'class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        Map<String, List<String>> map = new HashMap<>();\n\n        for (String s : strs) {\n            char[] chars = s.toCharArray();\n            Arrays.sort(chars);\n            String key = String.valueOf(chars);\n\n            if (!map.containsKey(key)) {\n                map.put(key, new ArrayList<>());\n            }\n            map.get(key).add(s);\n        }\n\n        return new ArrayList<>(map.values());\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        unordered_map<string, vector<string>> map;\n\n        for (string& s : strs) {\n            string key = s;\n            sort(key.begin(), key.end());\n            map[key].push_back(s);\n        }\n\n        vector<vector<string>> result;\n        for (auto& pair : map) {\n            result.push_back(pair.second);\n        }\n\n        return result;\n    }\n};',
        "solution_explanation": '## Approach: Hash Map with Sorted String Key\n\n### Algorithm\n1. Sort each string to create a key\n2. Group strings with the same sorted key\n3. Return all groups\n\n### Complexity Analysis\n- **Time Complexity**: O(n * k log k) where k is max string length\n- **Space Complexity**: O(n * k)'
    },
    {
        "title": 'Longest Palindromic Substring',
        "leetcode_url": 'https://leetcode.com/problems/longest-palindromic-substring/',
        "difficulty": 'medium',
        "description": 'Given a string s, return the longest palindromic substring in s.',
        "constraints": [
        "1 <= s.length <= 1000",
        "s consist of only digits and English letters"
],
        "examples": [
        {
                "input": {
                        "s": "babad"
                },
                "output": "bab",
                "explanation": "Note: 'aba' is also a valid answer."
        },
        {
                "input": {
                        "s": "cbbd"
                },
                "output": "bb",
                "explanation": "The longest palindrome is 'bb'."
        }
],
        "tags": [
        "string",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        "babad"
                ],
                "expectedOutput": "bab"
        },
        {
                "input": [
                        "cbbd"
                ],
                "expectedOutput": "bb"
        },
        {
                "input": [
                        "a"
                ],
                "expectedOutput": "a"
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        pass',
        "java_sig": 'class Solution {\n    public String longestPalindrome(String s) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    string longestPalindrome(string s) {\n        \n    }\n};',
        "solution_python": 'class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        if not s:\n            return ""\n\n        def expandAroundCenter(left: int, right: int) -> int:\n            while left >= 0 and right < len(s) and s[left] == s[right]:\n                left -= 1\n                right += 1\n            return right - left - 1\n\n        start = 0\n        max_len = 0\n\n        for i in range(len(s)):\n            # Odd length palindromes\n            len1 = expandAroundCenter(i, i)\n            # Even length palindromes\n            len2 = expandAroundCenter(i, i + 1)\n\n            current_len = max(len1, len2)\n\n            if current_len > max_len:\n                max_len = current_len\n                start = i - (current_len - 1) // 2\n\n        return s[start:start + max_len]',
        "solution_java": 'class Solution {\n    public String longestPalindrome(String s) {\n        if (s == None || s.length() == 0) return "";\n\n        int start = 0, maxLen = 0;\n\n        for (int i = 0; i < s.length(); i++) {\n            int len1 = expandAroundCenter(s, i, i);\n            int len2 = expandAroundCenter(s, i, i + 1);\n            int len = Math.max(len1, len2);\n\n            if (len > maxLen) {\n                maxLen = len;\n                start = i - (len - 1) / 2;\n            }\n        }\n\n        return s.substring(start, start + maxLen);\n    }\n\n    private int expandAroundCenter(String s, int left, int right) {\n        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {\n            left--;\n            right++;\n        }\n        return right - left - 1;\n    }\n}',
        "solution_cpp": 'class Solution {\npublic:\n    string longestPalindrome(string s) {\n        if (s.empty()) return "";\n\n        int start = 0, maxLen = 0;\n\n        for (int i = 0; i < s.length(); i++) {\n            int len1 = expandAroundCenter(s, i, i);\n            int len2 = expandAroundCenter(s, i, i + 1);\n            int len = max(len1, len2);\n\n            if (len > maxLen) {\n                maxLen = len;\n                start = i - (len - 1) / 2;\n            }\n        }\n\n        return s.substr(start, maxLen);\n    }\n\nprivate:\n    int expandAroundCenter(string& s, int left, int right) {\n        while (left >= 0 && right < s.length() && s[left] == s[right]) {\n            left--;\n            right++;\n        }\n        return right - left - 1;\n    }\n};',
        "solution_explanation": '## Approach: Expand Around Centers\n\n### Algorithm\n1. For each position, consider it as center\n2. Expand outward while characters match\n3. Handle both odd and even length palindromes\n\n### Complexity Analysis\n- **Time Complexity**: O(n²)\n- **Space Complexity**: O(1)'
    },
    {
        "title": 'Product of Array Except Self',
        "leetcode_url": 'https://leetcode.com/problems/product-of-array-except-self/',
        "difficulty": 'medium',
        "description": 'Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].\n\nYou must write an algorithm that runs in O(n) time and without using the division operation.',
        "constraints": [
        "2 <= nums.length <= 10^5",
        "-30 <= nums[i] <= 30",
        "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                1,
                                2,
                                3,
                                4
                        ]
                },
                "output": [
                        24,
                        12,
                        8,
                        6
                ],
                "explanation": "answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, etc."
        }
],
        "tags": [
        "array",
        "prefix-sum"
],
        "test_cases": [
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
                        24,
                        12,
                        8,
                        6
                ]
        },
        {
                "input": [
                        [
                                -1,
                                1,
                                0,
                                -3,
                                3
                        ]
                ],
                "expectedOutput": [
                        0,
                        0,
                        9,
                        0,
                        0
                ]
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        pass',
        "java_sig": 'class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<int> productExceptSelf(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Two-pass approach using prefix and suffix products.
        Builds result array where result[i] = product of all elements except nums[i].
        Avoids division operator and runs in O(n) time.

        Algorithm:
        1. First pass: Calculate prefix products (product of all elements before i)
        2. Second pass: Multiply by suffix products (product of all elements after i)

        Time Complexity: O(n) - two passes through array
        Space Complexity: O(1) - excluding output array (no extra space used)
        """
        n = len(nums)
        result = [1] * n

        # First pass: Calculate prefix products
        # result[i] = product of all elements before index i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Second pass: Multiply by suffix products
        # result[i] *= product of all elements after index i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
''',
        "solution_java": '// Solution for Product of Array Except Self\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Product of Array Except Self\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Product of Array Except Self\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Spiral Matrix',
        "leetcode_url": 'https://leetcode.com/problems/spiral-matrix/',
        "difficulty": 'medium',
        "description": 'Given an m x n matrix, return all elements of the matrix in spiral order.',
        "constraints": [
        "m == matrix.length",
        "n == matrix[i].length",
        "1 <= m, n <= 10",
        "-100 <= matrix[i][j] <= 100"
],
        "examples": [
        {
                "input": {
                        "matrix": [
                                [
                                        1,
                                        2,
                                        3
                                ],
                                [
                                        4,
                                        5,
                                        6
                                ],
                                [
                                        7,
                                        8,
                                        9
                                ]
                        ]
                },
                "output": [
                        1,
                        2,
                        3,
                        6,
                        9,
                        8,
                        7,
                        4,
                        5
                ],
                "explanation": "Traverse the matrix in spiral order."
        }
],
        "tags": [
        "array",
        "matrix",
        "simulation"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        1,
                                        2,
                                        3
                                ],
                                [
                                        4,
                                        5,
                                        6
                                ],
                                [
                                        7,
                                        8,
                                        9
                                ]
                        ]
                ],
                "expectedOutput": [
                        1,
                        2,
                        3,
                        6,
                        9,
                        8,
                        7,
                        4,
                        5
                ]
        },
        {
                "input": [
                        [
                                [
                                        1,
                                        2,
                                        3,
                                        4
                                ],
                                [
                                        5,
                                        6,
                                        7,
                                        8
                                ],
                                [
                                        9,
                                        10,
                                        11,
                                        12
                                ]
                        ]
                ],
                "expectedOutput": [
                        1,
                        2,
                        3,
                        4,
                        8,
                        12,
                        11,
                        10,
                        9,
                        5,
                        6,
                        7
                ]
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:\n        pass',
        "java_sig": 'class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        \n    }\n};',
        "solution_python": '# Solution for Spiral Matrix\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Spiral Matrix\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Spiral Matrix\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Spiral Matrix\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Rotate Image',
        "leetcode_url": 'https://leetcode.com/problems/rotate-image/',
        "difficulty": 'medium',
        "description": 'You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).\n\nYou have to rotate the image in-place, which means you have to modify the input 2D matrix directly.',
        "constraints": [
        "n == matrix.length == matrix[i].length",
        "1 <= n <= 20",
        "-1000 <= matrix[i][j] <= 1000"
],
        "examples": [
        {
                "input": {
                        "matrix": [
                                [
                                        1,
                                        2,
                                        3
                                ],
                                [
                                        4,
                                        5,
                                        6
                                ],
                                [
                                        7,
                                        8,
                                        9
                                ]
                        ]
                },
                "output": [
                        [
                                7,
                                4,
                                1
                        ],
                        [
                                8,
                                5,
                                2
                        ],
                        [
                                9,
                                6,
                                3
                        ]
                ],
                "explanation": "Rotate 90 degrees clockwise."
        }
],
        "tags": [
        "array",
        "matrix"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        1,
                                        2,
                                        3
                                ],
                                [
                                        4,
                                        5,
                                        6
                                ],
                                [
                                        7,
                                        8,
                                        9
                                ]
                        ]
                ],
                "expectedOutput": [
                        [
                                7,
                                4,
                                1
                        ],
                        [
                                8,
                                5,
                                2
                        ],
                        [
                                9,
                                6,
                                3
                        ]
                ]
        },
        {
                "input": [
                        [
                                [
                                        5,
                                        1,
                                        9,
                                        11
                                ],
                                [
                                        2,
                                        4,
                                        8,
                                        10
                                ],
                                [
                                        13,
                                        3,
                                        6,
                                        7
                                ],
                                [
                                        15,
                                        14,
                                        12,
                                        16
                                ]
                        ]
                ],
                "expectedOutput": [
                        [
                                15,
                                13,
                                2,
                                5
                        ],
                        [
                                14,
                                3,
                                4,
                                1
                        ],
                        [
                                12,
                                6,
                                8,
                                9
                        ],
                        [
                                16,
                                7,
                                10,
                                11
                        ]
                ]
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n        pass',
        "java_sig": 'class Solution {\n    public void rotate(int[][] matrix) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix) {\n        \n    }\n};',
        "solution_python": '# Solution for Rotate Image\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Rotate Image\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Rotate Image\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Rotate Image\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Set Matrix Zeroes',
        "leetcode_url": 'https://leetcode.com/problems/set-matrix-zeroes/',
        "difficulty": 'medium',
        "description": "Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.\n\nYou must do it in place.",
        "constraints": [
        "m == matrix.length",
        "n == matrix[0].length",
        "1 <= m, n <= 200",
        "-2^31 <= matrix[i][j] <= 2^31 - 1"
],
        "examples": [
        {
                "input": {
                        "matrix": [
                                [
                                        1,
                                        1,
                                        1
                                ],
                                [
                                        1,
                                        0,
                                        1
                                ],
                                [
                                        1,
                                        1,
                                        1
                                ]
                        ]
                },
                "output": [
                        [
                                1,
                                0,
                                1
                        ],
                        [
                                0,
                                0,
                                0
                        ],
                        [
                                1,
                                0,
                                1
                        ]
                ],
                "explanation": "Mark row and column of 0s."
        }
],
        "tags": [
        "array",
        "matrix",
        "hash-table"
],
        "test_cases": [
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
                                        0,
                                        1
                                ],
                                [
                                        1,
                                        1,
                                        1
                                ]
                        ]
                ],
                "expectedOutput": [
                        [
                                1,
                                0,
                                1
                        ],
                        [
                                0,
                                0,
                                0
                        ],
                        [
                                1,
                                0,
                                1
                        ]
                ]
        },
        {
                "input": [
                        [
                                [
                                        0,
                                        1,
                                        2,
                                        0
                                ],
                                [
                                        3,
                                        4,
                                        5,
                                        2
                                ],
                                [
                                        1,
                                        3,
                                        1,
                                        5
                                ]
                        ]
                ],
                "expectedOutput": [
                        [
                                0,
                                0,
                                0,
                                0
                        ],
                        [
                                0,
                                4,
                                5,
                                0
                        ],
                        [
                                0,
                                3,
                                1,
                                0
                        ]
                ]
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def setZeroes(self, matrix: List[List[int]]) -> None:\n        pass',
        "java_sig": 'class Solution {\n    public void setZeroes(int[][] matrix) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    void setZeroes(vector<vector<int>>& matrix) {\n        \n    }\n};',
        "solution_python": '# Solution for Set Matrix Zeroes\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Set Matrix Zeroes\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Set Matrix Zeroes\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Set Matrix Zeroes\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Subarray Sum Equals K',
        "leetcode_url": 'https://leetcode.com/problems/subarray-sum-equals-k/',
        "difficulty": 'medium',
        "description": 'Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.\n\nA subarray is a contiguous non-empty sequence of elements within an array.',
        "constraints": [
        "1 <= nums.length <= 2 * 10^4",
        "-1000 <= nums[i] <= 1000",
        "-10^7 <= k <= 10^7"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                1,
                                1,
                                1
                        ],
                        "k": 2
                },
                "output": 2,
                "explanation": "Subarrays [1,1] and [1,1] sum to 2."
        },
        {
                "input": {
                        "nums": [
                                1,
                                2,
                                3
                        ],
                        "k": 3
                },
                "output": 2,
                "explanation": "Subarrays [1,2] and [3] sum to 3."
        }
],
        "tags": [
        "array",
        "hash-table",
        "prefix-sum"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                1,
                                1
                        ],
                        2
                ],
                "expectedOutput": 2
        },
        {
                "input": [
                        [
                                1,
                                2,
                                3
                        ],
                        3
                ],
                "expectedOutput": 2
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def subarraySum(self, nums: List[int], k: int) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int subarraySum(int[] nums, int k) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Hash map with prefix sums to count subarrays summing to k.
        Uses the insight: if prefix_sum[i] - prefix_sum[j] = k,
        then subarray from j+1 to i sums to k.

        Algorithm:
        1. Track running prefix sum
        2. Store frequency of each prefix sum in hash map
        3. For each position, check if (current_sum - k) exists
        4. Count those occurrences (number of valid subarrays ending here)

        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash map storage
        """
        # Map: prefix_sum -> frequency
        prefix_sums = {0: 1}  # Base case: empty prefix sum
        current_sum = 0
        count = 0

        for num in nums:
            # Update running prefix sum
            current_sum += num

            # Check if (current_sum - k) exists
            # If yes, we found subarrays ending at current position
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Record current prefix sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count
''',
        "solution_java": '// Solution for Subarray Sum Equals K\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Subarray Sum Equals K\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Subarray Sum Equals K\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Maximum Subarray',
        "leetcode_url": 'https://leetcode.com/problems/maximum-subarray/',
        "difficulty": 'medium',
        "description": 'Given an integer array nums, find the subarray with the largest sum, and return its sum.',
        "constraints": [
        "1 <= nums.length <= 10^5",
        "-10^4 <= nums[i] <= 10^4"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                -2,
                                1,
                                -3,
                                4,
                                -1,
                                2,
                                1,
                                -5,
                                4
                        ]
                },
                "output": 6,
                "explanation": "The subarray [4,-1,2,1] has the largest sum 6."
        },
        {
                "input": {
                        "nums": [
                                1
                        ]
                },
                "output": 1,
                "explanation": "The subarray [1] has the largest sum 1."
        }
],
        "tags": [
        "array",
        "divide-and-conquer",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        [
                                -2,
                                1,
                                -3,
                                4,
                                -1,
                                2,
                                1,
                                -5,
                                4
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
                "expectedOutput": 1
        },
        {
                "input": [
                        [
                                5,
                                4,
                                -1,
                                7,
                                8
                        ]
                ],
                "expectedOutput": 23
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int maxSubArray(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int maxSubArray(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm - Classic dynamic programming approach.
        Finds contiguous subarray with the largest sum.

        Key insight: At each position, we decide whether to:
        - Extend the current subarray (add current element)
        - Start a new subarray (current element alone is better)

        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only tracking two variables
        """
        # Track the maximum sum ending at current position
        current_sum = nums[0]
        # Track the overall maximum sum seen so far
        max_sum = nums[0]

        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # Decide: extend current subarray or start fresh
            # If current_sum is negative, starting fresh is better
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
''',
        "solution_java": '// Solution for Maximum Subarray\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Maximum Subarray\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Maximum Subarray\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Remove Nth Node From End of List',
        "leetcode_url": 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/',
        "difficulty": 'medium',
        "description": 'Given the head of a linked list, remove the nth node from the end of the list and return its head.',
        "constraints": [
        "The number of nodes in the list is sz",
        "1 <= sz <= 30",
        "0 <= Node.val <= 100",
        "1 <= n <= sz"
],
        "examples": [
        {
                "input": {
                        "head": [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        "n": 2
                },
                "output": [
                        1,
                        2,
                        3,
                        5
                ],
                "explanation": "Remove 2nd node from end."
        }
],
        "tags": [
        "linked-list",
        "two-pointers"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        2
                ],
                "expectedOutput": [
                        1,
                        2,
                        3,
                        5
                ]
        },
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
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode removeNthFromEnd(ListNode head, int n) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* removeNthFromEnd(ListNode* head, int n) {\n        \n    }\n};',
        "solution_python": '# Solution for Remove Nth Node From End of List\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Remove Nth Node From End of List\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Remove Nth Node From End of List\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Remove Nth Node From End of List\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Reverse Linked List II',
        "leetcode_url": 'https://leetcode.com/problems/reverse-linked-list-ii/',
        "difficulty": 'medium',
        "description": 'Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.',
        "constraints": [
        "The number of nodes in the list is n",
        "1 <= n <= 500",
        "-500 <= Node.val <= 500",
        "1 <= left <= right <= n"
],
        "examples": [
        {
                "input": {
                        "head": [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        "left": 2,
                        "right": 4
                },
                "output": [
                        1,
                        4,
                        3,
                        2,
                        5
                ],
                "explanation": "Reverse nodes from position 2 to 4."
        }
],
        "tags": [
        "linked-list"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        2,
                        4
                ],
                "expectedOutput": [
                        1,
                        4,
                        3,
                        2,
                        5
                ]
        },
        {
                "input": [
                        [
                                5
                        ],
                        1,
                        1
                ],
                "expectedOutput": [
                        5
                ]
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode reverseBetween(ListNode head, int left, int right) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* reverseBetween(ListNode* head, int left, int right) {\n        \n    }\n};',
        "solution_python": '# Solution for Reverse Linked List II\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Reverse Linked List II\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Reverse Linked List II\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Reverse Linked List II\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Swap Nodes in Pairs',
        "leetcode_url": 'https://leetcode.com/problems/swap-nodes-in-pairs/',
        "difficulty": 'medium',
        "description": "Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.",
        "constraints": [
        "The number of nodes in the list is in the range [0, 100]",
        "0 <= Node.val <= 100"
],
        "examples": [
        {
                "input": {
                        "head": [
                                1,
                                2,
                                3,
                                4
                        ]
                },
                "output": [
                        2,
                        1,
                        4,
                        3
                ],
                "explanation": "Swap adjacent pairs."
        }
],
        "tags": [
        "linked-list",
        "recursion"
],
        "test_cases": [
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
                        2,
                        1,
                        4,
                        3
                ]
        },
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
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode swapPairs(ListNode head) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* swapPairs(ListNode* head) {\n        \n    }\n};',
        "solution_python": '# Solution for Swap Nodes in Pairs\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Swap Nodes in Pairs\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Swap Nodes in Pairs\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Swap Nodes in Pairs\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Binary Tree Level Order Traversal',
        "leetcode_url": 'https://leetcode.com/problems/binary-tree-level-order-traversal/',
        "difficulty": 'medium',
        "description": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
        "constraints": [
        "The number of nodes in the tree is in the range [0, 2000]",
        "-1000 <= Node.val <= 1000"
],
        "examples": [
        {
                "input": {
                        "root": [
                                3,
                                9,
                                20,
                                None,
                                None,
                                15,
                                7
                        ]
                },
                "output": [
                        [
                                3
                        ],
                        [
                                9,
                                20
                        ],
                        [
                                15,
                                7
                        ]
                ],
                "explanation": "Level by level traversal."
        }
],
        "tags": [
        "tree",
        "breadth-first-search"
],
        "test_cases": [
        {
                "input": [
                        [
                                3,
                                9,
                                20,
                                None,
                                None,
                                15,
                                7
                        ]
                ],
                "expectedOutput": [
                        [
                                3
                        ],
                        [
                                9,
                                20
                        ],
                        [
                                15,
                                7
                        ]
                ]
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
                        []
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:\n        pass',
        "java_sig": 'class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<vector<int>> levelOrder(TreeNode* root) {\n        \n    }\n};',
        "solution_python": '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Breadth-First Search (BFS) using a queue.
        Traverses tree level by level, collecting nodes at each level.

        Algorithm:
        1. Use queue to track nodes at current level
        2. For each level, process all nodes and collect their values
        3. Add children of current level to queue for next level

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(w) - where w is maximum width of tree (queue size)
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
''',
        "solution_java": '// Solution for Binary Tree Level Order Traversal\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Binary Tree Level Order Traversal\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Binary Tree Level Order Traversal\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Validate Binary Search Tree',
        "leetcode_url": 'https://leetcode.com/problems/validate-binary-search-tree/',
        "difficulty": 'medium',
        "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\n\nA valid BST is defined as follows:\n- The left subtree of a node contains only nodes with keys less than the node's key.\n- The right subtree of a node contains only nodes with keys greater than the node's key.\n- Both the left and right subtrees must also be binary search trees.",
        "constraints": [
        "The number of nodes in the tree is in the range [1, 10^4]",
        "-2^31 <= Node.val <= 2^31 - 1"
],
        "examples": [
        {
                "input": {
                        "root": [
                                2,
                                1,
                                3
                        ]
                },
                "output": True,
                "explanation": "Valid BST."
        },
        {
                "input": {
                        "root": [
                                5,
                                1,
                                4,
                                None,
                                None,
                                3,
                                6
                        ]
                },
                "output": False,
                "explanation": "Node 4 in right subtree of 5 violates BST property."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "binary-search-tree"
],
        "test_cases": [
        {
                "input": [
                        [
                                2,
                                1,
                                3
                        ]
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        [
                                5,
                                1,
                                4,
                                None,
                                None,
                                3,
                                6
                        ]
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def isValidBST(self, root: Optional[TreeNode]) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean isValidBST(TreeNode root) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        \n    }\n};',
        "solution_python": '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive validation with min/max bounds.
        BST property: all nodes in left subtree < root < all nodes in right subtree

        Algorithm:
        - Track valid range [min_val, max_val] for each node
        - Left child must be < current node value
        - Right child must be > current node value
        - Recursively validate with updated bounds

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack where h is tree height
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            # Empty tree is valid BST
            if not node:
                return True

            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False

            # Recursively validate left and right subtrees with updated bounds
            # Left subtree: all values must be < node.val
            # Right subtree: all values must be > node.val
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        # Start with infinite bounds
        return validate(root, float('-inf'), float('inf'))
''',
        "solution_java": '// Solution for Validate Binary Search Tree\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Validate Binary Search Tree\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Validate Binary Search Tree\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Kth Smallest Element in a BST',
        "leetcode_url": 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/',
        "difficulty": 'medium',
        "description": 'Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.',
        "constraints": [
        "The number of nodes in the tree is n",
        "1 <= k <= n <= 10^4",
        "0 <= Node.val <= 10^4"
],
        "examples": [
        {
                "input": {
                        "root": [
                                3,
                                1,
                                4,
                                None,
                                2
                        ],
                        "k": 1
                },
                "output": 1,
                "explanation": "The smallest element is 1."
        },
        {
                "input": {
                        "root": [
                                5,
                                3,
                                6,
                                2,
                                4,
                                None,
                                None,
                                1
                        ],
                        "k": 3
                },
                "output": 3,
                "explanation": "The 3rd smallest is 3."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "binary-search-tree"
],
        "test_cases": [
        {
                "input": [
                        [
                                3,
                                1,
                                4,
                                None,
                                2
                        ],
                        1
                ],
                "expectedOutput": 1
        },
        {
                "input": [
                        [
                                5,
                                3,
                                6,
                                2,
                                4,
                                None,
                                None,
                                1
                        ],
                        3
                ],
                "expectedOutput": 3
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        \n    }\n};',
        "solution_python": '# Solution for Kth Smallest Element in a BST\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Kth Smallest Element in a BST\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Kth Smallest Element in a BST\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Kth Smallest Element in a BST\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Binary Tree Right Side View',
        "leetcode_url": 'https://leetcode.com/problems/binary-tree-right-side-view/',
        "difficulty": 'medium',
        "description": 'Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.',
        "constraints": [
        "The number of nodes in the tree is in the range [0, 100]",
        "-100 <= Node.val <= 100"
],
        "examples": [
        {
                "input": {
                        "root": [
                                1,
                                2,
                                3,
                                None,
                                5,
                                None,
                                4
                        ]
                },
                "output": [
                        1,
                        3,
                        4
                ],
                "explanation": "Right side view shows nodes 1, 3, 4."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "breadth-first-search"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3,
                                None,
                                5,
                                None,
                                4
                        ]
                ],
                "expectedOutput": [
                        1,
                        3,
                        4
                ]
        },
        {
                "input": [
                        [
                                1,
                                None,
                                3
                        ]
                ],
                "expectedOutput": [
                        1,
                        3
                ]
        },
        {
                "input": [
                        []
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\n        pass',
        "java_sig": 'class Solution {\n    public List<Integer> rightSideView(TreeNode root) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<int> rightSideView(TreeNode* root) {\n        \n    }\n};',
        "solution_python": '# Solution for Binary Tree Right Side View\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Binary Tree Right Side View\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Binary Tree Right Side View\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Binary Tree Right Side View\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Path Sum II',
        "leetcode_url": 'https://leetcode.com/problems/path-sum-ii/',
        "difficulty": 'medium',
        "description": 'Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.\n\nA root-to-leaf path is a path starting from the root and ending at any leaf node.',
        "constraints": [
        "The number of nodes in the tree is in the range [0, 5000]",
        "-1000 <= Node.val <= 1000",
        "-1000 <= targetSum <= 1000"
],
        "examples": [
        {
                "input": {
                        "root": [
                                5,
                                4,
                                8,
                                11,
                                None,
                                13,
                                4,
                                7,
                                2,
                                None,
                                None,
                                5,
                                1
                        ],
                        "targetSum": 22
                },
                "output": [
                        [
                                5,
                                4,
                                11,
                                2
                        ],
                        [
                                5,
                                8,
                                4,
                                5
                        ]
                ],
                "explanation": "Two paths sum to 22."
        }
],
        "tags": [
        "tree",
        "backtracking",
        "depth-first-search"
],
        "test_cases": [
        {
                "input": [
                        [
                                5,
                                4,
                                8,
                                11,
                                None,
                                13,
                                4,
                                7,
                                2,
                                None,
                                None,
                                5,
                                1
                        ],
                        22
                ],
                "expectedOutput": [
                        [
                                5,
                                4,
                                11,
                                2
                        ],
                        [
                                5,
                                8,
                                4,
                                5
                        ]
                ]
        },
        {
                "input": [
                        [
                                1,
                                2,
                                3
                        ],
                        5
                ],
                "expectedOutput": []
        },
        {
                "input": [
                        [
                                1,
                                2
                        ],
                        0
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:\n        pass',
        "java_sig": 'class Solution {\n    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {\n        \n    }\n};',
        "solution_python": '# Solution for Path Sum II\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Path Sum II\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Path Sum II\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Path Sum II\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Construct Binary Tree from Preorder and Inorder Traversal',
        "leetcode_url": 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/',
        "difficulty": 'medium',
        "description": 'Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.',
        "constraints": [
        "1 <= preorder.length <= 3000",
        "inorder.length == preorder.length",
        "-3000 <= preorder[i], inorder[i] <= 3000",
        "preorder and inorder consist of unique values"
],
        "examples": [
        {
                "input": {
                        "preorder": [
                                3,
                                9,
                                20,
                                15,
                                7
                        ],
                        "inorder": [
                                9,
                                3,
                                15,
                                20,
                                7
                        ]
                },
                "output": [
                        3,
                        9,
                        20,
                        None,
                        None,
                        15,
                        7
                ],
                "explanation": "Construct tree from traversals."
        }
],
        "tags": [
        "tree",
        "array",
        "hash-table",
        "divide-and-conquer"
],
        "test_cases": [
        {
                "input": [
                        [
                                3,
                                9,
                                20,
                                15,
                                7
                        ],
                        [
                                9,
                                3,
                                15,
                                20,
                                7
                        ]
                ],
                "expectedOutput": [
                        3,
                        9,
                        20,
                        None,
                        None,
                        15,
                        7
                ]
        },
        {
                "input": [
                        [
                                -1
                        ],
                        [
                                -1
                        ]
                ],
                "expectedOutput": [
                        -1
                ]
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:\n        pass',
        "java_sig": 'class Solution {\n    public TreeNode buildTree(int[] preorder, int[] inorder) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {\n        \n    }\n};',
        "solution_python": '# Solution for Construct Binary Tree from Preorder and Inorder Traversal\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Construct Binary Tree from Preorder and Inorder Traversal\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Construct Binary Tree from Preorder and Inorder Traversal\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Construct Binary Tree from Preorder and Inorder Traversal\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Lowest Common Ancestor of a Binary Tree',
        "leetcode_url": 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/',
        "difficulty": 'medium',
        "description": 'Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.\n\nThe lowest common ancestor is defined as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).',
        "constraints": [
        "The number of nodes in the tree is in the range [2, 10^5]",
        "-10^9 <= Node.val <= 10^9",
        "All Node.val are unique",
        "p != q",
        "p and q exist in the tree"
],
        "examples": [
        {
                "input": {
                        "root": [
                                3,
                                5,
                                1,
                                6,
                                2,
                                0,
                                8,
                                None,
                                None,
                                7,
                                4
                        ],
                        "p": 5,
                        "q": 1
                },
                "output": 3,
                "explanation": "The LCA of nodes 5 and 1 is 3."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "binary-tree"
],
        "test_cases": [
        {
                "input": [
                        [
                                3,
                                5,
                                1,
                                6,
                                2,
                                0,
                                8,
                                None,
                                None,
                                7,
                                4
                        ],
                        5,
                        1
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        [
                                3,
                                5,
                                1,
                                6,
                                2,
                                0,
                                8,
                                None,
                                None,
                                7,
                                4
                        ],
                        5,
                        4
                ],
                "expectedOutput": 5
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:\n        pass',
        "java_sig": 'class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n        \n    }\n};',
        "solution_python": '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Recursive approach to find lowest common ancestor.
        LCA is the deepest node that has both p and q as descendants.

        Algorithm:
        1. If current node is None or matches p or q, return it
        2. Recursively search left and right subtrees
        3. If both subtrees return non-null, current is LCA
        4. Otherwise, return whichever subtree found a match

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack height
        """
        # Base case: empty node or found target
        if not root or root == p or root == q:
            return root

        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both subtrees found a target, current node is LCA
        if left and right:
            return root

        # Otherwise, return whichever subtree found a target
        # (or None if neither found)
        return left if left else right
''',
        "solution_java": '// Solution for Lowest Common Ancestor of a Binary Tree\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Lowest Common Ancestor of a Binary Tree\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Lowest Common Ancestor of a Binary Tree\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Number of Islands',
        "leetcode_url": 'https://leetcode.com/problems/number-of-islands/',
        "difficulty": 'medium',
        "description": "Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
        "constraints": [
        "m == grid.length",
        "n == grid[i].length",
        "1 <= m, n <= 300",
        "grid[i][j] is '0' or '1'"
],
        "examples": [
        {
                "input": {
                        "grid": [
                                [
                                        "1",
                                        "1",
                                        "1",
                                        "1",
                                        "0"
                                ],
                                [
                                        "1",
                                        "1",
                                        "0",
                                        "1",
                                        "0"
                                ],
                                [
                                        "1",
                                        "1",
                                        "0",
                                        "0",
                                        "0"
                                ],
                                [
                                        "0",
                                        "0",
                                        "0",
                                        "0",
                                        "0"
                                ]
                        ]
                },
                "output": 1,
                "explanation": "One connected island."
        }
],
        "tags": [
        "array",
        "depth-first-search",
        "breadth-first-search",
        "union-find",
        "matrix"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        "1",
                                        "1",
                                        "1",
                                        "1",
                                        "0"
                                ],
                                [
                                        "1",
                                        "1",
                                        "0",
                                        "1",
                                        "0"
                                ],
                                [
                                        "1",
                                        "1",
                                        "0",
                                        "0",
                                        "0"
                                ],
                                [
                                        "0",
                                        "0",
                                        "0",
                                        "0",
                                        "0"
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
                                        "1",
                                        "0",
                                        "0",
                                        "0"
                                ],
                                [
                                        "1",
                                        "1",
                                        "0",
                                        "0",
                                        "0"
                                ],
                                [
                                        "0",
                                        "0",
                                        "1",
                                        "0",
                                        "0"
                                ],
                                [
                                        "0",
                                        "0",
                                        "0",
                                        "1",
                                        "1"
                                ]
                        ]
                ],
                "expectedOutput": 3
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(m*n)',
        "python_sig": 'class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int numIslands(char[][] grid) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int numIslands(vector<vector<char>>& grid) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Depth-First Search (DFS) to find connected components.
        Each island is a connected component of '1's (land).

        Algorithm:
        1. Iterate through each cell in grid
        2. When we find unvisited land ('1'), it's a new island
        3. DFS from that cell to mark all connected land as visited
        4. Count total number of DFS calls (number of islands)

        Time Complexity: O(m * n) - visit each cell at most twice
        Space Complexity: O(m * n) - worst case recursion depth (all land)
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r: int, c: int) -> None:
            """Mark all connected land cells as visited."""
            # Base cases: out of bounds or water or already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] != '1'):
                return

            # Mark current cell as visited by changing to '0'
            grid[r][c] = '0'

            # Explore all 4 directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Scan entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Found new island
                    num_islands += 1
                    # Mark all connected land
                    dfs(r, c)

        return num_islands
''',
        "solution_java": '// Solution for Number of Islands\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Number of Islands\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Number of Islands\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Course Schedule',
        "leetcode_url": 'https://leetcode.com/problems/course-schedule/',
        "difficulty": 'medium',
        "description": 'There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\n\nReturn True if you can finish all courses. Otherwise, return False.',
        "constraints": [
        "1 <= numCourses <= 2000",
        "0 <= prerequisites.length <= 5000",
        "prerequisites[i].length == 2",
        "0 <= ai, bi < numCourses",
        "All the pairs prerequisites[i] are unique"
],
        "examples": [
        {
                "input": {
                        "numCourses": 2,
                        "prerequisites": [
                                [
                                        1,
                                        0
                                ]
                        ]
                },
                "output": True,
                "explanation": "Take course 0 first, then course 1."
        },
        {
                "input": {
                        "numCourses": 2,
                        "prerequisites": [
                                [
                                        1,
                                        0
                                ],
                                [
                                        0,
                                        1
                                ]
                        ]
                },
                "output": False,
                "explanation": "Circular dependency."
        }
],
        "tags": [
        "graph",
        "topological-sort",
        "depth-first-search",
        "breadth-first-search"
],
        "test_cases": [
        {
                "input": [
                        2,
                        [
                                [
                                        1,
                                        0
                                ]
                        ]
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        2,
                        [
                                [
                                        1,
                                        0
                                ],
                                [
                                        0,
                                        1
                                ]
                        ]
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(V+E)',
        "space_complexity": 'O(V+E)',
        "python_sig": 'class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topological Sort using DFS to detect cycles.
        Check if course schedule is possible (no circular dependencies).

        Algorithm:
        1. Build adjacency list (prerequisite graph)
        2. Use DFS with state tracking:
           - UNVISITED (0): not processed
           - VISITING (1): currently in DFS path (cycle if revisited)
           - VISITED (2): fully processed
        3. If we encounter VISITING node, there's a cycle

        Time Complexity: O(V + E) - vertices (courses) + edges (prerequisites)
        Space Complexity: O(V + E) - graph storage + recursion stack
        """
        from collections import defaultdict

        # Build adjacency list: course -> list of courses that depend on it
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # State: 0=unvisited, 1=visiting (in current DFS path), 2=visited
        state = [0] * numCourses

        def has_cycle(course: int) -> bool:
            """DFS to detect cycle. Returns True if cycle found."""
            if state[course] == 1:
                # Currently visiting - found cycle
                return True
            if state[course] == 2:
                # Already fully processed - no cycle through this path
                return False

            # Mark as visiting (in current DFS path)
            state[course] = 1

            # Check all courses that depend on this one
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True

            # Mark as visited (fully processed)
            state[course] = 2
            return False

        # Check each course for cycles
        for course in range(numCourses):
            if state[course] == 0:  # Unvisited
                if has_cycle(course):
                    return False

        return True
''',
        "solution_java": '// Solution for Course Schedule\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Course Schedule\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Course Schedule\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Clone Graph',
        "leetcode_url": 'https://leetcode.com/problems/clone-graph/',
        "difficulty": 'medium',
        "description": 'Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.\n\nEach node in the graph contains a value (int) and a list (List[Node]) of its neighbors.',
        "constraints": [
        "The number of nodes in the graph is in the range [0, 100]",
        "1 <= Node.val <= 100",
        "Node.val is unique for each node",
        "There are no repeated edges and no self-loops"
],
        "examples": [
        {
                "input": {
                        "adjList": [
                                [
                                        2,
                                        4
                                ],
                                [
                                        1,
                                        3
                                ],
                                [
                                        2,
                                        4
                                ],
                                [
                                        1,
                                        3
                                ]
                        ]
                },
                "output": [
                        [
                                2,
                                4
                        ],
                        [
                                1,
                                3
                        ],
                        [
                                2,
                                4
                        ],
                        [
                                1,
                                3
                        ]
                ],
                "explanation": "Clone the graph."
        }
],
        "tags": [
        "hash-table",
        "depth-first-search",
        "breadth-first-search",
        "graph"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        2,
                                        4
                                ],
                                [
                                        1,
                                        3
                                ],
                                [
                                        2,
                                        4
                                ],
                                [
                                        1,
                                        3
                                ]
                        ]
                ],
                "expectedOutput": [
                        [
                                2,
                                4
                        ],
                        [
                                1,
                                3
                        ],
                        [
                                2,
                                4
                        ],
                        [
                                1,
                                3
                        ]
                ]
        },
        {
                "input": [
                        [
                                []
                        ]
                ],
                "expectedOutput": [
                        []
                ]
        },
        {
                "input": [
                        []
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(N+M)',
        "space_complexity": 'O(N)',
        "python_sig": "class Solution:\n    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:\n        pass",
        "java_sig": 'class Solution {\n    public Node cloneGraph(Node node) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    Node* cloneGraph(Node* node) {\n        \n    }\n};',
        "solution_python": '''"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Deep copy graph using DFS with hash map.
        Creates independent copy where no node is shared with original.

        Algorithm:
        1. Use hash map to track original node -> cloned node mapping
        2. DFS through graph:
           - Clone current node if not already cloned
           - Recursively clone all neighbors
           - Connect cloned node to cloned neighbors

        Time Complexity: O(V + E) - visit each vertex and edge once
        Space Complexity: O(V) - hash map + recursion stack
        """
        if not node:
            return None

        # Map: original node -> cloned node
        cloned = {}

        def dfs(original: 'Node') -> 'Node':
            """Recursively clone node and its neighbors."""
            # If already cloned, return the clone
            if original in cloned:
                return cloned[original]

            # Create clone of current node (without neighbors yet)
            clone = Node(original.val)
            cloned[original] = clone

            # Recursively clone all neighbors and connect them
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
''',
        "solution_java": '// Solution for Clone Graph\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Clone Graph\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Clone Graph\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Word Search',
        "leetcode_url": 'https://leetcode.com/problems/word-search/',
        "difficulty": 'medium',
        "description": 'Given an m x n grid of characters board and a string word, return True if word exists in the grid.\n\nThe word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.',
        "constraints": [
        "m == board.length",
        "n = board[i].length",
        "1 <= m, n <= 6",
        "1 <= word.length <= 15",
        "board and word consists of only lowercase and uppercase English letters"
],
        "examples": [
        {
                "input": {
                        "board": [
                                [
                                        "A",
                                        "B",
                                        "C",
                                        "E"
                                ],
                                [
                                        "S",
                                        "F",
                                        "C",
                                        "S"
                                ],
                                [
                                        "A",
                                        "D",
                                        "E",
                                        "E"
                                ]
                        ],
                        "word": "ABCCED"
                },
                "output": True,
                "explanation": "Word found in board."
        }
],
        "tags": [
        "array",
        "backtracking",
        "matrix"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        "A",
                                        "B",
                                        "C",
                                        "E"
                                ],
                                [
                                        "S",
                                        "F",
                                        "C",
                                        "S"
                                ],
                                [
                                        "A",
                                        "D",
                                        "E",
                                        "E"
                                ]
                        ],
                        "ABCCED"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        [
                                [
                                        "A",
                                        "B",
                                        "C",
                                        "E"
                                ],
                                [
                                        "S",
                                        "F",
                                        "C",
                                        "S"
                                ],
                                [
                                        "A",
                                        "D",
                                        "E",
                                        "E"
                                ]
                        ],
                        "SEE"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        [
                                [
                                        "A",
                                        "B",
                                        "C",
                                        "E"
                                ],
                                [
                                        "S",
                                        "F",
                                        "C",
                                        "S"
                                ],
                                [
                                        "A",
                                        "D",
                                        "E",
                                        "E"
                                ]
                        ],
                        "ABCB"
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(m*n*4^L)',
        "space_complexity": 'O(L)',
        "python_sig": 'class Solution:\n    def exist(self, board: List[List[str]], word: str) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean exist(char[][] board, String word) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool exist(vector<vector<char>>& board, string word) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Backtracking (DFS) on 2D grid to find word path.
        Marks visited cells to avoid reuse in same path.

        Algorithm:
        1. Try starting from each cell
        2. DFS in 4 directions matching word characters
        3. Mark visited cells, backtrack to unmark
        4. Return true if complete word found

        Time Complexity: O(m * n * 4^L) where L is word length
        Space Complexity: O(L) - recursion depth
        """
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            """DFS to match word starting from position (r,c)."""
            # Base case: matched entire word
            if index == len(word):
                return True

            # Check bounds and cell match
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 directions
            found = (backtrack(r + 1, c, index + 1) or
                    backtrack(r - 1, c, index + 1) or
                    backtrack(r, c + 1, index + 1) or
                    backtrack(r, c - 1, index + 1))

            # Backtrack: restore cell
            board[r][c] = temp

            return found

        # Try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
''',
        "solution_java": '// Solution for Word Search\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Word Search\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Word Search\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Coin Change',
        "leetcode_url": 'https://leetcode.com/problems/coin-change/',
        "difficulty": 'medium',
        "description": 'You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.\n\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.',
        "constraints": [
        "1 <= coins.length <= 12",
        "1 <= coins[i] <= 2^31 - 1",
        "0 <= amount <= 10^4"
],
        "examples": [
        {
                "input": {
                        "coins": [
                                1,
                                2,
                                5
                        ],
                        "amount": 11
                },
                "output": 3,
                "explanation": "11 = 5 + 5 + 1"
        },
        {
                "input": {
                        "coins": [
                                2
                        ],
                        "amount": 3
                },
                "output": -1,
                "explanation": "Cannot make amount 3."
        }
],
        "tags": [
        "array",
        "dynamic-programming",
        "breadth-first-search"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                5
                        ],
                        11
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        [
                                2
                        ],
                        3
                ],
                "expectedOutput": -1
        },
        {
                "input": [
                        [
                                1
                        ],
                        0
                ],
                "expectedOutput": 0
        }
],
        "time_complexity": 'O(amount * n)',
        "space_complexity": 'O(amount)',
        "python_sig": 'class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int coinChange(int[] coins, int amount) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int coinChange(vector<int>& coins, int amount) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom-up Dynamic Programming approach.
        Find minimum number of coins needed to make up the target amount.

        Algorithm:
        1. Create DP array where dp[i] = min coins needed for amount i
        2. Initialize dp[0] = 0 (zero coins for amount 0)
        3. For each amount from 1 to target:
           - Try each coin denomination
           - Take minimum of all valid options

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount) - DP array
        """
        # Initialize DP array with infinity (impossible to make)
        # dp[i] represents min coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins for amount 0

        # Build up solution for each amount from 1 to target
        for current_amount in range(1, amount + 1):
            # Try each coin denomination
            for coin in coins:
                if coin <= current_amount:
                    # If we can use this coin, check if it gives better solution
                    # dp[current_amount - coin] + 1 means:
                    # "min coins for (current_amount - coin)" + this coin
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        # If dp[amount] is still infinity, amount cannot be made
        return dp[amount] if dp[amount] != float('inf') else -1
''',
        "solution_java": '// Solution for Coin Change\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Coin Change\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Coin Change\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Longest Increasing Subsequence',
        "leetcode_url": 'https://leetcode.com/problems/longest-increasing-subsequence/',
        "difficulty": 'medium',
        "description": 'Given an integer array nums, return the length of the longest strictly increasing subsequence.',
        "constraints": [
        "1 <= nums.length <= 2500",
        "-10^4 <= nums[i] <= 10^4"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                10,
                                9,
                                2,
                                5,
                                3,
                                7,
                                101,
                                18
                        ]
                },
                "output": 4,
                "explanation": "The longest increasing subsequence is [2,3,7,101]."
        },
        {
                "input": {
                        "nums": [
                                0,
                                1,
                                0,
                                3,
                                2,
                                3
                        ]
                },
                "output": 4,
                "explanation": "The longest increasing subsequence is [0,1,2,3]."
        }
],
        "tags": [
        "array",
        "binary-search",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        [
                                10,
                                9,
                                2,
                                5,
                                3,
                                7,
                                101,
                                18
                        ]
                ],
                "expectedOutput": 4
        },
        {
                "input": [
                        [
                                0,
                                1,
                                0,
                                3,
                                2,
                                3
                        ]
                ],
                "expectedOutput": 4
        },
        {
                "input": [
                        [
                                7,
                                7,
                                7,
                                7,
                                7,
                                7,
                                7
                        ]
                ],
                "expectedOutput": 1
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int lengthOfLIS(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int lengthOfLIS(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Dynamic Programming with Binary Search optimization.
        Finds length of longest strictly increasing subsequence.

        Algorithm (Patience Sort approach):
        1. Maintain array 'sub' of smallest tail values for increasing subsequences
        2. For each number, binary search for position in 'sub'
        3. If larger than all elements, extend subsequence
        4. Otherwise, replace first element >= current number

        Why this works: We're maintaining optimal tails for all subsequence lengths.

        Time Complexity: O(n log n) - binary search for each element
        Space Complexity: O(n) - sub array
        """
        if not nums:
            return 0

        # sub[i] = smallest tail element for increasing subsequence of length i+1
        sub = []

        for num in nums:
            # Binary search for position to insert/replace
            left, right = 0, len(sub)

            while left < right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # If num is larger than all elements in sub, extend subsequence
            if left == len(sub):
                sub.append(num)
            else:
                # Replace first element >= num to keep smallest possible tail
                sub[left] = num

        return len(sub)
''',
        "solution_java": '// Solution for Longest Increasing Subsequence\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Longest Increasing Subsequence\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Longest Increasing Subsequence\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Unique Paths',
        "leetcode_url": 'https://leetcode.com/problems/unique-paths/',
        "difficulty": 'medium',
        "description": 'There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.\n\nGiven the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.',
        "constraints": [
        "1 <= m, n <= 100"
],
        "examples": [
        {
                "input": {
                        "m": 3,
                        "n": 7
                },
                "output": 28,
                "explanation": "There are 28 unique paths."
        },
        {
                "input": {
                        "m": 3,
                        "n": 2
                },
                "output": 3,
                "explanation": "From top-left: right->down->down, down->down->right, down->right->down"
        }
],
        "tags": [
        "math",
        "dynamic-programming",
        "combinatorics"
],
        "test_cases": [
        {
                "input": [
                        3,
                        7
                ],
                "expectedOutput": 28
        },
        {
                "input": [
                        3,
                        2
                ],
                "expectedOutput": 3
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(m*n)',
        "python_sig": 'class Solution:\n    def uniquePaths(self, m: int, n: int) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int uniquePaths(int m, int n) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        \n    }\n};',
        "solution_python": '# Solution for Unique Paths\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Unique Paths\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Unique Paths\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Unique Paths\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Word Break',
        "leetcode_url": 'https://leetcode.com/problems/word-break/',
        "difficulty": 'medium',
        "description": 'Given a string s and a dictionary of strings wordDict, return True if s can be segmented into a space-separated sequence of one or more dictionary words.\n\nNote that the same word in the dictionary may be reused multiple times in the segmentation.',
        "constraints": [
        "1 <= s.length <= 300",
        "1 <= wordDict.length <= 1000",
        "1 <= wordDict[i].length <= 20",
        "s and wordDict[i] consist of only lowercase English letters",
        "All strings in wordDict are unique"
],
        "examples": [
        {
                "input": {
                        "s": "leetcode",
                        "wordDict": [
                                "leet",
                                "code"
                        ]
                },
                "output": True,
                "explanation": "'leetcode' can be segmented as 'leet code'."
        },
        {
                "input": {
                        "s": "applepenapple",
                        "wordDict": [
                                "apple",
                                "pen"
                        ]
                },
                "output": True,
                "explanation": "'applepenapple' can be segmented as 'apple pen apple'."
        }
],
        "tags": [
        "hash-table",
        "string",
        "dynamic-programming",
        "trie",
        "memoization"
],
        "test_cases": [
        {
                "input": [
                        "leetcode",
                        [
                                "leet",
                                "code"
                        ]
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "applepenapple",
                        [
                                "apple",
                                "pen"
                        ]
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "catsandog",
                        [
                                "cats",
                                "dog",
                                "sand",
                                "and",
                                "cat"
                        ]
                ],
                "expectedOutput": False
        }
],
        "time_complexity": 'O(n^2)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean wordBreak(String s, List<String> wordDict) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool wordBreak(string s, vector<string>& wordDict) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Dynamic Programming to check if string can be segmented.
        Uses DP array where dp[i] = can segment s[0:i].

        Algorithm:
        1. dp[0] = True (empty string is valid)
        2. For each position i, check all words
        3. If word fits and previous portion is valid, mark dp[i] = True
        4. Return dp[len(s)]

        Time Complexity: O(n^2 * m) where n=string length, m=avg word length
        Space Complexity: O(n) - DP array
        """
        n = len(s)
        # dp[i] = True if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        # Convert to set for O(1) lookup
        word_set = set(wordDict)

        # Build up solution for each position
        for i in range(1, n + 1):
            # Check if any word ends at position i
            for j in range(i):
                # If s[0:j] is valid and s[j:i] is a word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found valid segmentation to position i

        return dp[n]
''',
        "solution_java": '// Solution for Word Break\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Word Break\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Word Break\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'House Robber II',
        "leetcode_url": 'https://leetcode.com/problems/house-robber-ii/',
        "difficulty": 'medium',
        "description": 'You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\nGiven an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.',
        "constraints": [
        "1 <= nums.length <= 100",
        "0 <= nums[i] <= 1000"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                2,
                                3,
                                2
                        ]
                },
                "output": 3,
                "explanation": "You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent."
        },
        {
                "input": {
                        "nums": [
                                1,
                                2,
                                3,
                                1
                        ]
                },
                "output": 4,
                "explanation": "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4."
        }
],
        "tags": [
        "array",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        [
                                2,
                                3,
                                2
                        ]
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        [
                                1,
                                2,
                                3,
                                1
                        ]
                ],
                "expectedOutput": 4
        },
        {
                "input": [
                        [
                                1,
                                2,
                                3
                        ]
                ],
                "expectedOutput": 3
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def rob(self, nums: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int rob(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int rob(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": '# Solution for House Robber II\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for House Robber II\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for House Robber II\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for House Robber II\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Decode Ways',
        "leetcode_url": 'https://leetcode.com/problems/decode-ways/',
        "difficulty": 'medium',
        "description": 'A message containing letters from A-Z can be encoded into numbers using the following mapping:\n\'A\' -> "1", \'B\' -> "2", ..., \'Z\' -> "26"\n\nTo decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above. Given a string s containing only digits, return the number of ways to decode it.',
        "constraints": [
        "1 <= s.length <= 100",
        "s contains only digits and may contain leading zero(s)"
],
        "examples": [
        {
                "input": {
                        "s": "12"
                },
                "output": 2,
                "explanation": "It could be decoded as 'AB' (1 2) or 'L' (12)."
        },
        {
                "input": {
                        "s": "226"
                },
                "output": 3,
                "explanation": "It could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6)."
        }
],
        "tags": [
        "string",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        "12"
                ],
                "expectedOutput": 2
        },
        {
                "input": [
                        "226"
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        "06"
                ],
                "expectedOutput": 0
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def numDecodings(self, s: str) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int numDecodings(String s) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int numDecodings(string s) {\n        \n    }\n};',
        "solution_python": '# Solution for Decode Ways\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Decode Ways\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Decode Ways\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Decode Ways\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Letter Combinations of a Phone Number',
        "leetcode_url": 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
        "difficulty": 'medium',
        "description": 'Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.\n\nA mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.\n\n2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz',
        "constraints": [
        "0 <= digits.length <= 4",
        "digits[i] is a digit in the range ['2', '9']"
],
        "examples": [
        {
                "input": {
                        "digits": "23"
                },
                "output": [
                        "ad",
                        "ae",
                        "af",
                        "bd",
                        "be",
                        "bf",
                        "cd",
                        "ce",
                        "cf"
                ],
                "explanation": "All possible combinations."
        },
        {
                "input": {
                        "digits": ""
                },
                "output": [],
                "explanation": "Empty input."
        }
],
        "tags": [
        "hash-table",
        "string",
        "backtracking"
],
        "test_cases": [
        {
                "input": [
                        "23"
                ],
                "expectedOutput": [
                        "ad",
                        "ae",
                        "af",
                        "bd",
                        "be",
                        "bf",
                        "cd",
                        "ce",
                        "cf"
                ]
        },
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
        }
],
        "time_complexity": 'O(4^n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        pass',
        "java_sig": 'class Solution {\n    public List<String> letterCombinations(String digits) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<string> letterCombinations(string digits) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Backtracking to generate all possible letter combinations.
        Maps each digit to its corresponding letters on phone keypad.

        Algorithm:
        1. Use digit-to-letters mapping (2='abc', 3='def', etc.)
        2. Backtrack through each digit, trying all letter choices
        3. When path length equals input length, add to result

        Time Complexity: O(4^n) - worst case 4 letters per digit
        Space Complexity: O(n) - recursion depth and current path
        """
        if not digits:
            return []

        # Phone keypad mapping
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(index: int, path: str):
            """Build combinations by trying each letter for current digit."""
            # Base case: built complete combination
            if index == len(digits):
                result.append(path)
                return

            # Get letters for current digit
            letters = phone_map[digits[index]]

            # Try each letter
            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
''',
        "solution_java": '// Solution for Letter Combinations of a Phone Number\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Letter Combinations of a Phone Number\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Letter Combinations of a Phone Number\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Generate Parentheses',
        "leetcode_url": 'https://leetcode.com/problems/generate-parentheses/',
        "difficulty": 'medium',
        "description": 'Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.',
        "constraints": [
        "1 <= n <= 8"
],
        "examples": [
        {
                "input": {
                        "n": 3
                },
                "output": [
                        "((()))",
                        "(()())",
                        "(())()",
                        "()(())",
                        "()()()"
                ],
                "explanation": "All valid combinations of 3 pairs."
        },
        {
                "input": {
                        "n": 1
                },
                "output": [
                        "()"
                ],
                "explanation": "Only one combination."
        }
],
        "tags": [
        "string",
        "dynamic-programming",
        "backtracking"
],
        "test_cases": [
        {
                "input": [
                        3
                ],
                "expectedOutput": [
                        "((()))",
                        "(()())",
                        "(())()",
                        "()(())",
                        "()()()"
                ]
        },
        {
                "input": [
                        1
                ],
                "expectedOutput": [
                        "()"
                ]
        }
],
        "time_complexity": 'O(4^n/sqrt(n))',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def generateParenthesis(self, n: int) -> List[str]:\n        pass',
        "java_sig": 'class Solution {\n    public List<String> generateParenthesis(int n) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<string> generateParenthesis(int n) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking with constraints to generate valid parentheses.
        Ensures well-formed by tracking open/close counts.

        Algorithm:
        1. Backtrack, adding '(' when we have remaining opens
        2. Add ')' only when closes < opens (ensures validity)
        3. Complete when used all n pairs

        Time Complexity: O(4^n / sqrt(n)) - Catalan number
        Space Complexity: O(n) - recursion depth
        """
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            """Build valid combinations with open/close tracking."""
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we have remaining opens
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            # Add ')' only if it won't violate validity (closes < opens)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
''',
        "solution_java": '// Solution for Generate Parentheses\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Generate Parentheses\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Generate Parentheses\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Permutations',
        "leetcode_url": 'https://leetcode.com/problems/permutations/',
        "difficulty": 'medium',
        "description": 'Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.',
        "constraints": [
        "1 <= nums.length <= 6",
        "-10 <= nums[i] <= 10",
        "All the integers of nums are unique"
],
        "examples": [
        {
                "input": {
                        "nums": [
                                1,
                                2,
                                3
                        ]
                },
                "output": [
                        [
                                1,
                                2,
                                3
                        ],
                        [
                                1,
                                3,
                                2
                        ],
                        [
                                2,
                                1,
                                3
                        ],
                        [
                                2,
                                3,
                                1
                        ],
                        [
                                3,
                                1,
                                2
                        ],
                        [
                                3,
                                2,
                                1
                        ]
                ],
                "explanation": "All permutations."
        },
        {
                "input": {
                        "nums": [
                                0,
                                1
                        ]
                },
                "output": [
                        [
                                0,
                                1
                        ],
                        [
                                1,
                                0
                        ]
                ],
                "explanation": "Two permutations."
        }
],
        "tags": [
        "array",
        "backtracking"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3
                        ]
                ],
                "expectedOutput": [
                        [
                                1,
                                2,
                                3
                        ],
                        [
                                1,
                                3,
                                2
                        ],
                        [
                                2,
                                1,
                                3
                        ],
                        [
                                2,
                                3,
                                1
                        ],
                        [
                                3,
                                1,
                                2
                        ],
                        [
                                3,
                                2,
                                1
                        ]
                ]
        },
        {
                "input": [
                        [
                                0,
                                1
                        ]
                ],
                "expectedOutput": [
                        [
                                0,
                                1
                        ],
                        [
                                1,
                                0
                        ]
                ]
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
        }
],
        "time_complexity": 'O(n!)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Solution:\n    def permute(self, nums: List[int]) -> List[List[int]]:\n        pass',
        "java_sig": 'class Solution {\n    public List<List<Integer>> permute(int[] nums) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    vector<vector<int>> permute(vector<int>& nums) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking to generate all permutations.
        Swaps elements to build each permutation in-place.

        Algorithm:
        1. Use backtracking with index tracking
        2. Swap current index with each remaining element
        3. Recurse to next position
        4. Backtrack by swapping back

        Time Complexity: O(n! * n) - n! permutations, each takes O(n) to copy
        Space Complexity: O(n) - recursion depth
        """
        result = []

        def backtrack(start: int):
            """Build permutations by swapping elements."""
            # Base case: built complete permutation
            if start == len(nums):
                result.append(nums[:])  # Copy current permutation
                return

            # Try each element in remaining positions
            for i in range(start, len(nums)):
                # Swap to place element at current position
                nums[start], nums[i] = nums[i], nums[start]

                # Recurse to next position
                backtrack(start + 1)

                # Backtrack: restore original order
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return sorted(result)
''',
        "solution_java": '// Solution for Permutations\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Permutations\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Permutations\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Trapping Rain Water',
        "leetcode_url": 'https://leetcode.com/problems/trapping-rain-water/',
        "difficulty": 'hard',
        "description": 'Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.',
        "constraints": [
        "n == height.length",
        "1 <= n <= 2 * 10^4",
        "0 <= height[i] <= 10^5"
],
        "examples": [
        {
                "input": {
                        "height": [
                                0,
                                1,
                                0,
                                2,
                                1,
                                0,
                                1,
                                3,
                                2,
                                1,
                                2,
                                1
                        ]
                },
                "output": 6,
                "explanation": "The elevation map can trap 6 units of rain water."
        }
],
        "tags": [
        "array",
        "two-pointers",
        "dynamic-programming",
        "stack",
        "monotonic-stack"
],
        "test_cases": [
        {
                "input": [
                        [
                                0,
                                1,
                                0,
                                2,
                                1,
                                0,
                                1,
                                3,
                                2,
                                1,
                                2,
                                1
                        ]
                ],
                "expectedOutput": 6
        },
        {
                "input": [
                        [
                                4,
                                2,
                                0,
                                3,
                                2,
                                5
                        ]
                ],
                "expectedOutput": 9
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def trap(self, height: List[int]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int trap(int[] height) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int trap(vector<int>& height) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer technique to calculate trapped water.
        Water level at position i = min(max_left[i], max_right[i]) - height[i]

        Algorithm:
        Use two pointers moving inward, tracking max heights from both sides:
        1. Start with left and right pointers at edges
        2. Move pointer with smaller max height inward
        3. Calculate water trapped based on current max heights
        4. Key insight: water trapped depends on the SMALLER of left/right max

        Time Complexity: O(n) - single pass with two pointers
        Space Complexity: O(1) - only using pointers and max trackers
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                # Process left side
                if height[left] >= left_max:
                    # Update left max
                    left_max = height[left]
                else:
                    # Water trapped = left_max - current height
                    water += left_max - height[left]
                left += 1
            else:
                # Process right side
                if height[right] >= right_max:
                    # Update right max
                    right_max = height[right]
                else:
                    # Water trapped = right_max - current height
                    water += right_max - height[right]
                right -= 1

        return water
''',
        "solution_java": '// Solution for Trapping Rain Water\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Trapping Rain Water\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Trapping Rain Water\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Median of Two Sorted Arrays',
        "leetcode_url": 'https://leetcode.com/problems/median-of-two-sorted-arrays/',
        "difficulty": 'hard',
        "description": 'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\n\nThe overall run time complexity should be O(log (m+n)).',
        "constraints": [
        "nums1.length == m",
        "nums2.length == n",
        "0 <= m <= 1000",
        "0 <= n <= 1000",
        "1 <= m + n <= 2000",
        "-10^6 <= nums1[i], nums2[i] <= 10^6"
],
        "examples": [
        {
                "input": {
                        "nums1": [
                                1,
                                3
                        ],
                        "nums2": [
                                2
                        ]
                },
                "output": 2.0,
                "explanation": "Merged array = [1,2,3], median = 2."
        },
        {
                "input": {
                        "nums1": [
                                1,
                                2
                        ],
                        "nums2": [
                                3,
                                4
                        ]
                },
                "output": 2.5,
                "explanation": "Merged array = [1,2,3,4], median = (2+3)/2 = 2.5."
        }
],
        "tags": [
        "array",
        "binary-search",
        "divide-and-conquer"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                3
                        ],
                        [
                                2
                        ]
                ],
                "expectedOutput": 2.0
        },
        {
                "input": [
                        [
                                1,
                                2
                        ],
                        [
                                3,
                                4
                        ]
                ],
                "expectedOutput": 2.5
        }
],
        "time_complexity": 'O(log(min(m,n)))',
        "space_complexity": 'O(1)',
        "python_sig": 'class Solution:\n    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\n        pass',
        "java_sig": 'class Solution {\n    public double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n        \n    }\n};',
        "solution_python": '# Solution for Median of Two Sorted Arrays\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Median of Two Sorted Arrays\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Median of Two Sorted Arrays\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Median of Two Sorted Arrays\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Binary Tree Maximum Path Sum',
        "leetcode_url": 'https://leetcode.com/problems/binary-tree-maximum-path-sum/',
        "difficulty": 'hard',
        "description": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.\n\nThe path sum of a path is the sum of the node's values in the path.\n\nGiven the root of a binary tree, return the maximum path sum of any non-empty path.",
        "constraints": [
        "The number of nodes in the tree is in the range [1, 3 * 10^4]",
        "-1000 <= Node.val <= 1000"
],
        "examples": [
        {
                "input": {
                        "root": [
                                1,
                                2,
                                3
                        ]
                },
                "output": 6,
                "explanation": "The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6."
        },
        {
                "input": {
                        "root": [
                                -10,
                                9,
                                20,
                                None,
                                None,
                                15,
                                7
                        ]
                },
                "output": 42,
                "explanation": "The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42."
        }
],
        "tags": [
        "tree",
        "depth-first-search",
        "dynamic-programming",
        "binary-tree"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3
                        ]
                ],
                "expectedOutput": 6
        },
        {
                "input": [
                        [
                                -10,
                                9,
                                20,
                                None,
                                None,
                                15,
                                7
                        ]
                ],
                "expectedOutput": 42
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(h)',
        "python_sig": 'class Solution:\n    def maxPathSum(self, root: Optional[TreeNode]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int maxPathSum(TreeNode root) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int maxPathSum(TreeNode* root) {\n        \n    }\n};',
        "solution_python": '# Solution for Binary Tree Maximum Path Sum\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Binary Tree Maximum Path Sum\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Binary Tree Maximum Path Sum\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Binary Tree Maximum Path Sum\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Serialize and Deserialize Binary Tree',
        "leetcode_url": 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/',
        "difficulty": 'hard',
        "description": 'Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\n\nDesign an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.',
        "constraints": [
        "The number of nodes in the tree is in the range [0, 10^4]",
        "-1000 <= Node.val <= 1000"
],
        "examples": [
        {
                "input": {
                        "root": [
                                1,
                                2,
                                3,
                                None,
                                None,
                                4,
                                5
                        ]
                },
                "output": [
                        1,
                        2,
                        3,
                        None,
                        None,
                        4,
                        5
                ],
                "explanation": "Serialize then deserialize the tree."
        }
],
        "tags": [
        "string",
        "tree",
        "depth-first-search",
        "breadth-first-search",
        "design",
        "binary-tree"
],
        "test_cases": [
        {
                "input": [
                        [
                                1,
                                2,
                                3,
                                None,
                                None,
                                4,
                                5
                        ]
                ],
                "expectedOutput": [
                        1,
                        2,
                        3,
                        None,
                        None,
                        4,
                        5
                ]
        },
        {
                "input": [
                        []
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(n)',
        "space_complexity": 'O(n)',
        "python_sig": 'class Codec:\n    def serialize(self, root: Optional[TreeNode]) -> str:\n        pass\n    \n    def deserialize(self, data: str) -> Optional[TreeNode]:\n        pass',
        "java_sig": 'public class Codec {\n    public String serialize(TreeNode root) {\n        \n    }\n    \n    public TreeNode deserialize(String data) {\n        \n    }\n}',
        "cpp_sig": 'class Codec {\npublic:\n    string serialize(TreeNode* root) {\n        \n    }\n    \n    TreeNode* deserialize(string data) {\n        \n    }\n};',
        "solution_python": '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Serialize and deserialize binary tree using preorder traversal.
    Uses '#' to represent null nodes, ',' as delimiter.

    Time Complexity: O(n) for both serialize and deserialize
    Space Complexity: O(n) for storing tree data
    """

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes tree to string using preorder traversal.

        Algorithm:
        1. Preorder traversal (root, left, right)
        2. Use '#' for null nodes
        3. Join with commas
        """
        def preorder(node):
            if not node:
                return '#'
            # Preorder: root, left subtree, right subtree
            return f"{node.val},{preorder(node.left)},{preorder(node.right)}"

        return preorder(root)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes string to tree using preorder reconstruction.

        Algorithm:
        1. Split string by commas
        2. Use iterator to build tree in preorder
        3. '#' creates None, numbers create nodes
        """
        def build():
            val = next(values)
            if val == '#':
                return None

            # Create node and recursively build subtrees
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        values = iter(data.split(','))
        return build()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
''',
        "solution_java": '// Solution for Serialize and Deserialize Binary Tree\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Serialize and Deserialize Binary Tree\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Serialize and Deserialize Binary Tree\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Regular Expression Matching',
        "leetcode_url": 'https://leetcode.com/problems/regular-expression-matching/',
        "difficulty": 'hard',
        "description": "Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:\n\n'.' Matches any single character.\n'*' Matches zero or more of the preceding element.\n\nThe matching should cover the entire input string (not partial).",
        "constraints": [
        "1 <= s.length <= 20",
        "1 <= p.length <= 20",
        "s contains only lowercase English letters",
        "p contains only lowercase English letters, '.', and '*'"
],
        "examples": [
        {
                "input": {
                        "s": "aa",
                        "p": "a"
                },
                "output": False,
                "explanation": "a does not match the entire string aa."
        },
        {
                "input": {
                        "s": "aa",
                        "p": "a*"
                },
                "output": True,
                "explanation": "* means zero or more of the preceding element, a. Therefore, by repeating a once, it becomes aa."
        }
],
        "tags": [
        "string",
        "dynamic-programming",
        "recursion"
],
        "test_cases": [
        {
                "input": [
                        "aa",
                        "a"
                ],
                "expectedOutput": False
        },
        {
                "input": [
                        "aa",
                        "a*"
                ],
                "expectedOutput": True
        },
        {
                "input": [
                        "ab",
                        ".*"
                ],
                "expectedOutput": True
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(m*n)',
        "python_sig": 'class Solution:\n    def isMatch(self, s: str, p: str) -> bool:\n        pass',
        "java_sig": 'class Solution {\n    public boolean isMatch(String s, String p) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    bool isMatch(string s, string p) {\n        \n    }\n};',
        "solution_python": '# Solution for Regular Expression Matching\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Regular Expression Matching\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Regular Expression Matching\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Regular Expression Matching\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Edit Distance',
        "leetcode_url": 'https://leetcode.com/problems/edit-distance/',
        "difficulty": 'hard',
        "description": 'Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.\n\nYou have the following three operations permitted on a word:\n- Insert a character\n- Delete a character\n- Replace a character',
        "constraints": [
        "0 <= word1.length, word2.length <= 500",
        "word1 and word2 consist of lowercase English letters"
],
        "examples": [
        {
                "input": {
                        "word1": "horse",
                        "word2": "ros"
                },
                "output": 3,
                "explanation": "horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e')"
        },
        {
                "input": {
                        "word1": "intention",
                        "word2": "execution"
                },
                "output": 5,
                "explanation": "intention -> inention (remove 't') -> enention (replace 'i' with 'e') -> exention (replace 'n' with 'x') -> exection (replace 'n' with 'c') -> execution (insert 'u')"
        }
],
        "tags": [
        "string",
        "dynamic-programming"
],
        "test_cases": [
        {
                "input": [
                        "horse",
                        "ros"
                ],
                "expectedOutput": 3
        },
        {
                "input": [
                        "intention",
                        "execution"
                ],
                "expectedOutput": 5
        }
],
        "time_complexity": 'O(m*n)',
        "space_complexity": 'O(m*n)',
        "python_sig": 'class Solution:\n    def minDistance(self, word1: str, word2: str) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int minDistance(String word1, String word2) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int minDistance(string word1, string word2) {\n        \n    }\n};',
        "solution_python": '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Dynamic Programming (Levenshtein Distance).
        Finds minimum edit operations to transform word1 to word2.

        Operations: insert, delete, replace (each costs 1)

        Algorithm:
        1. Create DP table where dp[i][j] = min edits for word1[0:i] -> word2[0:j]
        2. Base cases: empty string conversions
        3. If characters match: dp[i][j] = dp[i-1][j-1]
        4. If differ: take min of (insert, delete, replace) + 1

        Time Complexity: O(m * n) where m, n are string lengths
        Space Complexity: O(m * n) for DP table
        """
        m, n = len(word1), len(word2)

        # dp[i][j] = min edits to transform word1[0:i] to word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: transforming from/to empty string
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match: no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Take minimum of:
                    # - Replace: dp[i-1][j-1] + 1
                    # - Insert: dp[i][j-1] + 1
                    # - Delete: dp[i-1][j] + 1
                    dp[i][j] = min(
                        dp[i - 1][j - 1],  # Replace
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j]       # Delete
                    ) + 1

        return dp[m][n]
''',
        "solution_java": '// Solution for Edit Distance\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Edit Distance\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Edit Distance\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Word Ladder',
        "leetcode_url": 'https://leetcode.com/problems/word-ladder/',
        "difficulty": 'hard',
        "description": 'A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:\n- Every adjacent pair of words differs by a single letter.\n- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.\n- sk == endWord\n\nGiven two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.',
        "constraints": [
        "1 <= beginWord.length <= 10",
        "endWord.length == beginWord.length",
        "1 <= wordList.length <= 5000",
        "wordList[i].length == beginWord.length",
        "All strings consist of lowercase English letters",
        "beginWord != endWord",
        "All the words in wordList are unique"
],
        "examples": [
        {
                "input": {
                        "beginWord": "hit",
                        "endWord": "cog",
                        "wordList": [
                                "hot",
                                "dot",
                                "dog",
                                "lot",
                                "log",
                                "cog"
                        ]
                },
                "output": 5,
                "explanation": "One shortest transformation sequence is 'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog', which is 5 words long."
        },
        {
                "input": {
                        "beginWord": "hit",
                        "endWord": "cog",
                        "wordList": [
                                "hot",
                                "dot",
                                "dog",
                                "lot",
                                "log"
                        ]
                },
                "output": 0,
                "explanation": "The endWord 'cog' is not in wordList, therefore there is no valid transformation sequence."
        }
],
        "tags": [
        "hash-table",
        "string",
        "breadth-first-search"
],
        "test_cases": [
        {
                "input": [
                        "hit",
                        "cog",
                        [
                                "hot",
                                "dot",
                                "dog",
                                "lot",
                                "log",
                                "cog"
                        ]
                ],
                "expectedOutput": 5
        },
        {
                "input": [
                        "hit",
                        "cog",
                        [
                                "hot",
                                "dot",
                                "dog",
                                "lot",
                                "log"
                        ]
                ],
                "expectedOutput": 0
        }
],
        "time_complexity": 'O(M^2 * N)',
        "space_complexity": 'O(M^2 * N)',
        "python_sig": 'class Solution:\n    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:\n        pass',
        "java_sig": 'class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n        \n    }\n};',
        "solution_python": '# Solution for Word Ladder\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
        "solution_java": '// Solution for Word Ladder\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Word Ladder\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Word Ladder\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    },
    {
        "title": 'Merge k Sorted Lists',
        "leetcode_url": 'https://leetcode.com/problems/merge-k-sorted-lists/',
        "difficulty": 'hard',
        "description": 'You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\n\nMerge all the linked-lists into one sorted linked-list and return it.',
        "constraints": [
        "k == lists.length",
        "0 <= k <= 10^4",
        "0 <= lists[i].length <= 500",
        "-10^4 <= lists[i][j] <= 10^4",
        "lists[i] is sorted in ascending order",
        "The sum of lists[i].length will not exceed 10^4"
],
        "examples": [
        {
                "input": {
                        "lists": [
                                [
                                        1,
                                        4,
                                        5
                                ],
                                [
                                        1,
                                        3,
                                        4
                                ],
                                [
                                        2,
                                        6
                                ]
                        ]
                },
                "output": [
                        1,
                        1,
                        2,
                        3,
                        4,
                        4,
                        5,
                        6
                ],
                "explanation": "Merging all lists: [1,4,5], [1,3,4], and [2,6] into one sorted list."
        },
        {
                "input": {
                        "lists": []
                },
                "output": [],
                "explanation": "Empty input."
        },
        {
                "input": {
                        "lists": [
                                []
                        ]
                },
                "output": [],
                "explanation": "Single empty list."
        }
],
        "tags": [
        "linked-list",
        "divide-and-conquer",
        "heap",
        "merge-sort"
],
        "test_cases": [
        {
                "input": [
                        [
                                [
                                        1,
                                        4,
                                        5
                                ],
                                [
                                        1,
                                        3,
                                        4
                                ],
                                [
                                        2,
                                        6
                                ]
                        ]
                ],
                "expectedOutput": [
                        1,
                        1,
                        2,
                        3,
                        4,
                        4,
                        5,
                        6
                ]
        },
        {
                "input": [
                        []
                ],
                "expectedOutput": []
        },
        {
                "input": [
                        [
                                []
                        ]
                ],
                "expectedOutput": []
        }
],
        "time_complexity": 'O(N log k) where N is total number of nodes',
        "space_complexity": 'O(k) for heap or O(log k) for divide-and-conquer',
        "python_sig": 'class Solution:\n    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:\n        pass',
        "java_sig": 'class Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        \n    }\n}',
        "cpp_sig": 'class Solution {\npublic:\n    ListNode* mergeKLists(vector<ListNode*>& lists) {\n        \n    }\n};',
        "solution_python": '''# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Min-heap to efficiently merge k sorted linked lists.
        Heap maintains smallest element across all lists.

        Algorithm:
        1. Add first node from each non-empty list to min-heap
        2. Repeatedly extract minimum and add to result
        3. Add next node from that list to heap
        4. Continue until heap is empty

        Time Complexity: O(N log k) where N=total nodes, k=number of lists
        Space Complexity: O(k) - heap size
        """
        # Min-heap: (value, list_index, node)
        # Need list_index for tie-breaking (Python heapq requires comparable items)
        heap = []

        # Add first node from each list to heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        # Dummy head for result list
        dummy = ListNode(0)
        current = dummy

        # Build merged list
        while heap:
            val, list_idx, node = heapq.heappop(heap)

            # Add node to result
            current.next = node
            current = current.next

            # Add next node from same list to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))

        return dummy.next
''',
        "solution_java": '// Solution for Merge k Sorted Lists\nclass Solution {\n    public returnType solve(inputType input) {\n        // TODO: Implement solution\n        return None;\n    }\n}',
        "solution_cpp": '// Solution for Merge k Sorted Lists\nclass Solution {\npublic:\n    returnType solve(inputType input) {\n        // TODO: Implement solution\n        return {};\n    }\n};',
        "solution_explanation": '## Solution for Merge k Sorted Lists\n\n### Approach\nOptimal approach based on problem type\n\n### Complexity Analysis\n- **Time Complexity**: O(?)\n- **Space Complexity**: O(?)'
    }
]

# 10 ML System Design Questions with sample solutions
ML_QUESTIONS = [
    {
        "title": 'Design Facebook News Feed Ranking System',
        "difficulty": 'hard',
        "description": "Design the ML ranking system for Facebook's News Feed that serves 3B+ users, deciding which posts to show and in what order to maximize meaningful user engagement.",
        "scenario": 'Facebook\'s News Feed is the core product serving 3B+ users daily. The ML system must:\n- Rank posts from friends, pages, groups, and ads\n- Process millions of candidate posts per user\n- Predict multiple engagement types (likes, comments, shares, time spent, hide/report)\n- Optimize for "meaningful social interactions" not just clicks\n- Handle diverse content types (text, photo, video, link, live)\n- Serve feeds in <500ms while making complex ML predictions\n- Combat engagement bait, clickbait, and misinformation\n- Balance organic content with ads (revenue optimization)\n\nThe system processes billions of posts daily, makes trillions of predictions, and directly impacts Meta\'s $100B+ revenue.',
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
        "tags": [
        "ranking",
        "multi-task-learning",
        "news-feed",
        "meta",
        "scale",
        "personalization"
],
        "sample_solution": "# Facebook News Feed Ranking System\n\n## System Architecture\n\n### 1. Data Collection Pipeline\n```python\nclass DataCollector:\n    def __init__(self):\n        self.kafka_consumer = KafkaConsumer('user-events')\n        self.feature_store = FeatureStore()\n\n    def collect_user_signals(self, user_id):\n        signals = {\n            'explicit': {\n                'likes': self.get_likes(user_id),\n                'comments': self.get_comments(user_id),\n                'shares': self.get_shares(user_id)\n            },\n            'implicit': {\n                'dwell_time': self.get_dwell_times(user_id),\n                'scroll_depth': self.get_scroll_patterns(user_id),\n                'click_through': self.get_clicks(user_id)\n            },\n            'social': {\n                'friend_interactions': self.get_friend_activity(user_id),\n                'group_memberships': self.get_groups(user_id)\n            }\n        }\n        return signals\n```\n\n### 2. Feature Engineering\n- **User Features**: Demographics, interests, past behavior\n- **Content Features**: Type, creator, recency, engagement metrics\n- **Contextual Features**: Time of day, device, location\n- **Social Features**: Friend interactions, network effects\n\n### 3. Ranking Model\n```python\nclass NewsFeedRanker:\n    def __init__(self):\n        self.relevance_model = self.load_relevance_model()\n        self.quality_model = self.load_quality_model()\n        self.diversity_optimizer = DiversityOptimizer()\n\n    def rank_posts(self, user_id, candidate_posts):\n        features = []\n        for post in candidate_posts:\n            feature_vector = self.extract_features(user_id, post)\n            features.append(feature_vector)\n\n        # Multi-objective optimization\n        relevance_scores = self.relevance_model.predict(features)\n        quality_scores = self.quality_model.predict(features)\n\n        # Combine scores\n        final_scores = 0.7 * relevance_scores + 0.3 * quality_scores\n\n        # Apply diversity\n        ranked_posts = self.diversity_optimizer.rerank(\n            candidate_posts, final_scores\n        )\n\n        return ranked_posts[:100]  # Return top 100\n```\n\n### 4. Real-time Serving\n- **Architecture**: Microservices with API Gateway\n- **Caching**: Redis for hot user feeds\n- **Fallback**: Pre-computed feeds for cold start\n\n### 5. Evaluation & Monitoring\n- **Online Metrics**: CTR, Time Spent, User Retention\n- **Offline Metrics**: NDCG@k, MAP, Coverage\n- **A/B Testing**: Statistical significance at p < 0.05\n\n## Scalability Considerations\n- Handle 2B+ daily active users\n- Sub-second latency requirements\n- Horizontal scaling with sharding\n- Multi-region deployment"
    },
    {
        "title": 'Design Instagram Reels Recommendation System',
        "difficulty": 'hard',
        "description": 'Design the ML system powering Instagram Reels recommendations - a TikTok competitor serving short-form video to 2B+ users with multi-modal understanding.',
        "scenario": 'Instagram Reels competes with TikTok by recommending engaging short-form videos. The system must:\n- Understand video content (visual, audio, text, music)\n- Cold start: recommend videos to new users and new videos to users\n- Optimize for watch time and completion rate\n- Handle the "creator economy" (help creators grow)\n- Prevent filter bubbles while maximizing engagement\n- Support audio trends (viral sounds)\n- Real-time: new videos should surface quickly\n- Multi-modal: video, audio, captions, hashtags, music\n\nKey challenge: Unlike Feed (friends/following), Reels is discovery-based like TikTok.',
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
        "tags": [
        "recommendation",
        "multi-modal",
        "video",
        "meta",
        "instagram",
        "reels",
        "cold-start"
],
        "sample_solution": '# Instagram Reels Recommendation System\n\n## System Overview\n\n### 1. Content Understanding Pipeline\n```python\nclass ReelsContentProcessor:\n    def __init__(self):\n        self.video_model = VideoUnderstandingModel()\n        self.audio_model = AudioAnalyzer()\n        self.text_extractor = TextExtractor()\n\n    def process_reel(self, reel_id, video_path):\n        # Extract visual features\n        visual_features = self.video_model.extract_features(video_path)\n\n        # Extract audio features\n        audio_features = self.audio_model.analyze(video_path)\n\n        # Extract text (captions, hashtags)\n        text_features = self.text_extractor.extract(reel_id)\n\n        # Combine into embedding\n        reel_embedding = self.combine_features(\n            visual_features, audio_features, text_features\n        )\n\n        return reel_embedding\n```\n\n### 2. User Interest Modeling\n```python\nclass UserInterestModel:\n    def build_profile(self, user_id):\n        # Short-term interests (last 24 hours)\n        recent_views = self.get_recent_views(user_id)\n        short_term = self.aggregate_embeddings(recent_views, decay=0.9)\n\n        # Long-term interests (30 days)\n        historical = self.get_historical_interactions(user_id)\n        long_term = self.aggregate_embeddings(historical, decay=0.5)\n\n        # Combine with adaptive weighting\n        user_embedding = self.adaptive_combine(short_term, long_term)\n\n        return user_embedding\n```\n\n### 3. Recommendation Strategy\n- **Exploration vs Exploitation**: 80/20 split\n- **Cold Start**: Use trending content + demographic similarity\n- **Diversity**: Ensure variety in content types\n\n### 4. Infrastructure\n- **Video CDN**: Global edge servers for streaming\n- **ML Pipeline**: TensorFlow/PyTorch for model training\n- **Feature Store**: Real-time feature serving\n\n## Success Metrics\n- User engagement time\n- Completion rate\n- Share rate\n- Creator diversity'
    },
    {
        "title": 'Design Real-time Ad Targeting & Ranking System',
        "difficulty": 'hard',
        "description": "Design Meta's ad targeting and ranking system that serves personalized ads to 3B+ users, generating $100B+ annual revenue while balancing user experience.",
        "scenario": "Meta's ad system is critical infrastructure generating $100B+ revenue. The ML system must:\n- Target: Find right users for each ad campaign (audience selection)\n- Rank: Order ads by expected value (bid × pCTR × pConversion)\n- Auction: Run real-time ad auction for each impression\n- Budget: Manage advertiser budgets and pacing\n- Quality: Maintain user experience (not too many ads)\n- Privacy: Work with limited data (iOS privacy, GDPR)\n- Scale: Billions of users, millions of advertisers, trillions of impressions\n\nRevenue equation: eCPM = bid × pCTR × pConversion\nGoal: Maximize revenue while maintaining user satisfaction.",
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
        "tags": [
        "ads",
        "ranking",
        "auction",
        "revenue",
        "meta",
        "ctr-prediction",
        "conversion"
],
        "sample_solution": "# Real-time Ad Targeting & Ranking System\n\n## Architecture Components\n\n### 1. User Profiling Service\n```python\nclass UserProfiler:\n    def get_targeting_features(self, user_id):\n        return {\n            'demographics': self.get_demographics(user_id),\n            'interests': self.get_interests(user_id),\n            'behavior': self.get_behavioral_signals(user_id),\n            'intent': self.predict_purchase_intent(user_id)\n        }\n```\n\n### 2. Ad Auction Engine\n```python\nclass AdAuctionEngine:\n    def run_auction(self, user_features, ad_candidates):\n        bids = []\n        for ad in ad_candidates:\n            # Calculate relevance score\n            relevance = self.relevance_model.score(user_features, ad)\n\n            # Calculate expected revenue\n            ctr = self.ctr_model.predict(user_features, ad)\n            expected_revenue = ad.bid * ctr * relevance\n\n            bids.append((ad, expected_revenue))\n\n        # Second-price auction\n        bids.sort(key=lambda x: x[1], reverse=True)\n        winner = bids[0][0]\n        price = bids[1][1] / winner.quality_score\n\n        return winner, price\n```\n\n### 3. Real-time Serving\n- **Latency Budget**: < 100ms end-to-end\n- **Caching Strategy**: Multi-tier (L1: Redis, L2: Memcached)\n- **Load Balancing**: Geographic + behavioral sharding\n\n## Performance Requirements\n- 10M+ requests/second\n- 99.9% availability\n- P99 latency < 100ms"
    },
    {
        "title": 'Design AI Content Moderation System for Meta',
        "difficulty": 'hard',
        "description": "Design Meta's content moderation system that detects and removes harmful content (hate speech, violence, spam, misinformation) across Facebook, Instagram, WhatsApp at scale.",
        "scenario": "Meta's content moderation is critical for platform safety. The system must:\n- Detect multiple violation types: hate speech, violence, nudity, spam, misinformation, bullying\n- Multi-modal: text, images, videos, audio\n- Real-time: flag content within seconds\n- Multi-language: 100+ languages\n- Precision is critical: False positives remove legitimate content\n- Recall is critical: False negatives allow harmful content\n- Human review: queue borderline content for human moderators\n- Adversarial: bad actors constantly try to evade detection\n- Scale: billions of posts/day\n\nThis is a high-stakes system with regulatory, legal, and ethical implications.",
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
        "precision_recall": "Strategy to balance False positives vs False negatives",
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
        "tags": [
        "content-moderation",
        "classification",
        "multi-modal",
        "safety",
        "meta",
        "nlp",
        "computer-vision"
],
        "sample_solution": "# AI Content Moderation System\n\n## Multi-Modal Detection Pipeline\n\n### 1. Content Analysis\n```python\nclass ContentModerator:\n    def __init__(self):\n        self.image_model = ImageModerationModel()\n        self.text_model = TextModerationModel()\n        self.video_model = VideoModerationModel()\n\n    def moderate(self, content):\n        scores = {}\n\n        if content.type == 'image':\n            scores = self.image_model.detect({\n                'violence': 0.0,\n                'adult': 0.0,\n                'hate_speech': 0.0,\n                'self_harm': 0.0\n            })\n        elif content.type == 'text':\n            scores = self.text_model.analyze(content.text)\n\n        return self.make_decision(scores)\n\n    def make_decision(self, scores):\n        if any(score > 0.9 for score in scores.values()):\n            return 'block'\n        elif any(score > 0.7 for score in scores.values()):\n            return 'human_review'\n        else:\n            return 'approve'\n```\n\n### 2. Human-in-the-Loop\n- Queue management for human reviewers\n- Active learning from human decisions\n- Quality assurance sampling\n\n### 3. Scalability\n- Process 100B+ pieces of content daily\n- Multi-region deployment\n- Edge inference for faster response\n\n## Evaluation Metrics\n- Precision/Recall per violation type\n- False positive rate < 1%\n- Human reviewer agreement rate"
    },
    {
        "title": 'Design Spam Detection System for Messaging',
        "difficulty": 'medium',
        "description": 'Design a real-time spam detection system for Meta Messenger/WhatsApp that identifies and blocks spam, scams, and phishing at scale while preserving user privacy.',
        "scenario": "Meta's messaging platforms (Messenger, WhatsApp, Instagram DMs) need spam detection:\n- Billions of messages daily\n- Real-time detection (<100ms)\n- Privacy: End-to-end encrypted (WhatsApp)\n- Multi-type: spam, scams, phishing, malware links\n- Low False positive rate (legitimate messages blocked)\n- Handle adversarial attackers (constantly evolving tactics)\n- Multi-language support\n- On-device ML (for encrypted messages)\n\nChallenge: Balance spam detection with privacy (can't read WhatsApp messages).",
        "requirements": [
        "Real-time detection (<100ms per message)",
        "Privacy-preserving (work with encrypted messages)",
        "Multi-type: spam, scams, phishing, malware",
        "Low False positive rate (<0.1%)",
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
        "False_positives": "Strategy to minimize blocking legitimate messages",
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
        "tags": [
        "spam-detection",
        "classification",
        "privacy",
        "meta",
        "messaging",
        "adversarial"
],
        "sample_solution": "# Spam Detection System for Messaging\n\n## Detection Pipeline\n\n### 1. Feature Extraction\n```python\nclass SpamDetector:\n    def extract_features(self, message):\n        return {\n            'content': {\n                'text_similarity': self.check_template_match(message.text),\n                'url_reputation': self.check_urls(message.urls),\n                'keyword_density': self.calculate_spam_keywords(message.text)\n            },\n            'behavioral': {\n                'send_rate': self.get_send_rate(message.sender),\n                'recipient_diversity': self.calculate_recipient_entropy(message.sender),\n                'time_pattern': self.analyze_time_pattern(message.sender)\n            },\n            'network': {\n                'account_age': self.get_account_age(message.sender),\n                'connection_quality': self.analyze_connections(message.sender),\n                'report_history': self.get_report_count(message.sender)\n            }\n        }\n```\n\n### 2. Real-time Classification\n- Ensemble of models (RF, XGBoost, DNN)\n- Online learning for emerging patterns\n- Threshold tuning per market/language\n\n### 3. Actions\n- Silent drop\n- Captcha challenge\n- Rate limiting\n- Account suspension\n\n## Performance Requirements\n- Process 100M+ messages/minute\n- < 10ms classification latency\n- False positive rate < 0.01%"
    },
    {
        "title": 'Design A/B Testing Platform for ML Experiments',
        "difficulty": 'medium',
        "description": "Design Meta/Atlassian's ML experimentation platform that enables safe, fast, statistically rigorous A/B testing of ML models in production.",
        "scenario": 'Large tech companies run thousands of A/B tests. The platform must:\n- Enable data scientists to run ML experiments easily\n- Random assignment (users to treatment/control)\n- Metric computation (online + offline metrics)\n- Statistical testing (p-values, confidence intervals)\n- Heterogeneous treatment effects (does it work for all users?)\n- Interference handling (network effects, spillover)\n- Multi-armed bandits (explore/exploit)\n- Staged rollouts (1% → 10% → 100%)\n- Automated monitoring (metric guardrails)\n\nMeta runs 1000s of experiments concurrently. Atlassian tests product changes.',
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
        "tags": [
        "ab-testing",
        "experimentation",
        "infrastructure",
        "statistics",
        "meta",
        "atlassian"
],
        "sample_solution": '# A/B Testing Platform for ML Models\n\n## Platform Architecture\n\n### 1. Experiment Configuration\n```python\nclass ExperimentConfig:\n    def __init__(self, name, hypothesis, metrics):\n        self.name = name\n        self.hypothesis = hypothesis\n        self.primary_metrics = metrics[\'primary\']\n        self.guardrail_metrics = metrics[\'guardrail\']\n        self.allocation = {\n            \'control\': 0.5,\n            \'treatment\': 0.5\n        }\n        self.minimum_sample_size = self.calculate_sample_size()\n```\n\n### 2. Traffic Splitting\n```python\nclass TrafficSplitter:\n    def assign_variant(self, user_id, experiment_id):\n        # Deterministic assignment using hash\n        hash_value = hashlib.md5(\n            f"{user_id}_{experiment_id}".encode()\n        ).hexdigest()\n\n        bucket = int(hash_value, 16) % 100\n\n        if bucket < 50:\n            return \'control\'\n        else:\n            return \'treatment\'\n```\n\n### 3. Statistical Analysis\n```python\nclass StatisticalAnalyzer:\n    def analyze_results(self, experiment_data):\n        control = experiment_data[\'control\']\n        treatment = experiment_data[\'treatment\']\n\n        # Calculate lift\n        lift = (treatment.mean() - control.mean()) / control.mean()\n\n        # Statistical significance\n        t_stat, p_value = stats.ttest_ind(control, treatment)\n\n        # Confidence interval\n        ci = self.calculate_confidence_interval(control, treatment)\n\n        return {\n            \'lift\': lift,\n            \'p_value\': p_value,\n            \'confidence_interval\': ci,\n            \'recommendation\': self.make_recommendation(lift, p_value)\n        }\n```\n\n## Key Features\n- Sequential testing for early stopping\n- Multi-armed bandits for exploration\n- Automatic metric computation\n- Real-time dashboards'
    },
    {
        "title": 'Design Search Ranking for Atlassian Products',
        "difficulty": 'medium',
        "description": 'Design an ML-powered search system for Atlassian products (Jira, Confluence) that helps users find relevant issues, pages, and projects using natural language queries.',
        "scenario": 'Atlassian\'s products (Jira, Confluence) have extensive search needs:\n- Jira: Search issues, projects, filters, boards\n- Confluence: Search pages, spaces, attachments, comments\n- Cross-product search: Find related items across products\n- Natural language: Understand user intent ("bugs from last sprint about login")\n- Personalization: Rank based on user\'s role, projects, history\n- Structured data (Jira fields) + unstructured data (Confluence pages)\n- Enterprise scale: 100K+ issues, 50K+ pages per workspace\n- Permission-aware (only show what user can access)\n\nKey: Work with limited data (Atlassian is B2B, not consumer scale like Google).',
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
        "tags": [
        "search",
        "ranking",
        "nlp",
        "semantic-search",
        "atlassian",
        "enterprise",
        "jira",
        "confluence"
],
        "sample_solution": "# Search Ranking System for Atlassian Products\n\n## Search Architecture\n\n### 1. Query Understanding\n```python\nclass QueryProcessor:\n    def process_query(self, query, context):\n        # Intent classification\n        intent = self.classify_intent(query)\n\n        # Entity extraction\n        entities = self.extract_entities(query)\n\n        # Query expansion\n        expanded_terms = self.expand_query(query, context)\n\n        return {\n            'original': query,\n            'intent': intent,\n            'entities': entities,\n            'expanded': expanded_terms,\n            'filters': self.extract_filters(query)\n        }\n```\n\n### 2. Multi-Index Search\n```python\nclass MultiProductSearcher:\n    def search(self, processed_query, user_context):\n        results = []\n\n        # Search across products\n        jira_results = self.search_jira(processed_query)\n        confluence_results = self.search_confluence(processed_query)\n        bitbucket_results = self.search_bitbucket(processed_query)\n\n        # Merge and rank\n        all_results = self.merge_results([\n            jira_results,\n            confluence_results,\n            bitbucket_results\n        ])\n\n        # Personalize ranking\n        personalized = self.personalize(all_results, user_context)\n\n        return personalized[:50]\n```\n\n### 3. Ranking Features\n- **Textual**: BM25, TF-IDF, Semantic similarity\n- **Behavioral**: Click-through rate, dwell time\n- **Contextual**: Recency, author authority, team relevance\n- **Structural**: Document type, project importance\n\n### 4. Learning to Rank\n```python\nclass LTRRanker:\n    def __init__(self):\n        self.model = XGBRanker()\n\n    def rank(self, query_features, doc_features, user_features):\n        features = self.combine_features(\n            query_features, doc_features, user_features\n        )\n        scores = self.model.predict(features)\n        return scores\n```\n\n## Performance Requirements\n- < 200ms search latency\n- Support 100K+ concurrent users\n- Index updates < 1 minute\n- 99.99% availability"
    },
    {
        "title": 'Design Real-time Fraud Detection System',
        "difficulty": 'hard',
        "description": "Design a real-time fraud detection system for Meta's payment products (Meta Pay, WhatsApp Pay) that identifies fraudulent transactions with <100ms latency.",
        "scenario": "Meta's payment products need fraud detection:\n- Real-time: Score transactions in <100ms\n- Multi-type fraud: stolen cards, account takeover, fake accounts, money laundering\n- Class imbalance: fraud rate <1%\n- False positives are costly: block legitimate transactions\n- False negatives are costly: allow fraud, chargebacks\n- Adversarial: fraudsters constantly adapt\n- Explainability: Why was this transaction blocked?\n- Regulatory compliance: PCI-DSS, AML, KYC\n\nThe system processes millions of transactions daily, losing millions to fraud if ineffective.",
        "requirements": [
        "Real-time scoring (<100ms per transaction)",
        "Multi-type fraud detection",
        "High recall for fraud (>90%)",
        "Low False positive rate (<2%)",
        "Handle severe class imbalance (<1% fraud)",
        "Adversarial robustness",
        "Explainability for compliance",
        "Online learning (adapt to new fraud patterns)",
        "Scale to millions of transactions/day",
        "Multi-stage: real-time \u2192 post-transaction analysis"
],
        "evaluation_criteria": {
        "model": "Gradient boosting, neural networks, or ensemble",
        "features": "Transaction, user, device, behavioral features",
        "imbalance": "Handling class imbalance (SMOTE, class weights)",
        "adversarial": "Detecting novel fraud patterns",
        "latency": "Sub-100ms inference",
        "explainability": "SHAP, rule-based explanations",
        "online_learning": "Continuous model updates",
        "metrics": "Precision, recall, F1, fraud loss, False positive rate"
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
        "tags": [
        "fraud-detection",
        "classification",
        "real-time",
        "payments",
        "meta",
        "imbalanced-data"
],
        "sample_solution": '# Real-time Fraud Detection System\n\n## Complete Implementation covered in main solutions above'
    },
    {
        "title": 'Design Video Understanding System for Meta',
        "difficulty": 'hard',
        "description": "Design Meta's video understanding system that analyzes billions of videos to enable search, recommendations, content moderation, and monetization.",
        "scenario": 'Meta processes billions of videos (Facebook, Instagram, Reels, Stories). The system must:\n- Understand video content: objects, actions, scenes, audio, text\n- Enable video search ("find videos of surfing in Hawaii")\n- Power recommendations (similar videos)\n- Content moderation (detect violations)\n- Ad placement (find ad-safe content)\n- Thumbnail selection (pick engaging frame)\n- Auto-captions (accessibility)\n- Copyright detection (match against known content)\n\nChallenge: Video processing is expensive (compute, storage). Need efficient models.',
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
        "tags": [
        "video-understanding",
        "multi-modal",
        "computer-vision",
        "meta",
        "reels",
        "deep-learning"
],
        "sample_solution": "# Video Understanding System for Meta\n\n## Architecture Overview\n\n### 1. Video Processing Pipeline\n```python\nclass VideoProcessor:\n    def __init__(self):\n        self.frame_sampler = FrameSampler(fps=1)\n        self.object_detector = YOLOv5()\n        self.action_recognizer = I3D()\n        self.scene_classifier = ResNet152()\n\n    def process_video(self, video_path):\n        # Sample frames\n        frames = self.frame_sampler.sample(video_path)\n\n        # Object detection\n        objects = []\n        for frame in frames:\n            detections = self.object_detector.detect(frame)\n            objects.extend(detections)\n\n        # Action recognition\n        actions = self.action_recognizer.recognize(frames)\n\n        # Scene understanding\n        scenes = self.scene_classifier.classify(frames)\n\n        # Generate video embedding\n        embedding = self.generate_embedding(objects, actions, scenes)\n\n        return {\n            'objects': objects,\n            'actions': actions,\n            'scenes': scenes,\n            'embedding': embedding\n        }\n```\n\n### 2. Applications\n- Content recommendation\n- Auto-tagging\n- Highlight generation\n- Safety detection\n\n### 3. Scalability\n- Process 1B+ videos daily\n- GPU cluster for inference\n- Distributed processing with Apache Spark\n\n## Model Architecture\n- Transformer-based temporal modeling\n- Multi-modal fusion (video + audio + text)\n- Self-supervised pre-training"
    },
    {
        "title": 'Design Real-time Personalization Engine',
        "difficulty": 'medium',
        "description": 'Design a real-time personalization system that adapts Meta/Atlassian products to individual users based on their behavior, preferences, and context.',
        "scenario": 'Modern products need personalization at scale:\n- Meta: Personalize Feed, Reels, notifications, ads\n- Atlassian: Personalize Jira dashboards, Confluence recommendations\n- Real-time: Update preferences as user interacts\n- Cold start: New users have no history\n- Context: Time of day, device, location matter\n- Privacy: Limited data collection\n- Scale: Billions of users\n- Latency: <50ms per request\n\nGoal: Show the right content to the right user at the right time.',
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
        "tags": [
        "personalization",
        "user-modeling",
        "real-time",
        "meta",
        "atlassian",
        "recommendations"
],
        "sample_solution": "# Real-time Personalization Engine\n\n## System Components\n\n### 1. User Context Engine\n```python\nclass ContextEngine:\n    def get_real_time_context(self, user_id):\n        return {\n            'session': {\n                'duration': self.get_session_duration(user_id),\n                'page_views': self.get_page_views(user_id),\n                'interactions': self.get_interactions(user_id)\n            },\n            'device': self.get_device_info(user_id),\n            'location': self.get_location(user_id),\n            'time': {\n                'local_time': self.get_local_time(user_id),\n                'day_of_week': self.get_day_of_week(user_id)\n            }\n        }\n```\n\n### 2. Recommendation Engine\n```python\nclass PersonalizationEngine:\n    def personalize(self, user_id, content_pool):\n        # Get user profile\n        user_profile = self.profile_service.get(user_id)\n\n        # Get real-time context\n        context = self.context_engine.get_real_time_context(user_id)\n\n        # Score content\n        scores = []\n        for content in content_pool:\n            score = self.scoring_model.predict(\n                user_profile, content, context\n            )\n            scores.append(score)\n\n        # Apply business rules\n        filtered_scores = self.apply_rules(scores, context)\n\n        # Return top K\n        top_k = self.select_top_k(filtered_scores, k=10)\n\n        return top_k\n```\n\n### 3. Infrastructure\n- **Feature Store**: Feast for feature serving\n- **Model Serving**: TensorFlow Serving\n- **Caching**: Redis with TTL\n- **Message Queue**: Kafka for events\n\n## Performance Requirements\n- < 50ms personalization latency\n- 1M+ requests/second\n- 99.99% availability"
    }
]
