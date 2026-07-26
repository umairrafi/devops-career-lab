# Lesson 2: Images, Containers, and Layers

**Reading time:** 20 minutes  
**After this lesson you'll understand:** How images are built from layers, why caching matters, and how to manage images/containers efficiently.

---

## Images Are Made of Layers

Every Docker image is a **stack of read-only layers**. Each instruction in a Dockerfile typically creates one layer.

```
┌─────────────────────────────────┐
│  Layer 4: COPY app.py /app/     │  ← Your code
├─────────────────────────────────┤
│  Layer 3: RUN pip install ...   │  ← Dependencies
├─────────────────────────────────┤
│  Layer 2: RUN apt-get install   │  ← System packages
├─────────────────────────────────┤
│  Layer 1: FROM python:3.11      │  ← Base image
└─────────────────────────────────┘
```

**Why layers matter:**

1. **Caching** — If layer 3 hasn't changed, Docker reuses cached layer 3 instead of rebuilding. Builds go from minutes to seconds.

2. **Sharing** — Two images with the same base layer share storage. Pull `python:3.11` once, use in 10 projects.

3. **Size** — Each layer adds size. Order instructions wisely (see Lesson 6).

---

## Image Lifecycle

```
Dockerfile  →  docker build  →  Image (local)  →  docker push  →  Registry (ECR/Docker Hub)
                                      │
                                      │ docker run
                                      ▼
                                 Container(s)
```

### Build an image

```bash
docker build -t my-app:1.0 .
#        │      │       │    └── Build context (current directory)
#        │      │       └── Tag/version
#        │      └── Image name
#        └── Build command
```

### Tag and push to registry

```bash
docker tag my-app:1.0 myregistry.com/my-app:1.0
docker push myregistry.com/my-app:1.0
```

### Pull and run elsewhere

```bash
docker pull myregistry.com/my-app:1.0
docker run myregistry.com/my-app:1.0
```

**Interview line:** "Images are immutable artifacts. You don't patch a running container — you build a new image version and redeploy."

---

## Container Lifecycle

```
Created → Running → Paused → Stopped → Removed
              ↑         │
              └─────────┘ (unpause)
```

```bash
# Create and start
docker run -d --name api my-app:1.0

# Pause (freezes process)
docker pause api

# Unpause
docker unpause api

# Stop (SIGTERM, then SIGKILL after timeout)
docker stop api

# Start again (same container, same filesystem changes)
docker start api

# Remove (must be stopped first, or use -f)
docker rm api
```

**Important:** Container filesystem changes are **lost** when you remove the container — unless you use volumes (Lesson 5).

---

## Inspecting Images and Containers

```bash
# Image details — see layers, env, cmd
docker inspect my-app:1.0

# History of layers in an image
docker history my-app:1.0

# Container logs
docker logs api
docker logs -f api    # follow (like tail -f)

# Resource usage
docker stats api

# Process inside container
docker top api

# Open shell inside running container
docker exec -it api /bin/sh
# or for Python images:
docker exec -it api python
```

`docker exec` is your best friend for debugging — you're inside the container as if you SSH'd in.

---

## Image Naming and Tags

Format: `[registry/][username/]repository[:tag]`

| Example | Meaning |
|---------|---------|
| `nginx` | Official nginx, latest tag |
| `nginx:1.25-alpine` | Specific version, Alpine variant |
| `123456789.dkr.ecr.me-south-1.amazonaws.com/my-api:v2.1.0` | AWS ECR (UAE region) |

**Tag best practices:**
- Never use `latest` in production — it's ambiguous
- Use semantic versioning: `v1.2.3` or git SHA: `abc1234`
- Same image, multiple tags: `docker tag my-app:1.0 my-app:latest`

---

## Build Cache in Action

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt    # ← Cached if requirements.txt unchanged
COPY . .                               # ← Invalidates cache below if ANY file changes
CMD ["python", "app.py"]
```

**Rule:** Put things that change ** rarely** first (base image, dependencies), things that change **often** last (your code).

First build: all layers built.  
Change only `app.py`: layers 1–3 cached, only layer 4+ rebuild.

```bash
# Force rebuild without cache (when debugging Dockerfile)
docker build --no-cache -t my-app:1.0 .
```

---

## Removing Unused Resources

Docker accumulates junk. Clean regularly:

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Nuclear option — remove all unused stuff
docker system prune -a
# ⚠️ Removes ALL images not used by a container
```

**Interview tip:** Mention you run `docker system prune` in CI agents or dev machines to avoid disk fill-up.

---

## Copy-on-Write (CoW)

When a container runs, Docker adds a **thin writable layer** on top of the read-only image layers.

```
┌──────────────────┐
│ Writable layer   │  ← Container writes here (logs, temp files)
├──────────────────┤
│ Read-only layers │  ← Image (shared across containers)
└──────────────────┘
```

Multiple containers from same image share read-only layers — efficient disk use.

---

## Check Your Understanding

1. Why should `COPY requirements.txt` come before `COPY . .` in a Dockerfile?
2. What's the difference between `docker stop` and `docker rm`?
3. How do you get a shell inside a running container?
4. Why shouldn't you use the `latest` tag in production?

<details>
<summary>Answers</summary>

1. So dependency install is cached when only app code changes — faster rebuilds.
2. `stop` halts the running process; `rm` deletes the container record. Stop first, then rm.
3. `docker exec -it <container> /bin/sh` (or `/bin/bash` if available).
4. `latest` doesn't point to a fixed version — tomorrow's `latest` might be different. Reproducibility breaks.

</details>

---

## Hands-on Preview

In Example 2 you'll build a Python API image and watch cache behavior when you change files.

---

## Next Lesson

👉 **[Lesson 3: Dockerfile Deep Dive](03-dockerfile-deep-dive.md)**
