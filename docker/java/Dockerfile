# Dockerfile for Java code execution sandbox
FROM eclipse-temurin:17-jre-jammy

# Install minimal dependencies (none needed - base image has everything)
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -u 1000 coderunner && \
    mkdir -p /code && \
    chown -R coderunner:coderunner /code

# Install Gson library for JSON parsing
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && mkdir -p /usr/share/java \
    && cd /usr/share/java \
    && wget -q https://repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar \
    && apt-get remove -y wget \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Set CLASSPATH to include Gson
ENV CLASSPATH=/usr/share/java/gson-2.10.1.jar:.

USER coderunner
WORKDIR /code

# Default command
CMD ["java"]
