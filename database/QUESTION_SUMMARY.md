# Interview Prep Platform - Question Summary

> Source of truth: `database/seed_meta_atlassian.sql`. This document highlights the same question set for quick browsing.

## Complete Question List (50 Total)

### LeetCode Questions (40)

#### Easy (5 questions)
1. Two Sum - Array, Hash Table
2. Valid Parentheses - Stack, String
3. Merge Two Sorted Lists - Linked List
4. Climbing Stairs - Dynamic Programming
5. Linked List Cycle - Linked List, Two Pointers

#### Medium (32 questions)

**Arrays & Strings (10)**
6. Longest Substring Without Repeating Characters - Sliding Window
7. 3Sum - Two Pointers, Sorting
8. Container With Most Water - Two Pointers
9. Group Anagrams - Hash Table, Sorting
10. Maximum Subarray - Dynamic Programming
11. Spiral Matrix - Matrix Simulation
12. Rotate Image - Matrix Manipulation
13. Subarray Sum Equals K - Prefix Sum, Hash Table
14. Merge Intervals - Sorting, Intervals
15. Product of Array Except Self - Prefix Sum

**Linked Lists (4)**
16. Add Two Numbers - Math, Linked List
17. Letter Combinations of Phone Number - Backtracking
18. Remove Nth Node From End of List - Two Pointers
19. Reverse Linked List - Linked List

**Trees (5)**
20. Binary Tree Level Order Traversal - BFS
21. Validate Binary Search Tree - DFS, BST
22. Kth Smallest Element in BST - DFS, In-order
23. Lowest Common Ancestor - Tree Traversal
24. Valid Sudoku - Hash Table, Matrix

**Graphs (4)**
25. Number of Islands - DFS/BFS, Matrix
26. Clone Graph - Graph Traversal
27. Course Schedule - Topological Sort
28. Search in Rotated Sorted Array - Binary Search

**Dynamic Programming (6)**
29. Unique Paths - Grid DP
30. Minimum Path Sum - Grid DP
31. Jump Game - Greedy/DP
32. Word Break - String DP
33. Longest Increasing Subsequence - DP/Binary Search
34. Coin Change - DP

**Design & Other (3)**
35. Permutations - Backtracking
36. Combination Sum - Backtracking
37. Set Matrix Zeroes - Matrix
38. LRU Cache - Design, Hash Table + Doubly Linked List
39. Implement Trie - Design, String

#### Hard (3 questions)
40. Merge K Sorted Lists - Heap, Divide & Conquer

### ML System Design Questions (10)

#### Social Media & Content (4)
1. **Facebook News Feed Ranking System** (Hard)
   - 3B+ users, real-time personalization
   - Multi-objective optimization
   - Candidate generation + ranking
   - Key: Scale, latency, engagement metrics

2. **Instagram Reels/Explore Recommendations** (Hard)
   - Multi-modal content (vision, audio, text)
   - Balance personalization with discovery
   - Trending content integration
   - Key: Content understanding, viral signals

3. **Content Moderation System** (Hard)
   - Multi-modal detection (text, images, videos)
   - Multiple violation categories
   - Human-in-the-loop
   - Key: Precision/recall trade-off, adversarial robustness

4. **YouTube Video Recommendations** (Hard)
   - Billions of videos and users
   - Multi-objective (watch time, satisfaction)
   - Cold start handling
   - Key: Video understanding, diversity

#### Business & Monetization (2)
5. **Ad Targeting and Ranking System** (Hard)
   - CTR/CVR prediction
   - Auction mechanism
   - Real-time serving
   - Key: Multi-stakeholder optimization

6. **Real-time Fraud Detection** (Hard)
   - Payment transactions
   - Extreme class imbalance
   - Real-time inference (<50ms)
   - Key: Handling imbalanced data, concept drift

#### Search & Retrieval (1)
7. **E-commerce Search Ranking** (Hard)
   - Query understanding
   - Candidate generation
   - Learning to rank
   - Key: Information retrieval, personalization

#### Classification & Detection (1)
8. **Spam Detection System** (Medium)
   - Email/message spam
   - Adversarial attacks
   - Multi-language
   - Key: Adversarial ML, concept drift

