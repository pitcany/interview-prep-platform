#!/bin/bash
# Quick script to verify Ollama is configured correctly

echo "=== Ollama Configuration Checker ==="
echo ""

# Check if Ollama is running
echo "1. Checking if Ollama is running..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "   ✓ Ollama is running on port 11434"
else
    echo "   ✗ Ollama is NOT running or not on port 11434"
    echo "   Run: ollama serve"
    exit 1
fi

# List available models
echo ""
echo "2. Available models:"
curl -s http://localhost:11434/api/tags | grep -o '"name":"[^"]*"' | cut -d'"' -f4

# Test OpenAI-compatible endpoint
echo ""
echo "3. Testing OpenAI-compatible API endpoint..."
if curl -s http://localhost:11434/v1/models > /dev/null 2>&1; then
    echo "   ✓ OpenAI-compatible endpoint is accessible"
else
    echo "   ✗ OpenAI-compatible endpoint failed"
fi

echo ""
echo "=== Configuration Summary ==="
echo "Add to your .env file:"
echo "LLM_BASE_URL=http://localhost:11434/v1"
echo "LLM_MODEL=<your-model-name-from-above>"
