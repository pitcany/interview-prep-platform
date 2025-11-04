# Dockerfile for C++ code execution sandbox
FROM gcc:12-bookworm

# Install minimal dependencies including nlohmann-json
RUN apt-get update && apt-get install -y --no-install-recommends \
    nlohmann-json3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    mkdir -p /code && \
    chown -R coderunner:coderunner /code

USER coderunner
WORKDIR /code

# Default command
CMD ["g++"]
