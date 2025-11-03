#!/bin/bash
# Check common LLM server ports

echo "Checking for local LLM servers..."
echo ""

ports=(8000 5000 8080 11434 5001)

for port in "${ports[@]}"; do
    echo -n "Checking http://localhost:$port ... "

    # Check if port is listening
    if nc -z localhost $port 2>/dev/null; then
        echo "✓ Port is open"

        # Try to get server info
        response=$(curl -s http://localhost:$port/v1/models 2>/dev/null)
        if [ $? -eq 0 ] && [ -n "$response" ]; then
            echo "  → OpenAI-compatible API detected: http://localhost:$port"
            echo "  → Models response: $response" | head -c 200
            echo ""
        else
            # Try health endpoint
            health=$(curl -s http://localhost:$port/health 2>/dev/null)
            if [ $? -eq 0 ]; then
                echo "  → Server detected but not OpenAI-compatible format"
            fi
        fi
    else
        echo "✗ Port is closed"
    fi
done

echo ""
echo "If you found an OpenAI-compatible API, use that URL in your .env file"
echo "Example: LLM_BASE_URL=http://localhost:8000"
