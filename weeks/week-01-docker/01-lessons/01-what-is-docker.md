# Lesson 1: What is Docker and Why It Exists

**Reading time:** 15 minutes  
**After this lesson you'll understand:** The problem Docker solves and why every DevOps interview asks about it.

---

## The Problem Before Docker

Imagine you built a Python Flask API on your Mac. It works perfectly. You send it to a colleague running Ubuntu — it crashes. Why?

- Different Python version (3.9 vs 3.11)
- Missing system library (`libpq` for PostgreSQL)
- Wrong environment variable
- "Works on my machine" became a meme for a reason

**Traditional fix:** Manual setup docs, VMs (slow, heavy), or praying.

---

## What Docker Actually Is

Docker packages your application **and everything it needs to run** into a single unit called an **image**.

Think of it like shipping a prefab house instead of sending lumber and hoping the builder knows what to do.

```
┌─────────────────────────────────────┐
│           Docker Image              │
│  ┌─────────┐ ┌─────────┐ ┌───────┐ │
│  │ Your    │ │ Python  │ │ OS    │ │
│  │ App     │ │ 3.11    │ │ libs  │ │
│  └─────────┘ └─────────┘ └───────┘ │
└─────────────────────────────────────┘
         │
         │  docker run
         ▼
┌─────────────────────────────────────┐
│         Running Container           │  ← Isolated process on your machine
└─────────────────────────────────────┘
```

**Image** = Blueprint (read-only template)  
**Container** = Running instance of that blueprint

You can run 10 containers from 1 image — like printing 10 copies of the same document.

---

## Docker vs Virtual Machines

| | Virtual Machine | Docker Container |
|---|-----------------|------------------|
| **Startup** | Minutes | Seconds |
| **Size** | GBs (full OS each) | MBs (shares host kernel) |
| **Isolation** | Full OS isolation | Process-level isolation |
| **Use case** | Different OS entirely | Same OS, packaged apps |

Docker containers share the **host OS kernel**. They don't boot a full Linux inside Linux — they run as isolated processes. That's why they're fast and small.

**Interview line:** "Containers share the host kernel; VMs virtualize hardware. Containers are lighter and start faster; VMs give stronger isolation across OS boundaries."

---

## Why Docker Matters for Your Career

1. **DevOps:** Every CI/CD pipeline builds Docker images. You deploy containers to ECS, EKS, Lambda (container images), Cloud Run.

2. **Consistency:** Dev, staging, prod run the same image. No more environment drift.

3. **Microservices:** Each service = one container. Scale independently.

4. **Your background:** You've used AWS Lambda. Lambda now supports **container images** — same Dockerfile skills apply.

---

## Core Docker Concepts (Preview)

You'll dive deep in later lessons. For now, know these names:

| Term | One-line meaning |
|------|------------------|
| **Dockerfile** | Text file with instructions to build an image |
| **Image** | Built artifact, stored in a registry (Docker Hub, ECR) |
| **Container** | Running instance of an image |
| **Registry** | Storage for images (like GitHub for code) |
| **Docker Compose** | Tool to run multiple containers together |
| **Volume** | Persistent storage that survives container deletion |

---

## Essential Commands (Try Now)

Open your terminal and run these:

```bash
# Check Docker is installed
docker --version

# Download and run a test image (creates a container, runs it, exits)
docker run hello-world

# List running containers (empty after hello-world exits)
docker ps

# List ALL containers including stopped
docker ps -a

# List images on your machine
docker images

# Download an image without running it
docker pull nginx:alpine

# Run nginx in background (-d = detached), map port 8080 on host to 80 in container
docker run -d -p 8080:80 --name my-nginx nginx:alpine

# Visit http://localhost:8080 in browser — you should see nginx welcome page

# See running containers
docker ps

# Stop the container
docker stop my-nginx

# Remove the container
docker rm my-nginx

# Remove the image (optional)
docker rmi nginx:alpine
```

**What happened:**
1. `docker pull` downloaded the image from Docker Hub
2. `docker run` created a container from that image and started it
3. `-p 8080:80` forwarded your laptop's port 8080 to container port 80
4. `docker stop` sent SIGTERM to gracefully shut down the process inside

---

## Mental Model: Restaurant Analogy

| Docker | Restaurant |
|--------|------------|
| **Dockerfile** | Recipe card |
| **Image** | Prepped ingredients kit (frozen, ready to cook) |
| **Container** | The actual dish being served right now |
| **Docker Hub** | Warehouse that stores ingredient kits |
| **docker run** | "Cook and serve one order" |
| **docker compose** | Full menu — kitchen coordinates appetizer + main + dessert together |

---

## Common Misconceptions

❌ **"Docker is only for development"**  
→ Production runs containers on AWS ECS, Kubernetes, etc.

❌ **"Docker replaces VMs entirely"**  
→ Often used together. VMs host Docker; containers run inside.

❌ **"I need to learn Kubernetes before Docker"**  
→ Docker first. Kubernetes orchestrates Docker containers at scale.

---

## Check Your Understanding

Answer these before moving to Lesson 2:

1. What is the difference between an image and a container?
2. Why are containers faster to start than VMs?
3. What does `-p 8080:80` mean in `docker run`?
4. Where does Docker store downloaded images locally?

<details>
<summary>Answers (try first!)</summary>

1. Image = read-only template; container = running instance of that template.
2. Containers share the host kernel; VMs boot a full OS each time.
3. Host port 8080 maps to container port 80 — traffic to localhost:8080 goes to the app listening on port 80 inside the container.
4. Local image cache — view with `docker images`. Stored in Docker's data directory (Docker Desktop manages this).

</details>

---

## Next Lesson

👉 **[Lesson 2: Images, Containers, and Layers](02-images-containers-layers.md)**

**Commit suggestion:** `git commit -m "week-01: complete lesson 01 what is docker"`
