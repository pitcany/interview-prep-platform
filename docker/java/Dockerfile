# Dockerfile for Java code execution sandbox
FROM openjdk:17-slim

# Install minimal dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    mkdir -p /code && \
    chown -R coderunner:coderunner /code

# Install Gson library for JSON parsing
RUN mkdir -p /usr/share/java && \
    cd /usr/share/java

USER coderunner
WORKDIR /code

# Default command
CMD ["java"]
