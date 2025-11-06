# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

An Electron-based desktop application for LeetCode and ML System Design interview preparation with AI-powered feedback. Built with React + TypeScript frontend, Node.js backend, and Python code execution service.

**Tech Stack:** Electron 28+, React 18, TypeScript, Monaco Editor, React Flow, TailwindCSS, SQLite (better-sqlite3), Local LLM (OpenAI-compatible API)

## Development Commands

### Setup & Installation
```bash
# Install all dependencies
npm install

# Set up Python environment
cd python-service && pip install -r requirements.txt && cd ..

# Initialize database (creates schema)
npm run db:init

# Import interview questions (50 questions for Meta/Atlassian)
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

### Development
```bash
# Start dev server (React + Electron with hot reload)
npm run dev

# Run only React dev server
npm run dev:react

# Run only Electron (requires React server running)
npm run dev:electron

# Type checking
npm run typecheck

# Linting
npm run lint
```

### Build & Package
```bash
# Build both React and Electron
npm run build

# Build only React frontend
npm run build:react

# Build only Electron main process
npm run build:electron

# Package for current platform
npm run package

# Platform-specific packaging
npm run package:mac
npm run package:win
npm run package:linux
```

### Testing
```bash
# Run tests with Vitest
npm run test
```

### Database Operations
```bash
# Initialize/reset database schema
npm run db:init

# Seed questions (deprecated - use SQL import instead)
npm run db:seed

# Import questions (recommended)
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql

# Database locations by platform:
# - Linux: ~/.config/interview-prep-platform/interview-prep.db
# - macOS: ~/Library/Application Support/interview-prep-platform/interview-prep.db
# - Windows: %APPDATA%\interview-prep-platform\interview-prep.db
```

### Question Management
```bash
# Modify questions source of truth
vim scripts/questions_data_full.py

# Regenerate SQL seed file
python3 scripts/generate_seed_sql.py

# Import updated questions
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

## Troubleshooting

### `npm start` fails with "Module version mismatch" error

**Symptom:**
```
Error: The module '/path/to/better-sqlite3/build/Release/better_sqlite3.node'
was compiled against a different Node.js version using
NODE_MODULE_VERSION 127. This version of Node.js requires
NODE_MODULE_VERSION 119.
```

**Root Cause:**
Native modules (like better-sqlite3) were compiled for system Node.js instead of Electron's embedded Node.js version.

**Solution:**
```bash
# Rebuild native modules for Electron
npx electron-rebuild

# Or reinstall dependencies (triggers postinstall hook)
npm install
```

**When this happens:**
- After cloning the repository
- After switching to a git worktree
- After updating Node.js or Electron versions
- If `node_modules` was copied from another location

**Prevention:**
The `postinstall` script in package.json automatically runs `electron-rebuild` and copies database files after `npm install`, but manual rebuild may be needed in worktrees or when dependencies are cached.

### Setting up a new git worktree

**When this happens:**
- After creating a new git worktree
- When `node_modules` is empty or incomplete
- When `dist/` directory doesn't exist

**Complete Setup Process:**
```bash
# 1. Install all dependencies (also runs electron-rebuild and copies database files)
npm install

# 2. Build Electron TypeScript code
npm run build:electron

# 3. Start the application
npm start
```

**Note:** The `postinstall` script automatically:
- Rebuilds native modules for Electron (`electron-rebuild`)
- Copies database SQL files to `dist/database/` (`npm run copy:database`)

This ensures worktrees are ready to run immediately after `npm install` and `npm run build:electron`.

### Port 5173 already in use

**Symptom:**
```
Error: Port 5173 is already in use
```

**Solution:**
```bash
# Find and kill the process using port 5173
lsof -ti:5173 | xargs kill -9

# Or use a different port in vite.config.ts
```

### Database not found

**Symptom:**
```
Error: SQLITE_CANTOPEN: unable to open database file
```

**Solution:**
```bash
# Initialize the database
npm run db:init

# Import questions
sqlite3 ~/.config/interview-prep-platform/interview-prep.db < database/seed_complete.sql
```

