# Interview Prep Platform - Question Database

This directory contains SQL seed files to populate your interview preparation platform with LeetCode and ML System Design questions.

## 📊 Question Distribution

### Complete Dataset (`seed_complete.sql`)
- **40 LeetCode Questions**
  - 8 Easy (20%)
  - 25 Medium (62.5%)
  - 7 Hard (17.5%)
- **10 ML System Design Questions**
  - Covering: Recommendations, Search, Computer Vision, NLP, Fraud Detection

**Total: 50 Questions**

## 🗂️ Files

### 1. `schema.sql`
Database schema definition with tables for:
- Questions (LeetCode & ML Design)
- User submissions and progress
- Mock interviews
- AI feedback

### 2. `seed_complete.sql`
**Complete question dataset** (40 LeetCode + 10 ML Design)
- Real LeetCode-style problems with full details
- Comprehensive ML system design questions
- Ready to import into your database

### 3. `seed_sample.sql`
Small sample dataset for testing (3 questions)

### 4. Other seed files
Legacy seed files from previous iterations

## 🚀 How to Import Questions

### Method 1: Using SQLite CLI

```bash
# Find your database location
# Linux: ~/.config/interview-prep-platform/interview-prep.db
# macOS: ~/Library/Application Support/interview-prep-platform/interview-prep.db
# Windows: %APPDATA%/interview-prep-platform/interview-prep.db

# Import complete dataset
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

### Method 2: Using Python Script

```bash
# From the app root directory
python3 scripts/add_all_questions.py
```

This script will:
- Automatically find your database
- Add all 40 LeetCode + 10 ML questions
- Show progress and confirmation

### Method 3: Using Node.js

```bash
npm run db:seed
```

## 📝 Question Details

### LeetCode Questions Include:
- Problem title and description
- Difficulty level
- Constraints and examples
- Test cases (3-5 per question)
- Function signatures (Python, Java, C++)
- Expected time/space complexity
- Tags for categorization

### ML System Design Questions Include:
- Problem scenario
- System requirements
- Evaluation criteria
- Key components to design
- Sample solutions and approaches

## 🎯 LeetCode Topics Covered

**Arrays & Strings** (12 questions)
- Sliding window, two pointers, hash tables
- Matrix operations, subarray problems

**Linked Lists** (4 questions)
- Traversal, reversal, cycle detection

**Trees** (8 questions)
- BST, traversals, LCA, construction

**Graphs** (4 questions)
- DFS, BFS, topological sort

**Dynamic Programming** (7 questions)
- Optimization problems, subsequences

**Backtracking** (3 questions)
- Combinations, permutations, constraints

**Other** (2 questions)
- Stack operations, greedy algorithms

## 🤖 ML System Design Topics Covered

1. **Recommendation Systems** (3)
   - Netflix, YouTube, E-commerce

2. **Search & Ranking** (3)
   - Google Search, E-commerce Search, News Feed

3. **Computer Vision** (2)
   - Face Recognition, Autonomous Vehicles

4. **NLP** (1)
   - Machine Translation

5. **Fraud Detection** (1)
   - Credit Card Fraud

## 🔍 Verify Import

```bash
# Check question count
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "SELECT category_id, COUNT(*) FROM questions GROUP BY category_id;"

# Expected output:
# 1|40    (LeetCode)
# 2|10    (ML Design)
```

## 📚 Question Quality

All questions are:
- ✅ Real LeetCode-style problems with proper difficulty
- ✅ Complete with examples, constraints, test cases
- ✅ Include function signatures for Python, Java, C++
- ✅ Tagged for easy filtering
- ✅ Production-ready for interview preparation

## 🛠️ Generating Custom Seed Files

To regenerate or customize the seed SQL:

```bash
# Edit questions in: scripts/complete_questions_data.py
# Then regenerate:
python3 scripts/generate_seed_sql.py
```

## 📖 Database Schema

### Core Tables
- `questions` - Main question data
- `leetcode_questions` - Coding problem specifics
- `ml_design_questions` - Design problem specifics
- `code_submissions` - User code submissions
- `design_submissions` - User design submissions
- `user_progress` - Tracking solved questions
- `mock_interviews` - Interview sessions
- `feedback` - AI-generated feedback

## 🎓 Usage Tips

1. **Start with Easy**: Filter by `difficulty = 'easy'` to build confidence
2. **Focus on Topics**: Use `tags` to practice specific areas
3. **Mock Interviews**: Select random questions for timed practice
4. **Track Progress**: The `user_progress` table tracks your journey
5. **Review Solutions**: Use test cases to validate your approach

## 📞 Support

If you encounter issues:
1. Verify database path is correct
2. Check schema is initialized (`schema.sql`)
3. Ensure no duplicate question IDs
4. Check file permissions

## 🔄 Updates

To add more questions:
1. Edit `scripts/complete_questions_data.py`
2. Run `python3 scripts/generate_seed_sql.py`
3. Import the updated `seed_complete.sql`

---

**Ready to start your interview preparation journey! 🚀**
