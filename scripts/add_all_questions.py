#!/usr/bin/env python3
"""
Add all 50 LeetCode and 15 ML System Design questions to the database.
Run this script to populate your interview prep platform with questions.

Usage:
    python scripts/add_all_questions.py
"""

import sqlite3
import os
import json
from pathlib import Path

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

# LeetCode Questions Data Structure
LEETCODE_QUESTIONS = [
    # EASY (8)
    {
        "title": "Two Sum",
        "difficulty": "easy",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\nYou can return the answer in any order.",
        "constraints": ["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "-10^9 <= target <= 10^9"],
        "examples": [{"input": {"nums": [2,7,11,15], "target": 9}, "output": [0,1], "explanation": "nums[0] + nums[1] == 9"}],
        "tags": ["array", "hash-table"],
        "test_cases": [
            {"input": [[2,7,11,15], 9], "expectedOutput": [0,1]},
            {"input": [[3,2,4], 6], "expectedOutput": [1,2]},
            {"input": [[3,3], 6], "expectedOutput": [0,1]}
        ],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "python_sig": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        pass",
        "java_sig": "class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        \n    }\n}",
        "cpp_sig": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        \n    }\n};"
    },
    # Add more questions here...
]

ML_QUESTIONS = [
    {
        "title": "Design Netflix Recommendation System",
        "difficulty": "medium",
        "description": "Design a personalized movie/TV show recommendation system for Netflix with 200M+ subscribers.",
        "scenario": "Netflix wants to improve user engagement by recommending personalized content. The system must handle real-time recommendations, cold start problems, and diverse content catalogs.",
        "requirements": [
            "Handle 200M+ active users",
            "Real-time personalized recommendations",
            "Handle cold start for new users",
            "Support multiple recommendation strategies",
            "A/B testing capability",
            "Explainability for recommendations"
        ],
        "evaluation_criteria": {
            "problem_understanding": "Clarified requirements and success metrics",
            "data_pipeline": "Comprehensive feature engineering approach",
            "model_design": "Appropriate model architecture for recommendations",
            "scalability": "System handles scale efficiently",
            "evaluation": "Clear offline and online metrics",
            "cold_start": "Strategy for new users/items"
        },
        "key_components": [
            "Data Collection & Features",
            "Candidate Generation", 
            "Ranking Model",
            "Serving Infrastructure",
            "Evaluation Metrics",
            "A/B Testing",
            "Cold Start Strategy"
        ],
        "tags": ["recommendation", "ranking", "distributed-systems", "collaborative-filtering"]
    },
    # Add more ML questions...
]

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
