# LeetCode Solutions Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement 10 priority LeetCode solutions with educational depth and automated validation.

**Architecture:** Replace placeholder `solve(self, input): pass` methods with proper implementations using correct method signatures. Create validation script to verify all solutions pass their test cases before regenerating database.

**Tech Stack:** Python 3, standard library, algorithm implementations

---

## Task 1: Create Validation Script Foundation

**Files:**
- Create: `scripts/validate_solutions.py`

**Step 1: Create validation script structure**

Create `scripts/validate_solutions.py`:

```python
#!/usr/bin/env python3
"""
Validation script for LeetCode solutions
Executes solutions against test cases and reports results
"""

import re
import sys
from typing import List, Optional, Any


def extract_method_name(python_sig: str) -> str:
    """Extract method name from python signature string."""
    # Pattern: def methodName(self, ...
    match = re.search(r'def\s+(\w+)\s*\(', python_sig)
    if match:
        return match.group(1)
    raise ValueError(f"Could not extract method name from: {python_sig}")


def validate_solution(question: dict) -> tuple[bool, list[str]]:
    """
    Validate a single question's solution against its test cases.

    Returns:
        (all_passed, error_messages)
    """
    title = question['title']
    solution_code = question.get('solution_python', '')
    python_sig = question.get('python_sig', '')
    test_cases = question.get('test_cases', [])

    # Skip if placeholder solution
    if 'TODO: Implement solution' in solution_code:
        return False, [f"Skipped - placeholder solution"]

    errors = []

    try:
        # Extract method name
        method_name = extract_method_name(python_sig)

        # Execute solution code to define the class
        exec(solution_code, globals())

        # Create instance
        solution = Solution()

        # Verify method exists
        if not hasattr(solution, method_name):
            return False, [f"Method '{method_name}' not found in solution"]

        # Run test cases
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case['input']
            expected = test_case['expectedOutput']

            # Call the method with unpacked inputs
            method = getattr(solution, method_name)
            actual = method(*test_input)

            # Compare results
            if actual != expected:
                errors.append(
                    f"  Test {i} FAILED:\n"
                    f"    Input: {test_input}\n"
                    f"    Expected: {expected}\n"
                    f"    Got: {actual}"
                )

        return len(errors) == 0, errors

    except Exception as e:
        return False, [f"  Error: {str(e)}"]


def main():
    """Main validation entry point."""
    # Import questions data
    sys.path.insert(0, '/home/yannik/Work/interview-prep-platform/.worktrees/experimental/scripts')
    from questions_data_full import LEETCODE_QUESTIONS

    # Questions to validate
    target_questions = [
        'Product of Array Except Self',
        'Maximum Subarray',
        'Number of Islands',
        'Coin Change',
        'Binary Tree Level Order Traversal',
        'Validate Binary Search Tree',
        'Longest Increasing Subsequence',
        'Course Schedule',
        'Clone Graph',
        'Trapping Rain Water'
    ]

    print("=" * 60)
    print("LeetCode Solutions Validation")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    for question in LEETCODE_QUESTIONS:
        if question['title'] not in target_questions:
            continue

        title = question['title']
        print(f"Testing: {title}")

        success, errors = validate_solution(question)

        if success:
            num_tests = len(question.get('test_cases', []))
            print(f"  ✓ All {num_tests} test cases passed")
            passed += 1
        else:
            print(f"  ✗ FAILED")
            for error in errors:
                print(error)
            failed += 1

        print()

    print("=" * 60)
    print(f"Summary: {passed}/{passed + failed} solutions passing")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
```

**Step 2: Test the validation script structure**

Run: `python3 scripts/validate_solutions.py`

Expected: Should run but show all 10 solutions as "Skipped - placeholder solution"

**Step 3: Commit validation script**

```bash
git add scripts/validate_solutions.py
git commit -m "feat: add validation script for LeetCode solutions

- Extracts method names from python signatures
- Executes solutions against test cases
- Reports pass/fail with detailed errors
- Targets 10 priority questions"
```

---

## Task 2: Implement Product of Array Except Self

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Product of Array Except Self" section, around line 1258)

**Step 1: Locate the question**

Search for: `"title": 'Product of Array Except Self'`

