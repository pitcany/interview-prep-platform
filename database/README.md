# Interview Questions Database

**50 Questions Optimized for Meta & Atlassian Senior ML Engineer Interviews**

## Quick Start

```bash
# Import all questions into your database
python3 scripts/import_all_questions.py

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
- **Facebook News Feed Ranking** (Hard) - Core Meta product, 3B+ users
- **Instagram Reels Recommendations** (Hard) - Multi-modal video ML
- **Real-time Ad Targeting & Ranking** (Hard) - Meta's revenue engine
- **AI Content Moderation** (Hard) - Platform safety at scale
- **Spam Detection for Messaging** (Medium) - Privacy-preserving ML
- **A/B Testing Platform** (Medium) - ML infrastructure
- **Atlassian Search Ranking** (Medium) - Enterprise search for Jira/Confluence
- **Real-time Fraud Detection** (Hard) - Payment systems
- **Video Understanding System** (Hard) - Multi-modal ML for billions of videos
- **Real-time Personalization** (Medium) - User modeling at scale

## Files

### Database
- `schema.sql` - Database schema definition
- `README.md` - This file

### Data Source
- `scripts/questions_complete.json` - **Source of truth** for all 50 questions

### Import Script
- `scripts/import_all_questions.py` - Python script to import all questions from JSON

## Import Method

### Using the Import Script (Recommended)
```bash
python3 scripts/import_all_questions.py
```

This script:
- Reads from `scripts/questions_complete.json`
- Imports all 50 questions with complete data
- Includes hidden test cases
- Sets up all question relationships

## Database Locations

- **Linux**: `~/.config/interview-prep-platform/interview-prep.db`
- **macOS**: `~/Library/Application Support/interview-prep-platform/interview-prep.db`
- **Windows**: `%APPDATA%\interview-prep-platform\interview-prep.db`

## Question Details

Each LeetCode question includes:
- Complete problem description
- Constraints and edge cases
- Examples with explanations
- Visible test cases (2-4 cases shown to user)
- Hidden test cases (run on submission for validation)
- Function signatures (Python, Java, C++)
- Time/space complexity requirements
- Topic tags
- **LeetCode URL** - Direct link to official solutions and discussions
- **Complete solutions** in Python, Java, and C++
- **Solution explanations** with algorithm approach

Each ML question includes:
- Detailed scenario
- System requirements
- Evaluation criteria
- Key components to design
- Success metrics
- **Hints** - Progressive hints to guide thinking
- **Sample solutions** with architecture diagrams

## Customization

To modify questions:

1. Edit `scripts/questions_complete.json`
2. Run the import script: `python3 scripts/import_all_questions.py`
3. Verify changes in the application

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
5. Ensure Python 3 and better-sqlite3 are available

---

**Ready to ace your Meta & Atlassian interviews!** 🚀
