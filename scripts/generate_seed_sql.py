#!/usr/bin/env python3
"""
Generate SQL seed file from questions_data.py

Single-purpose script: Converts Python question data to SQL INSERT statements.

Usage:
    python3 scripts/generate_seed_sql.py

Output:
    database/seed_complete.sql (ready to import)
"""

import json
import sys
from pathlib import Path

# Import from single source of truth
sys.path.insert(0, str(Path(__file__).parent))
from questions_data_full import LEETCODE_QUESTIONS, ML_QUESTIONS


def escape_sql_string(s):
    """Escape single quotes for SQL"""
    if s is None:
        return ""
    return str(s).replace("'", "''")


def generate_hints(q):
    """Generate helpful hints for a question based on tags and difficulty"""
    hints = []
    tags = q.get('tags', [])
    difficulty = q.get('difficulty', 'medium')
    title = q.get('title', '').lower()
    
    # Tag-based hints
    if 'hash-table' in tags or 'hash table' in tags:
        hints.append("Consider using a hash map or dictionary to store and look up values efficiently.")
    if 'array' in tags:
        hints.append("Think about the array indices and how you can traverse or manipulate them.")
    if 'two-pointers' in tags or 'two pointers' in tags:
        hints.append("Try using two pointers - one starting from the beginning and one from the end.")
    if 'sliding-window' in tags or 'sliding window' in tags:
        hints.append("Consider maintaining a window of elements that slides through the array.")
    if 'stack' in tags:
        hints.append("A stack data structure (LIFO) might be useful here.")
    if 'queue' in tags:
        hints.append("Consider using a queue (FIFO) data structure.")
    if 'tree' in tags or 'binary-tree' in tags:
        hints.append("Think about tree traversal: DFS (depth-first) or BFS (breadth-first).")
    if 'graph' in tags:
        hints.append("Consider graph traversal algorithms like DFS or BFS.")
    if 'dynamic-programming' in tags or 'dp' in tags:
        hints.append("Break down the problem into smaller subproblems. What's the optimal substructure?")
    if 'greedy' in tags:
        hints.append("Try making the locally optimal choice at each step.")
    if 'sorting' in tags:
        hints.append("Would sorting the input help simplify the problem?")
    if 'binary-search' in tags:
        hints.append("If the input is sorted, binary search can achieve O(log n) time complexity.")
    if 'backtracking' in tags:
        hints.append("Try exploring all possibilities using recursion and backtracking.")
    if 'string' in tags:
        hints.append("Consider string manipulation techniques like concatenation, slicing, or pattern matching.")
    
    # Difficulty-based hints
    if difficulty == 'easy':
        hints.append("Start with a brute force approach, then optimize if needed.")
    elif difficulty == 'medium':
        hints.append("Think about the time and space complexity trade-offs.")
    else:  # hard
        hints.append("This is a challenging problem. Break it down into smaller parts.")
    
    # Title-specific hints (common patterns)
    if 'sum' in title:
        hints.append("Consider what pairs or combinations of numbers could sum to the target.")
    if 'parentheses' in title or 'bracket' in title:
        hints.append("Track opening and closing brackets, ensuring they match correctly.")
    if 'merge' in title:
        hints.append("Think about how to combine two sorted sequences efficiently.")
    if 'reverse' in title:
        hints.append("Consider reversing the entire sequence or parts of it.")
    if 'search' in title:
        hints.append("If the data is sorted, binary search can be very efficient.")
    
    # Add LeetCode URL if available
    if 'leetcode_url' in q:
        hints.append(f"LeetCode URL: {q['leetcode_url']}")
    
    # Ensure we have at least ONE hint (required)
    if len(hints) == 0:
        hints.append("Read the problem description carefully and identify the key constraints.")
    elif len(hints) < 2:
        # Add a general hint if we only have one
        hints.insert(0, "Read the problem description carefully and identify the key constraints.")
        if len(hints) < 2:
            hints.append("Work through the examples step by step to understand the pattern.")
    
    return hints


