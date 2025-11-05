#!/usr/bin/env python3
"""
LeetCode Questions Data - Source of Truth
"""

from typing import List, Optional

LEETCODE_QUESTIONS = [
    {
        'title': 'Two Sum',
        'leetcode_url': 'https://leetcode.com/problems/two-sum/',
        'difficulty': 'easy',
        "description": '''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.''',
        'constraints': ['2 <= nums.length <= 10^4', '-10^9 <= nums[i] <= 10^9', '-10^9 <= target <= 10^9', 'Only one valid answer exists'],
        'examples': [{'input': {'nums': [2, 7, 11, 15], 'target': 9}, 'output': [0, 1], 'explanation': 'Because nums[0] + nums[1] == 9, we return [0, 1].'}, {'input': {'nums': [3, 2, 4], 'target': 6}, 'output': [1, 2], 'explanation': 'Because nums[1] + nums[2] == 6, we return [1, 2].'}],
        'tags': ['array', 'hash-table'],
        'test_cases': [{'input': [[2, 7, 11, 15], 9], 'expectedOutput': [0, 1]}, {'input': [[3, 2, 4], 6], 'expectedOutput': [1, 2]}, {'input': [[3, 3], 6], 'expectedOutput': [0, 1]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass''',
        "java_sig": '''class Solution {
    public int[] twoSum(int[] nums, int target) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};''',
        "solution_python": '''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map approach for O(n) time complexity
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []''',
        "solution_java": '''class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }

        return new int[] {};
    }
}''',
        "solution_cpp": '''class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }

        return {};
    }
};''',
        "solution_explanation": '''## Approach: Hash Table

### Algorithm
1. Create a hash map to store values and indices
2. For each number, calculate its complement (target - num)
3. Check if complement exists in hash map
4. If found, return indices; otherwise add current number to map

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - Hash map storage''',
    },
    {
        'title': 'Valid Parentheses',
        'leetcode_url': 'https://leetcode.com/problems/valid-parentheses/',
        'difficulty': 'easy',
        "description": '''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.''',
        'constraints': ['1 <= s.length <= 10^4', "s consists of parentheses only '()[]{}'"],
        'examples': [{'input': {'s': '()'}, 'output': True, 'explanation': 'The string is valid.'}, {'input': {'s': '()[]{}'}, 'output': True, 'explanation': 'All brackets are properly closed.'}, {'input': {'s': '(]'}, 'output': False, 'explanation': 'Mismatched brackets.'}],
        'tags': ['string', 'stack'],
        'test_cases': [{'input': ['()'], 'expectedOutput': True}, {'input': ['()[]{}'], 'expectedOutput': True}, {'input': ['(]'], 'expectedOutput': False}, {'input': ['([)]'], 'expectedOutput': False}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def isValid(self, s: str) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean isValid(String s) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool isValid(string s) {
        
    }
};''',
        "solution_python": '''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0''',
        "solution_java": '''class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                if (stack.isEmpty() || stack.peek() != map.get(c)) {
                    return False;
                }
                stack.pop();
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}''',
        "solution_cpp": '''class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mapping = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for (char c : s) {
            if (mapping.count(c)) {
                if (st.empty() || st.top() != mapping[c]) {
                    return False;
                }
                st.pop();
            } else {
                st.push(c);
            }
        }

        return st.empty();
    }
};''',
        "solution_explanation": '''## Approach: Stack

### Algorithm
1. Use a stack to track opening brackets
2. For closing brackets, check if they match the most recent opening bracket
3. Valid if all brackets are matched (stack is empty)

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)''',
    },
    {
        'title': 'Merge Two Sorted Lists',
        'leetcode_url': 'https://leetcode.com/problems/merge-two-sorted-lists/',
        'difficulty': 'easy',
        "description": '''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.''',
        'constraints': ['The number of nodes in both lists is in the range [0, 50]', '-100 <= Node.val <= 100', 'Both list1 and list2 are sorted in non-decreasing order'],
        'examples': [{'input': {'list1': [1, 2, 4], 'list2': [1, 3, 4]}, 'output': [1, 1, 2, 3, 4, 4], 'explanation': 'Merge both sorted lists.'}, {'input': {'list1': [], 'list2': []}, 'output': [], 'explanation': 'Both lists are empty.'}],
        'tags': ['linked-list', 'recursion'],
        'test_cases': [{'input': [[1, 2, 4], [1, 3, 4]], 'expectedOutput': [1, 1, 2, 3, 4, 4]}, {'input': [[], []], 'expectedOutput': []}, {'input': [[], [0]], 'expectedOutput': [0]}],
        'time_complexity': 'O(n+m)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
    }
};''',
        "solution_python": '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next''',
        "solution_java": '''class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (list1 != None && list2 != None) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        current.next = (list1 != None) ? list1 : list2;
        return dummy.next;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* current = &dummy;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                current->next = list1;
                list1 = list1->next;
            } else {
                current->next = list2;
                list2 = list2->next;
            }
            current = current->next;
        }

        current->next = list1 ? list1 : list2;
        return dummy.next;
    }
};''',
        "solution_explanation": '''## Approach: Iterative Merge

### Algorithm
1. Use dummy node to simplify edge cases
2. Compare nodes and attach smaller one
3. Attach remaining list when one is exhausted

### Complexity Analysis
- **Time Complexity**: O(n + m)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Best Time to Buy and Sell Stock',
        'leetcode_url': 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
        'difficulty': 'easy',
        "description": '''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.''',
        'constraints': ['1 <= prices.length <= 10^5', '0 <= prices[i] <= 10^4'],
        'examples': [{'input': {'prices': [7, 1, 5, 3, 6, 4]}, 'output': 5, 'explanation': 'Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.'}, {'input': {'prices': [7, 6, 4, 3, 1]}, 'output': 0, 'explanation': 'In this case, no transactions are done and the max profit = 0.'}],
        'tags': ['array', 'dynamic-programming'],
        'test_cases': [{'input': [[7, 1, 5, 3, 6, 4]], 'expectedOutput': 5}, {'input': [[7, 6, 4, 3, 1]], 'expectedOutput': 0}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int maxProfit(int[] prices) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};''',
        "solution_python": '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit''',
        "solution_java": '''class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            minPrice = min(minPrice, price);
            maxProfit = max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};''',
        "solution_explanation": '''## Approach: Dynamic Programming

### Algorithm
1. Track minimum price seen so far
2. Calculate profit at each day
3. Keep maximum profit

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Valid Palindrome',
        'leetcode_url': 'https://leetcode.com/problems/valid-palindrome/',
        'difficulty': 'easy',
        "description": '''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return True if it is a palindrome, or False otherwise.''',
        'constraints': ['1 <= s.length <= 2 * 10^5', 's consists only of printable ASCII characters'],
        'examples': [{'input': {'s': 'A man, a plan, a canal: Panama'}, 'output': True, 'explanation': 'After cleaning: amanaplanacanalpanama which is a palindrome.'}, {'input': {'s': 'race a car'}, 'output': False, 'explanation': 'After cleaning: raceacar which is not a palindrome.'}],
        'tags': ['two-pointers', 'string'],
        'test_cases': [{'input': ['A man, a plan, a canal: Panama'], 'expectedOutput': True}, {'input': ['race a car'], 'expectedOutput': False}, {'input': [' '], 'expectedOutput': True}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean isPalindrome(String s) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool isPalindrome(string s) {
        
    }
};''',
        "solution_python": '''class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True''',
        "solution_java": '''class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) !=
                Character.toLowerCase(s.charAt(right))) {
                return False;
            }

            left++;
            right--;
        }

        return True;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !isalnum(s[left])) {
                left++;
            }
            while (left < right && !isalnum(s[right])) {
                right--;
            }

            if (tolower(s[left]) != tolower(s[right])) {
                return False;
            }

            left++;
            right--;
        }

        return True;
    }
};''',
        "solution_explanation": '''## Approach: Two Pointers

### Algorithm
1. Use two pointers from start and end
2. Skip non-alphanumeric characters
3. Compare characters (case-insensitive)

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Climbing Stairs',
        'leetcode_url': 'https://leetcode.com/problems/climbing-stairs/',
        'difficulty': 'easy',
        "description": '''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?''',
        'constraints': ['1 <= n <= 45'],
        'examples': [{'input': {'n': 2}, 'output': 2, 'explanation': 'There are two ways: 1. 1 step + 1 step, 2. 2 steps'}, {'input': {'n': 3}, 'output': 3, 'explanation': 'There are three ways: 1. 1+1+1, 2. 1+2, 3. 2+1'}],
        'tags': ['dynamic-programming', 'math'],
        'test_cases': [{'input': [2], 'expectedOutput': 2}, {'input': [3], 'expectedOutput': 3}, {'input': [4], 'expectedOutput': 5}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def climbStairs(self, n: int) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int climbStairs(int n) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int climbStairs(int n) {
        
    }
};''',
        "solution_python": '''class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Dynamic programming - Fibonacci sequence
        prev2, prev1 = 1, 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1''',
        "solution_java": '''class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int prev2 = 1, prev1 = 2;

        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;

        int prev2 = 1, prev1 = 2;

        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
};''',
        "solution_explanation": '''## Approach: Dynamic Programming (Fibonacci)

### Algorithm
1. Base cases: 1 step = 1 way, 2 steps = 2 ways
2. For n steps: ways(n) = ways(n-1) + ways(n-2)
3. Use two variables to track previous values

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Binary Tree Inorder Traversal',
        'leetcode_url': 'https://leetcode.com/problems/binary-tree-inorder-traversal/',
        'difficulty': 'easy',
        "description": '''Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal: Left -> Root -> Right''',
        'constraints': ['The number of nodes in the tree is in the range [0, 100]', '-100 <= Node.val <= 100'],
        'examples': [{'input': {'root': [1, None, 2, 3]}, 'output': [1, 3, 2], 'explanation': 'Inorder traversal of the tree.'}, {'input': {'root': []}, 'output': [], 'explanation': 'Empty tree.'}],
        'tags': ['tree', 'depth-first-search', 'stack'],
        'test_cases': [{'input': [[1, None, 2, 3]], 'expectedOutput': [1, 3, 2]}, {'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass''',
        "java_sig": '''class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        
    }
};''',
        "solution_python": '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Current is None, so process the node on top of stack
            current = stack.pop()
            result.append(current.val)

            # Visit right subtree
            current = current.right

        return result''',
        "solution_java": '''class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        while (current != None || !stack.isEmpty()) {
            while (current != None) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            result.add(current.val);
            current = current.right;
        }

        return result;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> st;
        TreeNode* current = root;

        while (current || !st.empty()) {
            while (current) {
                st.push(current);
                current = current->left;
            }

            current = st.top();
            st.pop();
            result.push_back(current->val);
            current = current->right;
        }

        return result;
    }
};''',
        "solution_explanation": '''## Approach: Iterative using Stack

