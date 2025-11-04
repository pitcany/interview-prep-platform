# Dockerfile for Python code execution sandbox
FROM python:3.11-slim

# Install minimal dependencies (none needed - base image has everything)
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    mkdir -p /code && \
    chown -R coderunner:coderunner /code

# Set resource limits
USER coderunner
WORKDIR /code

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Default command (will be overridden)
CMD ["python3"]
