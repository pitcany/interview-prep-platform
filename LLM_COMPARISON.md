# LLM Comparison - Quick Reference Card

Choose the right AI feedback solution for your interview prep needs.

## TL;DR - Which Should I Use?

| Your Situation | Recommendation |
|----------------|----------------|
| **Just getting started** | ✅ Ollama (llama3.1:8b) |
| **Want best quality feedback** | ⭐ Ollama (qwen2.5:14b) or GPT-4 |
| **Limited RAM (<12GB)** | 💡 Ollama (llama3.2:3b) |
| **Need absolute fastest response** | 🚀 Cloud API (GPT-3.5/Claude Haiku) |
| **Privacy is critical** | 🔒 Ollama (any model) |
| **On a budget** | 💰 Ollama (free) |

## Side-by-Side Comparison

### Ollama (Local)

**What it is**: Run LLMs locally on your own hardware

**Cost**:
- ✅ **FREE** (no ongoing costs)
- Hardware already owned

**Privacy**:
- ✅ **100% Private** - Code never leaves your machine
- ✅ No data retention by third parties
- ✅ Works completely offline

**Performance**:
- Response time: **5-30 seconds** (depends on model & hardware)
- Small model (3B): ~5-10s
- Medium model (8B): ~10-20s
- Large model (14B): ~20-30s

**Quality**:
- Small models: Good for basic feedback
- Medium models: Great for detailed analysis
- Large models: Excellent, comparable to GPT-3.5

**Setup Difficulty**: ⭐⭐⭐⭐☆ (Easy - 5 minutes)
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b
```

**Pros**:
- ✅ No recurring costs
- ✅ Complete privacy
- ✅ Offline capable
- ✅ No rate limits
- ✅ Swap models anytime

**Cons**:
- ❌ Requires local resources (RAM/storage)
- ❌ Slower than high-end cloud models
- ❌ Quality varies by model choice

**Best For**: Most users who value privacy and want free, unlimited feedback

---

### Cloud APIs (OpenAI, Anthropic, etc.)

**What it is**: Use hosted LLMs via API calls

**Cost**:
- 💰 **Pay per use**
- GPT-3.5: ~$0.002 per request
- GPT-4: ~$0.10 per request
- Claude Sonnet: ~$0.05 per request
- Estimated monthly: $5-50 depending on usage

**Privacy**:
- ⚠️ Code sent to third-party servers
- ⚠️ Subject to provider's data retention policies
- ⚠️ Requires internet connection

**Performance**:
- Response time: **2-8 seconds**
- GPT-3.5 Turbo: ~2-4s
- GPT-4: ~5-8s
- Claude Sonnet: ~3-6s

**Quality**:
- GPT-3.5: Good, fast
- GPT-4: Excellent, industry-leading
- Claude Sonnet: Excellent, strong code analysis
- Claude Opus: Best-in-class

**Setup Difficulty**: ⭐⭐⭐☆☆ (Moderate - need API key)
```bash
# Sign up for API key, add to .env
echo "LLM_BASE_URL=https://api.openai.com" > .env
echo "OPENAI_API_KEY=sk-..." >> .env
```

**Pros**:
- ✅ Fastest response times
- ✅ Highest quality feedback (GPT-4, Claude Opus)
- ✅ No local resources needed
- ✅ Always up-to-date models

**Cons**:
- ❌ Ongoing costs
- ❌ Privacy concerns
- ❌ Requires internet
- ❌ Rate limits on some tiers
- ❌ API keys to manage

**Best For**: Users who need absolute best quality or fastest responses and are okay with costs/privacy trade-offs

---

## Detailed Feature Matrix

| Feature | Ollama (Local) | Cloud APIs |
|---------|----------------|------------|
| **Cost** | Free | $5-50/month |
| **Privacy** | 100% Private | Shared with provider |
| **Offline** | ✅ Yes | ❌ No |
| **Response Time** | 10-30s | 2-8s |
| **Feedback Quality** | Good to Excellent | Excellent to Best |
| **Setup Time** | 5 minutes | 10 minutes |
| **RAM Required** | 8-16GB | None |
| **Storage Required** | 2-10GB | None |
| **Rate Limits** | None | Depends on tier |
| **Model Updates** | Manual (`ollama pull`) | Automatic |
| **Hardware Acceleration** | GPU support | N/A |
| **Multi-model** | ✅ Easy to switch | 💰 Different pricing |

---

## Model-Specific Recommendations

### Ollama Models

| Model | Size | RAM | Speed | Quality | Use Case |
|-------|------|-----|-------|---------|----------|
| **llama3.2:3b** | 2GB | 8GB | ⚡⚡⚡ | ⭐⭐⭐ | Testing, quick feedback |
| **llama3.1:8b** | 4.7GB | 12GB | ⚡⚡ | ⭐⭐⭐⭐ | **Recommended default** |
| **codellama:13b** | 7.4GB | 16GB | ⚡ | ⭐⭐⭐⭐ | Code-focused analysis |
| **qwen2.5:14b** | 9GB | 16GB | ⚡ | ⭐⭐⭐⭐⭐ | Best local quality |
| **deepseek-coder:6.7b** | 3.8GB | 10GB | ⚡⚡ | ⭐⭐⭐⭐ | Good code understanding |

### Cloud Models

| Provider | Model | Cost/Request | Speed | Quality | Use Case |
|----------|-------|--------------|-------|---------|----------|
| **OpenAI** | gpt-3.5-turbo | $0.002 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Fast, affordable |
| **OpenAI** | gpt-4o | $0.10 | ⚡⚡ | ⭐⭐⭐⭐⭐ | Best quality |
| **Anthropic** | claude-3-haiku | $0.01 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Fast, good quality |
| **Anthropic** | claude-3-sonnet | $0.05 | ⚡⚡ | ⭐⭐⭐⭐⭐ | Strong code analysis |
| **Anthropic** | claude-3-opus | $0.15 | ⚡ | ⭐⭐⭐⭐⭐ | Best-in-class |

---

## Real-World Examples

### Example 1: Student on a Budget

**Scenario**: CS student preparing for internship interviews, limited budget

**Recommendation**: **Ollama (llama3.1:8b)**
- **Why**: Free, good quality, perfect for learning
- **Setup**: 5 minutes
- **Cost**: $0/month
- **Trade-off**: Slightly slower than cloud APIs

---

### Example 2: Senior Engineer, Privacy-Conscious

**Scenario**: Experienced engineer practicing system design, concerned about code privacy

**Recommendation**: **Ollama (qwen2.5:14b)**
- **Why**: Best local quality, no privacy concerns
- **Setup**: 5 minutes
- **Cost**: $0/month
- **Trade-off**: Requires 16GB+ RAM, slower responses

---

### Example 3: Time-Constrained Professional

**Scenario**: Working professional with limited practice time, needs fastest feedback

**Recommendation**: **GPT-4 Turbo or Claude Sonnet**
- **Why**: Fastest response times, excellent quality
- **Setup**: 10 minutes (API key signup)
- **Cost**: ~$20-30/month for heavy use
- **Trade-off**: Privacy concerns, ongoing costs

---

### Example 4: Laptop with 8GB RAM

**Scenario**: Older laptop, wants to use local LLM but limited resources

**Recommendation**: **Ollama (llama3.2:3b)**
- **Why**: Small footprint, still useful feedback
- **Setup**: 5 minutes
- **Cost**: $0/month
- **Trade-off**: Lower quality than larger models

---

## Configuration Examples

### Ollama Configuration (.env)

```env
# Fast & Balanced (Recommended)
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b

