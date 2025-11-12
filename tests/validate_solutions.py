#!/usr/bin/env python3
"""
Validation script for LeetCode solutions
Executes solutions against test cases and reports results
"""

import os
import re
import sys
import heapq
from collections import deque
from typing import List, Optional, Any


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


def tree_to_list(node: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert binary tree to level-order list representation."""
    if not node:
        return []
    result = []
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


# Graph node definition for graph-based problems
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Linked list node definition for linked list problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list_from_array(values: List[int]) -> Optional[ListNode]:
    """Build linked list from array representation."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def list_to_array(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to array for comparison."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def build_graph_from_adjacency_list(adj_list: List[List[int]]) -> Optional[Node]:
    """Build graph from adjacency list representation."""
    if not adj_list:
        return None

    # Special case: [[]] represents a single node with no neighbors
    if len(adj_list) == 1 and len(adj_list[0]) == 0:
        return Node(1)

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

    # Special case: single node with no neighbors should return [[]]
    if len(visited) == 1 and len(list(visited.values())[0]) == 0:
        return [[]]

    max_val = max(visited.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in visited.items():
        result[val - 1] = sorted(neighbors)

    return result


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

        # Execute solution code in isolated namespace with typing imports, TreeNode, and Node
        namespace = {'List': List, 'Optional': Optional, 'Any': Any, 'TreeNode': TreeNode, 'Node': Node, 'ListNode': ListNode, 'deque': deque, 'heapq': heapq}
        exec(solution_code, namespace)

        # Create instance from isolated namespace
        # Special handling for Codec class (Serialize/Deserialize)
        if 'Codec' in namespace:
            solution = namespace['Codec']()
        else:
            solution = namespace['Solution']()

        # Verify method exists
        if not hasattr(solution, method_name):
            return False, [f"Method '{method_name}' not found in solution"]

        # Run test cases
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case['input']
            expected = test_case['expectedOutput']

            # Handle tree-based inputs (convert list to TreeNode)
            # Exception: "Construct Binary Tree" takes lists as input, not TreeNode
            if ('Tree' in title or 'BST' in title or 'Path Sum' in title) and \
               'Construct Binary Tree' not in title and \
               test_input and isinstance(test_input[0], list):
                root = build_tree_from_list(test_input[0])
                test_input = [root] + test_input[1:]

                # For LCA, convert p and q values to TreeNode references
                if 'Lowest Common Ancestor' in title and len(test_input) >= 3:
                    p_val, q_val = test_input[1], test_input[2]
                    # Find nodes with these values
                    def find_node(node, val):
                        if not node:
                            return None
                        if node.val == val:
                            return node
                        left = find_node(node.left, val)
                        if left:
                            return left
                        return find_node(node.right, val)

                    p_node = find_node(root, p_val)
                    q_node = find_node(root, q_val)
                    test_input = [root, p_node, q_node]

            # Handle graph-based inputs (convert adjacency list to Node)
            if 'Graph' in title and test_input and isinstance(test_input[0], list):
                test_input = [build_graph_from_adjacency_list(test_input[0])]

            # Handle linked list inputs (convert array to ListNode)
            # Special case: Linked List Cycle - create cycle at given position
            if 'Linked List Cycle' in title and test_input and isinstance(test_input[0], list):
                arr, pos = test_input[0], test_input[1]
                head = build_list_from_array(arr)
                # Create cycle if pos != -1
                if pos != -1 and head:
                    # Find the node at position pos
                    cycle_node = head
                    for _ in range(pos):
                        if cycle_node:
                            cycle_node = cycle_node.next
                    # Find the tail and point it to cycle_node
                    tail = head
                    while tail.next:
                        tail = tail.next
                    tail.next = cycle_node
                test_input = [head]
            # Special case: Merge k Sorted Lists - list of lists
            elif 'Merge k' in title and test_input and isinstance(test_input[0], list):
                # Convert each list to ListNode
                list_of_lists = [build_list_from_array(arr) if arr else None for arr in test_input[0]]
                test_input = [list_of_lists]
            # Special case: Merge Two Sorted Lists, Add Two Numbers - two arrays to two ListNodes
            elif ('Merge Two Sorted Lists' in title or 'Add Two Numbers' in title) and len(test_input) == 2:
                list1 = build_list_from_array(test_input[0]) if test_input[0] else None
                list2 = build_list_from_array(test_input[1]) if test_input[1] else None
                test_input = [list1, list2]
            elif ('List' in title and 'Linked' in title and test_input and isinstance(test_input[0], list)) or \
                 ('Remove Nth Node' in title and test_input and isinstance(test_input[0], list)) or \
                 ('Swap Nodes in Pairs' in title and test_input and isinstance(test_input[0], list)):
                # Convert first array to linked list
                test_input = [build_list_from_array(test_input[0])] + test_input[1:]

            # Special handling for Serialize and Deserialize
            if 'Serialize and Deserialize' in title:
                # Build tree from input
                root = test_input[0] if test_input else None
                # Serialize then deserialize
                serialized = solution.serialize(root)
                deserialized = solution.deserialize(serialized)
                # Convert back to list for comparison
                actual = tree_to_list(deserialized)
            else:
                # Call the method with unpacked inputs
                method = getattr(solution, method_name)
                actual = method(*test_input)

                # Handle in-place modifications (methods that return None)
                # For these, the expected output is the modified input
                if actual is None and 'Rotate Image' in title:
                    actual = test_input[0]
                elif actual is None and 'Set Matrix Zeroes' in title:
                    actual = test_input[0]

            # Handle tree construction output (convert TreeNode to list)
            if 'Construct Binary Tree' in title and actual is not None:
                actual = tree_to_list(actual)

            # Handle graph output (convert back to adjacency list)
            if 'Graph' in title:
                actual = graph_to_adjacency_list(actual)

            # Handle linked list output (convert ListNode to array)
            if ('List' in title and 'Linked' in title) or 'Merge k' in title or 'Merge Two Sorted Lists' in title or 'Remove Nth Node' in title or 'Swap Nodes in Pairs' in title or 'Add Two Numbers' in title:
                if actual is None:
                    actual = []
                elif isinstance(actual, ListNode):
                    actual = list_to_array(actual)

            # Handle LCA output (convert TreeNode to value)
            if 'Lowest Common Ancestor' in title and actual is not None and hasattr(actual, 'val'):
                actual = actual.val

            # Compare results
            # Special comparison for Group Anagrams (order doesn't matter)
            if 'Group Anagrams' in title:
                # Convert to set of frozensets for order-independent comparison
                actual_set = {frozenset(group) for group in actual}
                expected_set = {frozenset(group) for group in expected}
                if actual_set != expected_set:
                    errors.append(
                        f"  Test {i} FAILED:\n"
                        f"    Input: {test_case['input']}\n"
                        f"    Expected: {expected}\n"
                        f"    Got: {actual}"
                    )
            elif actual != expected:
                errors.append(
                    f"  Test {i} FAILED:\n"
                    f"    Input: {test_case['input']}\n"
                    f"    Expected: {expected}\n"
                    f"    Got: {actual}"
                )

        return len(errors) == 0, errors

    except Exception as e:
        return False, [f"  Error: {str(e)}"]


def main():
    """Main validation entry point."""
    # Import questions data - use dynamic path resolution
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)
    from questions_data_full import LEETCODE_QUESTIONS

    # Questions to validate
    target_questions = [
        # Easy solutions (not in batches)
        'Two Sum',
        'Valid Parentheses',
        'Merge Two Sorted Lists',
        'Best Time to Buy and Sell Stock',
        'Climbing Stairs',
        'Binary Tree Inorder Traversal',
        'Valid Palindrome',
        'Linked List Cycle',
        # Medium solutions (not in batches)
        'Add Two Numbers',
        'Longest Substring Without Repeating Characters',
        '3Sum',
        'Container With Most Water',
        'Longest Palindromic Substring',
        'Group Anagrams',
        # Batch 1
        'Product of Array Except Self',
        'Maximum Subarray',
        'Number of Islands',
        'Coin Change',
        'Binary Tree Level Order Traversal',
        'Validate Binary Search Tree',
        'Longest Increasing Subsequence',
        'Course Schedule',
        'Clone Graph',
        'Trapping Rain Water',
        # Batch 2
        'Letter Combinations of a Phone Number',
        'Generate Parentheses',
        'Permutations',
        'Subarray Sum Equals K',
        'Word Search',
        'Word Break',
        'Lowest Common Ancestor of a Binary Tree',
        'Serialize and Deserialize Binary Tree',
        'Edit Distance',
        'Merge k Sorted Lists',
        # Batch 3
        'Spiral Matrix',
        'Rotate Image',
        'Set Matrix Zeroes',
        'Remove Nth Node From End of List',
        'Reverse Linked List II',
        'Swap Nodes in Pairs',
        'Kth Smallest Element in a BST',
        'Binary Tree Right Side View',
        'Path Sum II',
        # Batch 4
        'Construct Binary Tree from Preorder and Inorder Traversal',
        'Unique Paths',
        'House Robber II',
        'Decode Ways',
        # Batch 5
        'Median of Two Sorted Arrays',
        'Binary Tree Maximum Path Sum',
        'Regular Expression Matching',
        'Word Ladder'
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
