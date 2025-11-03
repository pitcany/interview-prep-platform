# Quick Start Guide

Get up and running with the Interview Prep Platform in 10 minutes!

## Prerequisites Installation

### 1. Install Node.js
```bash
# macOS (using Homebrew)
brew install node

# Windows (using Chocolatey)
choco install nodejs

# Or download from: https://nodejs.org/
```

### 2. Install Python
```bash
# macOS (using Homebrew)
brew install python@3.11

# Windows (using Chocolatey)
choco install python

# Or download from: https://www.python.org/
```

### 3. Install Docker
- macOS/Windows: Download Docker Desktop from https://www.docker.com/
- Linux: Follow instructions at https://docs.docker.com/engine/install/

## Installation (5 minutes)

```bash
# 1. Navigate to project directory
cd interview-prep-platform

# 2. Install Node dependencies
npm install

# 3. Set up Python environment
cd python-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..

# 4. Build Docker containers (one-time setup)
docker build -t interview-prep-python -f docker/python.Dockerfile docker/
docker build -t interview-prep-java -f docker/java.Dockerfile docker/
docker build -t interview-prep-cpp -f docker/cpp.Dockerfile docker/

# 5. Configure environment
cp .env.example .env
# Edit .env and add your CLAUDE_API_KEY

# 6. Initialize database
npm run db:init
npm run db:seed
```

## Run the Application

```bash
npm run dev
```

The app will open automatically in a new window!

## First Steps

1. **Create a User**
   - Click "Create New User"
   - Enter username and email
   - Click "Create User"

2. **Try Practice Mode**
   - Click "LeetCode Practice" from the dashboard
   - Select a question
   - Write your solution
   - Run tests

3. **Try Mock Interview**
   - Click "Mock Interview"
   - Choose interview type
   - Complete within 30 minutes
   - Get AI feedback

## Troubleshooting

### Docker Containers Not Running
```bash
# Check Docker is running
docker ps

# Rebuild containers if needed
docker build -t interview-prep-python -f docker/python.Dockerfile docker/
```

### Database Errors
```bash
# Reinitialize database
npm run db:init
npm run db:seed
```

### Port Already in Use
Edit `package.json` and change the port in `dev:react` script.

## Next Steps

1. Read [SETUP.md](./SETUP.md) for detailed configuration
2. Check [README.md](./README.md) for architecture details
3. Add more questions to the database
4. Customize the UI and themes

## Getting Help

- Review the detailed setup guide: `SETUP.md`
- Check the codebase documentation
- Look at example questions in `database/seed_sample.sql`

Happy interviewing! 🚀
