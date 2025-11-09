# Dockerfile for Java code execution sandbox
FROM eclipse-temurin:17-jre-jammy

# Install minimal dependencies (none needed - base image has everything)
RUN apt-get update && rm -rf /var/lib/apt/lists/*

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
