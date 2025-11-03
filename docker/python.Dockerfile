FROM python:3.11-slim

# Install minimal dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 sandbox && \
    mkdir -p /code && \
    chown sandbox:sandbox /code

# Set working directory
WORKDIR /code

# Switch to non-root user
USER sandbox

# Set Python to unbuffered mode
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python"]
