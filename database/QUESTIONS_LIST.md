# Complete Question List

This document lists all 50 LeetCode and 15 ML System Design questions that will be added to your platform.

## LeetCode Questions (50 Total)

### Easy (8 questions)
1. Two Sum - Array, Hash Table
2. Valid Parentheses - Stack, String
3. Merge Two Sorted Lists - Linked List
4. Best Time to Buy and Sell Stock - Array, DP
5. Valid Palindrome - Two Pointers, String
6. Climbing Stairs - Dynamic Programming
7. Binary Tree Inorder Traversal - Tree, DFS
8. Linked List Cycle - Linked List, Two Pointers

### Medium (35 questions)

**Arrays & Strings (12)**
9. Longest Substring Without Repeating Characters - Sliding Window
10. Add Two Numbers - Linked List, Math
11. Container With Most Water - Two Pointers
12. 3Sum - Array, Two Pointers
13. Group Anagrams - Hash Table, String
14. Longest Palindromic Substring - String, DP
15. Product of Array Except Self - Array, Prefix Sum
16. Spiral Matrix - Array, Matrix
17. Rotate Image - Array, Matrix
18. Set Matrix Zeroes - Array, Matrix
19. Subarray Sum Equals K - Array, Hash Table
20. Maximum Subarray - Array, Divide & Conquer

**Linked Lists (3)**
21. Remove Nth Node From End of List - Linked List, Two Pointers
22. Reverse Linked List II - Linked List
23. Swap Nodes in Pairs - Linked List, Recursion

**Trees (7)**
24. Binary Tree Level Order Traversal - Tree, BFS
25. Validate Binary Search Tree - Tree, DFS
26. Kth Smallest Element in BST - Tree, DFS
27. Binary Tree Right Side View - Tree, BFS
28. Path Sum II - Tree, Backtracking
29. Construct Binary Tree from Preorder and Inorder - Tree
30. Lowest Common Ancestor of Binary Tree - Tree, DFS

**Graphs (4)**
31. Number of Islands - Graph, DFS, BFS
32. Course Schedule - Graph, Topological Sort
33. Clone Graph - Graph, DFS, BFS
34. Word Search - Backtracking, DFS

**Dynamic Programming (6)**
35. Coin Change - DP
36. Longest Increasing Subsequence - DP
37. Unique Paths - DP
38. Word Break - DP
39. House Robber II - DP
40. Decode Ways - DP

**Other (3)**
41. Letter Combinations of Phone Number - Backtracking
42. Generate Parentheses - Backtracking
43. Permutations - Backtracking

### Hard (7 questions)

**Arrays & Strings (2)**
44. Trapping Rain Water - Array, Two Pointers, Stack
45. Median of Two Sorted Arrays - Binary Search, Divide & Conquer

**Trees (2)**
46. Binary Tree Maximum Path Sum - Tree, DFS
47. Serialize and Deserialize Binary Tree - Tree, Design

**Dynamic Programming (2)**
48. Regular Expression Matching - DP, String
49. Edit Distance - DP, String

**Graph (1)**
50. Word Ladder - Graph, BFS

## ML System Design Questions (15 Total)

### Recommendation Systems (3)
1. Design Netflix Movie Recommendation System
2. Design YouTube Video Recommendation Engine  
3. Design E-commerce Product Recommendation System

### Search & Ranking (3)
4. Design Google Search Ranking System
5. Design E-commerce Search with ML
6. Design News Feed Ranking (Facebook/Instagram)

### Computer Vision (2)
7. Design Face Recognition System
8. Design Object Detection System for Autonomous Vehicles

### NLP Systems (2)
9. Design Machine Translation System
10. Design Chatbot/Virtual Assistant

### Fraud & Anomaly Detection (2)
11. Design Credit Card Fraud Detection System
12. Design Spam Detection System

### Time Series & Forecasting (2)
13. Design Demand Forecasting System
14. Design Stock Price Prediction System

### Infrastructure (1)
15. Design A/B Testing Platform for ML Models

---

## How to Add These Questions

Run the generation script:
```bash
python scripts/add_all_questions.py
```

Or manually run the SQL file:
```bash
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

## Question Details

Each LeetCode question includes:
- ✅ Problem description
- ✅ Constraints
- ✅ Examples with explanations
- ✅ Test cases (3-5 per question)
- ✅ Function signatures (Python, Java, C++)
- ✅ Expected time/space complexity
- ✅ Tags for categorization

Each ML Design question includes:
- ✅ Scenario description
- ✅ Requirements list
- ✅ Evaluation criteria
- ✅ Key components to cover
- ✅ Sample solution approach
