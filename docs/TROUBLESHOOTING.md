# Troubleshooting Guide

Comprehensive troubleshooting guide for common issues with the Interview Prep Platform.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Build and Development Issues](#build-and-development-issues)
- [Runtime Issues](#runtime-issues)
- [Database Issues](#database-issues)
- [Code Execution Issues](#code-execution-issues)
- [LLM/AI Feedback Issues](#llmai-feedback-issues)
- [Performance Issues](#performance-issues)
- [Platform-Specific Issues](#platform-specific-issues)
- [Getting Help](#getting-help)

## Installation Issues

### npm install fails with "Module version mismatch"

**Symptom:**
```
Error: The module '/path/to/better-sqlite3/build/Release/better_sqlite3.node'
was compiled against a different Node.js version
```

**Cause:** Native modules compiled for system Node.js instead of Electron's Node.js version.

**Solution:**
```bash
# Rebuild native modules for Electron
npx @electron/rebuild

# Or reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Prevention:** The postinstall script should handle this automatically, but manual rebuild may be needed after switching branches or updating Electron.

---

### npm install fails with "C++20 or later required"

**Symptom:**
```
error: "C++20 or later required."
npm error command failed
```

**Cause:** Node.js v25+ requires C++20 for native module compilation.

**Solution:**
```bash
# Skip native module build during install
npm install --ignore-scripts

# Manually rebuild for Electron
npx @electron/rebuild
```

**Long-term Fix:** Update build tools to support C++20:
- **macOS:** Update Xcode Command Line Tools
- **Windows:** Install Visual Studio 2019/2022
- **Linux:** Update gcc/g++ to version 10+

---

### Python dependencies fail to install

**Symptom:**
```
ERROR: Could not find a version that satisfies the requirement <package>
```

**Solution:**
```bash
# Ensure Python 3.8+ is installed
python3 --version

# Update pip
python3 -m pip install --upgrade pip

# Install dependencies
cd python-service
pip3 install -r requirements.txt
```

**Alternative:** Use virtual environment:
```bash
cd python-service
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Build and Development Issues

### npm run dev fails - Port 5173 already in use

**Symptom:**
```
Error: Port 5173 is already in use
```

**Solution:**
```bash
# Find and kill process using port 5173
lsof -ti:5173 | xargs kill -9  # macOS/Linux

# Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

**Alternative:** Change port in `vite.config.ts`:
```typescript
export default defineConfig({
  server: {
    port: 5174,  // Changed from 5173
  },
});
```

---

### npm run build:electron fails with TypeScript errors

**Symptom:**
```
error TS2688: Cannot find type definition file for 'node'.
```

**Cause:** Missing @types/node or TypeScript misconfiguration.

**Solution:**
```bash
# Install missing types
npm install --save-dev @types/node

# Or reinstall dependencies
npm install
```

---

### Hot reload not working in development

**Symptom:** Changes to React components don't reflect in the running app.

**Solutions:**

1. **Check if Vite dev server is running:**
   ```bash
   # Should see output on http://localhost:5173
   npm run dev:react
   ```

2. **Clear Vite cache:**
   ```bash
   rm -rf node_modules/.vite
   npm run dev
   ```

3. **Check Electron is loading correct URL:**
   ```typescript
   // electron/main.ts should have:
   mainWindow.loadURL('http://localhost:5173');  // Not file://
   ```

---

### electron-builder fails to package

**Symptom:**
```
Error: Cannot find module 'app-builder-bin'
```

**Solution:**
```bash
# Reinstall electron-builder
npm install --save-dev electron-builder

# Clear cache and rebuild
rm -rf node_modules/.cache
npm run build
npm run package
```

## Runtime Issues

### App crashes on startup

**Check logs:**
```bash
# macOS
tail -f ~/Library/Logs/interview-prep-platform/main.log

# Windows
type %USERPROFILE%\AppData\Roaming\interview-prep-platform\logs\main.log

# Linux
tail -f ~/.config/interview-prep-platform/logs/main.log
```

**Common Causes:**

1. **Database initialization failed**
   ```bash
   # Manually initialize database
   npm run db:setup
   ```

2. **Electron version mismatch**
   ```bash
   # Rebuild native modules
   npx @electron/rebuild
   ```

3. **Missing environment variables**
   - Check `.env` file exists
   - Verify LLM configuration (at least one provider)

---

### Blank white screen on startup

**Symptoms:** App window opens but shows nothing.

**Solutions:**

1. **Check dev tools console (Ctrl+Shift+I / Cmd+Option+I)**
   - Look for React errors
   - Check for failed HTTP requests

2. **Verify React build:**
   ```bash
   npm run build:react
   ls -la dist/  # Should contain index.html and assets/
   ```

3. **Check window.loadURL:**
   ```typescript
   // In production, should load from file://
   mainWindow.loadURL(`file://${path.join(__dirname, '../dist/index.html')}`);
   ```

4. **Clear application data:**
   ```bash
   # macOS
   rm -rf ~/Library/Application\ Support/interview-prep-platform/

   # Windows
   rd /s "%APPDATA%\interview-prep-platform"

   # Linux
   rm -rf ~/.config/interview-prep-platform/
   ```

---

### "Electron API not available" error

**Symptom:**
```
Error: Electron API not available
```

**Cause:** Preload script not loaded or context isolation issue.

**Solution:**

1. **Verify preload script path in main.ts:**
   ```typescript
   webPreferences: {
     preload: path.join(__dirname, 'preload.js'),  // Correct path?
     contextIsolation: true,
     nodeIntegration: false,
   }
   ```

2. **Check preload script compiled:**
   ```bash
   ls -la dist/electron/preload.js
   ```

3. **Rebuild electron:**
   ```bash
   npm run build:electron
   ```

## Database Issues

### "Database not found" error

**Symptom:**
```
Error: SQLITE_CANTOPEN: unable to open database file
```

**Solution:**
```bash
# Initialize database
npm run db:setup

# Or manually:
npm run db:init
python3 scripts/import_all_questions.py
```

**Verify database exists:**
```bash
# macOS
ls -la ~/Library/Application\ Support/interview-prep-platform/interview-prep.db

# Windows
dir "%APPDATA%\interview-prep-platform\interview-prep.db"

# Linux
ls -la ~/.config/interview-prep-platform/interview-prep.db
```

---

### "SQLITE_CORRUPT" database error

**Symptom:**
```
Error: SQLITE_CORRUPT: database disk image is malformed
```

**Cause:** Database file corrupted (power loss, disk error, etc.).

**Solution:**

1. **Backup corrupted database:**
   ```bash
   cp interview-prep.db interview-prep.db.corrupted
   ```

2. **Try recovery:**
   ```bash
   # Dump database
   sqlite3 interview-prep.db ".dump" > backup.sql

   # Create new database
   rm interview-prep.db
   sqlite3 interview-prep.db < backup.sql
   ```

3. **If recovery fails, reinitialize:**
   ```bash
   rm interview-prep.db
   npm run db:setup
   ```

   **Warning:** This deletes all user data!

---

### "Database is locked" error

**Symptom:**
```
Error: SQLITE_BUSY: database is locked
```

**Cause:** Multiple processes accessing database or WAL mode issue.

**Solution:**

1. **Close all instances of the app**

2. **Remove lock files:**
   ```bash
   rm interview-prep.db-shm interview-prep.db-wal
   ```

3. **Restart the app**

## Code Execution Issues

### "Code execution timeout" error

**Symptom:**
```
Error: Code execution timed out after 10000ms
```

**Causes:**
- Infinite loop in user code
- Very slow algorithm
- Python service not responding

**Solutions:**

1. **Check for infinite loops in code**

2. **Increase timeout (if needed):**
   ```bash
   # In .env
   MAX_EXECUTION_TIME=20000  # 20 seconds
   ```

3. **Verify Python service:**
   ```bash
   cd python-service
   python3 executor.py
   # Should start without errors
   ```

---

### "ModuleNotFoundError" in Python execution

**Symptom:**
```
ModuleNotFoundError: No module named 'numpy'
```

**Solution:**
```bash
cd python-service
pip3 install -r requirements.txt

# Verify installation
python3 -c "import numpy; print('OK')"
```

---

### Code execution always fails

**Check execution service:**
```bash
# Test Python executor directly
cd python-service
echo '{"code": "print(1+1)", "language": "python", "test_cases": []}' | python3 executor.py
```

**Verify temp directory access:**
```bash
# Should be writable
ls -la /tmp/interview-prep-exec
chmod 755 /tmp/interview-prep-exec  # If needed
```

## LLM/AI Feedback Issues

### "LLM service not initialized" error

**Symptom:**
```
LLM service is not initialized
```

**Cause:** No LLM provider configured.

**Solution:**

1. **Configure LLM provider in `.env`:**

   **Option 1: Local LLM**
   ```bash
   LLM_BASE_URL=http://localhost:8000
   LLM_MODEL=gpt-oss-20b
   ```

   **Option 2: Claude API**
   ```bash
   CLAUDE_API_KEY=sk-ant-api03-your-key-here
   ```

   **Option 3: OpenAI API**
   ```bash
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4o
   ```

2. **Restart the application**

**Note:** Feedback will gracefully degrade with helpful instructions if LLM is unavailable.

---

### "Failed to generate feedback" with network error

**Symptom:**
```
Failed to generate feedback: fetch failed
```

**Causes:**
- Local LLM not running
- Network connectivity issue
- Wrong LLM_BASE_URL

**Solutions:**

1. **Verify local LLM is running:**
   ```bash
   curl http://localhost:8000/v1/models
   # Should return JSON with model list
   ```

2. **Check LLM_BASE_URL:**
   ```bash
   # In .env, ensure correct URL
   LLM_BASE_URL=http://localhost:8000  # Not https, not missing port
   ```

3. **Test network connectivity:**
   ```bash
   ping localhost
   curl -v http://localhost:8000
   ```

4. **Check firewall settings:**
   - Ensure port 8000 (or your LLM port) is not blocked

---

### Feedback generation very slow (>60s)

**Causes:**
- LLM model too large for hardware
- High API latency
- Network issues

**Solutions:**

1. **Use smaller/faster model:**
   ```bash
   # In .env
   LLM_MODEL=gpt-oss-7b  # Instead of gpt-oss-20b
   ```

2. **Increase timeout (if needed):**
   ```typescript
   // In LLM service
   retryWithBackoff(fn, {
     maxRetries: 3,
     baseDelay: 2000,
     maxDelay: 30000,  // Increase from 15000
   });
   ```

3. **Check LLM service logs:**
   ```bash
   # Look for slow queries
   tail -f /path/to/llm/logs
   ```

## Performance Issues

### High memory usage (>1GB)

**Expected Memory Usage:** 200-500MB

**Causes:**
- Memory leak in React components
- Too many Monaco Editor instances
- Large diagram with many nodes

**Solutions:**

1. **Check React DevTools Profiler:**
   - Look for components that never unmount
   - Check for growing component tree

2. **Limit Monaco Editor instances:**
   ```typescript
   // Dispose editor when unmounting
   useEffect(() => {
     return () => {
       editor?.dispose();
     };
   }, []);
   ```

3. **Optimize React Flow diagrams:**
   ```typescript
   // Limit number of nodes
   if (nodes.length > 100) {
     console.warn('Too many nodes');
   }
   ```

4. **Restart the app periodically**

---

### Slow UI rendering

**Symptoms:** Laggy typing, slow scrolling, delayed button clicks.

**Solutions:**

1. **Check CPU usage:**
   - If high, look for infinite re-renders
   - Use React DevTools Profiler

2. **Optimize React components:**
   ```typescript
   // Memoize expensive computations
   const result = useMemo(() => expensiveComputation(), [deps]);

   // Memoize components
   export default React.memo(MyComponent);
   ```

3. **Reduce Monaco Editor options:**
   ```typescript
   <MonacoEditor
     options={{
       minimap: { enabled: false },  // Disable minimap
       suggestOnTriggerCharacters: false,  // Reduce suggestions
     }}
   />
   ```

4. **Check for too many rerenders:**
   ```typescript
   // Add in component
   console.log('Render count:', ++renderCount);
   ```

---

### Database queries slow

**Symptoms:** Slow question loading, slow submission history.

**Solutions:**

1. **Check database size:**
   ```bash
   ls -lh interview-prep.db
   # Should be <10MB
   ```

2. **Vacuum database:**
   ```bash
   sqlite3 interview-prep.db "VACUUM;"
   ```

3. **Add indexes (if missing):**
   ```sql
   CREATE INDEX IF NOT EXISTS idx_submissions_user ON code_submissions(user_id);
   CREATE INDEX IF NOT EXISTS idx_progress_user ON user_progress(user_id);
   ```

## Platform-Specific Issues

### macOS: "App can't be opened because it is from an unidentified developer"

**Cause:** App not signed or notarized.

**User Workaround:**
1. Right-click app → Open
2. Click "Open" in dialog
3. Or: `sudo xattr -rd com.apple.quarantine /path/to/app`

**Developer Solution:** Sign and notarize the app (see [CODE_SIGNING.md](./CODE_SIGNING.md))

---

### macOS: "App is damaged and can't be opened"

**Cause:** Gatekeeper quarantine or missing notarization.

**Solution:**
```bash
# Remove quarantine attribute
sudo xattr -cr "/Applications/Interview Prep Platform.app"
```

**For Developers:** Properly notarize the app before distribution.

---

### Windows: "Windows protected your PC" warning

**Cause:** App not signed or insufficient SmartScreen reputation.

**User Workaround:**
1. Click "More info"
2. Click "Run anyway"

**Developer Solution:** Sign with EV certificate for instant reputation (see [CODE_SIGNING.md](./CODE_SIGNING.md))

---

### Linux: Missing shared libraries

**Symptom:**
```
error while loading shared libraries: libXXX.so.X: cannot open shared object file
```

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install -y libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 libatspi2.0-0 libsecret-1-0

# Fedora/RHEL
sudo dnf install -y gtk3 libnotify nss libXScrnSaver libXtst at-spi2-core libsecret

# Arch
sudo pacman -S gtk3 libnotify nss libxss libxtst at-spi2-core libsecret
```

---

### Linux: AppImage won't run

**Symptom:**
```
dlopen(): error loading libfuse.so.2
```

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install libfuse2

# Fedora
sudo dnf install fuse-libs

# Or extract and run directly
./Interview\ Prep\ Platform.AppImage --appimage-extract
./squashfs-root/AppRun
```

## Getting Help

### Before Asking for Help

1. **Check logs:**
   ```bash
   # Electron main process logs
   tail -50 ~/Library/Logs/interview-prep-platform/main.log  # macOS
   ```

2. **Reproduce the issue:**
   - Note exact steps to reproduce
   - Check if it happens consistently
   - Try on clean user account / VM

3. **Gather system info:**
   - OS version
   - Node.js version: `node --version`
   - npm version: `npm --version`
   - Electron version (from package.json)

### Where to Get Help

1. **GitHub Issues**
   - Search existing issues first
   - Provide full error messages
   - Include steps to reproduce
   - Attach logs if relevant

2. **Documentation**
   - [README.md](../README.md) - Quick start
   - [CLAUDE.md](../CLAUDE.md) - Development guide
   - [DEPLOYMENT.md](./DEPLOYMENT.md) - Deployment guide
   - [IPC_API.md](./IPC_API.md) - API reference

3. **Community**
   - Discord server (if available)
   - Stack Overflow (tag: electron, react)

### Creating a Good Bug Report

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots/Logs**
Attach relevant screenshots and logs.

**Environment:**
- OS: [e.g., macOS 13.2, Windows 11, Ubuntu 22.04]
- App Version: [e.g., 1.0.0]
- Node.js: [e.g., 22.12.0]
- Installation method: [e.g., built from source, downloaded release]

**Additional context**
Any other relevant information.
```

## Quick Diagnostics

Run this diagnostic script to check common issues:

```bash
#!/bin/bash
echo "=== Interview Prep Platform Diagnostics ==="
echo ""
echo "Node.js version:"
node --version
echo ""
echo "npm version:"
npm --version
echo ""
echo "Electron version:"
npx electron --version 2>/dev/null || echo "Electron not found"
echo ""
echo "Database exists:"
if [ -f ~/.config/interview-prep-platform/interview-prep.db ]; then
  echo "Yes"
  echo "Database size: $(du -h ~/.config/interview-prep-platform/interview-prep.db | cut -f1)"
else
  echo "No - run: npm run db:setup"
fi
echo ""
echo "Python version:"
python3 --version
echo ""
echo "Python dependencies:"
cd python-service && pip3 list | grep -E "(numpy|pandas)" || echo "Not installed"
cd ..
echo ""
echo "LLM configuration:"
if [ -f .env ]; then
  echo ".env exists"
  grep -E "^(LLM_|CLAUDE_|OPENAI_)" .env | sed 's/=.*/=***/'
else
  echo ".env not found"
fi
echo ""
echo "=== End Diagnostics ==="
```

Save as `diagnose.sh`, make executable, and run:
```bash
chmod +x diagnose.sh
./diagnose.sh
```

## Common Error Messages Reference

| Error | Likely Cause | Solution Section |
|-------|--------------|------------------|
| Module version mismatch | Native modules not rebuilt | [Installation Issues](#npm-install-fails-with-module-version-mismatch) |
| Port 5173 already in use | Dev server still running | [Dev Issues](#npm-run-dev-fails---port-5173-already-in-use) |
| Database not found | DB not initialized | [Database Issues](#database-not-found-error) |
| SQLITE_CORRUPT | Corrupted database | [Database Issues](#sqlite_corrupt-database-error) |
| Code execution timeout | Infinite loop or slow code | [Code Execution](#code-execution-timeout-error) |
| LLM service not initialized | No LLM provider configured | [LLM Issues](#llm-service-not-initialized-error) |
| Failed to generate feedback | LLM service unavailable | [LLM Issues](#failed-to-generate-feedback-with-network-error) |
| Electron API not available | Preload script issue | [Runtime Issues](#electron-api-not-available-error) |

---

**Still having issues?** Open an issue on GitHub with:
- Full error message
- Steps to reproduce
- System information
- Relevant logs

We're here to help! 🚀
