# 🚀 Quick Start: Import Questions

## Fastest Way to Import Questions

### Step 1: Locate Your Database

Your interview prep database is located at:

**Linux:**
```bash
~/.config/interview-prep-platform/interview-prep.db
```

**macOS:**
```bash
~/Library/Application Support/interview-prep-platform/interview-prep.db
```

**Windows:**
```bash
%APPDATA%\interview-prep-platform\interview-prep.db
```

### Step 2: Import Questions

Choose one method:

#### Method A: SQL Import (Fast & Reliable)

```bash
# Linux/macOS
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# Windows (PowerShell)
Get-Content database\seed_complete.sql | sqlite3 "$env:APPDATA\interview-prep-platform\interview-prep.db"
```

#### Method B: Python Script (Shows Progress)

```bash
python3 scripts/add_all_questions.py
```

This will:
- Find your database automatically
- Add all 50 questions
- Show you what was added
- Handle errors gracefully

### Step 3: Verify Import

```bash
# Check how many questions were added
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "SELECT COUNT(*) as total_questions FROM questions;"
```

Expected result: `50`

## ✅ Success!

You now have:
- ✅ 40 LeetCode questions (8 Easy, 25 Medium, 7 Hard)
- ✅ 10 ML System Design questions
- ✅ Complete test cases and function signatures
- ✅ Ready for your interview prep

## 📚 What's Next?

1. **Start the app** and browse questions
2. **Filter by difficulty** to find your level
3. **Use tags** to practice specific topics
4. **Track progress** as you solve problems
5. **Take mock interviews** for timed practice

## 📖 More Info

- **Full question list**: See `database/COMPLETE_QUESTION_LIST.md`
- **Database guide**: See `database/README.md`
- **Complete summary**: See `QUESTIONS_COMPLETE_SUMMARY.md`

## 🆘 Troubleshooting

### Database not found?
Make sure the interview prep app has been run at least once to create the database.

### Permission denied?
Check file permissions on the database directory.

### Questions already exist?
The SQL file uses `INSERT` (not `INSERT OR IGNORE`), so re-importing will create duplicates. If you need to re-import:

```bash
# Delete existing questions first
sqlite3 ~/.config/interview-prep-platform/interview-prep.db \
  "DELETE FROM questions;"

# Then import again
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

---

**Happy coding! 🎯**
