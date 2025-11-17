#!/bin/bash
# Build Docker images for code execution sandboxes
#
# This script builds all Docker images needed for code execution in different languages.
# Images are used to safely execute user-submitted code in isolated containers.

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOCKER_DIR="$PROJECT_ROOT/docker"

echo "================================================="
echo "Building Docker Images for Code Execution"
echo "================================================="
echo

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed or not in PATH"
    echo "   Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Docker daemon is running
if ! docker ps &> /dev/null; then
    echo "❌ Error: Docker daemon is not running"
    echo "   Please start Docker Desktop and try again"
    exit 1
fi

echo "✓ Docker is available and running"
echo

# Function to build a Docker image
build_image() {
    local name=$1
    local dir=$2
    local tag=$3

    echo "Building $name image..."
    echo "  Directory: $dir"
    echo "  Tag: $tag"

    if [ ! -d "$dir" ]; then
        echo "  ❌ Error: Directory not found: $dir"
        return 1
    fi

    if [ ! -f "$dir/Dockerfile" ]; then
        echo "  ❌ Error: Dockerfile not found: $dir/Dockerfile"
        return 1
    fi

    # Build the image
    if docker build -t "$tag" "$dir"; then
        echo "  ✓ Successfully built $tag"
        echo
        return 0
    else
        echo "  ❌ Failed to build $tag"
        echo
        return 1
    fi
}

# Build Python image
build_image "Python" "$DOCKER_DIR/python" "interview-prep-python"
PYTHON_STATUS=$?

# Build Java image
build_image "Java" "$DOCKER_DIR/java" "interview-prep-java"
JAVA_STATUS=$?

# Build C++ image
build_image "C++" "$DOCKER_DIR/cpp" "interview-prep-cpp"
CPP_STATUS=$?

# Summary
echo "================================================="
echo "Build Summary"
echo "================================================="
echo

if [ $PYTHON_STATUS -eq 0 ]; then
    echo "✓ Python image: interview-prep-python"
else
    echo "❌ Python image: FAILED"
fi

if [ $JAVA_STATUS -eq 0 ]; then
    echo "✓ Java image: interview-prep-java"
else
    echo "❌ Java image: FAILED"
fi

if [ $CPP_STATUS -eq 0 ]; then
    echo "✓ C++ image: interview-prep-cpp"
else
    echo "❌ C++ image: FAILED"
fi

echo
echo "================================================="

# Exit with error if any build failed
if [ $PYTHON_STATUS -ne 0 ] || [ $JAVA_STATUS -ne 0 ] || [ $CPP_STATUS -ne 0 ]; then
    echo "❌ Some builds failed. Please check the errors above."
    exit 1
else
    echo "✓ All images built successfully!"
    echo
    echo "You can now run code in Python, Java, and C++."
    echo
    echo "To verify, run:"
    echo "  docker images | grep interview-prep"
    exit 0
fi
