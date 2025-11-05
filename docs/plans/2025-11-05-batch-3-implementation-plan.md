# Batch 3 LeetCode Solutions Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement 9 additional LeetCode solutions (arrays, linked lists, trees) to reach 29/40 solutions (72.5% completion)

**Architecture:** Update solution_python fields in questions_data_full.py with optimal algorithms. Use existing validation infrastructure (TreeNode, ListNode classes). Follow TDD-like approach: implement → validate → fix → commit.

**Tech Stack:** Python 3.x, typing module, existing validation script

---

## Task 1: Implement Spiral Matrix

**Files:**
- Modify: `scripts/questions_data_full.py:1423`

**Step 1: Implement Spiral Matrix solution**

Replace the placeholder at line 1423 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Spiral Matrix"
```

Expected output:
```
Testing: Spiral Matrix
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Spiral Matrix solution

- Layer-by-layer traversal with boundary tracking
- O(m*n) time, O(1) space
- Handles edge cases: empty matrix, single row/column"
```

---

## Task 2: Implement Rotate Image

**Files:**
- Modify: `scripts/questions_data_full.py:1584`

**Step 1: Implement Rotate Image solution**

Replace the placeholder at line 1584 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Rotate Image"
```

Expected output:
```
Testing: Rotate Image
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Rotate Image solution

- Transpose + reverse rows approach
- O(n²) time, O(1) space in-place
- Clean two-step transformation"
```

---

## Task 3: Implement Set Matrix Zeroes

**Files:**
- Modify: `scripts/questions_data_full.py:1735`

**Step 1: Implement Set Matrix Zeroes solution**

Replace the placeholder at line 1735 with:

```python
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
        first_col_has_zero = False

        # Check if first column has zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and column as markers
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column

        # Set zeros based on markers (skip first row/col)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
''',
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Set Matrix Zeroes"
```

Expected output:
```
Testing: Set Matrix Zeroes
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Set Matrix Zeroes solution

- Use first row/col as markers
- O(m*n) time, O(1) space
- No extra space needed"
```

---

## Task 4: Implement Remove Nth Node From End of List

**Files:**
- Modify: `scripts/questions_data_full.py:2049`

**Step 1: Implement Remove Nth Node solution**

Replace the placeholder at line 2049 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Remove Nth Node"
```

Expected output:
```
Testing: Remove Nth Node From End of List
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Remove Nth Node From End of List solution

- Two-pointer technique
- O(n) time, O(1) space
- Dummy head handles edge cases"
```

---

## Task 5: Implement Reverse Linked List II

**Files:**
- Modify: `scripts/questions_data_full.py:2130`

**Step 1: Implement Reverse Linked List II solution**

Replace the placeholder at line 2130 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Reverse Linked List II"
```

Expected output:
```
Testing: Reverse Linked List II
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Reverse Linked List II solution

- Sublist reversal with pointer manipulation
- O(n) time, O(1) space
- Clean reconnection logic"
```

---

## Task 6: Implement Swap Nodes in Pairs

**Files:**
- Modify: `scripts/questions_data_full.py:2206`

**Step 1: Implement Swap Nodes in Pairs solution**

Replace the placeholder at line 2206 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Swap Nodes in Pairs"
```

Expected output:
```
Testing: Swap Nodes in Pairs
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Swap Nodes in Pairs solution

- Iterative pair swapping
- O(n) time, O(1) space
- Dummy head simplifies logic"
```

---

## Task 7: Implement Kth Smallest Element in a BST

**Files:**
- Modify: `scripts/questions_data_full.py:2557`

**Step 1: Implement Kth Smallest in BST solution**

Replace the placeholder at line 2557 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Kth Smallest"
```

Expected output:
```
Testing: Kth Smallest Element in a BST
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Kth Smallest Element in a BST solution

- In-order traversal with counter
- O(n) time, O(h) space
- Leverages BST sorted property"
```