def generate_hidden_test_cases(q):
    """Generate hidden test cases (typically 3) based on the question"""
    hidden_cases = []
    test_cases = q.get('test_cases', [])
    title = q.get('title', '').lower()
    tags = q.get('tags', [])
    
    # If the question already has hidden_test_cases defined, use those
    if 'hidden_test_cases' in q and q['hidden_test_cases']:
        return q['hidden_test_cases']
    
    # Generate 3 hidden test cases based on common edge cases
    # This is a simplified approach - in production, you'd want more sophisticated generation
    
    # Case 1: Edge case with larger input or boundary values
    # Case 2: Different pattern from visible test cases
    # Case 3: Corner case (empty-like scenarios if applicable, or max/min values)
    
    # For now, we'll generate some generic edge cases
    # In a real system, you'd analyze the problem structure more carefully
    
    # Generate at least 3 hidden test cases
    # Note: This is a simplified generator - you may want to manually specify hidden cases
    # in questions_data_full.py for better quality
    
    # If we can't generate intelligently, return empty list
    # The user can manually add hidden_test_cases to questions_data_full.py
    # For now, return empty - hidden cases should be manually added to questions_data_full.py
    # or we can generate basic variations
    
    return hidden_cases


def generate_leetcode_insert(q, question_id):
    """Generate SQL INSERT statements for a LeetCode question"""
    sql = []

    # Use hints from question data if available, otherwise generate them
    hints = q.get('hints', [])
    if not hints:
        hints = generate_hints(q)
    hints_json = json.dumps(hints) if hints else '[]'
    
    # Generate hidden test cases (typically 3)
    hidden_test_cases = generate_hidden_test_cases(q)
    hidden_test_cases_json = json.dumps(hidden_test_cases) if hidden_test_cases else '[]'
    
    # Insert main question
    sql.append(f"""-- {q['title']} ({q['difficulty'].upper()})
INSERT INTO questions (id, category_id, title, difficulty, description, constraints, examples, tags, hints) VALUES
({question_id}, 1, '{escape_sql_string(q['title'])}', '{q['difficulty']}',
'{escape_sql_string(q['description'])}',
'{escape_sql_string(json.dumps(q['constraints']))}',
'{escape_sql_string(json.dumps(q['examples']))}',
'{escape_sql_string(json.dumps(q['tags']))}',
'{escape_sql_string(hints_json)}');
""")
    
    # Insert LeetCode-specific data
    sql.append(f"""INSERT INTO leetcode_questions (question_id, function_signature_python, function_signature_java, function_signature_cpp, test_cases, hidden_test_cases, expected_time_complexity, expected_space_complexity, solution_python, solution_java, solution_cpp, solution_explanation) VALUES
({question_id},
'{escape_sql_string(q['python_sig'])}',
'{escape_sql_string(q['java_sig'])}',
'{escape_sql_string(q['cpp_sig'])}',
'{escape_sql_string(json.dumps(q['test_cases']))}',
'{escape_sql_string(hidden_test_cases_json)}',
'{escape_sql_string(q['time_complexity'])}',
'{escape_sql_string(q['space_complexity'])}',
'{escape_sql_string(q.get('solution_python', ''))}',
'{escape_sql_string(q.get('solution_java', ''))}',
'{escape_sql_string(q.get('solution_cpp', ''))}',
'{escape_sql_string(q.get('solution_explanation', ''))}');
""")
    
    return "\n".join(sql)


