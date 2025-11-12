# Interview Prep Platform

A lean desktop application for LeetCode and ML System Design interview preparation with personalized AI feedback.

## Features

- **Practice Mode**: 50 LeetCode questions + 20 ML System Design questions
- **Mock Interviews**: 30-minute timed sessions with realistic scenarios
- **Multi-language Support**: Python, Java, C++
- **Sandboxed Code Execution**: Secure local code running
- **Structured Diagrams**: Save and export system design diagrams
- **AI Feedback**: Personalized performance analysis via Local LLM (Ollama recommended) or Cloud APIs
- **Multi-user Support**: Track progress across multiple users
- **Progress Analytics**: Success rates, time spent, attempt history

## Tech Stack

### Frontend
- **Electron** (v28+) - Desktop app framework
- **React 18** + **TypeScript** - UI framework
- **Monaco Editor** - Code editing (VS Code editor)
- **React Flow** - Structured diagram tool
- **TailwindCSS** - Styling
- **Recharts** - Progress visualization

### Backend
- **Electron Main Process** (Node.js)
- **Python 3.10+** - Code execution service
- **SQLite** - Local database
- **Docker** (optional) - Code sandboxing
- **Local LLM** (Ollama/vLLM/llama.cpp) or Cloud APIs - AI feedback generation

### Code Execution Sandbox
- **Judge0 API** (self-hosted) or custom Docker containers
- Isolated execution environment per language
- Resource limits (CPU, memory, time)

## Project Structure

```
interview-prep-platform/
├── electron/                    # Electron main process
│   ├── main.ts                 # Entry point
│   ├── preload.ts              # IPC bridge
│   └── services/
│       ├── database.ts         # SQLite operations
│       ├── codeExecutor.ts     # Code execution manager
│       ├── localLLM.ts         # Local LLM feedback (current)
│       └── claudeAPI.ts        # Legacy Claude API (deprecated)
├── src/                        # React frontend
│   ├── components/
│   │   ├── CodeEditor/        # Monaco editor wrapper
│   │   ├── DiagramEditor/     # React Flow diagrams
│   │   ├── Timer/             # Mock interview timer
│   │   ├── QuestionList/      # Browse questions
│   │   └── FeedbackReport/    # AI feedback display
│   ├── pages/
│   │   ├── Dashboard.tsx      # Main landing
│   │   ├── Practice.tsx       # Practice mode
│   │   ├── MockInterview.tsx  # Timed interview
│   │   └── Progress.tsx       # Analytics
│   ├── services/
│   │   └── api.ts             # IPC communication
│   └── types/
│       └── index.ts           # TypeScript definitions
├── python-service/            # Python execution backend
│   ├── executor.py           # Code runner
│   ├── sandbox.py            # Security wrapper
│   └── test_runner.py        # Test case execution
├── database/
│   ├── schema.sql            # Database schema
│   └── seed.sql              # Initial questions
├── public/
│   └── questions/            # Question JSON files
│       ├── leetcode/
│       └── ml-design/
└── docker/                   # Sandboxing containers
    ├── python.Dockerfile
    ├── java.Dockerfile
    └── cpp.Dockerfile
```

## Database Schema

See `database/schema.sql` for full schema. Key tables:
- `users` - User profiles
- `questions` - LeetCode & ML design questions
- `submissions` - Code/diagram submissions
- `mock_interviews` - Interview sessions
- `feedback` - AI-generated feedback
- `progress` - Attempt tracking

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- Docker (optional - for code sandboxing)
- **Ollama** (recommended - for AI feedback) OR Cloud LLM API key

### Installation

```bash
# Install dependencies
npm install

# Set up Python environment
cd python-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure AI feedback (choose one option)
# Option 1: Ollama (recommended - see OLLAMA_SETUP.md)
ollama pull llama3.1:8b
echo "LLM_BASE_URL=http://localhost:11434" > .env
echo "LLM_MODEL=llama3.1:8b" >> .env

# Option 2: Cloud API (OpenAI/Anthropic/etc.)
# echo "LLM_BASE_URL=https://api.openai.com" > .env
# echo "LLM_MODEL=gpt-4" >> .env
# echo "OPENAI_API_KEY=your-key-here" >> .env

# Initialize database
npm run db:init

# Start development
npm run dev
```

## Development Commands

```bash
npm run dev          # Start Electron in dev mode
npm run build        # Build for production
npm run package      # Create distributable
npm run test         # Run tests
npm run db:migrate   # Run database migrations
npm run db:seed      # Seed initial questions
```

## Configuration

Edit `.env`:
```env
# AI Feedback Configuration
LLM_BASE_URL=http://localhost:11434  # Ollama default
LLM_MODEL=llama3.1:8b

# Code Execution Configuration
SANDBOX_MODE=docker  # 'docker' or 'local'
MAX_EXECUTION_TIME=10000  # milliseconds
MAX_MEMORY=512  # MB
```

**AI Feedback Options:**
- **Ollama (Recommended)**: Free, private, offline-capable - See [OLLAMA_SETUP.md](OLLAMA_SETUP.md)
- **Cloud APIs**: OpenAI, Anthropic, or any OpenAI-compatible API endpoint

## Troubleshooting

### `npm start` fails with "Module version mismatch"

If you see an error like:
```
Error: The module 'better-sqlite3' was compiled against a different Node.js version
```

**Fix:**
```bash
# Rebuild native modules for Electron
npx electron-rebuild
```

This typically happens:
- After cloning the repo
- After using git worktrees
- After updating Node.js or Electron

The `postinstall` script should handle this automatically, but may need manual rebuild in some cases.

### Port 5173 already in use

```bash
# Kill the process using the port
lsof -ti:5173 | xargs kill -9
```

### Database not initialized

```bash
# Initialize database and import questions
npm run db:init
python3 scripts/import_all_questions.py
```

## Usage

### Practice Mode
1. Select LeetCode or ML System Design
2. Choose a question
3. Write code/design diagrams
4. Run tests or submit
5. Review feedback

### Mock Interview Mode
1. Select interview type
2. 30-minute timer starts
3. Solve problem(s)
4. Submit when complete
5. Receive detailed AI feedback

## Architecture Decisions

### Why Electron?
- Cross-platform (Windows, Mac, Linux)
- Familiar React development
- Access to Node.js APIs
- No browser restrictions

### Why Local LLM (Ollama)?
- **Privacy**: Your code never leaves your machine
- **Cost**: Free after initial setup (no per-request fees)
- **Speed**: Low latency compared to cloud APIs
- **Offline**: Works without internet connection
- **Flexibility**: Swap models easily based on needs

### Why SQLite?
- No server setup
- Portable database file
- Fast for desktop apps
- Built-in with Node.js

### Why React Flow?
- Production-ready diagram library
- Customizable nodes
- Export/import capabilities
- Active community

## Security Considerations

- Code runs in isolated Docker containers (when enabled)
- Resource limits prevent infinite loops
- No network access during code execution
- User data stored 100% locally
- AI feedback runs locally (with Ollama) or via cloud (optional)
- No code sent to external services unless using cloud LLM option

## Roadmap

- [ ] Phase 1: Core structure + database (Week 1)
- [ ] Phase 2: Code editor + execution (Week 2)
- [ ] Phase 3: Diagram tool + ML questions (Week 3)
- [ ] Phase 4: Mock interview mode (Week 4)
- [ ] Phase 5: AI feedback integration (Week 5)
- [ ] Phase 6: Progress tracking + analytics (Week 6)

## License

MIT
