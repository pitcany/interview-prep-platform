#!/bin/bash
# Build Docker images for code execution sandboxes

set -e

echo "🐳 Building Docker images for code execution..."

# Build Python image
echo ""
echo "📦 Building Python execution container..."
docker build -t interview-prep-python:latest python/

# Build Java image (optional)
echo ""
echo "📦 Building Java execution container..."
docker build -t interview-prep-java:latest java/

# Build C++ image (optional)
echo ""
echo "📦 Building C++ execution container..."
docker build -t interview-prep-cpp:latest cpp/

echo ""
echo "✅ All Docker images built successfully!"
echo ""
echo "Images created:"
docker images | grep interview-prep

echo ""
echo "🎯 Next step: Update your .env file to use Docker mode:"
echo "   SANDBOX_MODE=docker"