### Algorithm
1. Use stack to simulate recursion
2. Go left as far as possible
3. Process node and go right

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)''',
    },
    {
        'title': 'Linked List Cycle',
        'leetcode_url': 'https://leetcode.com/problems/linked-list-cycle/',
        'difficulty': 'easy',
        "description": '''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.''',
        'constraints': ['The number of the nodes in the list is in the range [0, 10^4]', '-10^5 <= Node.val <= 10^5', 'pos is -1 or a valid index in the linked-list'],
        'examples': [{'input': {'head': [3, 2, 0, -4], 'pos': 1}, 'output': True, 'explanation': 'There is a cycle where the tail connects to the 1st node.'}, {'input': {'head': [1], 'pos': -1}, 'output': False, 'explanation': 'There is no cycle in the linked list.'}],
        'tags': ['linked-list', 'two-pointers', 'hash-table'],
        'test_cases': [{'input': [[3, 2, 0, -4], 1], 'expectedOutput': True}, {'input': [[1, 2], 0], 'expectedOutput': True}, {'input': [[1], -1], 'expectedOutput': False}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean hasCycle(ListNode head) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool hasCycle(ListNode *head) {
        
    }
};''',
        "solution_python": '''class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True''',
        "solution_java": '''public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == None || head.next == None) {
            return False;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while (slow != fast) {
            if (fast == None || fast.next == None) {
                return False;
            }
            slow = slow.next;
            fast = fast.next.next;
        }

        return True;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) return False;

        ListNode* slow = head;
        ListNode* fast = head->next;

        while (slow != fast) {
            if (!fast || !fast->next) return False;
            slow = slow->next;
            fast = fast->next->next;
        }

        return True;
    }
};''',
        "solution_explanation": '''## Approach: Floyd's Cycle Detection (Two Pointers)

### Algorithm
1. Use slow and fast pointers
2. Slow moves 1 step, fast moves 2 steps
3. If they meet, there's a cycle

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Longest Substring Without Repeating Characters',
        'leetcode_url': 'https://leetcode.com/problems/longest-substring-without-repeating-characters/',
        'difficulty': 'medium',
        'description': 'Given a string s, find the length of the longest substring without repeating characters.',
        'constraints': ['0 <= s.length <= 5 * 10^4', 's consists of English letters, digits, symbols and spaces'],
        'examples': [{'input': {'s': 'abcabcbb'}, 'output': 3, 'explanation': "The answer is 'abc', with the length of 3."}, {'input': {'s': 'bbbbb'}, 'output': 1, 'explanation': "The answer is 'b', with the length of 1."}],
        'tags': ['string', 'sliding-window', 'hash-table'],
        'test_cases': [{'input': ['abcabcbb'], 'expectedOutput': 3}, {'input': ['bbbbb'], 'expectedOutput': 1}, {'input': ['pwwkew'], 'expectedOutput': 3}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(min(m,n))',
        "python_sig": '''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int lengthOfLongestSubstring(String s) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
    }
};''',
        "solution_python": '''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length''',
        "solution_java": '''class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }

            charSet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            while (charSet.count(s[right])) {
                charSet.erase(s[left]);
                left++;
            }

            charSet.insert(s[right]);
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};''',
        "solution_explanation": '''## Approach: Sliding Window with Hash Set

### Algorithm
1. Use two pointers for sliding window
2. Expand window by moving right pointer
3. Contract window when duplicate found
4. Track maximum window size

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(min(n, m)) where m is charset size''',
    },
    {
        'title': 'Add Two Numbers',
        'leetcode_url': 'https://leetcode.com/problems/add-two-numbers/',
        'difficulty': 'medium',
        "description": '''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.''',
        'constraints': ['The number of nodes in each linked list is in the range [1, 100]', '0 <= Node.val <= 9', 'It is guaranteed that the list represents a number that does not have leading zeros'],
        'examples': [{'input': {'l1': [2, 4, 3], 'l2': [5, 6, 4]}, 'output': [7, 0, 8], 'explanation': '342 + 465 = 807.'}, {'input': {'l1': [0], 'l2': [0]}, 'output': [0], 'explanation': '0 + 0 = 0.'}],
        'tags': ['linked-list', 'math', 'recursion'],
        'test_cases': [{'input': [[2, 4, 3], [5, 6, 4]], 'expectedOutput': [7, 0, 8]}, {'input': [[0], [0]], 'expectedOutput': [0]}, {'input': [[9, 9, 9], [9, 9, 9, 9]], 'expectedOutput': [8, 9, 9, 0, 1]}],
        'time_complexity': 'O(max(m,n))',
        'space_complexity': 'O(max(m,n))',
        "python_sig": '''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
    }
};''',
        "solution_python": '''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next''',
        "solution_java": '''class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (l1 != None || l2 != None || carry != 0) {
            int val1 = (l1 != None) ? l1.val : 0;
            int val2 = (l2 != None) ? l2.val : 0;

            int total = val1 + val2 + carry;
            carry = total / 10;

            current.next = new ListNode(total % 10);
            current = current.next;

            l1 = (l1 != None) ? l1.next : None;
            l2 = (l2 != None) ? l2.next : None;
        }

        return dummy.next;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* current = &dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;

            int total = val1 + val2 + carry;
            carry = total / 10;

            current->next = new ListNode(total % 10);
            current = current->next;

            l1 = l1 ? l1->next : Noneptr;
            l2 = l2 ? l2->next : Noneptr;
        }

        return dummy.next;
    }
};''',
        "solution_explanation": '''## Approach: Elementary Math with Carry

### Algorithm
1. Add digits and carry from right to left
2. Handle carry for next position
3. Continue until both lists exhausted and no carry

### Complexity Analysis
- **Time Complexity**: O(max(m, n))
- **Space Complexity**: O(max(m, n))''',
    },
    {
        'title': 'Container With Most Water',
        'leetcode_url': 'https://leetcode.com/problems/container-with-most-water/',
        'difficulty': 'medium',
        "description": '''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.''',
        'constraints': ['n == height.length', '2 <= n <= 10^5', '0 <= height[i] <= 10^4'],
        'examples': [{'input': {'height': [1, 8, 6, 2, 5, 4, 8, 3, 7]}, 'output': 49, 'explanation': 'The max area is between index 1 (height 8) and index 8 (height 7).'}],
        'tags': ['array', 'two-pointers', 'greedy'],
        'test_cases': [{'input': [[1, 8, 6, 2, 5, 4, 8, 3, 7]], 'expectedOutput': 49}, {'input': [[1, 1]], 'expectedOutput': 1}, {'input': [[4, 3, 2, 1, 4]], 'expectedOutput': 16}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int maxArea(int[] height) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int maxArea(vector<int>& height) {
        
    }
};''',
        "solution_python": '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area''',
        "solution_java": '''class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentArea = Math.min(height[left], height[right]) * width;
            maxArea = Math.max(maxArea, currentArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentArea = min(height[left], height[right]) * width;
            maxArea = max(maxArea, currentArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
};''',
        "solution_explanation": '''## Approach: Two Pointers

### Algorithm
1. Start with widest container
2. Move pointer with smaller height inward
3. Track maximum area

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)''',
    },
    {
        'title': '3Sum',
        'leetcode_url': 'https://leetcode.com/problems/3sum/',
        'difficulty': 'medium',
        "description": '''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.''',
        'constraints': ['3 <= nums.length <= 3000', '-10^5 <= nums[i] <= 10^5'],
        'examples': [{'input': {'nums': [-1, 0, 1, 2, -1, -4]}, 'output': [[-1, -1, 2], [-1, 0, 1]], 'explanation': 'The distinct triplets are [-1,0,1] and [-1,-1,2].'}, {'input': {'nums': [0, 1, 1]}, 'output': [], 'explanation': 'The only possible triplet does not sum up to 0.'}],
        'tags': ['array', 'two-pointers', 'sorting'],
        'test_cases': [{'input': [[-1, 0, 1, 2, -1, -4]], 'expectedOutput': [[-1, -1, 2], [-1, 0, 1]]}, {'input': [[0, 1, 1]], 'expectedOutput': []}, {'input': [[0, 0, 0]], 'expectedOutput': [[0, 0, 0]]}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass''',
        "java_sig": '''class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
    }
};''',
        "solution_python": '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result''',
        "solution_java": '''class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = nums.size() - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});

                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }
};''',
        "solution_explanation": '''## Approach: Sort + Two Pointers

### Algorithm
1. Sort the array
2. Fix one element and find two others using two pointers
3. Skip duplicates to avoid duplicate triplets

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Group Anagrams',
        'leetcode_url': 'https://leetcode.com/problems/group-anagrams/',
        'difficulty': 'medium',
        "description": '''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.''',
        'constraints': ['1 <= strs.length <= 10^4', '0 <= strs[i].length <= 100', 'strs[i] consists of lowercase English letters'],
        'examples': [{'input': {'strs': ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']}, 'output': [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']], 'explanation': 'Group words that are anagrams.'}],
        'tags': ['array', 'hash-table', 'string', 'sorting'],
        'test_cases': [{'input': [['eat', 'tea', 'tan', 'ate', 'nat', 'bat']], 'expectedOutput': [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]}, {'input': [['']], 'expectedOutput': [['']]}, {'input': [['a']], 'expectedOutput': [['a']]}],
        'time_complexity': 'O(n*k)',
        'space_complexity': 'O(n*k)',
        "python_sig": '''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass''',
        "java_sig": '''class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
    }
};''',
        "solution_python": '''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            # Sort the string to create a key
            key = ''.join(sorted(s))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)

        return list(anagram_map.values())''',
        "solution_java": '''class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(s);
        }

        return new ArrayList<>(map.values());
    }
}''',
        "solution_cpp": '''class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for (string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            map[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto& pair : map) {
            result.push_back(pair.second);
        }

        return result;
    }
};''',
        "solution_explanation": '''## Approach: Hash Map with Sorted String Key

### Algorithm
1. Sort each string to create a key
2. Group strings with the same sorted key
3. Return all groups

