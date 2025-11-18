# Docker Execution Sandboxes

These Docker containers provide secure, isolated environments for executing user code submissions.

## Security Features

- **Non-root user**: Code runs as `coderunner` user (UID 1000)
- **Network isolation**: Containers run with `--network none` flag
- **Resource limits**: Memory and CPU limits enforced by Docker
- **Filesystem isolation**: Limited to `/code` directory only
- **Ephemeral**: Containers are removed after execution (`--rm` flag)

## Building the Images

Run the build script from this directory:

```bash
chmod +x build-images.sh
./build-images.sh
```

Or build individually:

```bash
# Python only
docker build -t interview-prep-python:latest python/

# All languages
docker build -t interview-prep-python:latest python/
docker build -t interview-prep-java:latest java/
docker build -t interview-prep-cpp:latest cpp/
```

## Configuration

Update your `.env` file to enable Docker execution:

```env
SANDBOX_MODE=docker
MAX_EXECUTION_TIME=10000  # 10 seconds
MAX_MEMORY=512  # 512 MB
```

## Testing

Test the Python container manually:

```bash
# Test basic execution
docker run --rm -v $(pwd)/test:/code interview-prep-python:latest python3 -c "print('Hello from Docker')"

# Test with resource limits
docker run --rm \
  --memory=512m \
  --cpus=1 \
  --network=none \
  -v $(pwd)/test:/code \
  interview-prep-python:latest \
  python3 /code/test.py
```

## Container Specs

### Python Container
- Base: `python:3.11-slim`
- Size: ~180 MB
- Languages: Python 3.11

### Java Container
- Base: `eclipse-temurin:17-jre-jammy`
- Size: ~400 MB
- Languages: Java 17
- Libraries: Gson 2.10.1 for JSON parsing (included in CLASSPATH)

### C++ Container
- Base: `gcc:12-bookworm`
- Size: ~1.2 GB
- Languages: C++17, C++20
- Libraries: nlohmann-json for JSON parsing

## Troubleshooting

### Permission Denied Errors
Ensure the mounted directory is readable:
```bash
chmod -R 755 /tmp/interview-prep-exec
```

### Container Not Found
Rebuild the images:
```bash
./build-images.sh
```

### Docker Daemon Not Running
Start Docker:
```bash
sudo systemctl start docker
```
