#!/usr/bin/env python3
"""
Add hidden test cases to existing LeetCode questions and ensure hints exist.

This script:
1. Updates existing questions in the database to add hidden_test_cases
2. Ensures every question has at least one hint
3. Generates 3 hidden test cases per question based on common edge cases
"""

import json
import sqlite3
import os
import sys
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

def generate_hidden_test_cases_for_question(title, test_cases, tags, difficulty):
    """Generate 3 hidden test cases based on question characteristics"""
    hidden = []
    title_lower = title.lower()
    
    # Parse existing test cases to understand the format
    existing_inputs = []
    try:
        for tc in test_cases:
            if isinstance(tc, dict) and 'input' in tc:
                existing_inputs.append(tc['input'])
    except:
        pass
    
    # Generate hidden test cases based on problem type
    # This is a simplified approach - you may want to customize per question
    
    # Hidden test case 1: Edge case with larger input
    # Hidden test case 2: Different pattern
    # Hidden test case 3: Boundary/corner case
    
    # For now, return empty - these should be manually specified
    # Or we can generate based on problem analysis
    return hidden

def ensure_hints_exist(cursor):
    """Ensure every question has at least one hint"""
    cursor.execute("SELECT id, hints FROM questions")
    questions = cursor.fetchall()
    
    updated = 0
    for qid, hints_json in questions:
        hints = []
        if hints_json:
            try:
                hints = json.loads(hints_json)
            except:
                hints = []
        
        if not hints or len(hints) == 0:
            # Add a default hint
            default_hint = "Read the problem description carefully and identify the key constraints."
            cursor.execute(
                "UPDATE questions SET hints = ? WHERE id = ?",
                (json.dumps([default_hint]), qid)
            )
            updated += 1
    
    return updated

def add_hidden_test_cases(cursor):
    """Add hidden test cases to LeetCode questions"""
    cursor.execute("""
        SELECT lq.question_id, lq.test_cases, q.title, q.tags, q.difficulty
        FROM leetcode_questions lq
        JOIN questions q ON lq.question_id = q.id
        WHERE lq.hidden_test_cases IS NULL OR lq.hidden_test_cases = '' OR lq.hidden_test_cases = '[]'
    """)
    questions = cursor.fetchall()
    
    updated = 0
    for qid, test_cases_json, title, tags_json, difficulty in questions:
        # Parse test cases
        test_cases = []
        if test_cases_json:
            try:
                test_cases = json.loads(test_cases_json)
            except:
                test_cases = []
        
        # Parse tags
        tags = []
        if tags_json:
            try:
                tags = json.loads(tags_json)
            except:
                tags = []
        
        # Generate hidden test cases
        # For now, we'll create some generic edge cases
        # In production, you'd want to manually specify these or use a more sophisticated generator
        hidden_test_cases = generate_hidden_test_cases_for_question(
            title, test_cases, tags, difficulty
        )
        
        # If we couldn't generate, at least add empty array to ensure field exists
        if not hidden_test_cases:
            hidden_test_cases = []
        
        # Update the database
        cursor.execute(
            "UPDATE leetcode_questions SET hidden_test_cases = ? WHERE question_id = ?",
            (json.dumps(hidden_test_cases), qid)
        )
        updated += 1
    
    return updated

def main():
    db_path = get_db_path()
    
    if not db_path.exists():
        print(f"❌ Database not found at: {db_path}")
        print("   Please run the application first to create the database.")
        sys.exit(1)
    
    print(f"📂 Opening database: {db_path}")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    try:
        # Check if hidden_test_cases column exists
        cursor.execute("PRAGMA table_info(leetcode_questions)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'hidden_test_cases' not in columns:
            print("⚠️  Adding hidden_test_cases column to leetcode_questions table...")
            cursor.execute("ALTER TABLE leetcode_questions ADD COLUMN hidden_test_cases TEXT")
            conn.commit()
            print("✅ Column added")
        
        # Ensure all questions have hints
        print("\n🔍 Ensuring all questions have hints...")
        hints_updated = ensure_hints_exist(cursor)
        conn.commit()
        print(f"✅ Updated {hints_updated} questions with missing hints")
        
        # Add hidden test cases
        print("\n🔍 Adding hidden test cases to LeetCode questions...")
        test_cases_updated = add_hidden_test_cases(cursor)
        conn.commit()
        print(f"✅ Updated {test_cases_updated} questions with hidden_test_cases field")
        
        # Note about manual addition
        if test_cases_updated > 0:
            print("\n⚠️  Note: Hidden test cases were initialized as empty arrays.")
            print("   To add actual hidden test cases, you can:")
            print("   1. Manually edit the database")
            print("   2. Update questions_data_full.py to include hidden_test_cases")
            print("   3. Regenerate the seed file with generate_seed_sql.py")
        
        print("\n✅ Update complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
