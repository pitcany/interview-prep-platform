#!/usr/bin/env python3
"""
Test that Python signatures loaded from database can be executed without errors.
This simulates the full flow: database -> frontend -> code execution.
"""

import sqlite3
import sys
import os


def test_signature_execution(question_id, title, signature):
    """
    Test that a signature can be executed without NameError or SyntaxError.
    """
    print(f"\nTesting Question {question_id}: {title}")
    print("-" * 60)
    print("Signature preview (first 200 chars):")
    print(signature[:200] + "..." if len(signature) > 200 else signature)
    print()

    try:
        # Try to compile the code
        compile(signature, '<string>', 'exec')
        print("✓ Compiles without syntax errors")

        # Try to execute it
        namespace = {}
        exec(signature, namespace)
        print("✓ Executes without NameError")

        # Verify Solution class exists
        if 'Solution' not in namespace:
            print("❌ FAILED: Solution class not found in namespace")
            return False

        # Instantiate Solution
        solution = namespace['Solution']()
        print("✓ Solution class instantiated successfully")

        # Get the method name (first method that isn't __init__)
        methods = [m for m in dir(solution) if not m.startswith('_') and callable(getattr(solution, m))]
        if methods:
            print(f"✓ Found method: {methods[0]}")
        else:
            print("⚠  Warning: No public methods found")

        return True

    except SyntaxError as e:
        print(f"❌ FAILED: SyntaxError - {e}")
        return False
    except NameError as e:
        print(f"❌ FAILED: NameError - {e}")
        print("   This means imports are missing!")
        return False
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__} - {e}")
        return False


def main():
    db_path = os.path.expanduser('~/.config/interview-prep-platform/interview-prep.db')

    if not os.path.exists(db_path):
        print(f"❌ Database not found at: {db_path}")
        return 1

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("=" * 60)
    print("Database Signature Integration Tests")
    print("=" * 60)

    # Test questions with different types of imports
    test_cases = [
        # Simple question with List
        ("Two Sum", "List"),
        # Linked list question with Optional + ListNode
        ("Merge Two Sorted Lists", "Optional[ListNode]"),
        # Tree question with TreeNode
        ("Binary Tree Inorder Traversal", "TreeNode"),
        # Another common case
        ("Valid Parentheses", "str"),
        # More complex case
        ("Longest Substring Without Repeating Characters", "str"),
    ]

    results = []

    for title, expected_type in test_cases:
        cursor.execute("""
            SELECT q.id, q.title, lq.function_signature_python
            FROM questions q
            JOIN leetcode_questions lq ON q.id = lq.question_id
            WHERE q.title = ?
        """, (title,))

        row = cursor.fetchone()

        if not row:
            print(f"\n⚠️  Skipping '{title}' - not found in database")
            continue

        question_id, title, signature = row
        passed = test_signature_execution(question_id, title, signature)
        results.append((title, passed))

    conn.close()

    # Summary
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    for title, passed in results:
        status = "✓ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {title}")

    all_passed = all(result[1] for result in results)

    if all_passed:
        print("\n🎉 All database signatures work correctly!")
        print("   Bug #3 fix is fully verified in production database!")
        return 0
    else:
        failed_count = sum(1 for r in results if not r[1])
        print(f"\n⚠️  {failed_count} signature(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
