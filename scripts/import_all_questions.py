#!/usr/bin/env python3
"""
Complete database setup from unified JSON file.
Replaces: seed_complete.sql + setup_database.py

This script imports all questions, test cases, and configuration from a single JSON source.

Usage:
    python3 scripts/import_all_questions.py
"""

import sqlite3
import json
import sys
import os
from pathlib import Path

def get_db_path():
    """Get the database path based on OS"""
    if os.name == 'nt':  # Windows
        db_path = Path(os.environ.get('APPDATA', '')) / 'interview-prep-platform' / 'interview-prep.db'
    elif sys.platform == 'darwin':  # macOS
        db_path = Path.home() / 'Library' / 'Application Support' / 'interview-prep-platform' / 'interview-prep.db'
    else:  # Linux
        db_path = Path.home() / '.config' / 'interview-prep-platform' / 'interview-prep.db'
    return db_path

def load_questions_data():
    """Load complete questions data from JSON"""
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'python-service' / 'data' / 'questions_complete.json'

    with open(data_file, 'r') as f:
        return json.load(f)

def import_leetcode_questions(cursor, questions):
    """Import LeetCode questions and their test cases"""
    print(f"\n📝 Importing {len(questions)} LeetCode questions...")

    for idx, q in enumerate(questions, 1):
        # Insert into questions table
        cursor.execute("""
            INSERT OR REPLACE INTO questions (title, description, difficulty, category_id, tags)
            VALUES (?, ?, ?, 1, ?)
        """, (
            q['title'],
            q['description'],
            q['difficulty'],
            json.dumps(q.get('tags', []))
        ))

        question_id = cursor.lastrowid

        # Prepare Python function signature (use python_imports if exists, otherwise function_signature)
        python_sig = q.get('python_imports', q.get('function_signature', {}).get('python', ''))

        # Insert into leetcode_questions table
        cursor.execute("""
            INSERT OR REPLACE INTO leetcode_questions (
                question_id, test_cases, hidden_test_cases,
                expected_time_complexity, expected_space_complexity,
                function_signature_python, function_signature_java, function_signature_cpp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            question_id,
            json.dumps(q.get('test_cases', [])),
            json.dumps(q.get('hidden_test_cases', [])),
            q.get('time_complexity', ''),
            q.get('space_complexity', ''),
            python_sig,
            q.get('function_signature', {}).get('java', ''),
            q.get('function_signature', {}).get('cpp', '')
        ))

        if idx % 10 == 0:
            print(f"   ✅ Imported {idx}/{len(questions)} questions...")

    print(f"   ✅ All {len(questions)} LeetCode questions imported")

def import_ml_questions(cursor, questions):
    """Import ML System Design questions"""
    print(f"\n📝 Importing {len(questions)} ML System Design questions...")

    for idx, q in enumerate(questions, 1):
        # Insert into questions table
        cursor.execute("""
            INSERT OR REPLACE INTO questions (title, description, difficulty, category_id, tags)
            VALUES (?, ?, ?, 2, ?)
        """, (
            q['title'],
            q['description'],
            q['difficulty'],
            json.dumps(q.get('tags', []))
        ))

        question_id = cursor.lastrowid

        # Insert into ml_design_questions table
        cursor.execute("""
            INSERT OR REPLACE INTO ml_design_questions (
                question_id, scenario, requirements,
                evaluation_criteria, sample_solution, key_components
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            question_id,
            q.get('scenario', ''),
            json.dumps(q.get('requirements', [])),
            json.dumps(q.get('evaluation_criteria', {})),
            q.get('sample_solution', ''),
            json.dumps(q.get('key_components', []))
        ))

        print(f"   ✅ Imported {idx}/{len(questions)} ML questions...")

    print(f"   ✅ All {len(questions)} ML System Design questions imported")

def verify_import(cursor):
    """Verify the import was successful"""
    print("\n🔍 Verifying import...")

    # Check total questions
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]

    # Check LeetCode questions
    cursor.execute("SELECT COUNT(*) FROM leetcode_questions")
    leetcode_count = cursor.fetchone()[0]

    # Check ML questions
    cursor.execute("SELECT COUNT(*) FROM ml_design_questions")
    ml_count = cursor.fetchone()[0]

    # Check questions with hidden tests
    cursor.execute("""
        SELECT COUNT(*)
        FROM leetcode_questions
        WHERE json_array_length(hidden_test_cases) > 0
    """)
    with_hidden = cursor.fetchone()[0]

    print(f"   Total questions: {total_questions}")
    print(f"   LeetCode questions: {leetcode_count}")
    print(f"   ML System Design questions: {ml_count}")
    print(f"   Questions with hidden tests: {with_hidden}/{leetcode_count}")

    return leetcode_count > 0 and ml_count > 0

def main():
    print("=" * 70)
    print("Complete Database Import from JSON")
    print("=" * 70)
    print()

    db_path = get_db_path()

    if not db_path.exists():
        print(f"❌ Database not found at: {db_path}")
        print("   Please run: npm run db:init")
        sys.exit(1)

    print(f"📂 Database: {db_path}")

    try:
        # Load questions data
        print("\n📦 Loading questions from JSON...")
        data = load_questions_data()
        leetcode_questions = data['leetcode_questions']
        ml_questions = data['ml_questions']
        print(f"   ✅ Loaded {len(leetcode_questions)} LeetCode questions")
        print(f"   ✅ Loaded {len(ml_questions)} ML questions")

        # Connect to database
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Import all questions
        import_leetcode_questions(cursor, leetcode_questions)
        import_ml_questions(cursor, ml_questions)

        # Commit changes
        conn.commit()

        # Verify import
        if verify_import(cursor):
            print("\n" + "=" * 70)
            print("✅ Database import complete!")
            print("=" * 70)
            print("\n📊 Summary:")
            print(f"   • {len(leetcode_questions)} LeetCode questions")
            print(f"   • {len(ml_questions)} ML System Design questions")
            print(f"   • ~{len(leetcode_questions) * 3} visible test cases")
            print(f"   • ~{len(leetcode_questions) * 4} hidden test cases")
            print(f"   • ~{len(leetcode_questions) * 7} total test cases")
            print("\n🚀 Next steps:")
            print("   1. Set execution mode in .env (SANDBOX_MODE=local or docker)")
            print("   2. Start the app: npm run dev")
            print("   3. Try submitting a solution!")
            conn.close()
            sys.exit(0)
        else:
            print("\n❌ Import verification failed")
            conn.close()
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"\n❌ File not found: {e}")
        print("   Make sure questions_complete.json exists")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSON: {e}")
        sys.exit(1)
    except sqlite3.Error as e:
        print(f"\n❌ Database error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
