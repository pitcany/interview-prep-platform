# Interview Prep Platform - Setup Guide

This guide will help you set up and run the Interview Prep Platform on your machine.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Node.js** (v18 or higher)
   - Download from: https://nodejs.org/
   - Verify: `node --version`

2. **Python** (3.10 or higher)
   - Download from: https://www.python.org/
   - Verify: `python --version` or `python3 --version`

3. **Docker** (for code sandboxing)
   - Download from: https://www.docker.com/
   - Verify: `docker --version`

4. **Claude API Key**
   - Get from: https://console.anthropic.com/
   - You'll need this for AI feedback generation

## Installation Steps

### 1. Clone and Install Dependencies

```bash
# Navigate to the project directory
cd interview-prep-platform

# Install Node.js dependencies
npm install

# Install Python dependencies
cd python-service
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Return to root
cd ..
```

### 2. Build Docker Images for Code Execution

Build the sandboxed execution environments:

```bash
# Build Python container
docker build -t interview-prep-python -f docker/python.Dockerfile docker/

# Build Java container
docker build -t interview-prep-java -f docker/java.Dockerfile docker/

# Build C++ container
docker build -t interview-prep-cpp -f docker/cpp.Dockerfile docker/

# Verify images
docker images | grep interview-prep
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your configuration:

```env
# Claude API Configuration
CLAUDE_API_KEY=your_api_key_here

# Code Execution Configuration
SANDBOX_MODE=docker
MAX_EXECUTION_TIME=10000
MAX_MEMORY=512

# Development
NODE_ENV=development
```

### 4. Initialize Database

```bash
# Initialize the database with schema
npm run db:init

# Seed with sample questions
npm run db:seed
```

The database will be created at:
- macOS/Linux: `~/.config/interview-prep-platform/interview-prep.db`
- Windows: `%APPDATA%/interview-prep-platform/interview-prep.db`

### 5. Create TypeScript Configuration

Create `tsconfig.json` in the root:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "allowJs": true,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "outDir": "dist",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

Create `electron/tsconfig.json`:

```json
{
  "extends": "../tsconfig.json",
  "compilerOptions": {
    "module": "CommonJS",
    "outDir": "../dist/electron"
  },
  "include": ["./**/*"],
  "exclude": ["node_modules"]
}
```

### 6. Create Vite Configuration

Create `vite.config.ts` in the root:

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  base: './',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    outDir: 'dist-react',
  },
});
```

### 7. Create Tailwind Configuration

Create `tailwind.config.js`:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Create `postcss.config.js`:

```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

### 8. Create Main CSS File

Create `src/App.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  @apply bg-gray-900 text-white;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
```

## Running the Application

### Development Mode

```bash
# Start the development server
npm run dev
```

This will:
1. Start the React dev server on http://localhost:5173
2. Launch Electron in development mode
3. Enable hot-reload for both frontend and Electron

### Building for Production

```bash
# Build the application
npm run build

# Package for your platform
npm run package

# Or package for specific platforms
npm run package:mac
npm run package:win
npm run package:linux
```

The packaged application will be in the `release/` directory.

## Usage

### First Time Setup

1. Launch the application
2. Create a new user or select an existing one
3. You'll be taken to the dashboard

### Practice Mode

1. Click "Practice" from the dashboard
2. Choose LeetCode or ML System Design
3. Select a question
4. Write your solution
5. Run tests or submit for feedback

### Mock Interview Mode

1. Click "Mock Interview" from the dashboard
2. Choose interview type (LeetCode or ML Design)
3. 30-minute timer will start
4. Complete the problems
5. Submit for AI feedback

### Progress Tracking

1. Click "Progress" from the dashboard
2. View your statistics, success rates, and history
3. Review past feedback

## Troubleshooting

### Docker Issues

If code execution fails:

```bash
# Check if Docker is running
docker ps

# Rebuild containers
docker build -t interview-prep-python -f docker/python.Dockerfile docker/
```

### Database Issues

If the database has issues:

```bash
# Delete and reinitialize
rm -rf ~/.config/interview-prep-platform/
npm run db:init
npm run db:seed
```

### Port Conflicts

If port 5173 is in use, you can change it in `package.json`:

```json
"dev:react": "vite --port 5174"
```

And update the port in `electron/main.ts`.

## Adding More Questions

### LeetCode Questions

1. Add to `database/seed.sql` following the pattern
2. Include test cases in JSON format
3. Run `npm run db:seed`

### ML Design Questions

1. Add to `database/seed.sql`
2. Include evaluation criteria and key components
3. Run `npm run db:seed`

## Development Tips

### Hot Reload

- React changes reload automatically
- Electron main process requires restart (Ctrl/Cmd + R)

### Debugging

- React: Open Chrome DevTools (Ctrl/Cmd + Shift + I)
- Electron: Check terminal for console logs
- Database: Use SQLite viewer to inspect data

### Testing

```bash
# Run tests
npm test
```

## Next Steps

1. Add more questions to the database
2. Customize the UI theme
3. Configure Claude API for feedback
4. Explore the codebase and extend features

## Support

For issues or questions:
- Check the README.md for architecture details
- Review the code comments
- Open an issue on GitHub

Happy coding! 🚀