---

## Task 8: Implement Binary Tree Right Side View

**Files:**
- Modify: `scripts/questions_data_full.py:2641`

**Step 1: Implement Binary Tree Right Side View solution**

Replace the placeholder at line 2641 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Binary Tree Right Side View"
```

Expected output:
```
Testing: Binary Tree Right Side View
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Binary Tree Right Side View solution

- Level-order BFS approach
- O(n) time, O(w) space
- Captures rightmost node per level"
```

---

## Task 9: Implement Path Sum II

**Files:**
- Modify: `scripts/questions_data_full.py:2760`

**Step 1: Implement Path Sum II solution**

Replace the placeholder at line 2760 with:

```python
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
```

**Step 2: Run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "Path Sum II"
```

Expected output:
```
Testing: Path Sum II
  ✓ All X test cases passed
```

**Step 3: Commit**

```bash
git add scripts/questions_data_full.py
git commit -m "feat: implement Path Sum II solution

- DFS backtracking approach
- O(n) time, O(h) space
- Copies path before adding to result"
```

---

## Task 10: Run Comprehensive Validation

**Step 1: Run full validation suite**

```bash
python3 scripts/validate_solutions.py
```

Expected output:
```
============================================================
LeetCode Solutions Validation
============================================================

[... 20 previous solutions passing ...]

Testing: Spiral Matrix
  ✓ All X test cases passed

Testing: Rotate Image
  ✓ All X test cases passed

Testing: Set Matrix Zeroes
  ✓ All X test cases passed

Testing: Remove Nth Node From End of List
  ✓ All X test cases passed

Testing: Reverse Linked List II
  ✓ All X test cases passed

Testing: Swap Nodes in Pairs
  ✓ All X test cases passed

Testing: Kth Smallest Element in a BST
  ✓ All X test cases passed

Testing: Binary Tree Right Side View
  ✓ All X test cases passed

Testing: Path Sum II
  ✓ All X test cases passed

============================================================
Summary: 29/29 solutions passing (100%)
============================================================
```

**Step 2: Document validation results**

If all tests pass, proceed to Task 12.
If any tests fail, proceed to Task 11.

---

## Task 11: Fix Validation Issues (if needed)

**This task only runs if Task 10 reveals failures**

**Step 1: Analyze failure**

Review error output from validation script:
- Which test case failed?
- What was expected vs actual output?
- Is it algorithm error or validation infrastructure issue?

**Step 2: Fix the issue**

Common issues:
- **Algorithm bug**: Fix logic in solution_python
- **Edge case**: Add handling for empty inputs, single elements
- **Type mismatch**: Check return type matches expected

**Step 3: Re-run validation**

```bash
python3 scripts/validate_solutions.py | grep -A 3 "[Problem Name]"
```

**Step 4: Commit fix**

```bash
git add scripts/questions_data_full.py
git commit -m "fix: correct [Problem Name] edge case handling"
```

**Step 5: Repeat until all tests pass**

Return to Task 10 Step 1 to verify all 29/29 solutions pass.

---

## Task 12: Regenerate Database

**Step 1: Generate SQL seed file**

```bash
cd scripts
python3 generate_seed_sql.py
cd ..
```

Expected: Script completes without errors, updates `database/seed_complete.sql`

**Step 2: Verify seed file size**

```bash
ls -lh database/seed_complete.sql
```

Expected: File size increased from ~211 KB to ~235 KB (approximately)

**Step 3: Verify file contains new solutions**

```bash
grep "Spiral Matrix" database/seed_complete.sql
```

Expected: Multiple matches showing the new solution is included

**Step 4: Commit database update**

```bash
git add database/seed_complete.sql
git commit -m "chore: regenerate database with Batch 3 solutions

- Added 9 new working solutions
- Database now contains 29/40 working solutions
- File size: ~235 KB"
```

---

## Task 13: Update Documentation

