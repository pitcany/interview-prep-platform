#!/usr/bin/env python3
"""
Script to add typing imports and class definitions to Python function signatures.
This ensures the code runs without NameError when users start a question.
"""

import re
import sys


def get_imports_and_classes(signature: str) -> str:
    """
    Determine which imports and class definitions are needed for a signature.

    Args:
        signature: The Python function signature

    Returns:
        String with imports and class definitions
    """
    lines = []

    # Check which typing hints are used
    needs_typing = []
    if 'List[' in signature:
        needs_typing.append('List')
    if 'Optional[' in signature:
        needs_typing.append('Optional')
    if 'Dict[' in signature:
        needs_typing.append('Dict')
    if 'Set[' in signature:
        needs_typing.append('Set')
    if 'Tuple[' in signature:
        needs_typing.append('Tuple')

    # Add typing import if needed
    if needs_typing:
        lines.append(f"from typing import {', '.join(sorted(needs_typing))}")
        lines.append("")

    # Add ListNode definition if needed
    if 'ListNode' in signature:
        lines.append("# Definition for singly-linked list.")
        lines.append("class ListNode:")
        lines.append("    def __init__(self, val=0, next=None):")
        lines.append("        self.val = val")
        lines.append("        self.next = next")
        lines.append("")

    # Add TreeNode definition if needed
    if 'TreeNode' in signature:
        lines.append("# Definition for a binary tree node.")
        lines.append("class TreeNode:")
        lines.append("    def __init__(self, val=0, left=None, right=None):")
        lines.append("        self.val = val")
        lines.append("        self.left = left")
        lines.append("        self.right = right")
        lines.append("")

    return '\n'.join(lines)


def update_python_signature(signature: str) -> str:
    """
    Add necessary imports and class definitions to a Python signature.

    Args:
        signature: Original Python function signature

    Returns:
        Updated signature with imports and definitions
    """
    imports_and_classes = get_imports_and_classes(signature)

    if imports_and_classes:
        return imports_and_classes + signature

    return signature


def main():
    input_file = 'questions_data_full.py'

    print(f"Reading {input_file}...")
    with open(input_file, 'r') as f:
        content = f.read()

    # Find all python_sig entries and update them
    # Pattern matches: 'python_sig': 'class Solution:...'
    pattern = r"('python_sig':\s*')([^']+)(')"

    updated_count = 0

    def replace_signature(match):
        nonlocal updated_count
        prefix = match.group(1)
        old_sig = match.group(2)
        suffix = match.group(3)

        # Unescape the signature
        old_sig_unescaped = old_sig.replace('\\n', '\n')

        # Update the signature
        new_sig_unescaped = update_python_signature(old_sig_unescaped)

        # Re-escape for Python string
        new_sig = new_sig_unescaped.replace('\n', '\\n')

        if old_sig != new_sig:
            updated_count += 1
            print(f"  Updated signature #{updated_count}")

        return prefix + new_sig + suffix

    # Replace all python_sig entries
    new_content = re.sub(pattern, replace_signature, content)

    # Write back
    print(f"\nWriting updated file...")
    with open(input_file, 'w') as f:
        f.write(new_content)

    print(f"\n✓ Successfully updated {updated_count} Python signatures!")
    print(f"  Added typing imports and class definitions where needed.")


if __name__ == '__main__':
    main()