## Architecture

### Process Model

The application follows Electron's multi-process architecture:

1. **Main Process** (`electron/main.ts`)
   - Creates BrowserWindow
   - Manages application lifecycle
   - Initializes all backend services (database, code executor, Local LLM)
   - Handles IPC communication via `ipcMain.handle()`
   - Database path: `app.getPath('userData')/interview-prep.db`

2. **Renderer Process** (React app in `src/`)
   - React 18 with TypeScript
   - Runs in sandboxed browser context (no Node.js access)
   - Uses Vite for dev server and builds
   - Communicates via `window.electronAPI` (exposed through preload script)

3. **Preload Script** (`electron/preload.ts`)
   - Bridges main and renderer processes using `contextBridge`
   - Exposes safe IPC methods as `window.electronAPI`
   - Security: `nodeIntegration: false`, `contextIsolation: true`

### Service Architecture

**Backend Services** (`electron/services/`):

- **DatabaseService** (`database.ts`)
  - Uses better-sqlite3 for synchronous SQLite operations
  - Schema auto-initialized from `database/schema.sql`
  - Handles users, questions, submissions, feedback, progress tracking
  - Key methods: `createUser()`, `getQuestions()`, `createCodeSubmission()`, `getUserProgress()`

- **CodeExecutorService** (`codeExecutor.ts`)
  - Executes Python/Java/C++ code in isolated environment
  - Uses temp directory: `os.tmpdir()/interview-prep-exec`
  - Timeout: 10s, Memory limit: 512MB
  - Test case execution with result comparison
  - **Note:** Python service integration is incomplete (files not yet implemented)

- **LocalLLMService** (`localLLM.ts`)
  - Generates personalized feedback using a local LLM (e.g., GPT OSS 20B)
  - Analyzes code submissions and system design diagrams
  - Returns structured feedback: scores, strengths, improvements
  - Connects to OpenAI-compatible API endpoint (vLLM, llama.cpp, text-generation-webui)
  - Configuration: `LLM_BASE_URL` and `LLM_MODEL` environment variables

### Frontend Architecture

**State Management** (`src/store/index.ts`):
- Zustand for global state (lightweight, no boilerplate)
- Stores: currentUser, preferences, currentQuestion, mockInterview, timerState
- No Redux needed for this app size

**API Layer** (`src/services/api.ts`):
- Single `APIService` class wrapping all `window.electronAPI` calls
- Type-safe wrappers for IPC communication
- Exported as singleton: `export const api = new APIService()`

**Key Components**:
- `CodeEditor/` - Monaco Editor wrapper for code editing
- `DiagramEditor/` - React Flow for ML system design diagrams
- `QuestionList/` - Browse and filter questions
- `TestRunner/` - Execute code against test cases
- `Timer/` - Mock interview countdown timer
- `MockInterviewSetup/` - Configure mock interview sessions
- `MockInterviewReport/` - Display results and feedback

**Pages**:
- `Login.tsx` - User selection/creation
- `Dashboard.tsx` - Main landing page
- `Practice.tsx` - Practice mode (LeetCode or ML Design)
- `MockInterview.tsx` - Timed interview sessions
- `Progress.tsx` - Analytics and submission history

### IPC Communication Pattern

All IPC follows this pattern:

1. **Main Process** (`electron/main.ts`):
   ```typescript
   ipcMain.handle('questions:getAll', async (_, category, difficulty) => {
     return await dbService.getQuestions(category, difficulty);
   });
   ```

2. **Preload** (`electron/preload.ts`):
   ```typescript
   contextBridge.exposeInMainWorld('electronAPI', {
     getQuestions: (category?, difficulty?) =>
       ipcRenderer.invoke('questions:getAll', category, difficulty)
   });
   ```

3. **Renderer** (`src/services/api.ts`):
   ```typescript
   async getQuestions(category?, difficulty?): Promise<Question[]> {
     return await this.api.getQuestions(category, difficulty);
   }
   ```

