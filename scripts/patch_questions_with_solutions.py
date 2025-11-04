#!/usr/bin/env python3
"""
Patch questions_data_full.py with comprehensive solutions
This script adds solutions to all questions in the database
"""

import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

# Import solutions
from comprehensive_solutions import get_leetcode_solution, get_ml_solution

def create_backup(file_path):
    """Create a backup of the original file"""
    backup_path = file_path.with_suffix(f'.backup.{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    shutil.copy2(file_path, backup_path)
    print(f"✅ Created backup: {backup_path}")
    return backup_path

def read_questions_file(file_path):
    """Read and parse the questions file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Execute the file to get the data
    local_vars = {}
    exec(content, {}, local_vars)

    return local_vars.get('LEETCODE_QUESTIONS', []), local_vars.get('ML_QUESTIONS', [])

def add_solutions_to_questions(leetcode_questions, ml_questions):
    """Add solutions to all questions"""

    # Add solutions to LeetCode questions
    enhanced_leetcode = []
    for question in leetcode_questions:
        q = question.copy()
        title = q.get('title', '')

        # Get solution for this question
        solution = get_leetcode_solution(title)

        # Add solution fields if not present
        if 'solution_python' not in q:
            q['solution_python'] = solution['solution_python']
        if 'solution_java' not in q:
            q['solution_java'] = solution['solution_java']
        if 'solution_cpp' not in q:
            q['solution_cpp'] = solution['solution_cpp']
        if 'solution_explanation' not in q:
            q['solution_explanation'] = solution['solution_explanation']

        enhanced_leetcode.append(q)
        print(f"  ✓ Added solutions for: {title}")

    # Add solutions to ML Design questions
    enhanced_ml = []
    for question in ml_questions:
        q = question.copy()
        title = q.get('title', '')

        # Get solution for this question
        solution = get_ml_solution(title)

        # Add sample solution if not present
        if 'sample_solution' not in q:
            q['sample_solution'] = solution

        enhanced_ml.append(q)
        print(f"  ✓ Added solution for: {title}")

    return enhanced_leetcode, enhanced_ml

def write_updated_file(file_path, leetcode_questions, ml_questions):
    """Write the updated questions back to file"""

    def format_dict(d, indent=4):
        """Format a dictionary as Python code"""
        lines = ["{"]
        items = list(d.items())
        for i, (key, value) in enumerate(items):
            # Format the value based on type
            if isinstance(value, str):
                # Properly escape the string
                value_str = repr(value)
            elif isinstance(value, (list, dict)):
                value_str = json.dumps(value, indent=8)
            else:
                value_str = repr(value)

            # Add comma except for last item
            comma = "," if i < len(items) - 1 else ""
            lines.append(f'        "{key}": {value_str}{comma}')

        lines.append("    }")
        return "\n".join(lines)

    content = '''#!/usr/bin/env python3
"""
Complete dataset of 40 LeetCode + 10 ML System Design questions with solutions
Distribution: 8 Easy, 35 Medium, 8 Hard LeetCode questions
Generated with comprehensive solutions added
"""

# 40 LeetCode Questions with complete solutions
LEETCODE_QUESTIONS = [
'''

    # Add each LeetCode question
    for i, q in enumerate(leetcode_questions):
        if i > 0:
            content += ",\n"
        content += "    " + format_dict(q)

    content += '''
]

# 10 ML System Design Questions with sample solutions
ML_QUESTIONS = [
'''

    # Add each ML question
    for i, q in enumerate(ml_questions):
        if i > 0:
            content += ",\n"
        content += "    " + format_dict(q)

    content += '''
]
'''

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Updated file: {file_path}")

def main():
    # Path to questions file
    questions_file = Path(__file__).parent / "questions_data_full.py"

    if not questions_file.exists():
        print(f"❌ Error: {questions_file} not found!")
        sys.exit(1)

    print("🚀 Starting to patch questions with solutions...")

    # Create backup
    backup_path = create_backup(questions_file)

    try:
        # Read existing questions
        print("\n📖 Reading existing questions...")
        leetcode_questions, ml_questions = read_questions_file(questions_file)
        print(f"  Found {len(leetcode_questions)} LeetCode questions")
        print(f"  Found {len(ml_questions)} ML Design questions")

        # Add solutions
        print("\n💡 Adding solutions to questions...")
        enhanced_leetcode, enhanced_ml = add_solutions_to_questions(
            leetcode_questions, ml_questions
        )

        # Write updated file
        print("\n💾 Writing updated file...")
        write_updated_file(questions_file, enhanced_leetcode, enhanced_ml)

        print("\n✅ Successfully patched all questions with solutions!")
        print(f"   Backup saved at: {backup_path}")
        print("\n📝 Next steps:")
        print("   1. Run: python3 scripts/generate_seed_sql.py")
        print("   2. Import: sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql")

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print(f"   Restoring from backup...")
        shutil.copy2(backup_path, questions_file)
        print(f"   ✅ Restored original file from backup")
        sys.exit(1)

if __name__ == "__main__":
    main()