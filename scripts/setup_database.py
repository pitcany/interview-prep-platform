#!/usr/bin/env python3
"""
Complete database setup script.
Initializes database and populates all test cases in one command.

Usage:
    python3 scripts/setup_database.py
"""

import sqlite3
import json
import sys
import os
from pathlib import Path

def load_test_data():
    """Load test case data from JSON files"""
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'python-service' / 'data'

    # Load hidden test cases
    with open(data_dir / 'hidden_test_cases.json', 'r') as f:
        hidden_test_cases = json.load(f)

    # Load Python imports
    with open(data_dir / 'python_imports.json', 'r') as f:
        python_imports = json.load(f)

    return hidden_test_cases, python_imports

def get_db_path():
    """Get the database path based on OS"""
    if os.name == 'nt':  # Windows
        db_path = Path(os.environ.get('APPDATA', '')) / 'interview-prep-platform' / 'interview-prep.db'
    elif sys.platform == 'darwin':  # macOS
        db_path = Path.home() / 'Library' / 'Application Support' / 'interview-prep-platform' / 'interview-prep.db'
    else:  # Linux
        db_path = Path.home() / '.config' / 'interview-prep-platform' / 'interview-prep.db'
    return db_path

def main():
    print("=" * 70)
    print("Complete Database Setup")
    print("=" * 70)
    print()

    # Load test data from JSON files
    print("📦 Loading test data from JSON files...")
    HIDDEN_TEST_CASES, PYTHON_IMPORTS = load_test_data()
    print(f"   ✅ Loaded {len(HIDDEN_TEST_CASES)} question test cases")
    print(f"   ✅ Loaded {len(PYTHON_IMPORTS)} Python import configurations")
    print()

    db_path = get_db_path()

    if not db_path.exists():
        print(f"❌ Database not found at: {db_path}")
        print("   Please run the application first to create the database.")
        print("   Or run: npm run db:init")
        sys.exit(1)

    print(f"📂 Database: {db_path}")
    print()

    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Update hidden test cases
        print("📝 Updating hidden test cases...")
        updated_count = 0
        for title, hidden_tests in HIDDEN_TEST_CASES.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET hidden_test_cases = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (json.dumps(hidden_tests), title))

            if cursor.rowcount > 0:
                updated_count += 1
                print(f"   ✅ {title}")

        print(f"\n✅ Updated hidden test cases for {updated_count} questions")

        # Update Python imports
        print("\n📝 Updating Python imports...")
        imports_count = 0
        for title, imports in PYTHON_IMPORTS.items():
            cursor.execute("""
                UPDATE leetcode_questions
                SET function_signature_python = ?
                WHERE question_id IN (
                    SELECT id FROM questions WHERE title = ?
                )
            """, (imports, title))

            if cursor.rowcount > 0:
                imports_count += 1
                print(f"   ✅ {title}")

        print(f"\n✅ Updated imports for {imports_count} questions")

        # Commit changes
        conn.commit()

        # Verify setup
        print("\n🔍 Verifying setup...")
        cursor.execute("""
            SELECT COUNT(*) as total,
                   SUM(CASE WHEN json_array_length(hidden_test_cases) > 0 THEN 1 ELSE 0 END) as with_hidden
            FROM leetcode_questions
        """)

        total, with_hidden = cursor.fetchone()

        print(f"   Total questions: {total}")
        print(f"   With hidden tests: {with_hidden}")

        if with_hidden == total and total > 0:
            print("\n" + "=" * 70)
            print("✅ Database setup complete!")
            print("=" * 70)
            print("\n📊 Summary:")
            print(f"   • {total} LeetCode questions")
            print(f"   • {with_hidden} questions with hidden tests")
            print(f"   • ~{with_hidden * 3} visible test cases")
            print(f"   • ~{with_hidden * 4} hidden test cases")
            print(f"   • ~{with_hidden * 7} total test cases")
            print("\n🚀 Next steps:")
            print("   1. Set execution mode in .env (SANDBOX_MODE=local or docker)")
            print("   2. Start the app: npm run dev")
            print("   3. Try submitting a solution!")
            sys.exit(0)
        else:
            print("\n❌ Some questions missing hidden tests")
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
