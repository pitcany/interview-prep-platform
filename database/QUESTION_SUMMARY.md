# Interview Prep Platform – Question Summary

> Source of truth: `database/seed_complete.sql` (generated via `scripts/generate_seed_sql.py`).

## LeetCode Breakdown (40 questions)

### Easy (5)
- Two Sum
- Valid Parentheses
- Best Time to Buy and Sell Stock
- Climbing Stairs
- Linked List Cycle

### Medium (27)
- **Arrays & Strings**: Longest Substring Without Repeating Characters, Container With Most Water, 3Sum, Group Anagrams, Longest Palindromic Substring, Product of Array Except Self, Spiral Matrix, Rotate Image, Set Matrix Zeroes, Subarray Sum Equals K, Maximum Subarray
- **Linked Lists**: Add Two Numbers, Remove Nth Node From End of List, Reverse Linked List II, Swap Nodes in Pairs
- **Trees**: Binary Tree Level Order Traversal, Validate Binary Search Tree, Kth Smallest Element in a BST, Binary Tree Right Side View, Path Sum II, Construct Binary Tree from Preorder and Inorder Traversal, Lowest Common Ancestor of a Binary Tree
- **Graphs & Backtracking**: Number of Islands, Course Schedule, Clone Graph, Word Search
- **Dynamic Programming**: Coin Change

### Hard (8)
- Trapping Rain Water
- Median of Two Sorted Arrays
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree
- Regular Expression Matching
- Edit Distance
- Word Ladder
- Merge k Sorted Lists

## ML System Design Scenarios (10)
- Design Netflix Movie Recommendation System
- Design YouTube Video Recommendation Engine
- Design E-commerce Product Recommendation System
- Design Google Search Ranking System
- Design E-commerce Search with ML
- Design News Feed Ranking (Facebook/Instagram)
- Design Face Recognition System
- Design Object Detection System for Autonomous Vehicles
- Design Machine Translation System
- Design Credit Card Fraud Detection System

## Difficulty Distribution
- **LeetCode**: 5 Easy · 27 Medium · 8 Hard (weighted toward senior-level interviews)
- **ML System Design**: 2 Medium · 8 Hard

## Coverage Snapshot
- **Data structures**: arrays, strings, hash tables, linked lists, trees, graphs, matrices, tries, heaps
- **Algorithmic patterns**: sliding window, two pointers, backtracking, BFS/DFS, topological sort, dynamic programming, divide & conquer, greedy, heap-based merging, system design data structures
- **ML themes**: large-scale ranking/recommendations, search, fraud/abuse detection, computer vision, NLP, experimentation, personalization, responsible AI, high-availability serving

## Regenerating the Seed
1. Update `scripts/questions_data_full.py`
2. Run `python3 scripts/generate_seed_sql.py`
3. Import with `sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql`

This keeps the repository DRY while ensuring the SQL seed, Python helpers, and documentation all reference the same dataset.

