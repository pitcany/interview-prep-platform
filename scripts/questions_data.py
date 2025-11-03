#!/usr/bin/env python3
"""
Single Source of Truth: Interview Questions Database

Optimized for Meta & Atlassian Senior ML Engineer Interviews (2025)

Contains:
- 40 LeetCode questions (5 Easy, 27 Medium, 8 Hard)
- 10 ML System Design questions

Based on actual interview patterns:
- Meta: Arrays/strings (38%), trees, graphs, sparse operations
- Atlassian: ML coding, practical systems, product design

Usage:
    from questions_data import LEETCODE_QUESTIONS, ML_QUESTIONS
"""

# Import full question database
from questions_data_full import LEETCODE_QUESTIONS as ALL_LC, ML_QUESTIONS as ALL_ML

# Meta/Atlassian specific additions
META_ATLASSIAN_ADDITIONS = [
    # Dot Product of Sparse Vectors - see questions_data_full.py line reference
    # K Closest Points - see questions_data_full.py  
    # Buildings With Ocean View - see questions_data_full.py
    # Minimum Remove to Make Valid Parentheses - see questions_data_full.py
    # Valid Parenthesis String - see questions_data_full.py
    # Expression Add Operators - see questions_data_full.py
]

# Questions to remove for senior level (too basic)
REMOVE_FOR_SENIOR = [
    "Merge Two Sorted Lists",
    "Valid Palindrome",
    "Binary Tree Inorder Traversal"
]

# Build optimized set: Remove basic + ensure exactly 40 questions
filtered_lc = [q for q in ALL_LC if q['title'] not in REMOVE_FOR_SENIOR]

# Select exactly 40: 5 Easy, 27 Medium, 8 Hard
easy = [q for q in filtered_lc if q['difficulty'] == 'easy'][:5]
medium = [q for q in filtered_lc if q['difficulty'] == 'medium'][:27]
hard = [q for q in filtered_lc if q['difficulty'] == 'hard'][:8]

# Export optimized questions
LEETCODE_QUESTIONS = easy + medium + hard
ML_QUESTIONS = ALL_ML  # Keep all 10 ML questions

# Metadata for reference
META_SPECIFIC = [
    "Dot Product of Two Sparse Vectors",
    "K Closest Points to Origin",
    "Buildings With an Ocean View",
    "Minimum Remove to Make Valid Parentheses",
    "Valid Parenthesis String",
    "Expression Add Operators"
]

ATLASSIAN_SPECIFIC_ML = [
    "Design Search/Discovery System for Atlassian Products"
]

if __name__ == "__main__":
    print(f"📊 Interview Questions Database")
    print(f"   Optimized for Meta & Atlassian Senior ML Engineer")
    print(f"")
    print(f"LeetCode: {len(LEETCODE_QUESTIONS)} questions")
    print(f"  Easy: {len(easy)}, Medium: {len(medium)}, Hard: {len(hard)}")
    print(f"")
    print(f"ML System Design: {len(ML_QUESTIONS)} questions")
    print(f"")
    print(f"Meta-specific: {len([q for q in LEETCODE_QUESTIONS if q['title'] in META_SPECIFIC])} LeetCode problems")
    print(f"Atlassian-specific: {len([q for q in ML_QUESTIONS if q['title'] in ATLASSIAN_SPECIFIC_ML])} ML problems")

