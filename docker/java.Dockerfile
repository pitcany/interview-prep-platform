FROM openjdk:17-slim

# Install Gson for JSON parsing
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download Gson JAR
RUN mkdir -p /usr/share/java && \
    wget -O /usr/share/java/gson.jar https://repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar

# Create non-root user
RUN useradd -m -u 1000 sandbox && \
    mkdir -p /code && \
    chown sandbox:sandbox /code

# Set working directory
WORKDIR /code

# Add Gson to classpath
ENV CLASSPATH=/usr/share/java/gson.jar:.

# Switch to non-root user
USER sandbox

# Default command
CMD ["java"]