Current broken solution (around line 1258):
```python
"solution_python": '# Solution for Product of Array Except Self\n# Implement the optimal algorithm here\nclass Solution:\n    def solve(self, input):\n        # TODO: Implement solution\n        pass',
```

**Step 2: Replace with working solution**

Replace the `solution_python` value with:

```python
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
```

**Step 3: Run validation for this solution**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Product of Array"`

Expected: `✓ All 3 test cases passed`

**Step 4: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Product of Array Except Self solution

- Uses prefix/suffix product technique
- O(n) time, O(1) space (excluding output)
- Includes educational comments explaining approach"
```

---

## Task 3: Implement Maximum Subarray

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Maximum Subarray" section, around line 1868)

**Step 1: Locate and replace solution**

Search for: `"title": 'Maximum Subarray'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Maximum Subarray"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Maximum Subarray solution (Kadane's Algorithm)

- Classic DP approach for maximum contiguous subarray sum
- O(n) time, O(1) space
- Includes explanation of key insight"
```

---

## Task 4: Implement Binary Tree Level Order Traversal

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Binary Tree Level Order Traversal" section, around line 2210)

**Step 1: Locate and replace solution**

Search for: `"title": 'Binary Tree Level Order Traversal'`

Replace `solution_python` with:

```python
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
```

**Step 2: Update validation script for tree structures**

We need to add TreeNode definition to validation script. Update `scripts/validate_solutions.py`:

After the imports, add:

```python
# Tree node definition for tree-based problems
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build binary tree from level-order list representation."""
    if not values:
        return None

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
```

Then update the `validate_solution` function to handle tree inputs. Replace the test execution section with:

```python
        # Run test cases
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case['input']
            expected = test_case['expectedOutput']

            # Handle tree-based inputs (convert list to TreeNode)
            if 'Tree' in title and test_input and isinstance(test_input[0], list):
                test_input = [build_tree_from_list(test_input[0])] + test_input[1:]

            # Call the method with unpacked inputs
            method = getattr(solution, method_name)
            actual = method(*test_input)

            # Compare results
            if actual != expected:
                errors.append(
                    f"  Test {i} FAILED:\n"
                    f"    Input: {test_case['input']}\n"
                    f"    Expected: {expected}\n"
                    f"    Got: {actual}"
                )
```

Also add `from collections import deque` to the imports at top of validate_solutions.py.

**Step 3: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Binary Tree Level"`

Expected: `✓ All test cases passed`

**Step 4: Commit**

```bash
git add scripts/questions_data_full.py scripts/validate_solutions.py
git commit -m "feat: implement Binary Tree Level Order Traversal + tree validation

Solution:
- BFS approach using queue
- O(n) time, O(w) space where w is tree width

Validation:
- Add TreeNode class definition
- Add tree builder from level-order list
- Handle tree inputs in test runner"
```

---

## Task 5: Implement Validate Binary Search Tree

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Validate Binary Search Tree" section, around line 2288)

**Step 1: Locate and replace solution**

Search for: `"title": 'Validate Binary Search Tree'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Validate Binary Search"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Validate Binary Search Tree solution

- Recursive approach with min/max bounds
- O(n) time, O(h) space for recursion stack
- Handles edge case of duplicate values correctly"
```

---

## Task 6: Implement Number of Islands

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Number of Islands" section, around line 2909)

**Step 1: Locate and replace solution**

Search for: `"title": 'Number of Islands'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Number of Islands"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Number of Islands solution

- DFS approach to find connected components
- O(m*n) time and space complexity
- Modifies grid in-place to mark visited cells"
```

---

## Task 7: Implement Coin Change

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Coin Change" section, around line 3343)

**Step 1: Locate and replace solution**

Search for: `"title": 'Coin Change'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Coin Change"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Coin Change solution

- Bottom-up DP approach
- O(amount * coins) time, O(amount) space
- Handles impossible cases returning -1"
```

---

## Task 8: Implement Longest Increasing Subsequence

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Longest Increasing Subsequence" section, around line 3443)

**Step 1: Locate and replace solution**

Search for: `"title": 'Longest Increasing Subsequence'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Longest Increasing"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Longest Increasing Subsequence solution

- DP with binary search (Patience Sort approach)
- O(n log n) time, O(n) space
- Optimal algorithm with detailed explanation"
```

---

## Task 9: Implement Course Schedule

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Course Schedule" section, around line 2999)

**Step 1: Locate and replace solution**

Search for: `"title": 'Course Schedule'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Course Schedule"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Course Schedule solution

- DFS-based cycle detection for topological sort
- O(V+E) time and space complexity
- Uses state tracking to detect cycles efficiently"
```

---

## Task 10: Implement Clone Graph

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Clone Graph" section, around line 3127)

**Step 1: Update validation script for graph structures**

First, add Node class definition to `scripts/validate_solutions.py`:

After TreeNode definition, add:

```python
# Graph node definition for graph-based problems
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def build_graph_from_adjacency_list(adj_list: List[List[int]]) -> Optional[Node]:
    """Build graph from adjacency list representation."""
    if not adj_list:
        return None

    # Create all nodes first
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    # Connect neighbors
    for i, neighbors in enumerate(adj_list):
        node = nodes[i + 1]
        node.neighbors = [nodes[neighbor] for neighbor in neighbors]

    return nodes.get(1)

def graph_to_adjacency_list(node: Optional[Node]) -> List[List[int]]:
    """Convert graph to adjacency list for comparison."""
    if not node:
        return []

    visited = {}

    def dfs(n: Node):
        if n.val in visited:
            return
        visited[n.val] = [neighbor.val for neighbor in n.neighbors]
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)

    # Convert to list format
    if not visited:
        return []
    max_val = max(visited.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in visited.items():
        result[val - 1] = sorted(neighbors)

    return result
```

Then update the test execution in `validate_solution` to handle graphs:

```python
        # Run test cases
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case['input']
            expected = test_case['expectedOutput']

            # Handle tree-based inputs (convert list to TreeNode)
            if 'Tree' in title and test_input and isinstance(test_input[0], list):
                test_input = [build_tree_from_list(test_input[0])] + test_input[1:]

            # Handle graph-based inputs (convert adjacency list to Node)
            if 'Graph' in title and test_input and isinstance(test_input[0], list):
                test_input = [build_graph_from_adjacency_list(test_input[0])]

            # Call the method with unpacked inputs
            method = getattr(solution, method_name)
            actual = method(*test_input)

            # Handle graph output (convert back to adjacency list)
            if 'Graph' in title and actual is not None:
                actual = graph_to_adjacency_list(actual)

            # Compare results
            if actual != expected:
                errors.append(
                    f"  Test {i} FAILED:\n"
                    f"    Input: {test_case['input']}\n"
                    f"    Expected: {expected}\n"
                    f"    Got: {actual}"
                )
```

**Step 2: Locate and replace solution**

Search for: `"title": 'Clone Graph'`

Replace `solution_python` with:

```python
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
```

**Step 3: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Clone Graph"`

Expected: `✓ All test cases passed`

**Step 4: Commit**

```bash
git add scripts/questions_data_full.py scripts/validate_solutions.py
git commit -m "feat: implement Clone Graph solution + graph validation

Solution:
- DFS with hash map for deep copy
- O(V+E) time and space complexity

Validation:
- Add Node class for graphs
- Add graph builder from adjacency list
- Add graph to adjacency list converter"
```

---

## Task 11: Implement Trapping Rain Water

**Files:**
- Modify: `scripts/questions_data_full.py` (find "Trapping Rain Water" section, around line 4124)

**Step 1: Locate and replace solution**

Search for: `"title": 'Trapping Rain Water'`

Replace `solution_python` with:

```python
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
```

**Step 2: Validate**

Run: `python3 scripts/validate_solutions.py | grep -A 5 "Trapping Rain Water"`

Expected: `✓ All test cases passed`

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Trapping Rain Water solution

- Two-pointer technique for optimal solution
- O(n) time, O(1) space complexity
- Detailed explanation of water trapping logic"
```

---

## Task 12: Run Final Validation

**Step 1: Run complete validation**

Run: `python3 scripts/validate_solutions.py`

Expected output:
```
============================================================
LeetCode Solutions Validation
============================================================

Testing: Product of Array Except Self
  ✓ All 3 test cases passed

Testing: Maximum Subarray
  ✓ All X test cases passed

... (all 10 solutions)

============================================================
Summary: 10/10 solutions passing (100%)
============================================================
```

**Step 2: Fix any failures**

If any tests fail, review the error messages and fix the solutions.

**Step 3: Commit if changes made**

```bash
git add scripts/questions_data_full.py
git commit -m "fix: resolve validation failures"
```

---

## Task 13: Regenerate Database

**Step 1: Regenerate SQL seed file**

Run: `python3 scripts/generate_seed_sql.py`

Expected: Creates/updates `database/seed_complete.sql`

**Step 2: Verify SQL was generated**

Run: `ls -lh database/seed_complete.sql`

Expected: File exists and shows recent modification time

**Step 3: Import into database**

Run: `sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql`

Expected: No errors, completes silently

**Step 4: Commit regenerated SQL**

```bash
git add database/seed_complete.sql
git commit -m "chore: regenerate database with implemented solutions

- All 10 priority LeetCode solutions now functional
- Database updated with working Python implementations"
```

---

## Task 14: Test in Application

**Step 1: Start the application**

Run: `npm run dev`

Expected: Application starts successfully

**Step 2: Manual testing**

In the application:
1. Log in as a user
2. Navigate to Practice mode
3. Select one of the implemented questions (e.g., "Product of Array Except Self")
4. Verify the solution code appears correctly (not placeholder)
5. Write test code or use existing solution
6. Submit and verify test cases pass

**Step 3: Verify at least 3 different questions**

Test at least:
- Product of Array Except Self (array)
- Binary Tree Level Order Traversal (tree)
- Number of Islands (graph)

**Step 4: Document any issues**

If any issues found, document them for fixing.

---

## Task 15: Final Commit and Summary

**Step 1: Create summary of work**

Create file `docs/implementation-summary.md`:

```markdown
# LeetCode Solutions Implementation Summary

## Completed Work

Successfully implemented 10 priority LeetCode solutions with educational depth.

### Solutions Implemented

1. ✓ Product of Array Except Self - Prefix/suffix products, O(n)
2. ✓ Maximum Subarray - Kadane's Algorithm, O(n)
3. ✓ Binary Tree Level Order Traversal - BFS, O(n)
4. ✓ Validate Binary Search Tree - Recursive bounds, O(n)
5. ✓ Number of Islands - DFS connected components, O(m*n)
6. ✓ Coin Change - Bottom-up DP, O(amount * coins)
7. ✓ Longest Increasing Subsequence - DP + Binary Search, O(n log n)
8. ✓ Course Schedule - DFS cycle detection, O(V+E)
9. ✓ Clone Graph - DFS with hash map, O(V+E)
10. ✓ Trapping Rain Water - Two pointers, O(n)

### Validation Results

All 10 solutions pass their test cases: **100% success rate**

### Files Modified

- `scripts/questions_data_full.py` - 10 solution implementations
- `scripts/validate_solutions.py` - Created test runner
- `database/seed_complete.sql` - Regenerated with new solutions

### Next Steps

Remaining 27 questions can be implemented using same approach:
- Use validation script to verify correctness
- Follow same educational comment style
- Commit after each solution passes tests
```

**Step 2: Commit summary**

```bash
git add docs/implementation-summary.md
git commit -m "docs: add implementation summary for LeetCode solutions

Completed 10/10 priority solutions with 100% test pass rate"
```

**Step 3: Done!**

All tasks complete. Solutions are implemented, validated, and ready for use.

---

## Verification Commands

**Quick verification at any time:**

```bash
# Validate all solutions
python3 scripts/validate_solutions.py

# Check specific solution
python3 scripts/validate_solutions.py | grep -A 5 "Product of Array"

# Verify database has new data
sqlite3 ~/.config/interview-prep-platform/interview-prep.db "SELECT title FROM questions WHERE title IN ('Product of Array Except Self', 'Maximum Subarray') LIMIT 5;"
```

---

**Estimated Total Time:** 8-10 hours
- Task 1 (Validation script): 30 min
- Tasks 2-6 (First 5 solutions): 3-4 hours
- Tasks 7-11 (Next 5 solutions): 4-5 hours
- Tasks 12-15 (Testing, DB, docs): 30-60 min