### Complexity Analysis
- **Time Complexity**: O(n * k log k) where k is max string length
- **Space Complexity**: O(n * k)''',
    },
    {
        'title': 'Longest Palindromic Substring',
        'leetcode_url': 'https://leetcode.com/problems/longest-palindromic-substring/',
        'difficulty': 'medium',
        'description': 'Given a string s, return the longest palindromic substring in s.',
        'constraints': ['1 <= s.length <= 1000', 's consist of only digits and English letters'],
        'examples': [{'input': {'s': 'babad'}, 'output': 'bab', 'explanation': "Note: 'aba' is also a valid answer."}, {'input': {'s': 'cbbd'}, 'output': 'bb', 'explanation': "The longest palindrome is 'bb'."}],
        'tags': ['string', 'dynamic-programming'],
        'test_cases': [{'input': ['babad'], 'expectedOutput': 'bab'}, {'input': ['cbbd'], 'expectedOutput': 'bb'}, {'input': ['a'], 'expectedOutput': 'a'}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass''',
        "java_sig": '''class Solution {
    public String longestPalindrome(String s) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    string longestPalindrome(string s) {
        
    }
};''',
        "solution_python": '''class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        max_len = 0

        for i in range(len(s)):
            # Odd length palindromes
            len1 = expandAroundCenter(i, i)
            # Even length palindromes
            len2 = expandAroundCenter(i, i + 1)

            current_len = max(len1, len2)

            if current_len > max_len:
                max_len = current_len
                start = i - (current_len - 1) // 2

        return s[start:start + max_len]''',
        "solution_java": '''class Solution {
    public String longestPalindrome(String s) {
        if (s == None || s.length() == 0) return "";

        int start = 0, maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);

            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }

        return s.substring(start, start + maxLen);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}''',
        "solution_cpp": '''class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int start = 0, maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = max(len1, len2);

            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }

        return s.substr(start, maxLen);
    }

private:
    int expandAroundCenter(string& s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
};''',
        "solution_explanation": '''## Approach: Expand Around Centers

### Algorithm
1. For each position, consider it as center
2. Expand outward while characters match
3. Handle both odd and even length palindromes

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)''',
    },
    {
        'title': 'Product of Array Except Self',
        'leetcode_url': 'https://leetcode.com/problems/product-of-array-except-self/',
        'difficulty': 'medium',
        "description": '''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.''',
        'constraints': ['2 <= nums.length <= 10^5', '-30 <= nums[i] <= 30', 'The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer'],
        'examples': [{'input': {'nums': [1, 2, 3, 4]}, 'output': [24, 12, 8, 6], 'explanation': 'answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, etc.'}],
        'tags': ['array', 'prefix-sum'],
        'test_cases': [{'input': [[1, 2, 3, 4]], 'expectedOutput': [24, 12, 8, 6]}, {'input': [[-1, 1, 0, -3, 3]], 'expectedOutput': [0, 0, 9, 0, 0]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass''',
        "java_sig": '''class Solution {
    public int[] productExceptSelf(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
    }
};''',
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
        "solution_java": '''// Solution for Product of Array Except Self
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Product of Array Except Self
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Product of Array Except Self

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Spiral Matrix',
        'leetcode_url': 'https://leetcode.com/problems/spiral-matrix/',
        'difficulty': 'medium',
        'description': 'Given an m x n matrix, return all elements of the matrix in spiral order.',
        'constraints': ['m == matrix.length', 'n == matrix[i].length', '1 <= m, n <= 10', '-100 <= matrix[i][j] <= 100'],
        'examples': [{'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, 'output': [1, 2, 3, 6, 9, 8, 7, 4, 5], 'explanation': 'Traverse the matrix in spiral order.'}],
        'tags': ['array', 'matrix', 'simulation'],
        'test_cases': [{'input': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 'expectedOutput': [1, 2, 3, 6, 9, 8, 7, 4, 5]}, {'input': [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], 'expectedOutput': [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass''',
        "java_sig": '''class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
    }
};''',
        "solution_python": '''# Solution for Spiral Matrix
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return elements of matrix in spiral order.

        Approach:
        - Track four boundaries: top, bottom, left, right
        - Traverse right → down → left → up
        - Shrink boundaries after each direction
        - Stop when boundaries cross

        Time: O(m*n) - visit each element once
        Space: O(1) - excluding output array
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse right along top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse down along right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse left along bottom row (if row exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse up along left column (if column exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
''',
        "solution_java": '''// Solution for Spiral Matrix
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Spiral Matrix
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Spiral Matrix

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Rotate Image',
        'leetcode_url': 'https://leetcode.com/problems/rotate-image/',
        'difficulty': 'medium',
        "description": '''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.''',
        'constraints': ['n == matrix.length == matrix[i].length', '1 <= n <= 20', '-1000 <= matrix[i][j] <= 1000'],
        'examples': [{'input': {'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, 'output': [[7, 4, 1], [8, 5, 2], [9, 6, 3]], 'explanation': 'Rotate 90 degrees clockwise.'}],
        'tags': ['array', 'matrix'],
        'test_cases': [{'input': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 'expectedOutput': [[7, 4, 1], [8, 5, 2], [9, 6, 3]]}, {'input': [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]], 'expectedOutput': [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pass''',
        "java_sig": '''class Solution {
    public void rotate(int[][] matrix) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
    }
};''',
        "solution_python": '''# Solution for Rotate Image
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate matrix 90 degrees clockwise in-place.

        Approach:
        1. Transpose matrix (swap matrix[i][j] with matrix[j][i])
        2. Reverse each row
        Result: 90° clockwise rotation

        Time: O(n²) - process each element twice
        Space: O(1) - in-place modification
        """
        n = len(matrix)

        # Step 1: Transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
''',
        "solution_java": '''// Solution for Rotate Image
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Rotate Image
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Rotate Image

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Set Matrix Zeroes',
        'leetcode_url': 'https://leetcode.com/problems/set-matrix-zeroes/',
        'difficulty': 'medium',
        "description": '''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.''',
        'constraints': ['m == matrix.length', 'n == matrix[0].length', '1 <= m, n <= 200', '-2^31 <= matrix[i][j] <= 2^31 - 1'],
        'examples': [{'input': {'matrix': [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}, 'output': [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 'explanation': 'Mark row and column of 0s.'}],
        'tags': ['array', 'matrix', 'hash-table'],
        'test_cases': [{'input': [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]], 'expectedOutput': [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}, {'input': [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]], 'expectedOutput': [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pass''',
        "java_sig": '''class Solution {
    public void setZeroes(int[][] matrix) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
    }
};''',
        "solution_python": '''# Solution for Set Matrix Zeroes
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Set entire row and column to zero if element is zero.

        Approach:
        - Use first row and first column as markers
        - Track separately if first column has zeros
        - Mark zeros in first row/col
        - Apply zeros using markers
        - Handle first row/col last

        Time: O(m*n)
        Space: O(1) - reuse matrix for markers
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and column as markers (skip row 0, col 0)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column

        # Set zeros based on markers (skip first row/col)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first column first (including row 0)
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        # Handle first row second (will overwrite matrix[0][0] if needed)
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
''',
        "solution_java": '''// Solution for Set Matrix Zeroes
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Set Matrix Zeroes
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Set Matrix Zeroes

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Subarray Sum Equals K',
        'leetcode_url': 'https://leetcode.com/problems/subarray-sum-equals-k/',
        'difficulty': 'medium',
        "description": '''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.''',
        'constraints': ['1 <= nums.length <= 2 * 10^4', '-1000 <= nums[i] <= 1000', '-10^7 <= k <= 10^7'],
        'examples': [{'input': {'nums': [1, 1, 1], 'k': 2}, 'output': 2, 'explanation': 'Subarrays [1,1] and [1,1] sum to 2.'}, {'input': {'nums': [1, 2, 3], 'k': 3}, 'output': 2, 'explanation': 'Subarrays [1,2] and [3] sum to 3.'}],
        'tags': ['array', 'hash-table', 'prefix-sum'],
        'test_cases': [{'input': [[1, 1, 1], 2], 'expectedOutput': 2}, {'input': [[1, 2, 3], 3], 'expectedOutput': 2}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int subarraySum(int[] nums, int k) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
    }
};''',
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
        "solution_java": '''// Solution for Subarray Sum Equals K
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Subarray Sum Equals K
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Subarray Sum Equals K

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Maximum Subarray',
        'leetcode_url': 'https://leetcode.com/problems/maximum-subarray/',
        'difficulty': 'medium',
        'description': 'Given an integer array nums, find the subarray with the largest sum, and return its sum.',
        'constraints': ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4'],
        'examples': [{'input': {'nums': [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, 'output': 6, 'explanation': 'The subarray [4,-1,2,1] has the largest sum 6.'}, {'input': {'nums': [1]}, 'output': 1, 'explanation': 'The subarray [1] has the largest sum 1.'}],
        'tags': ['array', 'divide-and-conquer', 'dynamic-programming'],
        'test_cases': [{'input': [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 'expectedOutput': 6}, {'input': [[1]], 'expectedOutput': 1}, {'input': [[5, 4, -1, 7, 8]], 'expectedOutput': 23}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int maxSubArray(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};''',
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
        "solution_java": '''// Solution for Maximum Subarray
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Maximum Subarray
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Maximum Subarray

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Remove Nth Node From End of List',
        'leetcode_url': 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/',
        'difficulty': 'medium',
        'description': 'Given the head of a linked list, remove the nth node from the end of the list and return its head.',
        'constraints': ['The number of nodes in the list is sz', '1 <= sz <= 30', '0 <= Node.val <= 100', '1 <= n <= sz'],
        'examples': [{'input': {'head': [1, 2, 3, 4, 5], 'n': 2}, 'output': [1, 2, 3, 5], 'explanation': 'Remove 2nd node from end.'}],
        'tags': ['linked-list', 'two-pointers'],
        'test_cases': [{'input': [[1, 2, 3, 4, 5], 2], 'expectedOutput': [1, 2, 3, 5]}, {'input': [[1], 1], 'expectedOutput': []}, {'input': [[1, 2], 1], 'expectedOutput': [1]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
    }
};''',
        "solution_python": '''# Solution for Remove Nth Node From End of List
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove nth node from end of linked list in one pass.

        Approach:
        - Use dummy head to handle edge cases
        - Two pointers: fast moves n steps ahead
        - Move both until fast reaches end
        - slow.next is the node to remove

        Time: O(L) where L is list length
        Space: O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next
''',
        "solution_java": '''// Solution for Remove Nth Node From End of List
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Remove Nth Node From End of List
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Remove Nth Node From End of List

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Reverse Linked List II',
        'leetcode_url': 'https://leetcode.com/problems/reverse-linked-list-ii/',
        'difficulty': 'medium',
        "description": '''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.''',
        'constraints': ['The number of nodes in the list is n', '1 <= n <= 500', '-500 <= Node.val <= 500', '1 <= left <= right <= n'],
        'examples': [{'input': {'head': [1, 2, 3, 4, 5], 'left': 2, 'right': 4}, 'output': [1, 4, 3, 2, 5], 'explanation': 'Reverse nodes from position 2 to 4.'}],
        'tags': ['linked-list'],
        'test_cases': [{'input': [[1, 2, 3, 4, 5], 2, 4], 'expectedOutput': [1, 4, 3, 2, 5]}, {'input': [[5], 1, 1], 'expectedOutput': [5]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
    }
};''',
        "solution_python": '''# Solution for Reverse Linked List II
from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse linked list from position left to right.

        Approach:
        - Use dummy head for clean edge case handling
        - Find node before left position
        - Reverse sublist using standard three-pointer reversal
        - Reconnect reversed portion

        Time: O(n)
        Space: O(1)
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move to node before left position
        for _ in range(left - 1):
            prev = prev.next

        # Reverse from left to right
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
''',
        "solution_java": '''// Solution for Reverse Linked List II
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Reverse Linked List II
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Reverse Linked List II

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Swap Nodes in Pairs',
        'leetcode_url': 'https://leetcode.com/problems/swap-nodes-in-pairs/',
        'difficulty': 'medium',
        "description": '''Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.''',
        'constraints': ['The number of nodes in the list is in the range [0, 100]', '0 <= Node.val <= 100'],
        'examples': [{'input': {'head': [1, 2, 3, 4]}, 'output': [2, 1, 4, 3], 'explanation': 'Swap adjacent pairs.'}],
        'tags': ['linked-list', 'recursion'],
        'test_cases': [{'input': [[1, 2, 3, 4]], 'expectedOutput': [2, 1, 4, 3]}, {'input': [[]], 'expectedOutput': []}, {'input': [[1]], 'expectedOutput': [1]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode swapPairs(ListNode head) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        
    }
};''',
        "solution_python": '''# Solution for Swap Nodes in Pairs
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in linked list.

        Approach:
        - Use dummy head for clean handling
        - For each pair: adjust pointers to swap
        - Move to next pair

        Time: O(n)
        Space: O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # Identify nodes to swap
            first = prev.next
            second = prev.next.next

            # Perform swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move to next pair
            prev = first

        return dummy.next
''',
        "solution_java": '''// Solution for Swap Nodes in Pairs
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Swap Nodes in Pairs
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Swap Nodes in Pairs

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Binary Tree Level Order Traversal',
        'leetcode_url': 'https://leetcode.com/problems/binary-tree-level-order-traversal/',
        'difficulty': 'medium',
        "description": '''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).''',
        'constraints': ['The number of nodes in the tree is in the range [0, 2000]', '-1000 <= Node.val <= 1000'],
        'examples': [{'input': {'root': [3, 9, 20, None, None, 15, 7]}, 'output': [[3], [9, 20], [15, 7]], 'explanation': 'Level by level traversal.'}],
        'tags': ['tree', 'breadth-first-search'],
        'test_cases': [{'input': [[3, 9, 20, None, None, 15, 7]], 'expectedOutput': [[3], [9, 20], [15, 7]]}, {'input': [[1]], 'expectedOutput': [[1]]}, {'input': [[]], 'expectedOutput': []}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass''',
        "java_sig": '''class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        
    }
};''',
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
        "solution_java": '''// Solution for Binary Tree Level Order Traversal
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Binary Tree Level Order Traversal
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Binary Tree Level Order Traversal

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Validate Binary Search Tree',
        'leetcode_url': 'https://leetcode.com/problems/validate-binary-search-tree/',
        'difficulty': 'medium',
        "description": '''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.''',
        'constraints': ['The number of nodes in the tree is in the range [1, 10^4]', '-2^31 <= Node.val <= 2^31 - 1'],
        'examples': [{'input': {'root': [2, 1, 3]}, 'output': True, 'explanation': 'Valid BST.'}, {'input': {'root': [5, 1, 4, None, None, 3, 6]}, 'output': False, 'explanation': 'Node 4 in right subtree of 5 violates BST property.'}],
        'tags': ['tree', 'depth-first-search', 'binary-search-tree'],
        'test_cases': [{'input': [[2, 1, 3]], 'expectedOutput': True}, {'input': [[5, 1, 4, None, None, 3, 6]], 'expectedOutput': False}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean isValidBST(TreeNode root) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool isValidBST(TreeNode* root) {
        
    }
};''',
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
        "solution_java": '''// Solution for Validate Binary Search Tree
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Validate Binary Search Tree
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Validate Binary Search Tree

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Kth Smallest Element in a BST',
        'leetcode_url': 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/',
        'difficulty': 'medium',
        "description": '''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.''',
        'constraints': ['The number of nodes in the tree is n', '1 <= k <= n <= 10^4', '0 <= Node.val <= 10^4'],
        'examples': [{'input': {'root': [3, 1, 4, None, 2], 'k': 1}, 'output': 1, 'explanation': 'The smallest element is 1.'}, {'input': {'root': [5, 3, 6, 2, 4, None, None, 1], 'k': 3}, 'output': 3, 'explanation': 'The 3rd smallest is 3.'}],
        'tags': ['tree', 'depth-first-search', 'binary-search-tree'],
        'test_cases': [{'input': [[3, 1, 4, None, 2], 1], 'expectedOutput': 1}, {'input': [[5, 3, 6, 2, 4, None, None, 1], 3], 'expectedOutput': 3}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int kthSmallest(TreeNode root, int k) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        
    }
};''',
        "solution_python": '''# Solution for Kth Smallest Element in a BST
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find kth smallest element in BST.

        Approach:
        - In-order traversal of BST yields sorted sequence
        - Use counter to track position
        - Return when counter reaches k

        Time: O(n) worst case, O(k) average
        Space: O(h) for recursion stack
        """
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            # Traverse left subtree
            inorder(node.left)

            # Process current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.result
''',
        "solution_java": '''// Solution for Kth Smallest Element in a BST
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Kth Smallest Element in a BST
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Kth Smallest Element in a BST

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Binary Tree Right Side View',
        'leetcode_url': 'https://leetcode.com/problems/binary-tree-right-side-view/',
        'difficulty': 'medium',
        "description": '''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.''',
        'constraints': ['The number of nodes in the tree is in the range [0, 100]', '-100 <= Node.val <= 100'],
        'examples': [{'input': {'root': [1, 2, 3, None, 5, None, 4]}, 'output': [1, 3, 4], 'explanation': 'Right side view shows nodes 1, 3, 4.'}],
        'tags': ['tree', 'depth-first-search', 'breadth-first-search'],
        'test_cases': [{'input': [[1, 2, 3, None, 5, None, 4]], 'expectedOutput': [1, 3, 4]}, {'input': [[1, None, 3]], 'expectedOutput': [1, 3]}, {'input': [[]], 'expectedOutput': []}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pass''',
        "java_sig": '''class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        
    }
};''',
        "solution_python": '''# Solution for Binary Tree Right Side View
from typing import Optional, List
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return values of nodes visible from right side of tree.

        Approach:
        - Level-order traversal (BFS)
        - Capture rightmost node at each level
        - Rightmost = last node processed per level

        Time: O(n) - visit each node once
        Space: O(w) where w is max width of tree
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Last node in this level is rightmost
                if i == level_size - 1:
                    result.append(node.val)

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
''',
        "solution_java": '''// Solution for Binary Tree Right Side View
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Binary Tree Right Side View
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Binary Tree Right Side View

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Path Sum II',
        'leetcode_url': 'https://leetcode.com/problems/path-sum-ii/',
        'difficulty': 'medium',
        "description": '''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.''',
        'constraints': ['The number of nodes in the tree is in the range [0, 5000]', '-1000 <= Node.val <= 1000', '-1000 <= targetSum <= 1000'],
        'examples': [{'input': {'root': [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 'targetSum': 22}, 'output': [[5, 4, 11, 2], [5, 8, 4, 5]], 'explanation': 'Two paths sum to 22.'}],
        'tags': ['tree', 'backtracking', 'depth-first-search'],
        'test_cases': [{'input': [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22], 'expectedOutput': [[5, 4, 11, 2], [5, 8, 4, 5]]}, {'input': [[1, 2, 3], 5], 'expectedOutput': []}, {'input': [[1, 2], 0], 'expectedOutput': []}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pass''',
        "java_sig": '''class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        
    }
};''',
        "solution_python": '''# Solution for Path Sum II
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths that sum to target.

        Approach:
        - DFS backtracking
        - Maintain current path
        - At leaf, check if sum equals target
        - IMPORTANT: Copy path before adding to result

        Time: O(n) - visit each node once
        Space: O(h) for recursion stack
        """
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return

            # Add current node to path
            current_path.append(node.val)
            current_sum += node.val

            # Check if leaf node with target sum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(current_path[:])  # Must copy path

            # Recurse on children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            # Backtrack
            current_path.pop()

        dfs(root, [], 0)
        return result
''',
        "solution_java": '''// Solution for Path Sum II
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Path Sum II
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Path Sum II

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Construct Binary Tree from Preorder and Inorder Traversal',
        'leetcode_url': 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/',
        'difficulty': 'medium',
        "description": '''Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.''',
        'constraints': ['1 <= preorder.length <= 3000', 'inorder.length == preorder.length', '-3000 <= preorder[i], inorder[i] <= 3000', 'preorder and inorder consist of unique values'],
        'examples': [{'input': {'preorder': [3, 9, 20, 15, 7], 'inorder': [9, 3, 15, 20, 7]}, 'output': [3, 9, 20, None, None, 15, 7], 'explanation': 'Construct tree from traversals.'}],
        'tags': ['tree', 'array', 'hash-table', 'divide-and-conquer'],
        'test_cases': [{'input': [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], 'expectedOutput': [3, 9, 20, None, None, 15, 7]}, {'input': [[-1], [-1]], 'expectedOutput': [-1]}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass''',
        "java_sig": '''class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
    }
};''',
        "solution_python": '''# Solution for Construct Binary Tree from Preorder and Inorder Traversal
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct binary tree from preorder and inorder traversals.

        Approach:
        - Preorder: [root, left subtree, right subtree]
        - Inorder: [left subtree, root, right subtree]
        - Use first element of preorder as root
        - Find root in inorder to split left/right subtrees
        - Recursively build left and right subtrees

        Optimization:
        - Use hashmap for O(1) inorder index lookup (instead of O(n) search)
        - Track global preorder index
        - Pass inorder bounds to avoid array slicing

        Time: O(n) - visit each node once
        Space: O(n) - hashmap storage + O(h) recursion stack
        """
        if not preorder or not inorder:
            return None

        # Build hashmap: value -> index in inorder traversal
        # This allows O(1) lookup to find root position
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Track current position in preorder traversal
        self.preorder_idx = 0

        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            """
            Build tree for inorder range [in_left, in_right].
            Uses and advances self.preorder_idx.
            """
            # Base case: empty range
            if in_left > in_right:
                return None

            # Get root value from preorder and advance index
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            # Create root node
            root = TreeNode(root_val)

            # Find root position in inorder (O(1) with hashmap)
            in_root_idx = inorder_map[root_val]

            # Build left subtree: inorder range [in_left, in_root_idx - 1]
            # Must build left before right (preorder visits left first)
            root.left = build(in_left, in_root_idx - 1)

            # Build right subtree: inorder range [in_root_idx + 1, in_right]
            root.right = build(in_root_idx + 1, in_right)

            return root

        # Build entire tree: inorder range [0, n-1]
        return build(0, len(inorder) - 1)
''',
        "solution_java": '''// Solution for Construct Binary Tree from Preorder and Inorder Traversal
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Construct Binary Tree from Preorder and Inorder Traversal
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Construct Binary Tree from Preorder and Inorder Traversal

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Lowest Common Ancestor of a Binary Tree',
        'leetcode_url': 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/',
        'difficulty': 'medium',
        "description": '''Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).''',
        'constraints': ['The number of nodes in the tree is in the range [2, 10^5]', '-10^9 <= Node.val <= 10^9', 'All Node.val are unique', 'p != q', 'p and q exist in the tree'],
        'examples': [{'input': {'root': [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 'p': 5, 'q': 1}, 'output': 3, 'explanation': 'The LCA of nodes 5 and 1 is 3.'}],
        'tags': ['tree', 'depth-first-search', 'binary-tree'],
        'test_cases': [{'input': [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], 'expectedOutput': 3}, {'input': [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], 'expectedOutput': 5}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass''',
        "java_sig": '''class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
    }
};''',
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
        "solution_java": '''// Solution for Lowest Common Ancestor of a Binary Tree
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Lowest Common Ancestor of a Binary Tree
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Lowest Common Ancestor of a Binary Tree

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Number of Islands',
        'leetcode_url': 'https://leetcode.com/problems/number-of-islands/',
        'difficulty': 'medium',
        "description": '''Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.''',
        'constraints': ['m == grid.length', 'n == grid[i].length', '1 <= m, n <= 300', "grid[i][j] is '0' or '1'"],
        'examples': [{'input': {'grid': [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]}, 'output': 1, 'explanation': 'One connected island.'}],
        'tags': ['array', 'depth-first-search', 'breadth-first-search', 'union-find', 'matrix'],
        'test_cases': [{'input': [[['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]], 'expectedOutput': 1}, {'input': [[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]], 'expectedOutput': 3}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(m*n)',
        "python_sig": '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int numIslands(char[][] grid) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
    }
};''',
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
        "solution_java": '''// Solution for Number of Islands
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Number of Islands
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Number of Islands

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Course Schedule',
        'leetcode_url': 'https://leetcode.com/problems/course-schedule/',
        'difficulty': 'medium',
        "description": '''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return True if you can finish all courses. Otherwise, return False.''',
        'constraints': ['1 <= numCourses <= 2000', '0 <= prerequisites.length <= 5000', 'prerequisites[i].length == 2', '0 <= ai, bi < numCourses', 'All the pairs prerequisites[i] are unique'],
        'examples': [{'input': {'numCourses': 2, 'prerequisites': [[1, 0]]}, 'output': True, 'explanation': 'Take course 0 first, then course 1.'}, {'input': {'numCourses': 2, 'prerequisites': [[1, 0], [0, 1]]}, 'output': False, 'explanation': 'Circular dependency.'}],
        'tags': ['graph', 'topological-sort', 'depth-first-search', 'breadth-first-search'],
        'test_cases': [{'input': [2, [[1, 0]]], 'expectedOutput': True}, {'input': [2, [[1, 0], [0, 1]]], 'expectedOutput': False}],
        'time_complexity': 'O(V+E)',
        'space_complexity': 'O(V+E)',
        "python_sig": '''class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
    }
};''',
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
        "solution_java": '''// Solution for Course Schedule
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Course Schedule
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Course Schedule

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Clone Graph',
        'leetcode_url': 'https://leetcode.com/problems/clone-graph/',
        'difficulty': 'medium',
        "description": '''Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.''',
        'constraints': ['The number of nodes in the graph is in the range [0, 100]', '1 <= Node.val <= 100', 'Node.val is unique for each node', 'There are no repeated edges and no self-loops'],
        'examples': [{'input': {'adjList': [[2, 4], [1, 3], [2, 4], [1, 3]]}, 'output': [[2, 4], [1, 3], [2, 4], [1, 3]], 'explanation': 'Clone the graph.'}],
        'tags': ['hash-table', 'depth-first-search', 'breadth-first-search', 'graph'],
        'test_cases': [{'input': [[[2, 4], [1, 3], [2, 4], [1, 3]]], 'expectedOutput': [[2, 4], [1, 3], [2, 4], [1, 3]]}, {'input': [[[]]], 'expectedOutput': [[]]}, {'input': [[]], 'expectedOutput': []}],
        'time_complexity': 'O(N+M)',
        'space_complexity': 'O(N)',
        "python_sig": '''class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        pass''',
        "java_sig": '''class Solution {
    public Node cloneGraph(Node node) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    Node* cloneGraph(Node* node) {
        
    }
};''',
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
        "solution_java": '''// Solution for Clone Graph
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Clone Graph
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Clone Graph

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Word Search',
        'leetcode_url': 'https://leetcode.com/problems/word-search/',
        'difficulty': 'medium',
        "description": '''Given an m x n grid of characters board and a string word, return True if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.''',
        'constraints': ['m == board.length', 'n = board[i].length', '1 <= m, n <= 6', '1 <= word.length <= 15', 'board and word consists of only lowercase and uppercase English letters'],
        'examples': [{'input': {'board': [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'word': 'ABCCED'}, 'output': True, 'explanation': 'Word found in board.'}],
        'tags': ['array', 'backtracking', 'matrix'],
        'test_cases': [{'input': [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'], 'expectedOutput': True}, {'input': [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'], 'expectedOutput': True}, {'input': [[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'], 'expectedOutput': False}],
        'time_complexity': 'O(m*n*4^L)',
        'space_complexity': 'O(L)',
        "python_sig": '''class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean exist(char[][] board, String word) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
    }
};''',
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
        "solution_java": '''// Solution for Word Search
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Word Search
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Word Search

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Coin Change',
        'leetcode_url': 'https://leetcode.com/problems/coin-change/',
        'difficulty': 'medium',
        "description": '''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.''',
        'constraints': ['1 <= coins.length <= 12', '1 <= coins[i] <= 2^31 - 1', '0 <= amount <= 10^4'],
        'examples': [{'input': {'coins': [1, 2, 5], 'amount': 11}, 'output': 3, 'explanation': '11 = 5 + 5 + 1'}, {'input': {'coins': [2], 'amount': 3}, 'output': -1, 'explanation': 'Cannot make amount 3.'}],
        'tags': ['array', 'dynamic-programming', 'breadth-first-search'],
        'test_cases': [{'input': [[1, 2, 5], 11], 'expectedOutput': 3}, {'input': [[2], 3], 'expectedOutput': -1}, {'input': [[1], 0], 'expectedOutput': 0}],
        'time_complexity': 'O(amount * n)',
        'space_complexity': 'O(amount)',
        "python_sig": '''class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int coinChange(int[] coins, int amount) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
    }
};''',
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
        "solution_java": '''// Solution for Coin Change
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Coin Change
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Coin Change

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Longest Increasing Subsequence',
        'leetcode_url': 'https://leetcode.com/problems/longest-increasing-subsequence/',
        'difficulty': 'medium',
        'description': 'Given an integer array nums, return the length of the longest strictly increasing subsequence.',
        'constraints': ['1 <= nums.length <= 2500', '-10^4 <= nums[i] <= 10^4'],
        'examples': [{'input': {'nums': [10, 9, 2, 5, 3, 7, 101, 18]}, 'output': 4, 'explanation': 'The longest increasing subsequence is [2,3,7,101].'}, {'input': {'nums': [0, 1, 0, 3, 2, 3]}, 'output': 4, 'explanation': 'The longest increasing subsequence is [0,1,2,3].'}],
        'tags': ['array', 'binary-search', 'dynamic-programming'],
        'test_cases': [{'input': [[10, 9, 2, 5, 3, 7, 101, 18]], 'expectedOutput': 4}, {'input': [[0, 1, 0, 3, 2, 3]], 'expectedOutput': 4}, {'input': [[7, 7, 7, 7, 7, 7, 7]], 'expectedOutput': 1}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int lengthOfLIS(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
    }
};''',
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
        "solution_java": '''// Solution for Longest Increasing Subsequence
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Longest Increasing Subsequence
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Longest Increasing Subsequence

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Unique Paths',
        'leetcode_url': 'https://leetcode.com/problems/unique-paths/',
        'difficulty': 'medium',
        "description": '''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.''',
        'constraints': ['1 <= m, n <= 100'],
        'examples': [{'input': {'m': 3, 'n': 7}, 'output': 28, 'explanation': 'There are 28 unique paths.'}, {'input': {'m': 3, 'n': 2}, 'output': 3, 'explanation': 'From top-left: right->down->down, down->down->right, down->right->down'}],
        'tags': ['math', 'dynamic-programming', 'combinatorics'],
        'test_cases': [{'input': [3, 7], 'expectedOutput': 28}, {'input': [3, 2], 'expectedOutput': 3}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int uniquePaths(int m, int n) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int uniquePaths(int m, int n) {
        
    }
};''',
        "solution_python": '''# Solution for Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        2D Dynamic Programming with Space Optimization

        Problem: Count unique paths in m x n grid from top-left to bottom-right
        Constraint: Can only move right or down

        Key Insight:
        - dp[i][j] = number of ways to reach cell (i, j)
        - Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
          (paths from above + paths from left)
        - Base case: All cells in first row/column have exactly 1 path

        Space Optimization:
        - Full 2D DP would use O(m*n) space
        - We only need previous row to compute current row
        - Use single 1D array of size n, update in-place

        Time: O(m*n) - visit each cell once
        Space: O(n) - only store one row
        """
        # Initialize dp array representing one row
        # All positions in first row have 1 path (move right only)
        dp = [1] * n

        # Process each row starting from row 1
        for i in range(1, m):
            # For each column in current row
            for j in range(1, n):
                # dp[j] currently holds value from previous row (paths from above)
                # dp[j-1] holds value from current row (paths from left)
                # Sum them to get total paths to current cell
                dp[j] += dp[j - 1]

            # Note: dp[0] stays 1 (first column always has 1 path - move down only)

        # Bottom-right corner value is stored at dp[n-1]
        return dp[n - 1]
''',
        "solution_java": '''// Solution for Unique Paths
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Unique Paths
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Unique Paths

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Word Break',
        'leetcode_url': 'https://leetcode.com/problems/word-break/',
        'difficulty': 'medium',
        "description": '''Given a string s and a dictionary of strings wordDict, return True if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.''',
        'constraints': ['1 <= s.length <= 300', '1 <= wordDict.length <= 1000', '1 <= wordDict[i].length <= 20', 's and wordDict[i] consist of only lowercase English letters', 'All strings in wordDict are unique'],
        'examples': [{'input': {'s': 'leetcode', 'wordDict': ['leet', 'code']}, 'output': True, 'explanation': "'leetcode' can be segmented as 'leet code'."}, {'input': {'s': 'applepenapple', 'wordDict': ['apple', 'pen']}, 'output': True, 'explanation': "'applepenapple' can be segmented as 'apple pen apple'."}],
        'tags': ['hash-table', 'string', 'dynamic-programming', 'trie', 'memoization'],
        'test_cases': [{'input': ['leetcode', ['leet', 'code']], 'expectedOutput': True}, {'input': ['applepenapple', ['apple', 'pen']], 'expectedOutput': True}, {'input': ['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']], 'expectedOutput': False}],
        'time_complexity': 'O(n^2)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        
    }
};''',
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
        "solution_java": '''// Solution for Word Break
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Word Break
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Word Break

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'House Robber II',
        'leetcode_url': 'https://leetcode.com/problems/house-robber-ii/',
        'difficulty': 'medium',
        "description": '''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.''',
        'constraints': ['1 <= nums.length <= 100', '0 <= nums[i] <= 1000'],
        'examples': [{'input': {'nums': [2, 3, 2]}, 'output': 3, 'explanation': 'You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.'}, {'input': {'nums': [1, 2, 3, 1]}, 'output': 4, 'explanation': 'Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.'}],
        'tags': ['array', 'dynamic-programming'],
        'test_cases': [{'input': [[2, 3, 2]], 'expectedOutput': 3}, {'input': [[1, 2, 3, 1]], 'expectedOutput': 4}, {'input': [[1, 2, 3]], 'expectedOutput': 3}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def rob(self, nums: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int rob(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int rob(vector<int>& nums) {
        
    }
};''',
        "solution_python": '''class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber II - Houses arranged in a circle

        Key Insight: The circular constraint means we cannot rob both
        the first AND last house. This reduces the problem to:
        max(rob houses 0 to n-2, rob houses 1 to n-1)

        Each subproblem is solved using House Robber I logic (linear DP).

        Time Complexity: O(n) - two linear passes
        Space Complexity: O(1) - only track prev1 and prev2
        """
        n = len(nums)

        # Edge case: only one house - rob it
        if n == 1:
            return nums[0]

        # Edge case: two houses - rob the one with more money
        if n == 2:
            return max(nums[0], nums[1])

        # Helper function: House Robber I for a range [start, end)
        def rob_linear(start: int, end: int) -> int:
            """
            Rob houses from index start to end-1 (linear street).

            DP recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            - dp[i-1]: skip current house, take max up to previous
            - dp[i-2] + nums[i]: rob current house, add to max from 2 houses back

            Space optimization: only need prev1 (dp[i-1]) and prev2 (dp[i-2])
            """
            prev2 = 0  # dp[i-2]: max money 2 houses back
            prev1 = 0  # dp[i-1]: max money 1 house back

            for i in range(start, end):
                # Current choice: skip (prev1) or rob (prev2 + nums[i])
                current = max(prev1, prev2 + nums[i])

                # Shift variables for next iteration
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Rob houses 0 to n-2 (exclude last house)
        # This allows us to rob the first house if beneficial
        case1 = rob_linear(0, n - 1)

        # Case 2: Rob houses 1 to n-1 (exclude first house)
        # This allows us to rob the last house if beneficial
        case2 = rob_linear(1, n)

        # Return the maximum of both strategies
        return max(case1, case2)

    def solve(self, input):
        """Wrapper for test framework"""
        nums = input[0]
        return self.rob(nums)''',
        "solution_java": '''// Solution for House Robber II
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for House Robber II
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for House Robber II

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Decode Ways',
        'leetcode_url': 'https://leetcode.com/problems/decode-ways/',
        'difficulty': 'medium',
        "description": '''A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above. Given a string s containing only digits, return the number of ways to decode it.''',
        'constraints': ['1 <= s.length <= 100', 's contains only digits and may contain leading zero(s)'],
        'examples': [{'input': {'s': '12'}, 'output': 2, 'explanation': "It could be decoded as 'AB' (1 2) or 'L' (12)."}, {'input': {'s': '226'}, 'output': 3, 'explanation': "It could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6)."}],
        'tags': ['string', 'dynamic-programming'],
        'test_cases': [{'input': ['12'], 'expectedOutput': 2}, {'input': ['226'], 'expectedOutput': 3}, {'input': ['06'], 'expectedOutput': 0}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def numDecodings(self, s: str) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int numDecodings(String s) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int numDecodings(string s) {
        
    }
};''',
        "solution_python": '''# Solution for Decode Ways
# Optimal Algorithm: Bottom-up DP with space optimization
# Time: O(n), Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Count the number of ways to decode a digit string.

        Key Insight: Similar to climbing stairs, but with validation constraints.
        - Each position can contribute to 1-digit decode (if valid)
        - Each position can contribute to 2-digit decode (if valid with previous)

        DP Recurrence:
        dp[i] = number of ways to decode s[0:i]
        dp[i] = (dp[i-1] if s[i] is '1'-'9') + (dp[i-2] if s[i-1:i+1] is '10'-'26')

        Base Cases:
        - dp[0] = 1 (empty string has one way: decode nothing)
        - dp[1] = 1 if s[0] != '0', else 0 (single digit must be valid)

        Invalid Cases:
        - Leading zeros: "06" -> 0 ways (can't decode '0' alone)
        - Isolated zeros: "30" -> 0 ways ('0' must be paired with 1 or 2)
        """
        n = len(s)

        # Edge case: empty string or starts with '0'
        if n == 0 or s[0] == '0':
            return 0

        # Space optimization: only track dp[i-2] and dp[i-1]
        # prev2 = dp[i-2]: ways to decode up to 2 positions back
        # prev1 = dp[i-1]: ways to decode up to 1 position back
        prev2 = 1  # dp[0]: empty string has 1 way
        prev1 = 1  # dp[1]: first character is valid (checked above)

        # Process each position starting from index 1
        for i in range(1, n):
            current = 0  # dp[i]: ways to decode up to position i

            # Check 1-digit decode: s[i] alone
            # Valid if s[i] is '1' through '9' (not '0')
            one_digit = int(s[i])
            if 1 <= one_digit <= 9:
                current += prev1  # Add ways from dp[i-1]

            # Check 2-digit decode: s[i-1:i+1] together
            # Valid if value is between 10 and 26
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2  # Add ways from dp[i-2]

            # Shift variables for next iteration
            prev2 = prev1
            prev1 = current

        return prev1

    def solve(self, input):
        """Wrapper for test framework"""
        s = input[0]
        return self.numDecodings(s)''',
        "solution_java": '''// Solution for Decode Ways
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Decode Ways
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Decode Ways

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Letter Combinations of a Phone Number',
        'leetcode_url': 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
        'difficulty': 'medium',
        "description": '''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz''',
        'constraints': ['0 <= digits.length <= 4', "digits[i] is a digit in the range ['2', '9']"],
        'examples': [{'input': {'digits': '23'}, 'output': ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], 'explanation': 'All possible combinations.'}, {'input': {'digits': ''}, 'output': [], 'explanation': 'Empty input.'}],
        'tags': ['hash-table', 'string', 'backtracking'],
        'test_cases': [{'input': ['23'], 'expectedOutput': ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']}, {'input': [''], 'expectedOutput': []}, {'input': ['2'], 'expectedOutput': ['a', 'b', 'c']}],
        'time_complexity': 'O(4^n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass''',
        "java_sig": '''class Solution {
    public List<String> letterCombinations(String digits) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
    }
};''',
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
        "solution_java": '''// Solution for Letter Combinations of a Phone Number
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Letter Combinations of a Phone Number
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Letter Combinations of a Phone Number

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Generate Parentheses',
        'leetcode_url': 'https://leetcode.com/problems/generate-parentheses/',
        'difficulty': 'medium',
        "description": '''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.''',
        'constraints': ['1 <= n <= 8'],
        'examples': [{'input': {'n': 3}, 'output': ['((()))', '(()())', '(())()', '()(())', '()()()'], 'explanation': 'All valid combinations of 3 pairs.'}, {'input': {'n': 1}, 'output': ['()'], 'explanation': 'Only one combination.'}],
        'tags': ['string', 'dynamic-programming', 'backtracking'],
        'test_cases': [{'input': [3], 'expectedOutput': ['((()))', '(()())', '(())()', '()(())', '()()()']}, {'input': [1], 'expectedOutput': ['()']}],
        'time_complexity': 'O(4^n/sqrt(n))',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass''',
        "java_sig": '''class Solution {
    public List<String> generateParenthesis(int n) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
    }
};''',
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
        "solution_java": '''// Solution for Generate Parentheses
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Generate Parentheses
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Generate Parentheses

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Permutations',
        'leetcode_url': 'https://leetcode.com/problems/permutations/',
        'difficulty': 'medium',
        "description": '''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.''',
        'constraints': ['1 <= nums.length <= 6', '-10 <= nums[i] <= 10', 'All the integers of nums are unique'],
        'examples': [{'input': {'nums': [1, 2, 3]}, 'output': [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], 'explanation': 'All permutations.'}, {'input': {'nums': [0, 1]}, 'output': [[0, 1], [1, 0]], 'explanation': 'Two permutations.'}],
        'tags': ['array', 'backtracking'],
        'test_cases': [{'input': [[1, 2, 3]], 'expectedOutput': [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}, {'input': [[0, 1]], 'expectedOutput': [[0, 1], [1, 0]]}, {'input': [[1]], 'expectedOutput': [[1]]}],
        'time_complexity': 'O(n!)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass''',
        "java_sig": '''class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        
    }
};''',
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
        "solution_java": '''// Solution for Permutations
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Permutations
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Permutations

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Trapping Rain Water',
        'leetcode_url': 'https://leetcode.com/problems/trapping-rain-water/',
        'difficulty': 'hard',
        "description": '''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.''',
        'constraints': ['n == height.length', '1 <= n <= 2 * 10^4', '0 <= height[i] <= 10^5'],
        'examples': [{'input': {'height': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}, 'output': 6, 'explanation': 'The elevation map can trap 6 units of rain water.'}],
        'tags': ['array', 'two-pointers', 'dynamic-programming', 'stack', 'monotonic-stack'],
        'test_cases': [{'input': [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 'expectedOutput': 6}, {'input': [[4, 2, 0, 3, 2, 5]], 'expectedOutput': 9}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def trap(self, height: List[int]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int trap(int[] height) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int trap(vector<int>& height) {
        
    }
};''',
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
        "solution_java": '''// Solution for Trapping Rain Water
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Trapping Rain Water
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Trapping Rain Water

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Median of Two Sorted Arrays',
        'leetcode_url': 'https://leetcode.com/problems/median-of-two-sorted-arrays/',
        'difficulty': 'hard',
        "description": '''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).''',
        'constraints': ['nums1.length == m', 'nums2.length == n', '0 <= m <= 1000', '0 <= n <= 1000', '1 <= m + n <= 2000', '-10^6 <= nums1[i], nums2[i] <= 10^6'],
        'examples': [{'input': {'nums1': [1, 3], 'nums2': [2]}, 'output': 2.0, 'explanation': 'Merged array = [1,2,3], median = 2.'}, {'input': {'nums1': [1, 2], 'nums2': [3, 4]}, 'output': 2.5, 'explanation': 'Merged array = [1,2,3,4], median = (2+3)/2 = 2.5.'}],
        'tags': ['array', 'binary-search', 'divide-and-conquer'],
        'test_cases': [{'input': [[1, 3], [2]], 'expectedOutput': 2.0}, {'input': [[1, 2], [3, 4]], 'expectedOutput': 2.5}],
        'time_complexity': 'O(log(min(m,n)))',
        'space_complexity': 'O(1)',
        "python_sig": '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass''',
        "java_sig": '''class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
    }
};''',
        "solution_python": '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary Search Solution for Median of Two Sorted Arrays
        
        PROBLEM STATEMENT:
        Find the median of two sorted arrays in O(log(min(m,n))) time.
        
        KEY INSIGHT:
        Instead of merging arrays, we can use binary search to find the correct "partition point"
        that divides both arrays such that all elements on the left are <= all elements on the right.
        
        WHY BINARY SEARCH ON PARTITION POINTS WORKS:
        1. A median divides a sorted array into two equal halves
        2. For combined arrays, we need to partition both so that:
           - Total elements on left = Total elements on right (or differ by 1)
           - All left elements <= All right elements
        3. If we choose partition i in nums1, partition j in nums2 is determined:
           j = (m + n + 1) // 2 - i
        4. We binary search for the correct i value
        
        PARTITION VISUALIZATION:
        nums1: [1, 3, 8, 9, 15]  partition at i=2: [1, 3 | 8, 9, 15]
        nums2: [7, 11, 18, 19, 21, 25]  partition at j=4: [7, 11, 18, 19 | 21, 25]
        
        Combined left half: [1, 3, 7, 11, 18, 19]  (6 elements)
        Combined right half: [8, 9, 15, 21, 25]    (5 elements)
        
        Valid partition conditions:
        - nums1[i-1] <= nums2[j]  (nums1's left <= nums2's right)
        - nums2[j-1] <= nums1[i]  (nums2's left <= nums1's right)
        
        ALGORITHM STEPS:
        1. Ensure nums1 is the smaller array (minimize search space)
        2. Binary search on nums1's partition point (i)
        3. Calculate corresponding partition in nums2 (j)
        4. Check if partition is valid
        5. If valid, calculate median from boundary elements
        6. If invalid, adjust binary search range
        
        TIME COMPLEXITY: O(log(min(m,n))) - binary search on smaller array
        SPACE COMPLEXITY: O(1) - only using variables
        """
        
        # Step 1: Ensure nums1 is the smaller array for optimal binary search
        # This minimizes our search space to log(min(m,n))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        
        # Step 2: Binary search on nums1's partition point
        # We search for position i where:
        # - i represents number of elements from nums1 in left partition
        # - Range: [0, m] (we can take 0 to all elements from nums1)
        left, right = 0, m
        
        while left <= right:
            # Step 3: Choose partition point i in nums1
            # This determines how many elements from nums1 go to left half
            i = (left + right) // 2
            
            # Step 4: Calculate partition point j in nums2
            # Total elements in left half should be (m+n+1)//2
            # If we take i from nums1, we need j = (m+n+1)//2 - i from nums2
            # The +1 handles both odd and even length cases correctly
            j = (m + n + 1) // 2 - i
            
            # Step 5: Get boundary elements around partitions
            # Use -infinity and +infinity for edge cases (partition at start/end)
            
            # Left side of nums1's partition (largest element in nums1's left half)
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            
            # Right side of nums1's partition (smallest element in nums1's right half)
            nums1_right = float('inf') if i == m else nums1[i]
            
            # Left side of nums2's partition (largest element in nums2's left half)
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            
            # Right side of nums2's partition (smallest element in nums2's right half)
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Step 6: Check if this partition is valid
            # Valid partition means: all left elements <= all right elements
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # VALID PARTITION FOUND!
                
                # Step 7: Calculate median based on total length (odd vs even)
                if (m + n) % 2 == 0:
                    # Even total length: median = average of two middle elements
                    # Left middle = max of left boundaries
                    # Right middle = min of right boundaries
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                else:
                    # Odd total length: median = largest element in left half
                    # This works because left half has one more element than right
                    return float(max(nums1_left, nums2_left))
            
            # Step 8: Adjust binary search based on partition validity
            elif nums1_left > nums2_right:
                # nums1's left side is too large
                # We have too many elements from nums1 in left partition
                # Move partition i to the left (take fewer from nums1)
                right = i - 1
            else:
                # nums2_left > nums1_right
                # nums1's left side is too small
                # We have too few elements from nums1 in left partition
                # Move partition i to the right (take more from nums1)
                left = i + 1
        
        # Should never reach here if inputs are valid sorted arrays
        raise ValueError("Input arrays are not sorted or invalid")
''',
        "solution_java": '''// Solution for Median of Two Sorted Arrays
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Median of Two Sorted Arrays
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Median of Two Sorted Arrays

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Binary Tree Maximum Path Sum',
        'leetcode_url': 'https://leetcode.com/problems/binary-tree-maximum-path-sum/',
        'difficulty': 'hard',
        "description": '''A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.''',
        'constraints': ['The number of nodes in the tree is in the range [1, 3 * 10^4]', '-1000 <= Node.val <= 1000'],
        'examples': [{'input': {'root': [1, 2, 3]}, 'output': 6, 'explanation': 'The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.'}, {'input': {'root': [-10, 9, 20, None, None, 15, 7]}, 'output': 42, 'explanation': 'The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.'}],
        'tags': ['tree', 'depth-first-search', 'dynamic-programming', 'binary-tree'],
        'test_cases': [{'input': [[1, 2, 3]], 'expectedOutput': 6}, {'input': [[-10, 9, 20, None, None, 15, 7]], 'expectedOutput': 42}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(h)',
        "python_sig": '''class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int maxPathSum(TreeNode root) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int maxPathSum(TreeNode* root) {
        
    }
};''',
        "solution_python": '''# Binary Tree Maximum Path Sum - Post-Order DFS Solution
# Time Complexity: O(n) - visit each node exactly once
# Space Complexity: O(h) - recursion stack depth equals tree height

"""
PROBLEM INTUITION:
We need to find the maximum path sum in a binary tree where:
1. A path is any sequence of connected nodes (doesn't need to go through root)
2. Each node can appear at most once in the path
3. The path can start and end at any node

KEY INSIGHT: Post-Order Traversal is Essential
We use post-order DFS because we need information from children BEFORE
making decisions at the parent. This is a bottom-up dynamic programming approach.

CRITICAL DISTINCTION (This is where most people get confused):
For each node, we track TWO different values:
1. "Path through this node" = node.val + left_sum + right_sum
   - This uses BOTH children (forms an inverted V-shape: left->node->right)
   - Can be a candidate for the global maximum
   - CANNOT be returned to parent (already used both branches)

2. "Path to parent" = node.val + max(left_sum, right_sum)
   - Uses only ONE child (forms a single line that can extend upward)
   - Can be extended by the parent node
   - This is what we RETURN

Example visualization:
       10
      /  \
     2    10
    / \     \
   20  1    -25
              /  \
             3    4

At node 10 (root):
- left_sum from left child = 20 (best path going up from left subtree)
- right_sum from right child = 10 (best path going up from right subtree)
- path_through_node = 10 + 20 + 10 = 40 (uses both children)
- return to parent = 10 + max(20, 10) = 30 (uses only best child)

HANDLING NEGATIVE VALUES:
Use max(0, child_sum) to exclude negative paths. If a subtree has negative
sum, it's better to NOT include it in our path. This is equivalent to
"cutting off" the negative branch.

Example with negative values:
       -10
       /  \
      9   20
         /  \
        15   7

At node 20:
- left_sum = 15, right_sum = 7
- path_through_node = 20 + 15 + 7 = 42 (this becomes our answer)
- At root -10, we would exclude it since adding -10 makes things worse
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize global maximum to smallest possible value
        # This handles the case where all values are negative (we must include at least one node)
        self.max_sum = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            """
            Post-order DFS that returns the maximum path sum going UP from this node.
            
            Returns:
                The maximum sum of a path that:
                - Starts at this node
                - Goes through AT MOST ONE of its children (can extend upward)
                - Could be just the node itself if both children are negative
            
            Side Effect:
                Updates self.max_sum with the maximum path sum that goes THROUGH this node
                (which may use both children)
            """
            # Base case: null nodes contribute 0 to any path
            if not node:
                return 0
            
            # Recursively get maximum path sums from left and right subtrees
            # Post-order: process children before parent
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # CRITICAL: Use max(0, sum) to exclude negative paths
            # If a subtree has negative sum, better to not include it (equivalent to pruning)
            # This handles cases like: node=10, left_sum=-5 -> we take 10+0 instead of 10+(-5)
            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)
            
            # Calculate the maximum path sum that goes THROUGH this node
            # This path uses the node and potentially BOTH children (forms inverted V)
            # Four possible paths through this node:
            #   1. Just the node (both children excluded/negative)
            #   2. Node + left_sum (right excluded/negative)
            #   3. Node + right_sum (left excluded/negative)
            #   4. Node + left_sum + right_sum (both children included)
            # Because we already excluded negatives, we can safely add both
            path_through_node = node.val + left_sum + right_sum
            
            # Update global maximum if this path is better than anything we've seen
            # This is a CANDIDATE for the final answer
            self.max_sum = max(self.max_sum, path_through_node)
            
            # Return the maximum path sum going UP from this node
            # We can only use ONE child (left OR right) because the parent might
            # want to extend this path upward (can't branch in multiple directions)
            # Three possible return values:
            #   1. Just the node (if both children are negative/excluded)
            #   2. Node + left_sum (if left is better)
            #   3. Node + right_sum (if right is better)
            return node.val + max(left_sum, right_sum)
        
        # Start DFS from root
        dfs(root)
        
        # Return the global maximum found
        # This could be a path anywhere in the tree (not necessarily through root)
        return self.max_sum
    
    def solve(self, input):
        """
        Wrapper method for validation framework.
        Input format: List of tree nodes [root_array]
        """
        # Input is a list containing one element: the tree array
        tree_array = input[0]
        
        # Build tree from array representation
        root = self._build_tree(tree_array)
        
        # Solve and return result
        return self.maxPathSum(root)
    
    def _build_tree(self, values):
        """Build binary tree from level-order list representation."""
        if not values:
            return None
        
        from collections import deque
        
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root


"""
COMPLEXITY ANALYSIS:

Time Complexity: O(n)
- We visit each node exactly once in the DFS traversal
- At each node, we perform O(1) operations (comparisons and additions)
- Therefore, total time is O(n) where n is the number of nodes

Space Complexity: O(h)
- The space is used by the recursion call stack
- In the worst case (skewed tree), the height h = n, giving O(n) space
- In the best case (balanced tree), the height h = log(n), giving O(log n) space
- Average case for a balanced binary tree: O(log n)

EDGE CASES HANDLED:
1. Single node tree: Returns the node value
2. All negative values: Returns the least negative value (must include at least one node)
3. Skewed tree (like a linked list): Works correctly with O(n) space
4. Path doesn't include root: Algorithm finds it correctly
5. Optimal path uses both children of a node: Tracked in path_through_node
6. Mixed positive and negative values: max(0, sum) excludes negative branches

COMMON MISTAKES TO AVOID:
1. Forgetting to use max(0, child_sum) to exclude negative paths
2. Confusing "path through node" with "path to parent"
3. Returning the wrong value (should return path extending upward, not max path)
4. Not initializing max_sum to -infinity (fails when all values are negative)
5. Trying to use both children in the return value (breaks the path constraint)

INTERVIEW TIPS:
1. Draw out the tree and trace through the algorithm
2. Explain the difference between local max (through node) and return value (to parent)
3. Explain why post-order traversal is necessary
4. Discuss the negative value handling
5. Mention the time/space complexity clearly
"""''',
        "solution_java": '''// Solution for Binary Tree Maximum Path Sum
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Binary Tree Maximum Path Sum
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Binary Tree Maximum Path Sum

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Serialize and Deserialize Binary Tree',
        'leetcode_url': 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/',
        'difficulty': 'hard',
        "description": '''Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.''',
        'constraints': ['The number of nodes in the tree is in the range [0, 10^4]', '-1000 <= Node.val <= 1000'],
        'examples': [{'input': {'root': [1, 2, 3, None, None, 4, 5]}, 'output': [1, 2, 3, None, None, 4, 5], 'explanation': 'Serialize then deserialize the tree.'}],
        'tags': ['string', 'tree', 'depth-first-search', 'breadth-first-search', 'design', 'binary-tree'],
        'test_cases': [{'input': [[1, 2, 3, None, None, 4, 5]], 'expectedOutput': [1, 2, 3, None, None, 4, 5]}, {'input': [[]], 'expectedOutput': []}],
        'time_complexity': 'O(n)',
        'space_complexity': 'O(n)',
        "python_sig": '''class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass''',
        "java_sig": '''public class Codec {
    public String serialize(TreeNode root) {
        
    }
    
    public TreeNode deserialize(String data) {
        
    }
}''',
        "cpp_sig": '''class Codec {
public:
    string serialize(TreeNode* root) {
        
    }
    
    TreeNode* deserialize(string data) {
        
    }
};''',
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
        "solution_java": '''// Solution for Serialize and Deserialize Binary Tree
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Serialize and Deserialize Binary Tree
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Serialize and Deserialize Binary Tree

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Regular Expression Matching',
        'leetcode_url': 'https://leetcode.com/problems/regular-expression-matching/',
        'difficulty': 'hard',
        "description": '''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).''',
        'constraints': ['1 <= s.length <= 20', '1 <= p.length <= 20', 's contains only lowercase English letters', "p contains only lowercase English letters, '.', and '*'"],
        'examples': [{'input': {'s': 'aa', 'p': 'a'}, 'output': False, 'explanation': 'a does not match the entire string aa.'}, {'input': {'s': 'aa', 'p': 'a*'}, 'output': True, 'explanation': '* means zero or more of the preceding element, a. Therefore, by repeating a once, it becomes aa.'}],
        'tags': ['string', 'dynamic-programming', 'recursion'],
        'test_cases': [{'input': ['aa', 'a'], 'expectedOutput': False}, {'input': ['aa', 'a*'], 'expectedOutput': True}, {'input': ['ab', '.*'], 'expectedOutput': True}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(m*n)',
        "python_sig": '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass''',
        "java_sig": '''class Solution {
    public boolean isMatch(String s, String p) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    bool isMatch(string s, string p) {
        
    }
};''',
        "solution_python": '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        2D Dynamic Programming for Regular Expression Matching.
        Matches string 's' against pattern 'p' with '.' and '*' operators.
        
        WHY 2D DP?
        - Subproblem structure: Match status of s[0:i] vs p[0:j] depends on
          previous subproblems (smaller prefixes)
        - Optimal substructure: dp[i][j] built from dp[i-1][j-1], dp[i-1][j], etc.
        - Overlapping subproblems: Same prefixes checked multiple times
        
        KEY INSIGHTS:
        1. '.' operator: Matches ANY single character (simple substitution)
        2. '*' operator: Matches ZERO or MORE of the PRECEDING character
           - Think of 'a*' as a UNIT (not separate 'a' and '*')
           - p[j-2] is the char that '*' modifies (p[j-1] is the '*')
        3. For '*', we have TWO choices:
           a) Use ZERO occurrences: dp[i][j-2] (skip char + '*')
           b) Use ONE+ occurrences: dp[i-1][j] IF chars match
        
        DP RECURRENCE RELATION:
        - dp[i][j] = True if s[0:i] matches p[0:j]
        - Base case: dp[0][0] = True (empty matches empty)
        - Base case: dp[0][j] = handle patterns like "a*b*" (can match empty)
        
        Algorithm:
        1. Create (m+1) x (n+1) DP table
        2. Initialize base cases
        3. For each cell dp[i][j]:
           - If p[j-1] is '*': combine zero-occurrence OR one+-occurrence
           - Else: match current chars and use dp[i-1][j-1]
        
        Time Complexity: O(m * n) where m = len(s), n = len(p)
        Space Complexity: O(m * n) for DP table (can optimize to O(n))
        """
        m, n = len(s), len(p)
        
        # dp[i][j] = does s[0:i] match p[0:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: Handle patterns that can match empty string
        # Pattern like "a*", "a*b*", "a*b*c*" can match empty string
        # The '*' makes preceding character optional (zero occurrences)
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                # '*' can make preceding char disappear
                dp[0][j] = dp[0][j - 2]
        
        # Helper function: check if two characters match
        def matches(s_char: str, p_char: str) -> bool:
            """Check if pattern character matches string character."""
            return p_char == '.' or s_char == p_char
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' operator: MODIFIES the PRECEDING character p[j-2]
                    # Two choices:
                    
                    # Choice 1: Use ZERO occurrences of preceding char
                    # Skip both the character and '*' in pattern
                    # Example: "ab" matches "abc*" by ignoring "c*"
                    dp[i][j] = dp[i][j - 2]
                    
                    # Choice 2: Use ONE or MORE occurrences
                    # Check if current string char matches the char before '*'
                    # If match, we can "consume" one char from string and
                    # keep the "char*" pattern (for more matches)
                    # Example: "aaa" matches "a*" by consuming each 'a'
                    if matches(s[i - 1], p[j - 2]):
                        # dp[i-1][j] means: we matched one char from string,
                        # but keep the "char*" pattern for potential more matches
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                else:
                    # Regular character or '.' operator
                    # Must match current characters exactly (or '.' wildcard)
                    if matches(s[i - 1], p[j - 1]):
                        # Both chars match: inherit result from previous state
                        dp[i][j] = dp[i - 1][j - 1]
        
        # Final answer: does full string match full pattern?
        return dp[m][n]
''',
        "solution_java": '''// Solution for Regular Expression Matching
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Regular Expression Matching
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Regular Expression Matching

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Edit Distance',
        'leetcode_url': 'https://leetcode.com/problems/edit-distance/',
        'difficulty': 'hard',
        "description": '''Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character''',
        'constraints': ['0 <= word1.length, word2.length <= 500', 'word1 and word2 consist of lowercase English letters'],
        'examples': [{'input': {'word1': 'horse', 'word2': 'ros'}, 'output': 3, 'explanation': "horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e')"}, {'input': {'word1': 'intention', 'word2': 'execution'}, 'output': 5, 'explanation': "intention -> inention (remove 't') -> enention (replace 'i' with 'e') -> exention (replace 'n' with 'x') -> exection (replace 'n' with 'c') -> execution (insert 'u')"}],
        'tags': ['string', 'dynamic-programming'],
        'test_cases': [{'input': ['horse', 'ros'], 'expectedOutput': 3}, {'input': ['intention', 'execution'], 'expectedOutput': 5}],
        'time_complexity': 'O(m*n)',
        'space_complexity': 'O(m*n)',
        "python_sig": '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int minDistance(String word1, String word2) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int minDistance(string word1, string word2) {
        
    }
};''',
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
        "solution_java": '''// Solution for Edit Distance
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Edit Distance
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Edit Distance

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Word Ladder',
        'leetcode_url': 'https://leetcode.com/problems/word-ladder/',
        'difficulty': 'hard',
        "description": '''A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.''',
        'constraints': ['1 <= beginWord.length <= 10', 'endWord.length == beginWord.length', '1 <= wordList.length <= 5000', 'wordList[i].length == beginWord.length', 'All strings consist of lowercase English letters', 'beginWord != endWord', 'All the words in wordList are unique'],
        'examples': [{'input': {'beginWord': 'hit', 'endWord': 'cog', 'wordList': ['hot', 'dot', 'dog', 'lot', 'log', 'cog']}, 'output': 5, 'explanation': "One shortest transformation sequence is 'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog', which is 5 words long."}, {'input': {'beginWord': 'hit', 'endWord': 'cog', 'wordList': ['hot', 'dot', 'dog', 'lot', 'log']}, 'output': 0, 'explanation': "The endWord 'cog' is not in wordList, therefore there is no valid transformation sequence."}],
        'tags': ['hash-table', 'string', 'breadth-first-search'],
        'test_cases': [{'input': ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']], 'expectedOutput': 5}, {'input': ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']], 'expectedOutput': 0}],
        'time_complexity': 'O(M^2 * N)',
        'space_complexity': 'O(M^2 * N)',
        "python_sig": '''class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass''',
        "java_sig": '''class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
    }
};''',
        "solution_python": '''# Solution for Word Ladder
# Implement the optimal algorithm here
class Solution:
    def solve(self, input):
        # TODO: Implement solution
        pass''',
        "solution_java": '''// Solution for Word Ladder
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Word Ladder
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Word Ladder

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    },
    {
        'title': 'Merge k Sorted Lists',
        'leetcode_url': 'https://leetcode.com/problems/merge-k-sorted-lists/',
        'difficulty': 'hard',
        "description": '''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.''',
        'constraints': ['k == lists.length', '0 <= k <= 10^4', '0 <= lists[i].length <= 500', '-10^4 <= lists[i][j] <= 10^4', 'lists[i] is sorted in ascending order', 'The sum of lists[i].length will not exceed 10^4'],
        'examples': [{'input': {'lists': [[1, 4, 5], [1, 3, 4], [2, 6]]}, 'output': [1, 1, 2, 3, 4, 4, 5, 6], 'explanation': 'Merging all lists: [1,4,5], [1,3,4], and [2,6] into one sorted list.'}, {'input': {'lists': []}, 'output': [], 'explanation': 'Empty input.'}, {'input': {'lists': [[]]}, 'output': [], 'explanation': 'Single empty list.'}],
        'tags': ['linked-list', 'divide-and-conquer', 'heap', 'merge-sort'],
        'test_cases': [{'input': [[[1, 4, 5], [1, 3, 4], [2, 6]]], 'expectedOutput': [1, 1, 2, 3, 4, 4, 5, 6]}, {'input': [[]], 'expectedOutput': []}, {'input': [[[]]], 'expectedOutput': []}],
        'time_complexity': 'O(N log k) where N is total number of nodes',
        'space_complexity': 'O(k) for heap or O(log k) for divide-and-conquer',
        "python_sig": '''class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass''',
        "java_sig": '''class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
    }
}''',
        "cpp_sig": '''class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
    }
};''',
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
        "solution_java": '''// Solution for Merge k Sorted Lists
class Solution {
    public returnType solve(inputType input) {
        // TODO: Implement solution
        return None;
    }
}''',
        "solution_cpp": '''// Solution for Merge k Sorted Lists
class Solution {
public:
    returnType solve(inputType input) {
        // TODO: Implement solution
        return {};
    }
};''',
        "solution_explanation": '''## Solution for Merge k Sorted Lists

### Approach
Optimal approach based on problem type

### Complexity Analysis
- **Time Complexity**: O(?)
- **Space Complexity**: O(?)''',
    }
]
