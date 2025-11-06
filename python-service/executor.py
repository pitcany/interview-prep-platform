#!/usr/bin/env python3
"""
Code Executor Service
Executes Python code safely with resource limits and timeout.
"""

import sys
import json
import traceback
import signal
import threading
import multiprocessing
import queue
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
from typing import Any, Dict

try:
    import resource
except ImportError:  # pragma: no cover - not available on Windows
    resource = None


TIMEOUT_ERROR_MSG = "Code execution exceeded time limit"


class TimeoutException(Exception):
    """Raised when code execution exceeds time limit."""


def timeout_handler(signum, frame):
    """Signal handler for execution timeout."""
    raise TimeoutException(TIMEOUT_ERROR_MSG)


SUPPORTS_SIGALRM = hasattr(signal, "SIGALRM")

if SUPPORTS_SIGALRM:
    signal.signal(signal.SIGALRM, timeout_handler)


def set_resource_limits(max_memory_mb: int = 512):
    """Set resource limits for code execution."""
    if resource is None:
        warning = (
            "Warning: Resource module not available; "
            "skipping resource limits."
        )
        print(warning, file=sys.stderr)
        return

    try:
        # Set memory limit (in bytes)
        max_memory = max_memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (max_memory, max_memory))

        # Set CPU time limit (in seconds)
        resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    except Exception as e:
        print(f"Warning: Could not set resource limits: {e}", file=sys.stderr)


def _initialize_result() -> Dict[str, Any]:
    return {
        'success': False,
        'output': None,
        'stdout': '',
        'stderr': '',
        'error': None,
        'error_type': None
    }


def _timeout_result() -> Dict[str, Any]:
    result = _initialize_result()
    result['error'] = TIMEOUT_ERROR_MSG
    result['error_type'] = 'timeout'
    return result


def _execution_error_result(message: str) -> Dict[str, Any]:
    result = _initialize_result()
    result['error'] = message
    result['error_type'] = 'execution_error'
    return result


def _list_to_linked_list(values):
    """Convert a Python list to a ListNode linked list."""
    if not values:
        return None

    # Get ListNode class from the code's namespace (will be set by caller)
    ListNode = _list_to_linked_list.ListNode
    if ListNode is None:
        raise ValueError("ListNode class not found in code")

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Storage for ListNode class reference
_list_to_linked_list.ListNode = None


