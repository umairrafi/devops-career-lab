# Week 1: Docker — Complete Course

**Duration:** 7 days (15–20 hours total)  
**Outcome:** Containerize apps, orchestrate multi-service stacks, production-ready Dockerfiles — plus a portfolio capstone project.

---

## What You'll Know by End of Week

After this week, you can confidently answer in interviews:

- "What's the difference between an image and a container?"
- "Walk me through your Dockerfile — why each line?"
- "How do you reduce image size?"
- "How do services talk to each other in Docker Compose?"
- "How do you debug a container that exits immediately?"

---

## Weekly Schedule

| Day | Focus | Folder | Time |
|-----|-------|--------|------|
| **Day 1** | Lessons 1–3: Concepts, images, Dockerfile | `01-lessons/` | 2–3 hrs |
| **Day 2** | Lessons 4–6: Compose, networking, multi-stage | `01-lessons/` | 2–3 hrs |
| **Day 3** | Lessons 7–8 + Hands-on 1–2 | `01-lessons/`, `02-hands-on/` | 2–3 hrs |
| **Day 4** | Hands-on 3–4 (multi-stage, full stack) | `02-hands-on/` | 2–3 hrs |
| **Day 5** | Exercises 1–4 | `03-exercises/` | 2 hrs |
| **Day 6** | Exercises 5–6 + start capstone | `03-exercises/`, `04-capstone-project/` | 3 hrs |
| **Day 7** | Finish capstone + write README | `04-capstone-project/` | 3–4 hrs |

---

## Course Structure

### Part 1 — Lessons (Read & Understand)

| # | Lesson | File |
|---|--------|------|
| 1 | What is Docker and why it exists | [01-what-is-docker.md](01-lessons/01-what-is-docker.md) |
| 2 | Images, containers, and layers | [02-images-containers-layers.md](01-lessons/02-images-containers-layers.md) |
| 3 | Dockerfile deep dive | [03-dockerfile-deep-dive.md](01-lessons/03-dockerfile-deep-dive.md) |
| 4 | Docker Compose | [04-docker-compose.md](01-lessons/04-docker-compose.md) |
| 5 | Networking and volumes | [05-networking-and-volumes.md](01-lessons/05-networking-and-volumes.md) |
| 6 | Multi-stage builds and optimization | [06-multi-stage-builds.md](01-lessons/06-multi-stage-builds.md) |
| 7 | Security and production practices | [07-security-production.md](01-lessons/07-security-production.md) |
| 8 | Debugging and troubleshooting | [08-debugging-troubleshooting.md](01-lessons/08-debugging-troubleshooting.md) |

### Part 2 — Hands-on Examples (Run & Learn)

| # | Example | What you'll learn |
|---|---------|-------------------|
| 1 | [Hello World](02-hands-on/example-01-hello-world/) | First container, basic commands |
| 2 | [Python Flask API](02-hands-on/example-02-python-api/) | Real app, ports, env vars |
| 3 | [Multi-stage Go build](02-hands-on/example-03-multi-stage-go/) | Small production images |
| 4 | [Full stack with Compose](02-hands-on/example-04-compose-stack/) | App + Postgres + Redis |

### Part 3 — Practice Exercises

[03-exercises/README.md](03-exercises/README.md) — 6 exercises with solutions (try first, then check).

### Part 4 — Capstone Project

**[TaskFlow Platform](04-capstone-project/)** — A mini internal task-management API with:
- Python FastAPI backend
- PostgreSQL database
- Redis cache
- Nginx reverse proxy
- All orchestrated with Docker Compose
- Production-style Dockerfiles (multi-stage, non-root user, health checks)

This becomes a Git portfolio piece and the foundation for Week 2 (Terraform) and Week 3 (GitHub Actions).

---

## Prerequisites

```bash
# Install Docker Desktop (Mac/Windows) or Docker Engine (Linux)
docker --version          # Should show 24.x or higher
docker compose version    # Should show v2.x

# Verify
docker run hello-world
```

---

## How to Study Each Lesson

1. **Read** the lesson fully once
2. **Run** every command in your terminal — don't copy-paste blindly; type and observe output
3. **Break it** — change something, see what fails, understand why
4. **Explain aloud** — "An image is like a recipe, a container is the cooked dish"
5. **Note questions** in [docs/learning-journey.md](../../docs/learning-journey.md)
6. **Commit** when done: `git commit -m "week-01: complete lesson 03 dockerfile"`

---

## Progress Checklist

Copy to your notes and check off:

```
Lessons
[ ] 01 - What is Docker
[ ] 02 - Images, containers, layers
[ ] 03 - Dockerfile deep dive
[ ] 04 - Docker Compose
[ ] 05 - Networking and volumes
[ ] 06 - Multi-stage builds
[ ] 07 - Security and production
[ ] 08 - Debugging

Hands-on
[ ] Example 01 - Hello World
[ ] Example 02 - Python API
[ ] Example 03 - Multi-stage Go
[ ] Example 04 - Compose stack

Exercises
[ ] Exercise 01 - Fix broken Dockerfile
[ ] Exercise 02 - Optimize image size
[ ] Exercise 03 - Add health checks
[ ] Exercise 04 - Environment variables
[ ] Exercise 05 - Compose networking
[ ] Exercise 06 - Volume persistence

Capstone
[ ] TaskFlow backend running
[ ] Postgres + Redis connected
[ ] Nginx reverse proxy working
[ ] README with architecture diagram
[ ] Pushed to GitHub
```

---

## Next Step

👉 Start with **[Lesson 1: What is Docker](01-lessons/01-what-is-docker.md)**

When you finish a section, tell me and we'll review together or move to the next part.
