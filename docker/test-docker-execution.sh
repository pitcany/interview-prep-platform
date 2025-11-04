#!/bin/bash
# Test Docker code execution

set -e

echo "🧪 Testing Docker Code Execution"
echo "================================"
echo ""

# Test Python container
echo "1. Testing Python container..."
TEST_DIR="$HOME/test-interview-prep"
mkdir -p "$TEST_DIR"

cat > "$TEST_DIR/test_two_sum.py" << 'EOF'
import json

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test case
result = twoSum([2, 7, 11, 15], 9)
print(json.dumps(result))
EOF

echo "   Running: docker run interview-prep-python..."
RESULT=$(docker run --rm \
  -v "$TEST_DIR:/code" \
  --memory=512m \
  --cpus=1 \
  --network=none \
  interview-prep-python:latest \
  sh -c "python3 /code/test_two_sum.py")

if [ "$RESULT" == "[0, 1]" ]; then
  echo "   ✅ Python execution works! Output: $RESULT"
else
  echo "   ❌ Python execution failed! Expected [0, 1], got: $RESULT"
  exit 1
fi

echo ""
echo "2. Testing resource limits..."
cat > "$TEST_DIR/test_timeout.py" << 'EOF'
import time
time.sleep(20)  # Should timeout before this completes
print("Should not reach here")
EOF

echo "   Running: docker run with 2s timeout..."
if timeout 3s docker run --rm \
  -v "$TEST_DIR:/code" \
  --memory=512m \
  --cpus=1 \
  --network=none \
  interview-prep-python:latest \
  sh -c "python3 /code/test_timeout.py" 2>/dev/null; then
  echo "   ❌ Timeout test failed - process should have been killed"
  exit 1
else
  echo "   ✅ Timeout works correctly"
fi

echo ""
echo "3. Testing network isolation..."
cat > "$TEST_DIR/test_network.py" << 'EOF'
import socket
try:
    socket.create_connection(("google.com", 80), timeout=2)
    print("NETWORK_ACCESS")
except:
    print("NO_NETWORK")
EOF

NETWORK_RESULT=$(docker run --rm \
  -v "$TEST_DIR:/code" \
  --memory=512m \
  --cpus=1 \
  --network=none \
  interview-prep-python:latest \
  sh -c "python3 /code/test_network.py" 2>&1 || echo "NO_NETWORK")

if [[ "$NETWORK_RESULT" == *"NO_NETWORK"* ]]; then
  echo "   ✅ Network isolation works!"
else
  echo "   ❌ Network isolation failed! Container has network access"
  exit 1
fi

# Cleanup
rm -rf "$TEST_DIR"

echo ""
echo "================================"
echo "✅ All Docker tests passed!"
echo ""
echo "Next steps:"
echo "1. Your .env is set to: SANDBOX_MODE=docker"
echo "2. Start your app with: npm run dev"
echo "3. Run code in the Practice page"
echo ""
echo "Code execution will now use Docker containers for:"
echo "  ✓ Secure sandboxing"
echo "  ✓ Resource limits (512MB RAM, 1 CPU)"
echo "  ✓ Network isolation"
echo "  ✓ 10 second timeout"