# Highest Quality Local
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=qwen2.5:14b

# Low Resource
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.2:3b

# Code-Focused
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=codellama:13b
```

### Cloud API Configuration (.env)

```env
# OpenAI GPT-4
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4o
OPENAI_API_KEY=sk-your-key-here

# OpenAI GPT-3.5 (cheaper)
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-3.5-turbo
OPENAI_API_KEY=sk-your-key-here

# Anthropic Claude
LLM_BASE_URL=https://api.anthropic.com/v1
LLM_MODEL=claude-3-sonnet-20240229
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

---

## Switching Between Options

You can easily switch between local and cloud LLMs:

```bash
# Switch to Ollama
ollama serve  # Start if not running
cat > .env << EOF
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b
EOF

# Switch to OpenAI
cat > .env << EOF
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4o
OPENAI_API_KEY=your-key-here
EOF

# Restart the app
npm run dev
```

---

## Cost Estimation Tool

### Ollama (Local)
- **Upfront**: $0 (uses existing hardware)
- **Per month**: $0
- **Per 100 feedback requests**: $0
- **Per year**: $0

### Cloud APIs (Estimated)

**Light usage** (5 feedback requests/day, ~150/month):
- GPT-3.5: $0.30/month = $3.60/year
- GPT-4: $15/month = $180/year
- Claude Sonnet: $7.50/month = $90/year

**Medium usage** (20 feedback requests/day, ~600/month):
- GPT-3.5: $1.20/month = $14.40/year
- GPT-4: $60/month = $720/year
- Claude Sonnet: $30/month = $360/year

**Heavy usage** (50 feedback requests/day, ~1500/month):
- GPT-3.5: $3/month = $36/year
- GPT-4: $150/month = $1,800/year
- Claude Sonnet: $75/month = $900/year

---

## Decision Flowchart

```
Start: Do you need AI feedback?
  │
  ├─[No]──> Skip this setup
  │
  └─[Yes]──> Is privacy critical?
      │
      ├─[Yes]──> Use Ollama (100% local)
      │            │
      │            └─> RAM < 12GB? → llama3.2:3b
      │                RAM 12-16GB? → llama3.1:8b ⭐
      │                RAM 16GB+? → qwen2.5:14b
      │
      └─[No]──> Is cost a concern?
          │
          ├─[Yes]──> Use Ollama (free)
          │            └─> Recommended: llama3.1:8b
          │
          └─[No]──> Want absolute best quality?
              │
              ├─[Yes]──> Use GPT-4 or Claude Opus
              │
              └─[No]──> Use GPT-3.5 or Claude Haiku
```

---

## FAQ

**Q: Can I use both Ollama and Cloud APIs?**
A: Yes! Just change your `.env` file and restart the app. You can switch anytime.

**Q: Is Ollama quality good enough for interview prep?**
A: Absolutely. Medium models (llama3.1:8b, codellama:13b) provide excellent feedback comparable to GPT-3.5.

**Q: How much does cloud API usage actually cost in practice?**
A: For typical interview prep (5-10 requests/day), expect $5-20/month with GPT-4, or $1-5/month with GPT-3.5.

**Q: Can I try both and decide?**
A: Yes! Start with Ollama (free), then try a cloud API if you want to compare quality.

**Q: Which is faster?**
A: Cloud APIs (2-8s) are generally faster than Ollama (10-30s), but Ollama has no network latency.

**Q: Do I need a GPU for Ollama?**
A: No, but GPU acceleration helps. Ollama works fine on CPU-only systems.

---

## Getting Started Links

- **Ollama Setup**: [OLLAMA_SETUP.md](OLLAMA_SETUP.md)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Main README**: [README.md](README.md)

---

**Recommendation**: Start with **Ollama (llama3.1:8b)** for the best balance of quality, privacy, and cost. You can always switch to cloud APIs later if needed.
