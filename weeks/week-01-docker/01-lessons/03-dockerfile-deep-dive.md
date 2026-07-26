# Lesson 3: Dockerfile Deep Dive

**Reading time:** 25 minutes  
**After this lesson you'll understand:** Every common Dockerfile instruction and how to write production-quality Dockerfiles.

---

## Anatomy of a Dockerfile

A Dockerfile is a step-by-step recipe. Docker executes each line top to bottom, creating a layer per instruction.

```dockerfile
# Comment — ignored by Docker

FROM python:3.11-slim          # Base image (required first instruction)
WORKDIR /app                   # Set working directory inside container
COPY requirements.txt .        # Copy files from host to container
RUN pip install -r requirements.txt   # Execute command at BUILD time
COPY . .                       # Copy application code
EXPOSE 8000                    # Document which port app listens on (metadata only)
ENV APP_ENV=production         # Set environment variable
USER appuser                   # Run as non-root user
CMD ["python", "app.py"]       # Default command when container STARTS
```

---

## Instruction Reference

### `FROM` — Base image

```dockerfile
FROM python:3.11-slim
# or
FROM golang:1.22-alpine AS builder   # Named stage for multi-stage builds
```

- Must be first instruction (except ARG before FROM)
- `slim` / `alpine` = smaller images (prefer for production)

### `WORKDIR` — Set directory

```dockerfile
WORKDIR /app
# All following RUN, COPY, CMD run relative to /app
```

Always use WORKDIR instead of `RUN cd /app && ...`

### `COPY` vs `ADD`

```dockerfile
COPY requirements.txt .           # Preferred — copy files/directories
COPY src/ ./src/

ADD archive.tar.gz /app/          # Can extract tar, fetch URLs — avoid unless needed
```

**Rule:** Use `COPY` unless you specifically need ADD's extra features.

### `RUN` — Execute at build time

```dockerfile
# Shell form (runs in /bin/sh -c)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Exec form
RUN ["pip", "install", "-r", "requirements.txt"]
```

**Best practice:** Combine commands with `&&` in one RUN to reduce layers and clean up in same layer:

```dockerfile
# Bad — 2 layers, apt cache stays in layer 1
RUN apt-get update
RUN apt-get install -y curl

# Good — 1 layer, cache cleaned
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

### `EXPOSE` — Document port

```dockerfile
EXPOSE 8000
```

Does **NOT** publish the port to your host. It documents intent. Actual publishing: `docker run -p 8000:8000` or Compose `ports:`.

### `ENV` — Environment variables

```dockerfile
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgresql://localhost/mydb
```

Available at build time (RUN) and runtime (CMD).

### `ARG` — Build-time variables

```dockerfile
ARG VERSION=1.0.0
RUN echo "Building version $VERSION"
```

Not available in running container unless re-declared as ENV. Used for build flexibility:

```bash
docker build --build-arg VERSION=2.0.0 -t my-app .
```

### `USER` — Run as non-root

```dockerfile
RUN adduser --disabled-password --gecos '' appuser
USER appuser
```

**Security:** Never run production containers as root. Interviewers ask this.

### `CMD` vs `ENTRYPOINT`

| | CMD | ENTRYPOINT |
|---|-----|------------|
| **Purpose** | Default command, overridable | Main executable, args append |
| **Override** | `docker run img other-cmd` replaces entirely | `docker run img --flag` appends to entrypoint |

```dockerfile
# CMD only — fully replaceable
CMD ["python", "app.py"]

# ENTRYPOINT + CMD — CMD becomes default args
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myapp server.py  → runs python server.py
```

**Pattern for production:**

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

### `HEALTHCHECK` — Container health

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

Orchestrators (ECS, Kubernetes) use this to restart unhealthy containers.

---

## Complete Example: Python Flask API

```dockerfile
FROM python:3.11-slim

# Prevent Python from writing .pyc and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "app.py"]
```

Build and run:

```bash
docker build -t flask-api:1.0 .
docker run -d -p 5000:5000 --name flask-api flask-api:1.0
curl http://localhost:5000/health
```

---

## .dockerignore — Critical for Speed and Security

Same concept as `.gitignore`. Excludes files from build context.

```
.git
.gitignore
__pycache__
*.pyc
.env
.venv
node_modules
README.md
Dockerfile
docker-compose*.yml
*.md
tests/
```

**Why it matters:**
- Faster builds (smaller context sent to Docker daemon)
- Secrets in `.env` won't accidentally get COPY'd into image
- Smaller images

---

## Common Mistakes (Interview Favorites)

| Mistake | Fix |
|---------|-----|
| Running as root | Add USER directive |
| Copying secrets into image | Use .dockerignore + runtime env/secrets |
| `COPY . .` before dependencies | Copy requirements first |
| Using `latest` base tag | Pin version: `python:3.11-slim` |
| Huge images | Multi-stage builds, alpine/slim bases |
| No HEALTHCHECK | Add health endpoint + HEALTHCHECK |
| One process per container violated | Don't run nginx + app in one container without supervisor |

---

## One Container = One Process (Ideal)

Docker philosophy: one main process per container.

```
✅ Good:  Container A = API, Container B = Postgres, Container C = Redis
❌ Bad:   One container running API + Postgres + Redis via shell script
```

Use **Docker Compose** to run multiple containers as one logical app (Lesson 4).

---

## Check Your Understanding

1. What's the difference between RUN and CMD?
2. Why use `.dockerignore`?
3. What's the difference between ARG and ENV?
4. Why copy `requirements.txt` before the rest of the code?

<details>
<summary>Answers</summary>

1. RUN executes at **build time** (creates layers). CMD is the **default command at runtime** when container starts.
2. Excludes files from build context — faster builds, prevents secrets/large dirs in image.
3. ARG is build-time only (can pass via `--build-arg`). ENV persists into running container.
4. Docker caches layers — dependencies change less often than code, so pip install stays cached.

</details>

---

## Next Lesson

👉 **[Lesson 4: Docker Compose](04-docker-compose.md)**

Then run **[Hands-on Example 2: Python API](../02-hands-on/example-02-python-api/)**