**Files:**
- Modify: `docs/implementation-summary.md`

**Step 1: Update summary header**

Find line ~5 and change from:
```markdown
Successfully implemented 20 priority LeetCode solutions across two batches
```

To:
```markdown
Successfully implemented 29 priority LeetCode solutions across three batches with educational depth and automated validation.
```

**Step 2: Add Batch 3 Solutions section**

After the Batch 2 Solutions section (around line 115), add:

```markdown
### Batch 3 Solutions (9 Additional)

**Arrays (3 solutions):**

21. ✓ **Spiral Matrix** - Layer-by-layer traversal, O(m*n)
    - Commit: `[commit-sha]`
    - Algorithm: Boundary tracking with four-directional traversal
    - Test cases: X/X passing

22. ✓ **Rotate Image** - Transpose + reverse, O(n²)
    - Commit: `[commit-sha]`
    - Algorithm: Two-step in-place transformation
    - Test cases: X/X passing

23. ✓ **Set Matrix Zeroes** - First row/col markers, O(1) space
    - Commit: `[commit-sha]`
    - Algorithm: Reuse matrix for marking without extra space
    - Test cases: X/X passing

**Linked Lists (3 solutions):**

24. ✓ **Remove Nth Node From End of List** - Two pointers, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: Fast/slow pointer technique
    - Test cases: X/X passing

25. ✓ **Reverse Linked List II** - Sublist reversal, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: Three-pointer reversal with reconnection
    - Test cases: X/X passing

26. ✓ **Swap Nodes in Pairs** - Iterative swapping, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: Pointer manipulation for adjacent pairs
    - Test cases: X/X passing

**Trees (3 solutions):**

27. ✓ **Kth Smallest Element in a BST** - In-order traversal, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: In-order traversal with counter
    - Test cases: X/X passing

28. ✓ **Binary Tree Right Side View** - Level-order BFS, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: BFS capturing rightmost nodes
    - Test cases: X/X passing

29. ✓ **Path Sum II** - DFS backtracking, O(n)
    - Commit: `[commit-sha]`
    - Algorithm: DFS with path tracking and backtracking
    - Test cases: X/X passing
```

**Step 3: Update Validation Results section**

Change from:
```markdown
**All 20 solutions pass their test cases: 100% success rate**

Total test cases executed: 50/50 passing
```

To:
```markdown
**All 29 solutions pass their test cases: 100% success rate**

Total test cases executed: XX/XX passing
```

**Step 4: Update algorithm categories**

Update the "Algorithm Categories Covered" section to reflect new problems:
- Arrays: Add Spiral Matrix, Rotate Image, Set Matrix Zeroes
- Linked Lists: Add Remove Nth Node, Reverse Linked List II, Swap Nodes in Pairs
- Trees: Add Kth Smallest BST, Right Side View, Path Sum II

**Step 5: Update Project Impact section**

Change from:
```markdown
**After:**
- 20/40 LeetCode questions have working solutions (50%)
```

To:
```markdown
**After:**
- 29/40 LeetCode questions have working solutions (72.5%)
```

**Step 6: Update Success Metrics**

Change from:
```markdown
✅ All 20 priority solutions implemented (Batch 1 + Batch 2)
✅ 100% test pass rate (50/50 test cases)
```

To:
```markdown
✅ All 29 priority solutions implemented (Batches 1-3)
✅ 100% test pass rate (XX/XX test cases)
```

**Step 7: Commit documentation**

```bash
git add docs/implementation-summary.md
git commit -m "docs: update summary with Batch 3 results

- Added 9 Batch 3 solutions (arrays, linked lists, trees)
- Updated to 29/40 solutions (72.5%)
- Updated validation results and metrics
- Enhanced algorithm category coverage"
```

---

## Task 14: Push to Remote

**Step 1: Push experimental branch**

```bash
git push origin experimental
```