#### Infrastructure & Platform (2)
9. **A/B Testing Platform for ML** (Medium)
   - Experiment design
   - Statistical analysis
   - Guardrail metrics
   - Key: Experimentation, statistics

10. **Real-time Personalization Engine** (Hard)
    - Cross-surface personalization
    - Real-time feature updates
    - Low latency (<50ms)
    - Key: Real-time ML, distributed systems

## Difficulty Distribution

### LeetCode
- Easy: 5 (12.5%)
- Medium: 32 (80%)
- Hard: 3 (7.5%)

**Average Difficulty**: Medium (optimized for senior interviews)

### ML System Design
- Medium: 2 (20%)
- Hard: 8 (80%)

## Key Topics Coverage

### Data Structures
- ✅ Arrays & Strings
- ✅ Hash Tables
- ✅ Linked Lists
- ✅ Stacks
- ✅ Trees (Binary Trees, BST)
- ✅ Graphs
- ✅ Heaps
- ✅ Tries

### Algorithms
- ✅ Two Pointers
- ✅ Sliding Window
- ✅ Binary Search
- ✅ DFS/BFS
- ✅ Backtracking
- ✅ Dynamic Programming
- ✅ Greedy
- ✅ Topological Sort

### ML Topics
- ✅ Recommendation Systems
- ✅ Ranking Systems
- ✅ Real-time ML
- ✅ Computer Vision
- ✅ NLP
- ✅ Fraud Detection
- ✅ Content Moderation
- ✅ Search & Retrieval
- ✅ A/B Testing
- ✅ Distributed Systems
- ✅ Feature Engineering
- ✅ Model Serving

## Company Relevance

### Meta-Focused (7 questions)
- News Feed Ranking ⭐⭐⭐
- Instagram Recommendations ⭐⭐⭐
- Content Moderation ⭐⭐⭐
- Ad Ranking ⭐⭐⭐
- Real-time Personalization ⭐⭐
- Fraud Detection ⭐⭐
- Spam Detection ⭐

### Atlassian-Focused (5 questions)
- Search Ranking ⭐⭐⭐
- A/B Testing Platform ⭐⭐⭐
- Spam Detection ⭐⭐
- Real-time Systems ⭐⭐
- Personalization ⭐

### Universal (All LeetCode + General ML)
- All 40 LeetCode questions are relevant
- System design principles apply everywhere

## Time Estimates

### LeetCode
- Easy: 15-20 minutes each
- Medium: 25-35 minutes each
- Hard: 40-50 minutes each

**Total practice time**: ~20-25 hours for all LeetCode

### ML System Design
- Medium: 30-40 minutes each
- Hard: 45-60 minutes each

**Total practice time**: ~8-10 hours for all ML design

## Study Plan (8 weeks)

### Weeks 1-2: Foundation (Easy + Basic Medium)
- Practice: Questions 1-15
- Focus: Arrays, Strings, Hash Tables

### Weeks 3-4: Core Algorithms (Medium)
- Practice: Questions 16-30
- Focus: Trees, Graphs, DP

### Weeks 5-6: Advanced + ML Design (Medium + Hard LeetCode + ML)
- LeetCode: Questions 31-40
- ML Design: Questions 1-6

### Weeks 7-8: ML Design + Mock Interviews
- ML Design: Questions 7-10
- Mock interviews using platform
- Review and iterate

## Success Metrics

### LeetCode
- ✅ Solve without hints
- ✅ Optimal time complexity
- ✅ Clean, readable code
- ✅ Handle edge cases
- ✅ Explain approach clearly

### ML System Design
- ✅ Clarify requirements
- ✅ Discuss trade-offs
- ✅ Draw clear diagrams
- ✅ Cover all components
- ✅ Discuss evaluation
- ✅ Production considerations

## Next Steps

1. **Seed the database**: Run the SQL file
2. **Start with Easy**: Build confidence
3. **Progress to Medium**: Focus here (80% of questions)
4. **Master ML Design**: 2 per week
5. **Mock Interviews**: Practice under time pressure
6. **Review feedback**: Learn from mistakes

Good luck! 🚀
