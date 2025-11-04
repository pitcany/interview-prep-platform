# Ollama Setup for AI Feedback

Complete guide to setting up Ollama as your local LLM for AI-powered interview feedback.

## What is Ollama?

Ollama is a lightweight tool that lets you run large language models (LLMs) locally on your machine. It provides an OpenAI-compatible API, making it perfect for the Interview Prep Platform's AI feedback system.

**Benefits:**
- ✅ **100% Private** - Your code never leaves your machine
- ✅ **No API costs** - Free to use once installed
- ✅ **Offline capable** - Works without internet connection
- ✅ **Fast responses** - Low latency compared to cloud APIs
- ✅ **Easy setup** - Simple installation and model management

## Prerequisites

### System Requirements
- **RAM**: Minimum 8GB (16GB+ recommended)
- **Storage**: 4-50GB depending on model size
- **OS**: macOS, Linux, or Windows (WSL2)
- **Optional**: GPU for faster inference (NVIDIA/AMD/Apple Silicon)

### Model Recommendations

| Model | Size | RAM Required | Speed | Quality | Best For |
|-------|------|--------------|-------|---------|----------|
| `llama3.2:3b` | 2GB | 8GB | ⚡⚡⚡ Fast | Good | Quick feedback, testing |
| `llama3.1:8b` | 4.7GB | 12GB | ⚡⚡ Medium | Great | Balanced quality/speed |
| `qwen2.5:14b` | 9GB | 16GB | ⚡ Slow | Excellent | Best feedback quality |
| `codellama:13b` | 7.4GB | 16GB | ⚡ Slow | Excellent | Code-focused feedback |

**Recommendation for most users**: Start with `llama3.1:8b` for the best balance of quality and performance.

## Installation

### Step 1: Install Ollama

