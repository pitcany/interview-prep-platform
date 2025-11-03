# Interview Questions Database

**50 Questions Optimized for Meta & Atlassian Senior ML Engineer Interviews**

## Quick Start

```bash
# Import all questions into your database
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# Verify
sqlite3 ~/.config/interview-prep-platform/interview-prep.db "SELECT COUNT(*) FROM questions;"
# Expected: 50
```

## Contents

### LeetCode Questions (40)
- **5 Easy** - Foundation problems
- **27 Medium** - Core interview focus (67.5%)
- **8 Hard** - Senior-level challenges

**Meta-Frequently Asked:**
- Merge k Sorted Lists (Hard) - Classic Meta problem
- Trapping Rain Water (Hard)
- Arrays & strings focus matching Meta's 38% interview emphasis

### ML System Design (10)
- **Content Moderation** (Meta-specific)
- **News Feed Ranking** (Meta/Facebook)
- **Atlassian Search System** (Jira/Confluence)
- **Recommendation Systems** (Netflix, YouTube, E-commerce)
- **Search & Ranking** (Google Search)
- **Computer Vision** (Face Recognition, Autonomous Vehicles)
- **NLP** (Machine Translation)
- **Fraud Detection** (Credit Card Fraud)

## Files

### Database
- `schema.sql` - Database schema definition
- `seed_complete.sql` - All 50 questions ready to import
- `README.md` - This file

### Scripts
- `questions_data.py` - **Source of truth** for all questions
- `generate_seed_sql.py` - Generates seed_complete.sql from questions_data.py
- `add_all_questions.py` - Python script to import questions directly

## Import Methods

### Method 1: SQL Import (Recommended)
```bash
sqlite3 /path/to/interview-prep.db < database/seed_complete.sql
```

### Method 2: Python Script
```bash
python3 scripts/add_all_questions.py
```

### Method 3: Custom Import
```python
from scripts.questions_data import LEETCODE_QUESTIONS, ML_QUESTIONS
# Use questions in your own code
```

## Database Locations

- **Linux**: `~/.config/interview-prep-platform/interview-prep.db`
- **macOS**: `~/Library/Application Support/interview-prep-platform/interview-prep.db`
- **Windows**: `%APPDATA%\interview-prep-platform\interview-prep.db`

## Question Details

Each LeetCode question includes:
- Complete problem description
- Constraints and edge cases
- Examples with explanations
- 3-5 test cases
- Function signatures (Python, Java, C++)
- Time/space complexity
- Topic tags
- **LeetCode URL** - Direct link to official solutions and discussions

Each ML question includes:
- Detailed scenario
- System requirements
- Evaluation criteria
- Key components to design
- Success metrics

## Customization

To modify questions:

1. Edit `scripts/questions_data.py`
2. Regenerate: `python3 scripts/generate_seed_sql.py`
3. Import updated SQL file

## Why These Questions?

**Meta Focus:**
- 38% arrays/strings (matches Meta interview data)
- Sparse operations (frequently asked)
- Practical array/string problems
- Content moderation & news feed systems

**Atlassian Focus:**
- Reduced easy questions (senior level)
- Product-specific ML systems (Jira/Confluence)
- Emphasis on deployment & monitoring

**Senior Level:**
- Only 5 easy questions (vs typical 8)
- 27 medium questions (core focus)
- 8 hard questions for depth

## Support

For issues:
1. Check database path is correct
2. Verify schema exists: `sqlite3 db.db < database/schema.sql`
3. Review import logs for errors
4. Check file permissions

---

**Ready to ace your Meta & Atlassian interviews!** 🚀
