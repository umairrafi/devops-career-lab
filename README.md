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

## 16-Week Master Roadmap

### Foundation (Weeks 1–6) — Platform & Full Stack

| Week | Topic | Capstone Project |
|------|-------|------------------|
| **1** | Docker | [TaskFlow Platform](weeks/week-01-docker/04-capstone-project/) — multi-service app with Compose |
| **2** | Terraform | AWS infrastructure for TaskFlow (VPC, ECS, RDS) |
| **3** | GitHub Actions | CI/CD pipelines — test, build, deploy |
| **4** | Kubernetes basics | Deploy TaskFlow to EKS/local k3s |
| **5** | Next.js + TypeScript | TaskFlow dashboard frontend |
| **6** | System design | Architecture docs + ADRs for TaskFlow |

### AI Agents Track (Weeks 7–10) — Build & Automate

| Week | Topic | Capstone | Resources |
|------|-------|----------|-----------|
| **7** | AI agents + ReAct | TaskFlow AI Agent v1 | [50-resource map → Phase 1–2](tracks/ai-agents/RESOURCE-MAP.md) |
| **8** | RAG + MCP | TaskFlow doc Q&A + MCP server | Phase 3–4 |
| **9** | Multi-agent + automation | DevOps agent team | Phase 5–6 |
| **10** | Evals + LLMOps | Agent CI in GitHub Actions | Phase 7 |

👉 **[AI Agents Track overview](tracks/ai-agents/README.md)** — all 50 LinkedIn resources organized  
👉 **[Automation playbook](tracks/ai-agents/AUTOMATION-PLAYBOOK.md)** — what to automate at work

### Career (Weeks 11–16)

| Week | Topic |
|------|-------|
| **11** | Observability (logging, metrics, tracing) |
| **12** | Security hardening |
| **13** | End-to-end integration + demo |
| **14** | Interview prep + system design |
| **15** | Portfolio + LinkedIn push |
| **16** | Job switch + negotiation |

---

## Legacy 12-Week View (compact)

Weeks 1–6 same as above · Week 7–10 AI track · Weeks 11–12 interview + job switch (compress 11–16 if time-boxed).

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