Expected:
```
To https://github.com/[repo]/interview-prep-platform.git
   [prev-sha]..[new-sha]  experimental -> experimental
```

---

## Task 15: Create Pull Request

**Step 1: Create PR using GitHub CLI**

```bash
gh pr create --title "feat: Implement Batch 3 LeetCode Solutions (9 Additional Problems)" --body "$(cat <<'EOF'
## Summary

Implements 9 additional priority LeetCode solutions (Batch 3), bringing total to 29 working solutions (72.5% of LeetCode questions).

### Solutions Implemented (Batch 3)

**Arrays (3 solutions):**
1. Spiral Matrix - Layer-by-layer traversal, O(m*n)
2. Rotate Image - Transpose + reverse, O(n²) in-place
3. Set Matrix Zeroes - First row/col markers, O(1) space

**Linked Lists (3 solutions):**
4. Remove Nth Node From End of List - Two pointers, O(n)
5. Reverse Linked List II - Sublist reversal, O(n)
6. Swap Nodes in Pairs - Iterative swapping, O(n)

**Trees (3 solutions):**
7. Kth Smallest Element in a BST - In-order traversal, O(n)
8. Binary Tree Right Side View - Level-order BFS, O(n)
9. Path Sum II - DFS backtracking, O(n)

### Test Results

**100% Success Rate**
- All 29 solutions passing validation
- XX/XX test cases executed successfully

### Files Changed

- `scripts/questions_data_full.py` - Added 9 solution implementations
- `database/seed_complete.sql` - Regenerated (235 KB, 29 working solutions)
- `docs/implementation-summary.md` - Updated with Batch 3 results

### Project Impact

**Before this PR:**
- 20/40 solutions (50%)

**After this PR:**
- 29/40 solutions (72.5%)
- Comprehensive coverage: arrays, trees, graphs, DP, backtracking, linked lists, heaps

### Commit Breakdown

**Batch 3 Implementation (9 commits):**
1. Spiral Matrix
2. Rotate Image
3. Set Matrix Zeroes
4. Remove Nth Node From End of List
5. Reverse Linked List II
6. Swap Nodes in Pairs
7. Kth Smallest Element in a BST
8. Binary Tree Right Side View
9. Path Sum II

**Infrastructure (2 commits):**
1. Database regeneration
2. Documentation update

### Testing

Run validation:
\`\`\`bash
python3 scripts/validate_solutions.py
\`\`\`

Expected output: \`29/29 solutions passing (100%)\`

### Next Steps

- Batch 4: Final 8 solutions (Hard trees, DP, and Hard problems)
- Will reach 37/40 solutions (92.5%)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)" --base main
```

Expected: PR URL is returned

**Step 2: Note PR URL**

Save the PR URL for reference.

---

## Validation Commands Reference

**Single problem validation:**
```bash
python3 scripts/validate_solutions.py | grep -A 3 "[Problem Name]"
```

**Full validation:**
```bash
python3 scripts/validate_solutions.py
```

**Check specific commit:**
```bash
git show [commit-sha]
```

**View commit history:**
```bash
git log --oneline -15
```

---

## Success Criteria

✅ All 9 solutions implemented with optimal algorithms
✅ 100% test pass rate (29/29 solutions total)
✅ Educational comments explaining each algorithm
✅ Database regenerated successfully (~235 KB)
✅ Documentation updated with Batch 3 section
✅ All commits follow conventional format
✅ PR created and ready for review

---

## Estimated Timeline

- Tasks 1-9 (Implementation): ~5-6 hours
- Task 10-11 (Validation): ~1 hour
- Task 12 (Database): ~5 minutes
- Task 13 (Documentation): ~30 minutes
- Task 14-15 (Push & PR): ~10 minutes
- **Total: ~7-8 hours**

---

**Plan Status:** Ready for Execution
**Next Step:** Use `@superpowers:executing-plans` to implement this plan task-by-task
