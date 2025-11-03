# Adding All 50 LeetCode + 15 ML Questions

## Quick Start

### Option 1: Use the Generator Script (Recommended)

```bash
cd interview-prep-platform

# Make script executable
chmod +x scripts/generate_and_add_questions.sh

# Run it!
./scripts/generate_and_add_questions.sh
```

This will:
1. Generate all 50 LeetCode questions
2. Generate all 15 ML System Design questions
3. Add them to your database
4. Show confirmation

### Option 2: Manual SQL Import

```bash
cd interview-prep-platform

# Run the comprehensive seed file
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_all.sql
```

### Option 3: Add Incrementally

Start with what we have (6 questions) and add more as needed:

```bash
# Current: 3 LeetCode + 3 ML (from seed_sample.sql)
# Already loaded if you ran `npm run db:seed`
```

## What's Included

### LeetCode Questions by Category

**Arrays (15 questions)**
- Two Sum, 3Sum, Container With Most Water
- Product of Array Except Self, Maximum Subarray
- Trapping Rain Water, Median of Two Sorted Arrays
- Spiral Matrix, Rotate Image, Set Matrix Zeroes
- Subarray Sum Equals K, And more...

**Strings (8 questions)**
- Longest Substring Without Repeating Characters
- Valid Parentheses, Valid Palindrome
- Longest Palindromic Substring, Group Anagrams
- Word Search, Word Break, Letter Combinations

**Linked Lists (6 questions)**
- Merge Two Sorted Lists, Add Two Numbers
- Linked List Cycle, Remove Nth Node
- Reverse Linked List II, Swap Nodes in Pairs

**Trees (10 questions)**
- Binary Tree Inorder Traversal, Level Order Traversal
- Validate BST, Kth Smallest in BST
- Binary Tree Right Side View, Path Sum II
- Lowest Common Ancestor, Serialize/Deserialize
- Binary Tree Maximum Path Sum, Construct from Traversals

**Graphs (4 questions)**
- Number of Islands, Course Schedule
- Clone Graph, Word Ladder

**Dynamic Programming (10 questions)**
- Climbing Stairs, Best Time to Buy/Sell Stock
- Coin Change, Longest Increasing Subsequence
- Unique Paths, Word Break, House Robber II
- Decode Ways, Regular Expression Matching, Edit Distance

**Backtracking (3 questions)**
- Generate Parentheses, Permutations, Letter Combinations

### ML System Design Questions

**Recommendation Systems (3)**
1. Netflix Movie Recommendations
2. YouTube Video Recommendations
3. E-commerce Product Recommendations

**Search & Ranking (3)**
4. Google Search Ranking
5. E-commerce Search
6. News Feed Ranking (Facebook/Instagram)

**Computer Vision (2)**
7. Face Recognition System
8. Object Detection for Autonomous Vehicles

**NLP (2)**
9. Machine Translation System
10. Chatbot/Virtual Assistant

**Fraud Detection (2)**
11. Credit Card Fraud Detection
12. Spam Detection System

**Forecasting (2)**
13. Demand Forecasting
14. Stock Price Prediction

**Infrastructure (1)**
15. A/B Testing Platform for ML

## Question Quality

Each question includes:

**LeetCode:**
- ✅ Complete problem description
- ✅ Constraints clearly specified
- ✅ 2-3 example test cases with explanations
- ✅ 3-5 actual test cases for validation
- ✅ Function signatures for Python, Java, C++
- ✅ Expected time and space complexity
- ✅ Relevant tags for categorization

**ML Design:**
- ✅ Realistic scenario (Meta/Google/Netflix scale)
- ✅ Clear requirements list
- ✅ Evaluation criteria (what to cover)
- ✅ Key components to design
- ✅ Sample solution approach
- ✅ Tags for categorization

## Verification

After adding questions, verify:

```bash
# Check question count
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "SELECT 
     (SELECT COUNT(*) FROM questions WHERE category_id=1) as leetcode,
     (SELECT COUNT(*) FROM questions WHERE category_id=2) as ml_design;"
```

Expected output:
```
leetcode|ml_design
50|15
```

## Testing

1. **Start the app:**
   ```bash
   npm run dev
   ```

2. **Go to Practice page**

3. **Filter by difficulty:**
   - Easy: Should see 8 questions
   - Medium: Should see 35 questions
   - Hard: Should see 7 questions

4. **Try a few questions:**
   - Select different difficulties
   - Try different languages
   - Run test cases

5. **Check Progress page:**
   - Stats should update after submissions
   - Charts should show data

## Adding More Questions Later

To add more questions, edit `scripts/add_all_questions.py`:

1. Add to `LEETCODE_QUESTIONS` list:
```python
{
    "title": "Your Question Title",
    "difficulty": "medium",
    "description": "...",
    "constraints": [...],
    "examples": [...],
    "tags": [...],
    "test_cases": [...],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "python_sig": "...",
    "java_sig": "...",
    "cpp_sig": "..."
}
```

2. Or add to `ML_QUESTIONS` list:
```python
{
    "title": "Design X System",
    "difficulty": "hard",
    "description": "...",
    "scenario": "...",
    "requirements": [...],
    "evaluation_criteria": {...},
    "key_components": [...],
    "tags": [...]
}
```

3. Run the script again:
```bash
python scripts/add_all_questions.py
```

## Question Sources

Questions are inspired by:
- LeetCode Top Interview Questions
- Meta/Google/Amazon interview patterns
- "Cracking the Coding Interview"
- "Elements of Programming Interviews"
- Meta ML System Design Interviews
- "Machine Learning System Design Interview" book

## Difficulty Distribution

**LeetCode:**
- Easy: 16% (8/50) - Good for warming up
- Medium: 70% (35/50) - Most common in interviews
- Hard: 14% (7/50) - For advanced practice

**ML Design:**
- Medium: 60% (9/15) - Standard system design
- Hard: 40% (6/15) - Complex, large-scale systems

## Next Steps

After adding all questions:

1. ✅ Practice mode is fully stocked
2. ✅ Users can practice 50 coding problems
3. ✅ Users can practice 15 ML system designs
4. ⏳ Build mock interview feature
5. ⏳ Add ML diagram editor
6. ⏳ Polish and deploy

## Customization

Want to focus on specific topics?

**For FAANG prep:** Keep all questions
**For startup interviews:** Focus on medium difficulty
**For specific role:** Filter by tags (use SQL queries)

Example: Get all graph questions:
```sql
SELECT * FROM questions 
WHERE tags LIKE '%graph%';
```

## Support

If you encounter issues:
1. Check database exists
2. Verify schema is up to date
3. Check for duplicate titles
4. Look at error messages
5. Refer to troubleshooting section in main README

---

**You're ready to add all 65 questions!** 🚀

Run the generator script and you'll have a fully-stocked interview prep platform.
