# Quick Start Guide

Get your Interview Prep Platform running in 5 minutes.

## Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.10+
- Git
- **Ollama** (recommended for AI feedback) - See [OLLAMA_SETUP.md](OLLAMA_SETUP.md)

## Setup

```bash
# 1. Install dependencies
npm install
cd python-service && pip install -r requirements.txt && cd ..

# 2. Initialize database
npm run db:init

# 3. Import questions (50 questions for Meta/Atlassian interviews)
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# 4. Configure AI Feedback (Optional but Recommended)
# See OLLAMA_SETUP.md for full instructions
ollama pull llama3.1:8b  # Takes 2-5 minutes
echo "LLM_BASE_URL=http://localhost:11434" > .env
echo "LLM_MODEL=llama3.1:8b" >> .env

# 5. Start the app
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
- **AI-powered feedback** (100% local with Ollama - no cloud required!)
- Progress analytics
- **LeetCode solution links** - Access official solutions for each question

## Customization

### Add More Questions

1. Edit `scripts/questions_data_full.py`
2. Run `python3 scripts/generate_seed_sql.py`
3. Import: `sqlite3 path/to/db < database/seed_complete.sql`

### Configure AI Feedback

**Option 1: Ollama (Recommended - Free & Private)**
```bash
# Full guide: OLLAMA_SETUP.md
ollama pull llama3.1:8b
# Configure .env as shown in setup step 4 above
```

**Option 2: Cloud LLM (OpenAI, Anthropic, etc.)**
```bash
# Point to any OpenAI-compatible API
echo "LLM_BASE_URL=https://api.openai.com" > .env
echo "LLM_MODEL=gpt-4" >> .env
echo "OPENAI_API_KEY=your-key-here" >> .env
```

See [LLM_COMPARISON.md](LLM_COMPARISON.md) for detailed comparison.

## Documentation

- **Ollama Setup**: See `OLLAMA_SETUP.md` (AI feedback configuration)
- **LLM Comparison**: See `LLM_COMPARISON.md` (Ollama vs Cloud APIs)
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

**AI feedback not working?**
- Run `ollama list` to verify model is installed
- Check `ollama serve` is running
- Verify `.env` file exists with correct settings
- See `OLLAMA_SETUP.md` for detailed troubleshooting

---

**Ready to practice!** 🚀