4. **React Component**:
   ```typescript
   import { api } from '../services/api';
   const questions = await api.getQuestions('leetcode', 'medium');
   ```

### Database Schema

**Key Tables**:
- `users` - User profiles and last login
- `user_preferences` - Editor theme, font size, etc.
- `question_categories` - `leetcode` and `ml_system_design`
- `questions` - All interview questions (50 total)
- `leetcode_questions` - Code problem details (test cases, function signatures, complexity)
- `ml_design_questions` - System design scenarios and requirements
- `code_submissions` - Code submission history with execution results
- `design_submissions` - Diagram data and explanations
- `mock_interviews` - Mock interview sessions (30min timed)
- `mock_interview_questions` - Questions assigned to each mock
- `feedback` - AI-generated feedback with scores
- `user_progress` - Per-question attempt tracking and stats

**Important Relationships**:
- Questions have category_id → question_categories
- LeetCode/ML Design questions extend base questions table (same ID)
- Submissions reference users and questions
- Feedback references submissions (polymorphic: code or design)
- Progress tracks attempts/solved status per user per question

### Data Flow Examples

**Code Submission Flow**:
1. User writes code in Monaco Editor
2. Click "Submit" → calls `api.submitCode()`
3. IPC to main process → `code:submit` handler
4. CodeExecutorService runs code against test cases
5. DatabaseService saves submission with results
6. Progress tracking updated (solved status, attempt count)
7. Optionally generate AI feedback via LocalLLMService

**Mock Interview Flow**:
1. User selects interview type → `api.startMockInterview()`
2. Main process creates mock_interviews row, returns mockId
3. Frontend starts 30min timer, randomly selects questions
4. Questions added to mock via `api.addQuestionToMock()`
5. User solves questions (same submission flow as practice)
6. Timer ends → `api.completeMockInterview()`
7. Generate comprehensive feedback for all submissions

## Important Patterns

### Type Safety
- All types defined in `src/types/index.ts`
- Shared between frontend and Electron main process
- Database results match TypeScript interfaces
- IPC calls are fully typed through preload definitions

### Question Data Management
- **Source of truth**: `scripts/questions_data_full.py`
- Generate SQL: `python3 scripts/generate_seed_sql.py` → `database/seed_complete.sql`
- Import: `sqlite3 <db-path> < database/seed_complete.sql`
- DO NOT manually edit SQL files (auto-generated)
- All questions include LeetCode URLs for official solutions

### Security Considerations
- Code execution sandboxed (temp directory, resource limits)
- No network access during code execution
- Renderer process isolated (no Node.js access)
- User data stored locally only
- Local LLM only receives code/diagrams for feedback (not executed there)

### Monaco Editor Integration
- Language support: Python, Java, C++
- Syntax highlighting and IntelliSense
- Theme syncs with user preferences
- Function signatures pre-populated from question data

### React Flow Diagrams
- Custom nodes for ML system components
- Export diagrams as JSON (stored in design_submissions)
- Future: Image export via html-to-image package

## Common Development Scenarios

### Adding a New IPC Method
1. Add handler in `electron/main.ts`: `ipcMain.handle('namespace:action', async (_, args) => {...})`
2. Expose in `electron/preload.ts`: Add to `electronAPI` object
3. Add type to `ElectronAPI` interface in preload.ts
4. Add wrapper method in `src/services/api.ts`
5. Use in React components via `api.methodName()`

### Adding a New Question Type
1. Update database schema in `database/schema.sql`
2. Add category to `question_categories` table
3. Create detail table (similar to `leetcode_questions` or `ml_design_questions`)
4. Add Python data in `scripts/questions_data_full.py`
5. Update `generate_seed_sql.py` to handle new type
6. Add TypeScript types in `src/types/index.ts`
7. Update UI components to render new question type

### Debugging IPC Issues
- Check DevTools console (renderer process errors)
- Check terminal output (main process errors)
- Verify handler name matches in main.ts, preload.ts, and api.ts
- Ensure preload script is compiled (`npm run build:electron`)
- In dev mode, main process runs with `NODE_ENV=development`