**macOS & Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows (WSL2):**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows (Native - Preview):**
Download from [https://ollama.com/download](https://ollama.com/download)

**Verify installation:**
```bash
ollama --version
```

### Step 2: Pull a Model

Choose and download a model (we recommend starting with llama3.1:8b):

```bash
# Recommended: Balanced model (4.7GB)
ollama pull llama3.1:8b

# OR Small/fast model (2GB)
ollama pull llama3.2:3b

# OR Code-focused model (7.4GB)
ollama pull codellama:13b

# OR High-quality model (9GB)
ollama pull qwen2.5:14b
```

**Note**: First pull will take several minutes depending on your internet speed.

### Step 3: Start Ollama Server

Ollama runs as a background service by default. To start it manually:

```bash
ollama serve
```

By default, Ollama listens on `http://localhost:11434`.

**Verify the server is running:**
```bash
curl http://localhost:11434/api/tags
```

You should see a JSON response listing your installed models.

### Step 4: Configure Interview Prep Platform

Create or edit the `.env` file in your project root:

```bash
# Navigate to project directory
cd /path/to/interview-prep-platform

# Create .env file
cat > .env << 'EOF'
# Ollama Configuration
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b

# Code Execution Configuration (optional)
SANDBOX_MODE=local
MAX_EXECUTION_TIME=10000
MAX_MEMORY=512
EOF
```

**Important**: Replace `llama3.1:8b` with whichever model you pulled in Step 2.

### Step 5: Test Your Setup

1. **Start the Interview Prep Platform:**
   ```bash
   npm run dev
   ```

2. **Check the console logs** - you should see:
   ```
   LocalLLM configured: http://localhost:11434 (model: llama3.1:8b)
   ```

3. **Test AI feedback**:
   - Go to Practice mode
   - Solve a LeetCode question
   - Submit your solution
   - Click "Get AI Feedback"
   - Wait 10-30 seconds for feedback to generate

## Troubleshooting

### Ollama Server Not Running

**Symptom**: Error connecting to `http://localhost:11434`

**Solutions**:
```bash
# Check if Ollama is running
ps aux | grep ollama

# Start Ollama manually
ollama serve

# On macOS/Linux, check system service
sudo systemctl status ollama    # Linux
launchctl list | grep ollama    # macOS
```

### Model Not Found Error

**Symptom**: `Error: model 'llama3.1:8b' not found`

**Solutions**:
```bash
# List installed models
ollama list

# Pull the model you configured in .env
ollama pull llama3.1:8b
```

### Slow Feedback Generation

**Symptom**: Feedback takes 60+ seconds to generate

**Solutions**:
1. **Use a smaller model** (llama3.2:3b instead of qwen2.5:14b)
2. **Enable GPU acceleration** (automatic with NVIDIA/AMD/Apple Silicon)
3. **Increase timeout** in electron/services/localLLM.ts (if you're comfortable with code)

### Out of Memory Errors

**Symptom**: Ollama crashes or system becomes unresponsive

**Solutions**:
1. **Switch to smaller model**:
   ```bash
   ollama pull llama3.2:3b
   # Update LLM_MODEL in .env to llama3.2:3b
   ```

2. **Stop other memory-intensive applications**

3. **Set model context size** (reduces memory usage):
   ```bash
   # In a separate terminal
   ollama run llama3.1:8b --ctx-size 2048
   ```

### Bad Quality Feedback

**Symptom**: Feedback is generic, incorrect, or poorly formatted

**Solutions**:
1. **Use a larger model** (qwen2.5:14b or codellama:13b)
2. **Check model temperature** (hardcoded to 0.7 in localLLM.ts - good default)
3. **Verify model pulled correctly**:
   ```bash
   ollama list
   # Re-pull if corrupted
   ollama pull llama3.1:8b
   ```

### Port Conflicts

**Symptom**: `Error: address already in use: 11434`

**Solutions**:
```bash
# Option 1: Find and kill the process using port 11434
lsof -ti:11434 | xargs kill -9

# Option 2: Use a different port
OLLAMA_HOST=0.0.0.0:11435 ollama serve
# Update LLM_BASE_URL in .env to http://localhost:11435
```

## Advanced Configuration

### Custom Port

To run Ollama on a different port:

```bash
# Start Ollama on custom port
OLLAMA_HOST=0.0.0.0:8080 ollama serve
```

Update `.env`:
```env
LLM_BASE_URL=http://localhost:8080
```

### Performance Tuning

**Enable GPU acceleration** (automatic, but verify):
```bash
# Check GPU is detected
ollama run llama3.1:8b --verbose
# Should show GPU info if available
```

**Adjust context window** (trade memory for capability):
```bash
# Smaller context = less memory (2048 tokens)
ollama run llama3.1:8b --ctx-size 2048

# Larger context = more memory (8192 tokens)
ollama run llama3.1:8b --ctx-size 8192
```

### Remote Ollama Server

Running Ollama on a different machine:

1. **On the Ollama server machine**:
   ```bash
   OLLAMA_HOST=0.0.0.0:11434 ollama serve
   ```

2. **Update `.env` on client machine**:
   ```env
   LLM_BASE_URL=http://192.168.1.100:11434
   ```

Replace `192.168.1.100` with your server's IP address.

## Model Management

### List Installed Models
```bash
ollama list
```

### Remove a Model
```bash
ollama rm llama3.1:8b
```

### Update a Model
```bash
ollama pull llama3.1:8b
```

### Check Model Info
```bash
ollama show llama3.1:8b
```

## Comparing Ollama to Other Options

| Feature | Ollama | vLLM | llama.cpp | Cloud APIs |
|---------|--------|------|-----------|------------|
| **Ease of Setup** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Memory Efficiency** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | N/A |
| **API Compatibility** | ✅ OpenAI-compatible | ✅ OpenAI-compatible | ⚠️ Custom | ✅ Native |
| **Privacy** | ✅ 100% Local | ✅ 100% Local | ✅ 100% Local | ❌ Cloud |
| **Cost** | 💰 Free | 💰 Free | 💰 Free | 💰💰💰 Paid |

**Recommendation**: Ollama is the best choice for most users due to its simplicity and OpenAI-compatible API.

## Testing the API Directly

You can test Ollama's API independently of the app:

```bash
# Test with curl
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.1:8b",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful coding assistant."
      },
      {
        "role": "user",
        "content": "Explain what time complexity is in one sentence."
      }
    ]
  }'
```

Expected response: JSON with the model's answer.

## FAQ

### Q: Do I need internet to use Ollama?
**A**: Only for initial installation and model downloads. After that, everything runs offline.

### Q: Can I use multiple models?
**A**: Yes! Pull multiple models with `ollama pull` and switch between them by changing `LLM_MODEL` in `.env`.

### Q: How do I uninstall Ollama?
**A**:
- **macOS/Linux**: `sudo rm -rf /usr/local/bin/ollama ~/.ollama`
- **Windows**: Uninstall via Add/Remove Programs

### Q: Does Ollama work on Apple Silicon (M1/M2/M3)?
**A**: Yes! Ollama has excellent Apple Silicon support with automatic GPU acceleration.

### Q: What if I already have llama.cpp or vLLM running?
**A**: The Interview Prep Platform works with any OpenAI-compatible API. Just point `LLM_BASE_URL` to your existing server.

### Q: Can I use Ollama for multiple applications?
**A**: Absolutely! Ollama can handle multiple concurrent requests from different apps.

## Resources

- **Ollama Website**: [https://ollama.com](https://ollama.com)
- **Ollama GitHub**: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
- **Model Library**: [https://ollama.com/library](https://ollama.com/library)
- **Ollama Discord**: Join for community support

## Next Steps

1. ✅ Ollama installed and model pulled
2. ✅ `.env` configured with your model
3. ✅ Interview Prep Platform running
4. 🎯 Start practicing and get AI feedback!

**Tip**: Try solving a LeetCode problem with an intentional bug, then request feedback. Ollama should identify the issue and suggest improvements!

---

**Need more help?** Check the main project documentation or open an issue on GitHub.
