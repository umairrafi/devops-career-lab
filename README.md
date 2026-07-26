# DevOps Career Lab

**Your structured, project-based path to DevOps + Backend + Full Stack + AI Agent Engineering.**

Built for engineers with real backend experience who want to level up fast and switch jobs with proof — not certificates.

## Who This Is For

- 3+ years backend experience (Python, Go, AWS Lambda, etc.)
- Already touching Docker, Terraform, GitHub Actions at work
- Want interview-ready skills in **weeks**, not months
- Learn by building, committing, and explaining

## How Each Week Works

Every week follows the same proven structure:

```
week-XX-topic/
├── README.md              ← Start here: goals, schedule, checklist
├── 01-lessons/            ← Concepts explained simply (read → understand)
├── 02-hands-on/           ← Copy-run examples (do → see it work)
├── 03-exercises/          ← Practice problems (try → check solutions)
└── 04-capstone-project/   ← Real project (build → portfolio piece)
```

| Phase | Time | What you do |
|-------|------|-------------|
| **Lessons** | Day 1–2 | Read concepts, take notes, ask questions |
| **Hands-on** | Day 2–4 | Run every example, break things on purpose |
| **Exercises** | Day 4–5 | Solve problems without peeking at solutions |
| **Capstone** | Day 5–7 | Build the week project, push to Git, write README |

## 12-Week Roadmap

| Week | Topic | Capstone Project |
|------|-------|------------------|
| **1** | Docker | [TaskFlow Platform](weeks/week-01-docker/04-capstone-project/) — multi-service app with Compose |
| **2** | Terraform | AWS infrastructure for TaskFlow (VPC, ECS, RDS) |
| **3** | GitHub Actions | CI/CD pipelines — test, build, deploy |
| **4** | Kubernetes basics | Deploy TaskFlow to EKS/local k3s |
| **5** | Next.js + TypeScript | TaskFlow dashboard frontend |
| **6** | System design | Architecture docs + ADRs for TaskFlow |
| **7** | AI agents | TaskFlow AI assistant (tool use, RAG) |
| **8** | Observability | Logging, metrics, tracing for TaskFlow |
| **9** | Security | Hardening, secrets, supply chain |
| **10** | Integration | End-to-end deploy + demo |
| **11** | Interview prep | Mock interviews, system design drills |
| **12** | Job switch | Applications, resume, negotiation |

## Getting Started

1. **Clone and enter Week 1:**
   ```bash
   cd weeks/week-01-docker
   cat README.md
   ```

2. **Prerequisites:** Docker Desktop installed ([Install guide](https://docs.docker.com/get-docker/))

3. **Verify Docker works:**
   ```bash
   docker --version
   docker run hello-world
   ```

4. **Follow the week README day by day.** Commit after each section.

## Git Workflow

```bash
# After each lesson or example
git checkout -b week-01/day-2-hands-on
git add .
git commit -m "week-01: complete hands-on example 03 multi-stage build"
git push origin week-01/day-2-hands-on
```

Use conventional commits: `week-XX: <what you did>`

## Progress Tracking

Mark your progress in each week's `PROGRESS.md` file.

## Current Week

👉 **[Week 1: Docker → Start here](weeks/week-01-docker/README.md)**