def generate_ml_insert(q, question_id):
    """Generate SQL INSERT statements for an ML System Design question"""
    sql = []
    
    # Insert main question
    sql.append(f"""-- {q['title']} ({q['difficulty'].upper()})
INSERT INTO questions (id, category_id, title, difficulty, description, tags) VALUES
({question_id}, 2, '{escape_sql_string(q['title'])}', '{q['difficulty']}',
'{escape_sql_string(q['description'])}',
'{escape_sql_string(json.dumps(q['tags']))}');
""")
    
    # Insert ML-specific data
    sql.append(f"""INSERT INTO ml_design_questions (question_id, scenario, requirements, evaluation_criteria, key_components, sample_solution) VALUES
({question_id},
'{escape_sql_string(q['scenario'])}',
'{escape_sql_string(json.dumps(q['requirements']))}',
'{escape_sql_string(json.dumps(q['evaluation_criteria']))}',
'{escape_sql_string(json.dumps(q['key_components']))}',
'{escape_sql_string(q.get('sample_solution', ''))}');
""")
    
    return "\n".join(sql)


def main():
    output_file = Path(__file__).parent.parent / "database" / "seed_complete.sql"
    
    # LEETCODE_QUESTIONS is already optimized to exactly 40 questions (5 Easy, 27 Medium, 8 Hard)
    selected_leetcode = LEETCODE_QUESTIONS
    
    easy_count = len([q for q in selected_leetcode if q['difficulty'] == 'easy'])
    medium_count = len([q for q in selected_leetcode if q['difficulty'] == 'medium'])
    hard_count = len([q for q in selected_leetcode if q['difficulty'] == 'hard'])
    
    print(f"🔧 Generating seed SQL file (Optimized for Meta & Atlassian)...")
    print(f"   LeetCode questions: {len(selected_leetcode)} ({easy_count} Easy, {medium_count} Medium, {hard_count} Hard)")
    print(f"   ML Design questions: {len(ML_QUESTIONS)}")
    
    sql_lines = [
        "-- Complete Seed Data: 40 LeetCode + 10 ML System Design Questions",
        "-- Optimized for Meta & Atlassian Senior ML Engineer Interviews",
        "-- Generated by generate_seed_sql.py",
        "-- ",
        "-- Distribution:",
        f"--   LeetCode: {easy_count} Easy, {medium_count} Medium, {hard_count} Hard = {len(selected_leetcode)} Total",
        f"--   ML Design: {len(ML_QUESTIONS)} questions",
        "--",
        "-- Meta-specific additions: Sparse Vectors, K Closest Points, Buildings with Ocean View, etc.",
        "-- Atlassian-specific: Search/Discovery system for Jira/Confluence",
        "",
        "-- Ensure categories exist",
        "INSERT OR IGNORE INTO question_categories (id, name, description) VALUES",
        "    (1, 'leetcode', 'LeetCode-style coding problems'),",
        "    (2, 'ml_system_design', 'Machine Learning System Design questions');",
        "",
        "-- ============================================",
        "-- LEETCODE QUESTIONS",
        "-- ============================================",
        ""
    ]
    
    question_id = 1
    
    # Add LeetCode questions
    for i, q in enumerate(selected_leetcode, 1):
        sql_lines.append(f"-- Question {question_id}: {q['title']}")
        sql_lines.append(generate_leetcode_insert(q, question_id))
        sql_lines.append("")
        question_id += 1
    
    # Add ML questions
    sql_lines.append("")
    sql_lines.append("-- ============================================")
    sql_lines.append("-- ML SYSTEM DESIGN QUESTIONS")
    sql_lines.append("-- ============================================")
    sql_lines.append("")
    
    for i, q in enumerate(ML_QUESTIONS, 1):
        sql_lines.append(f"-- Question {question_id}: {q['title']}")
        sql_lines.append(generate_ml_insert(q, question_id))
        sql_lines.append("")
        question_id += 1
    
    # Write to file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))
    
    print(f"✅ Generated: {output_file}")
    print(f"   Total questions: {question_id - 1}")
    print(f"   File size: {output_file.stat().st_size / 1024:.1f} KB")
    print("")
    print("📝 To import into database:")
    print("   sqlite3 path/to/interview-prep.db < database/seed_complete.sql")


if __name__ == '__main__':
    main()