### Testing Code Execution
- Python service files not yet implemented (`python-service/` only has requirements.txt)
- CodeExecutorService expects: `executor.py`, `sandbox.py`, `test_runner.py`
- Temp files created in `os.tmpdir()/interview-prep-exec`
- Check execution logs in terminal when running `npm run dev`

## File Organization

```
interview-prep-platform/
├── electron/              # Main process code
│   ├── main.ts           # App entry, window creation, IPC handlers
│   ├── preload.ts        # IPC bridge (contextBridge)
│   └── services/         # Backend services
│       ├── database.ts   # SQLite operations
│       ├── codeExecutor.ts
│       ├── claudeAPI.ts      # DEPRECATED - Legacy Claude API service
│       └── localLLM.ts       # Local LLM service (current)
├── src/                  # React frontend (renderer process)
│   ├── components/       # Reusable UI components
│   ├── pages/           # Top-level route components
│   ├── services/
│   │   └── api.ts       # IPC wrapper for React
│   ├── store/
│   │   └── index.ts     # Zustand state management
│   └── types/
│       └── index.ts     # Shared TypeScript types
├── database/
│   ├── schema.sql       # Database structure
│   ├── seed_complete.sql # All 50 questions (auto-generated)
│   └── README.md
├── scripts/
│   ├── questions_data_full.py  # SOURCE OF TRUTH for questions
│   ├── generate_seed_sql.py    # Generate seed_complete.sql
│   ├── initDatabase.js         # npm run db:init
│   └── seedQuestions.js        # npm run db:seed (deprecated)
└── python-service/       # Code execution (NOT YET IMPLEMENTED)
    └── requirements.txt
```

## Environment Variables

Create `.env` file in project root:
```
# Local LLM Configuration
LLM_BASE_URL=http://localhost:8000  # Your local LLM API endpoint
LLM_MODEL=gpt-oss-20b  # Model name/identifier

# Code Execution Configuration
SANDBOX_MODE=local  # 'docker' or 'local' (docker not yet implemented)
MAX_EXECUTION_TIME=10000  # milliseconds
MAX_MEMORY=512  # MB
```

**Note:** Environment variables must be loaded before starting Electron. The main process reads `process.env.LLM_BASE_URL` and `process.env.LLM_MODEL` at startup.

### Running a Local LLM

Before starting the application, you need to run a local LLM with an OpenAI-compatible API. Options include:

**Option 1: vLLM (recommended for performance)**
```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server \
  --model /path/to/gpt-oss-20b \
  --host 0.0.0.0 \
  --port 8000 \
  --max-model-len 4096
```

**Option 2: llama.cpp server**
```bash
./server -m /path/to/model.gguf \
  --port 8000 \
  --host 0.0.0.0 \
  --ctx-size 4096
```

**Option 3: text-generation-webui with API**
```bash
python server.py --api --api-port 8000
```

## Known Limitations & TODOs

1. **Python Code Execution Service**: ✅ Implemented (see `python-service/` directory)
   - `python-service/executor.py` - Code execution logic with resource limits
   - `python-service/sandbox.py` - Security wrapper
   - `python-service/test_runner.py` - Test case runner

2. **LLM Feedback Quality**: Local LLMs may not follow JSON format as reliably as Claude API. The service includes robust parsing with fallbacks.

3. **Docker Sandboxing**: Planned but not implemented. Currently uses local execution (security risk).

4. **Java/C++ Execution**: CodeExecutorService has placeholders but no implementation.

5. **Diagram Export**: html-to-image dependency added but image export not fully implemented.

6. **Test Coverage**: Test files not yet created (Vitest configured but no tests).

## Resources

- Electron IPC: https://www.electronjs.org/docs/latest/tutorial/ipc
- better-sqlite3 docs: https://github.com/WiseLibs/better-sqlite3
- Monaco Editor React: https://github.com/suren-atoyan/monaco-react
- React Flow: https://reactflow.dev/
- Zustand: https://github.com/pmndrs/zustand
