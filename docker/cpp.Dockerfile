FROM gcc:13-bookworm

# Install JSON library (nlohmann/json)
RUN apt-get update && apt-get install -y --no-install-recommends \
    nlohmann-json3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 sandbox && \
    mkdir -p /code && \
    chown sandbox:sandbox /code

# Set working directory
WORKDIR /code

# Switch to non-root user
USER sandbox

# Default command
CMD ["g++"]
