#!/usr/bin/env python3
"""
Import questions directly into SQLite database

Alternative to SQL import - adds questions programmatically.
Automatically finds your interview-prep database and imports all questions.

Usage:
    python3 scripts/add_all_questions.py
"""

import sqlite3
import os
import json
import sys
from pathlib import Path

# Import from single source of truth
sys.path.insert(0, str(Path(__file__).parent))
from questions_data import LEETCODE_QUESTIONS, ML_QUESTIONS

# Find database path
def get_db_path():
    home = Path.home()
    if os.name == 'nt':  # Windows
        db_path = home / 'AppData' / 'Roaming' / 'interview-prep-platform' / 'interview-prep.db'
    elif os.uname().sysname == 'Darwin':  # macOS
        db_path = home / 'Library' / 'Application Support' / 'interview-prep-platform' / 'interview-prep.db'
    else:  # Linux
        db_path = home / '.config' / 'interview-prep-platform' / 'interview-prep.db'
    
    return str(db_path)

def add_leetcode_question(cursor, q, category_id=1):
    """Add a LeetCode question to the database"""
    # Insert main question
    cursor.execute('''
        INSERT INTO questions (category_id, title, difficulty, description, constraints, examples, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        category_id,
        q['title'],
        q['difficulty'],
        q['description'],
        json.dumps(q['constraints']),
        json.dumps(q['examples']),
        json.dumps(q['tags'])
    ))
    
    question_id = cursor.lastrowid
    
    # Insert LeetCode-specific data
    cursor.execute('''
        INSERT INTO leetcode_questions 
        (question_id, function_signature_python, function_signature_java, function_signature_cpp,
         test_cases, expected_time_complexity, expected_space_complexity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        question_id,
        q.get('python_sig', ''),
        q.get('java_sig', ''),
        q.get('cpp_sig', ''),
        json.dumps(q['test_cases']),
        q['time_complexity'],
        q['space_complexity']
    ))
    
    return question_id

def add_ml_question(cursor, q, category_id=2):
    """Add an ML System Design question to the database"""
    # Insert main question
    cursor.execute('''
        INSERT INTO questions (category_id, title, difficulty, description, tags)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        category_id,
        q['title'],
        q['difficulty'],
        q['description'],
        json.dumps(q['tags'])
    ))
    
    question_id = cursor.lastrowid
    
    # Insert ML-specific data
    cursor.execute('''
        INSERT INTO ml_design_questions
        (question_id, scenario, requirements, evaluation_criteria, key_components)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        question_id,
        q['scenario'],
        json.dumps(q['requirements']),
        json.dumps(q['evaluation_criteria']),
        json.dumps(q['key_components'])
    ))
    
    return question_id

def main():
    db_path = get_db_path()
    
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        print("Please run 'npm run db:init' first")
        return
    
    print(f"📊 Adding questions to database: {db_path}")
    
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    try:
        # Count existing questions
        cursor.execute("SELECT COUNT(*) FROM questions WHERE category_id = 1")
        existing_leetcode = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM questions WHERE category_id = 2")
        existing_ml = cursor.fetchone()[0]
        
        print(f"\n📈 Current state:")
        print(f"   LeetCode questions: {existing_leetcode}")
        print(f"   ML Design questions: {existing_ml}")
        
        if existing_leetcode or existing_ml:
            print("\n🧹 Clearing existing interview questions (categories 1 & 2)...")
            clear_sql = """
                DELETE FROM leetcode_questions WHERE question_id IN (
                    SELECT id FROM questions WHERE category_id IN (1, 2)
                );
                DELETE FROM ml_design_questions WHERE question_id IN (
                    SELECT id FROM questions WHERE category_id IN (1, 2)
                );
                DELETE FROM questions WHERE category_id IN (1, 2);
            """
            cursor.executescript(clear_sql)
            conn.commit()
            print("   ✔️ Existing entries removed. Seeding fresh data...")
        
        # Add LeetCode questions
        print(f"\n➕ Adding {len(LEETCODE_QUESTIONS)} LeetCode questions...")
        for i, q in enumerate(LEETCODE_QUESTIONS, 1):
            question_id = add_leetcode_question(cursor, q)
            print(f"   {i}. {q['title']} (ID: {question_id})")
        
        # Add ML questions  
        print(f"\n➕ Adding {len(ML_QUESTIONS)} ML Design questions...")
        for i, q in enumerate(ML_QUESTIONS, 1):
            question_id = add_ml_question(cursor, q)
            print(f"   {i}. {q['title']} (ID: {question_id})")
        
        conn.commit()
        
        # Final count
        cursor.execute("SELECT COUNT(*) FROM questions WHERE category_id = 1")
        final_leetcode = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM questions WHERE category_id = 2")
        final_ml = cursor.fetchone()[0]
        
        print(f"\n✅ Success!")
        print(f"   Total LeetCode questions: {final_leetcode}")
        print(f"   Total ML Design questions: {final_ml}")
        print(f"\n🎉 Added {final_leetcode - existing_leetcode} LeetCode and {final_ml - existing_ml} ML questions!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    main()
