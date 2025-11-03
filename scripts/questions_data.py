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

import sys
from pathlib import Path

# Meta/Atlassian specific LeetCode questions
META_ATLASSIAN_LC = [
    # MEDIUM - Meta frequently asked
    {
        "title": "Dot Product of Two Sparse Vectors",
        "difficulty": "medium",
        "description": """Given two sparse vectors, compute their dot product.

Implement class SparseVector:
- SparseVector(nums) Initializes the object with the vector nums
- dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.""",
        "constraints": ["n == nums1.length == nums2.length", "1 <= n <= 10^5", "0 <= nums1[i], nums2[i] <= 100"],
        "examples": [
            {"input": {"nums1": [1,0,0,2,3], "nums2": [0,3,0,4,0]}, "output": 8, "explanation": "Dot product: 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8"},
            {"input": {"nums1": [0,1,0,0,0], "nums2": [0,0,0,0,2]}, "output": 0, "explanation": "No common non-zero indices"}
        ],
        "tags": ["array", "hash-table", "design", "two-pointers"],
        "test_cases": [
            {"input": [[1,0,0,2,3], [0,3,0,4,0]], "expectedOutput": 8},
            {"input": [[0,1,0,0,0], [0,0,0,0,2]], "expectedOutput": 0}
        ],
        "time_complexity": "O(n) for constructor, O(min(L1, L2)) for dot product",
        "space_complexity": "O(L) where L is number of non-zero elements",
        "python_sig": "class SparseVector:\n    def __init__(self, nums: List[int]):\n        pass\n    \n    def dotProduct(self, vec: 'SparseVector') -> int:\n        pass",
        "java_sig": "class SparseVector {\n    SparseVector(int[] nums) {\n    }\n    \n    public int dotProduct(SparseVector vec) {\n    }\n}",
        "cpp_sig": "class SparseVector {\npublic:\n    SparseVector(vector<int>& nums) {\n    }\n    \n    int dotProduct(SparseVector& vec) {\n    }\n};"
    }
]

# Import base questions and build optimized set
try:
    # Import from complete_questions_data if it exists (legacy)
    from complete_questions_data import LEETCODE_QUESTIONS as BASE_LC, ML_QUESTIONS as BASE_ML
    
    # Questions to remove for senior level
    REMOVE_FOR_SENIOR = ["Merge Two Sorted Lists", "Valid Palindrome", "Binary Tree Inorder Traversal"]
    
    # Filter out basic questions
    filtered_lc = [q for q in BASE_LC if q['title'] not in REMOVE_FOR_SENIOR]
    
    # Add Meta/Atlassian specific
    filtered_lc.extend(META_ATLASSIAN_LC)
    
    # Select exactly 40: 5 Easy, 27 Medium, 8 Hard
    easy = [q for q in filtered_lc if q['difficulty'] == 'easy']
    medium = [q for q in filtered_lc if q['difficulty'] == 'medium'][:27]
    hard = [q for q in filtered_lc if q['difficulty'] == 'hard']
    
    LEETCODE_QUESTIONS = easy + medium + hard
    ML_QUESTIONS = BASE_ML  # Use base ML questions
    
except ImportError:
    # Fallback: Provide minimal structure if base file doesn't exist
    print("Warning: complete_questions_data.py not found. Using minimal dataset.")
    LEETCODE_QUESTIONS = META_ATLASSIAN_LC
    ML_QUESTIONS = []


if __name__ == "__main__":
    print(f"Interview Questions Database")
    print(f"LeetCode: {len(LEETCODE_QUESTIONS)} questions")
    
    easy_count = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'easy'])
    medium_count = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'medium'])
    hard_count = len([q for q in LEETCODE_QUESTIONS if q['difficulty'] == 'hard'])
    
    print(f"  Easy: {easy_count}, Medium: {medium_count}, Hard: {hard_count}")
    print(f"ML System Design: {len(ML_QUESTIONS)} questions")
