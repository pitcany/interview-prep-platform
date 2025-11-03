# Quick Start Guide

Get your Interview Prep Platform running in 5 minutes.

## Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.10+
- Git

## Setup

```bash
# 1. Install dependencies
npm install
cd python-service && pip install -r requirements.txt && cd ..

# 2. Initialize database
npm run db:init

# 3. Import questions (50 questions for Meta/Atlassian interviews)
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# 4. Start the app
npm start
```

## Database Locations

- **Linux**: `~/.config/interview-prep-platform/interview-prep.db`
- **macOS**: `~/Library/Application Support/interview-prep-platform/interview-prep.db`
- **Windows**: `%APPDATA%\interview-prep-platform\interview-prep.db`

## Usage

1. **Practice Mode**: Browse and solve 40 LeetCode + 10 ML System Design questions
2. **Mock Interviews**: Take timed 30-minute interview sessions
3. **Progress Tracking**: View your stats and improvement over time

## Key Features

- 40 LeetCode questions (optimized for Meta & Atlassian)
- 10 ML System Design questions
- Multi-language support (Python, Java, C++)
- AI-powered feedback
- Progress analytics

## Customization

### Add More Questions

1. Edit `scripts/questions_data_full.py`
2. Run `python3 scripts/generate_seed_sql.py`
3. Import: `sqlite3 path/to/db < database/seed_complete.sql`

### Configure AI Feedback

Edit Claude API settings in the app preferences.

## Documentation

- **Questions Database**: See `database/README.md`
- **Project Details**: See main `README.md`

## Troubleshooting

**Database not found?**
- Run `npm run db:init` first

**Questions not showing?**
- Import seed file: Check database location above

**App won't start?**
- Verify Node.js and Python versions
- Check `npm install` completed successfully

---

**Ready to practice!** 🚀