def _linked_list_to_list(node):
    """Convert a ListNode linked list to a Python list."""
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def _list_to_tree(values, TreeNode):
    """Convert a Python list to a TreeNode binary tree (level-order)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

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


# Storage for TreeNode class reference
_list_to_tree.TreeNode = None


def _tree_to_list(node):
    """Convert a TreeNode binary tree to a Python list (level-order)."""
    if not node:
        return []

    result = []
    queue = [node]

    while queue:
        current = queue.pop(0)
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


def _execute_user_code(code: str, test_input: Any) -> Dict[str, Any]:
    stdout_capture = StringIO()
    stderr_capture = StringIO()
    result = _initialize_result()

    # Debug logging to stderr (won't interfere with JSON output)
    print(f"[DEBUG] _execute_user_code called", file=sys.stderr)
    print(f"[DEBUG] Code length: {len(code)}", file=sys.stderr)
    print(f"[DEBUG] Test input: {test_input}", file=sys.stderr)
    print(f"[DEBUG] Code contains 'ListNode': {'ListNode' in code}", file=sys.stderr)

    try:
        # Import typing classes needed by solutions
        from typing import List, Optional, Dict as TDict, Set, Tuple

        # Define common data structures used in LeetCode problems
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        class Node:
            def __init__(self, val=0, neighbors=None):
                self.val = val
                self.neighbors = neighbors if neighbors is not None else []

        def _build_graph_from_adjacency_list(adj_list, NodeClass):
            """Build a graph from adjacency list representation."""
            if not adj_list:
                return None

            # Create all nodes first
            nodes = {}
            for i in range(len(adj_list)):
                nodes[i + 1] = NodeClass(i + 1)

            # Connect neighbors
            for i, neighbors_list in enumerate(adj_list):
                node_val = i + 1
                for neighbor_val in neighbors_list:
                    nodes[node_val].neighbors.append(nodes[neighbor_val])

            return nodes[1] if 1 in nodes else None

        def _graph_to_adjacency_list(node):
            """Convert a graph to adjacency list representation."""
            if not node:
                return []

            # BFS to build node value -> position mapping
            visited = {}
            queue = [node]
            visited[node.val] = node
            nodes_in_order = [node]

            while queue:
                current = queue.pop(0)
                for neighbor in current.neighbors:
                    if neighbor.val not in visited:
                        visited[neighbor.val] = neighbor
                        nodes_in_order.append(neighbor)
                        queue.append(neighbor)

            # Build adjacency list
            adj_list = []
            for n in nodes_in_order:
                neighbors = [neighbor.val for neighbor in n.neighbors]
                adj_list.append(neighbors)

            return adj_list

        exec_globals = {
            '__builtins__': __builtins__,
            'input_value': test_input,
            # Typing imports
            'List': List,
            'Optional': Optional,
            'Dict': TDict,
            'Set': Set,
            'Tuple': Tuple,
            # Data structures
            'ListNode': ListNode,
            'TreeNode': TreeNode,
            'Node': Node,
        }

        # Store the pre-defined classes so we can detect if user overrides them
        predefined_ListNode = exec_globals['ListNode']
        predefined_TreeNode = exec_globals['TreeNode']
        predefined_Node = exec_globals['Node']

        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code, exec_globals)

            # Special handling for Codec class (serialize/deserialize problems)
            codec_class = exec_globals.get('Codec')
            if codec_class and 'serialize' in code and 'deserialize' in code:
                # This is a serialize/deserialize problem
                # Need to: convert input to tree, serialize, deserialize, convert back to list
                codec = codec_class()

                # Input is a tree structure - convert to TreeNode
                tree_input = test_input[0] if isinstance(test_input, list) and len(test_input) == 1 else test_input
                if isinstance(tree_input, list):
                    root = _list_to_tree(tree_input, TreeNode)
                else:
                    root = tree_input

                # Serialize then deserialize
                serialized = codec.serialize(root)
                deserialized = codec.deserialize(serialized)

                # Convert back to list for comparison
                output = _tree_to_list(deserialized) if deserialized else []

                result['success'] = True
                result['output'] = output
                return result

            # First, check if there's a Solution class (LeetCode style)
            solution_class = exec_globals.get('Solution')
            solution_func = None
            
            if solution_class and isinstance(solution_class, type):
                # Get all methods from the Solution class
                # In Python, instance methods are stored as functions in the class __dict__
                method_names = [
                    name for name, method in solution_class.__dict__.items()
                    if callable(method) and not name.startswith('_')
                ]
                
                # Common LeetCode method names to try
                # Note: 'solve' is NOT included here - LeetCode solutions don't use 'solve'
                common_methods = [
                    'twoSum', 'threeSum', 'maxProfit', 'findMedianSortedArrays',
                    'lengthOfLongestSubstring', 'longestPalindrome', 'reverse',
                    'myAtoi', 'isMatch', 'maxArea', 'intToRoman', 'romanToInt',
                    'longestCommonPrefix', 'isValid', 'mergeTwoLists', 'removeDuplicates',
                    'search', 'searchInsert', 'plusOne', 'addBinary', 'mySqrt',
                    'climbStairs', 'deleteDuplicates', 'merge', 'isSameTree',
                    'isSymmetric', 'maxDepth', 'levelOrder', 'sortedArrayToBST',
                    'inorderTraversal', 'preorderTraversal', 'postorderTraversal',
                    'hasPathSum', 'minDepth', 'isBalanced', 'flatten', 'connect',
                    'buildTree', 'numIslands', 'cloneGraph', 'canFinish', 'findOrder'
                ]
                
                # Try to find a method name in order of preference
                method_name = None
                for method in common_methods:
                    if method in method_names:
                        method_name = method
                        break
                
                # If no common method found, use the first method (excluding __init__)
                if method_name is None and method_names:
                    # Filter out __init__ if present
                    non_init_methods = [m for m in method_names if m != '__init__']
                    if non_init_methods:
                        method_name = non_init_methods[0]
                
                if method_name:
                    # Instantiate Solution class and get the method
                    try:
                        solution_instance = solution_class()
                        solution_func = getattr(solution_instance, method_name)
                        # Verify it's actually callable
                        if not callable(solution_func):
                            solution_func = None
                            method_name = None
                    except AttributeError:
                        # Method doesn't exist, reset and try fallback
                        solution_func = None
                        method_name = None
                
                # If we still don't have a method, try to use any available method
                if solution_func is None and method_names:
                    non_init_methods = [m for m in method_names if m != '__init__']
                    if non_init_methods:
                        try:
                            solution_instance = solution_class()
                            method_name = non_init_methods[0]
                            solution_func = getattr(solution_instance, method_name)
                            if not callable(solution_func):
                                solution_func = None
                        except AttributeError:
                            solution_func = None
            
            # If no Solution class found, look for standalone functions
            # Only do this if we didn't find a Solution class
            if solution_func is None and not (solution_class and isinstance(solution_class, type)):
                func_names = [
                    'solution', 'twoSum', 'threeSum', 'maxProfit',
                    'findMedianSortedArrays', 'lengthOfLongestSubstring',
                    'longestPalindrome', 'reverse', 'myAtoi', 'isMatch',
                    'maxArea', 'intToRoman', 'romanToInt', 'longestCommonPrefix'
                    # Note: 'solve' removed from here to avoid calling non-existent methods
                ]

                for func_name in func_names:
                    if (
                        func_name in exec_globals
                        and callable(exec_globals[func_name])
                    ):
                        solution_func = exec_globals[func_name]
                        break

                if solution_func is None:
                    for name, obj in exec_globals.items():
                        if callable(obj) and not name.startswith('_'):
                            solution_func = obj
                            break

            # Final check - if we still don't have a function, raise an error
            if solution_func is None:
                if solution_class and isinstance(solution_class, type):
                    # Try to get any method from Solution class as last resort
                    try:
                        solution_instance = solution_class()
                        # Get all methods using dir() and introspection
                        all_methods = [m for m in dir(solution_instance) 
                                     if not m.startswith('_') 
                                     and callable(getattr(solution_instance, m))]
                        if all_methods:
                            solution_func = getattr(solution_instance, all_methods[0])
                        else:
                            raise ValueError(
                                f"Solution class found but no callable methods found. "
                                f"Available attributes: {[m for m in dir(solution_instance) if not m.startswith('__')]}"
                            )
                    except Exception as e:
                        raise ValueError(
                            f"Solution class found but could not find or call any method. "
                            f"Error: {str(e)}"
                        )
                else:
                    raise ValueError("No callable function or Solution class method found in code")

            # Check if this is a linked list problem
            # Two cases: 1) user redefined ListNode, 2) code references ListNode in the source
            ListNode = exec_globals.get('ListNode')
            user_redefined_listnode = ListNode is not None and ListNode is not predefined_ListNode
            code_uses_listnode = 'ListNode' in code
            uses_linked_list = user_redefined_listnode or code_uses_listnode

            # Check if this is a tree problem
            TreeNode = exec_globals.get('TreeNode')
            user_redefined_treenode = TreeNode is not None and TreeNode is not predefined_TreeNode
            code_uses_treenode = 'TreeNode' in code
            uses_tree = user_redefined_treenode or code_uses_treenode

            # Check if this is a graph problem (Clone Graph)
            code_uses_node = 'Node' in code and 'cloneGraph' in code

            # Prepare input - convert lists to ListNodes/TreeNodes/Nodes if needed
            processed_input = test_input
            if code_uses_node and isinstance(test_input, (list, tuple)):
                # Special handling for cloneGraph - input is adjacency list
                if len(test_input) == 1 and isinstance(test_input[0], list):
                    adj_list = test_input[0]
                    graph_node = _build_graph_from_adjacency_list(adj_list, Node)
                    processed_input = [graph_node]
                else:
                    processed_input = test_input
            elif uses_linked_list and isinstance(test_input, (list, tuple)):
                # Set the ListNode class for our conversion functions
                _list_to_linked_list.ListNode = ListNode

                # Special handling for hasCycle - input format is [list_values, pos]
                # where pos indicates where tail connects to create cycle
                if 'hasCycle' in code and len(test_input) == 2 and isinstance(test_input[0], list) and isinstance(test_input[1], int):
                    head = _list_to_linked_list(test_input[0])
                    pos = test_input[1]

                    # Create cycle if pos >= 0
                    if pos >= 0 and head:
                        # Find the node at position pos
                        cycle_node = head
                        for _ in range(pos):
                            if cycle_node:
                                cycle_node = cycle_node.next

                        # Find the tail and connect it to cycle_node
                        tail = head
                        while tail.next:
                            tail = tail.next
                        tail.next = cycle_node

                    processed_input = [head]
                else:
                    # Check if this is mergeKLists (list of lists)
                    is_merge_k = 'mergeKLists' in code

                    # Convert each list in the input to a ListNode
                    processed_input = []
                    for item in test_input:
                        if isinstance(item, list):
                            if is_merge_k:
                                # mergeKLists: convert list of lists to list of ListNodes
                                converted_lists = []
                                for inner_list in item:
                                    if inner_list:
                                        converted_lists.append(_list_to_linked_list(inner_list))
                                    else:
                                        converted_lists.append(None)
                                processed_input.append(converted_lists)
                            else:
                                # Regular linked list problem
                                processed_input.append(_list_to_linked_list(item))
                        else:
                            # Keep non-list items as-is (e.g., integers for position)
                            processed_input.append(item)
            elif uses_tree and isinstance(test_input, (list, tuple)):
                # Set the TreeNode class for our conversion functions
                _list_to_tree.TreeNode = TreeNode

                # Special handling for lowestCommonAncestor - input format is [tree, p_val, q_val]
                # Need to find actual nodes with those values
                if 'lowestCommonAncestor' in code and len(test_input) == 3 and isinstance(test_input[0], list):
                    root = _list_to_tree(test_input[0], TreeNode)
                    p_val = test_input[1]
                    q_val = test_input[2]

                    # Find nodes with values p_val and q_val
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

                    processed_input = [root, p_node, q_node]
                else:
                    # Convert each list in the input to a TreeNode
                    # BUT: only convert if the list represents a tree (contains None or is the first input and looks like tree data)
                    # Don't convert if it's a list of integers meant to be processed as-is (like preorder/inorder traversals)
                    processed_input = []
                    for idx, item in enumerate(test_input):
                        if isinstance(item, list):
                            # Check if this looks like a tree representation
                            looks_like_tree = any(x is None for x in item) if item else True

                            # If it's the first input and we have multiple inputs, it's likely the tree
                            if idx == 0 and len(test_input) > 1:
                                looks_like_tree = True

                            # Special case: if there's only one list input, it's definitely a tree
                            if len(test_input) == 1:
                                looks_like_tree = True

                            # Exception: if we have exactly 2 list inputs, they're likely preorder/inorder (buildTree)
                            if len(test_input) == 2 and isinstance(test_input[0], list) and isinstance(test_input[1], list):
                                looks_like_tree = False

                            if looks_like_tree:
                                processed_input.append(_list_to_tree(item, TreeNode))
                            else:
                                # Keep as regular list (e.g., for buildTree(preorder, inorder))
                                processed_input.append(item)
                        else:
                            # Keep non-list items as-is (e.g., integers for target values)
                            processed_input.append(item)

            # Debug: show what function we're calling
            print(f"[DEBUG] Calling solution function: {solution_func}", file=sys.stderr)
            print(f"[DEBUG] Processed input: {processed_input}", file=sys.stderr)

            # Call the solution function with processed input
            if isinstance(processed_input, dict):
                output = solution_func(**processed_input)
            elif isinstance(processed_input, (list, tuple)):
                output = solution_func(*processed_input)
            else:
                output = solution_func(processed_input)

            print(f"[DEBUG] Raw output from function: {output}", file=sys.stderr)
            print(f"[DEBUG] Output type: {type(output)}", file=sys.stderr)

            # Convert ListNode output back to list if needed
            if uses_linked_list:
                if output is None:
                    output = []
                elif hasattr(output, 'val') and hasattr(output, 'next'):
                    output = _linked_list_to_list(output)

            # Convert TreeNode output back to list if needed
            if uses_tree:
                if hasattr(output, 'val') and hasattr(output, 'left'):
                    # Special case: lowestCommonAncestor returns a node, but test expects just the value
                    if 'lowestCommonAncestor' in code:
                        output = output.val if output else None
                    else:
                        output = _tree_to_list(output)

            # Convert Node (graph) output back to adjacency list if needed
            if code_uses_node:
                if output is None:
                    output = []
                elif hasattr(output, 'val') and hasattr(output, 'neighbors'):
                    output = _graph_to_adjacency_list(output)

            print(f"[DEBUG] Final output after conversions: {output}", file=sys.stderr)

            result['success'] = True
            result['output'] = output

    except TimeoutException as e:
        result['error'] = str(e)
        result['error_type'] = 'timeout'

    except MemoryError:
        result['error'] = "Memory limit exceeded"
        result['error_type'] = 'memory_error'

    except Exception as e:
        result['error'] = str(e)
        result['error_type'] = type(e).__name__
        result['traceback'] = traceback.format_exc()

    finally:
        result['stdout'] = stdout_capture.getvalue()
        result['stderr'] = stderr_capture.getvalue()

    return result


def _execution_worker(
    code: str,
    test_input: Any,
    result_queue: multiprocessing.Queue,
) -> None:
    try:
        result = _execute_user_code(code, test_input)
    except Exception as exc:  # pragma: no cover - defensive programming
        result = _execution_error_result(f"Executor worker failed: {exc}")
        result['traceback'] = traceback.format_exc()
    result_queue.put(result)


def _execute_code_in_subprocess(
    code: str,
    test_input: Any,
    timeout_seconds: int,
) -> Dict[str, Any]:
    result_queue: multiprocessing.Queue = multiprocessing.Queue()
    process = multiprocessing.Process(
        target=_execution_worker,
        args=(code, test_input, result_queue),
    )

    try:
        process.start()
        process.join(timeout_seconds)

        if process.is_alive():
            process.terminate()
            process.join()
            result = _timeout_result()
        else:
            try:
                result = result_queue.get_nowait()
            except queue.Empty:
                result = _execution_error_result(
                    "No result returned from execution process."
                )
    finally:
        result_queue.close()
        result_queue.join_thread()

    return result


def _can_use_unix_alarm() -> bool:
    return (
        SUPPORTS_SIGALRM
        and threading.current_thread() is threading.main_thread()
    )


def execute_code(
    code: str,
    test_input: Any,
    timeout_seconds: int = 10,
) -> Dict[str, Any]:
    """
    Execute Python code with a single test input.

    Args:
        code: Python code to execute
        test_input: Input value to pass to the function
        timeout_seconds: Maximum execution time in seconds

    Returns:
        Dict with execution results
    """
    if _can_use_unix_alarm():
        signal.alarm(timeout_seconds)
        try:
            return _execute_user_code(code, test_input)
        finally:
            signal.alarm(0)

    return _execute_code_in_subprocess(code, test_input, timeout_seconds)


def main():
    """Main entry point for the executor service."""
    if len(sys.argv) < 2:
        print(json.dumps({
            'error': 'Usage: executor.py <input_json>',
            'success': False
        }))
        sys.exit(1)

    try:
        # Parse input JSON
        input_data = json.loads(sys.argv[1])
        code = input_data.get('code', '')
        test_input = input_data.get('input')
        timeout = input_data.get('timeout', 10)
        max_memory = input_data.get('max_memory', 512)

        # Set resource limits
        set_resource_limits(max_memory)

        # Execute code
        result = execute_code(code, test_input, timeout)

        # Output result as JSON
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__,
            'traceback': traceback.format_exc()
        }))
        sys.exit(1)


if __name__ == '__main__':
    main()
