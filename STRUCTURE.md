# Repository Structure

Clean, DRY structure with zero redundancies.

## Files (9 total)

### Root (2 files)
- `README.md` - Project overview, tech stack, architecture
- `QUICKSTART.md` - 5-minute setup guide

### Database (3 files)
- `schema.sql` - Database table definitions (174 lines)
- `seed_complete.sql` - 50 interview questions ready to import (auto-generated)
- `README.md` - Database usage guide

### Scripts (5 files)
- `questions_data_full.py` - Source of truth: 51 base questions with LeetCode URLs
- `questions_data.py` - Smart filter: Selects 40 for Meta/Atlassian
- `generate_seed_sql.py` - Converts Python → SQL
- `add_all_questions.py` - Alternative Python-based import
- `add_leetcode_urls.py` - Helper: Generates LeetCode URLs from titles

## Data Flow

```
questions_data_full.py (edit this to change questions)
         ↓
questions_data.py (filters & optimizes)
         ↓
generate_seed_sql.py (run: python3 scripts/generate_seed_sql.py)
         ↓
seed_complete.sql (import: sqlite3 db.db < database/seed_complete.sql)
```

## What Was Removed

- **19 redundant markdown files** (6,292 lines)
- **4 empty/partial SQL files**
- **1 duplicate Python script**

Total: **24 files removed**, **73% reduction**

## Single Source of Truth

Each concept exists in exactly ONE place:
- Questions data → `questions_data_full.py`
- Import SQL → `seed_complete.sql` (auto-generated)
- Database schema → `schema.sql`
- Setup guide → `QUICKSTART.md`
- Project docs → `README.md`

## Quick Reference

**Start developing:**
```bash
cat QUICKSTART.md
```

**Modify questions:**
```bash
vim scripts/questions_data_full.py
python3 scripts/generate_seed_sql.py
```

**Import questions:**
```bash
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

---

Everything you need, nothing you don't. ✨
