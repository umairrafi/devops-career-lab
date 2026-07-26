# Capstone Project: TaskFlow Platform

**Time:** 6–8 hours (Days 6–7 of Week 1)  
**Goal:** Build a portfolio-ready multi-service platform that proves Docker mastery.

---

## What You're Building

**TaskFlow** — an internal task management platform (like a mini Jira/Trello backend).

```
                    ┌──────────────┐
   Browser/curl ──▶ │    Nginx     │ :80
                    │  (reverse    │
                    │   proxy)     │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   FastAPI    │ :8000
                    │   (api)      │
                    └──┬───────┬───┘
                       │       │
              ┌────────▼─┐  ┌──▼────────┐
              │ Postgres │  │   Redis   │
              │   (db)   │  │  (cache)  │
              └──────────┘  └───────────┘
```

---

## Requirements Checklist

### Must Have (complete these for Week 1 pass)

- [ ] FastAPI backend with CRUD for tasks and projects
- [ ] PostgreSQL with persistent named volume
- [ ] Redis for caching task counts
- [ ] Nginx reverse proxy in front of API
- [ ] Multi-service `docker-compose.yml`
- [ ] Production Dockerfiles: non-root, HEALTHCHECK, slim base
- [ ] DB healthcheck + `depends_on: condition: service_healthy`
- [ ] `.env.example` — secrets via env, not in images
- [ ] README with architecture diagram and run instructions
- [ ] All services show `(healthy)` in `docker compose ps`

### Nice to Have (stretch goals)

- [ ] Multi-stage Dockerfile for API
- [ ] `docker-compose.prod.yml` override
- [ ] API `/docs` (FastAPI auto Swagger) accessible via Nginx
- [ ] Makefile with common commands

---

## Project Structure

```
04-capstone-project/
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
├── Makefile
├── README.md
├── nginx/
│   └── nginx.conf
├── api/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── database.py
│       ├── models.py
│       └── routes/
│           ├── tasks.py
│           └── projects.py
└── docs/
    └── ARCHITECTURE.md
```

---

## Step-by-Step Build Guide

### Step 1: Start the stack (15 min)

```bash
cd weeks/week-01-docker/04-capstone-project

cp .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs -f
```

Fix any startup errors before continuing.

### Step 2: Test the API (15 min)

```bash
# Via Nginx (port 80)
curl http://localhost/health
curl http://localhost/docs

# Create project
curl -X POST http://localhost/api/projects \
  -H "Content-Type: application/json" \
  -d '{"name": "Week 1 Docker", "description": "Learn containerization"}'

# Create task
curl -X POST http://localhost/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete capstone", "project_id": 1, "priority": "high"}'

# List tasks
curl http://localhost/api/tasks
curl http://localhost/api/stats
```

### Step 3: Verify production patterns (30 min)

```bash
# Non-root
docker compose exec api whoami

# Health
docker compose ps  # all healthy

# Persistence
docker compose down
docker compose up -d
curl http://localhost/api/tasks  # data survived

# Secrets not in image
docker history taskflow-api 2>/dev/null | head
```

### Step 4: Write your README (30 min)

Update `README.md` with:
- What TaskFlow does
- Architecture diagram (Mermaid provided in ARCHITECTURE.md)
- How to run
- What you learned
- Screenshots or curl output

### Step 5: Push to GitHub (15 min)

```bash
git add .
git commit -m "week-01: TaskFlow capstone complete"
git push origin main
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check (db + redis) |
| GET | `/api/stats` | Task counts (cached in Redis) |
| GET | `/api/projects` | List projects |
| POST | `/api/projects` | Create project |
| GET | `/api/tasks` | List tasks (filter by project_id) |
| POST | `/api/tasks` | Create task |
| PATCH | `/api/tasks/{id}` | Update task status |
| DELETE | `/api/tasks/{id}` | Delete task |

---

## Interview Pitch (Memorize This)

> "TaskFlow is a multi-service task platform I containerized with Docker. It runs FastAPI, PostgreSQL, Redis, and Nginx behind Docker Compose. I used production patterns — multi-stage builds, non-root users, health checks, named volumes for persistence, and internal networking without exposing the database. It's the foundation for my Week 2 Terraform deployment and Week 3 CI/CD pipeline."

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| 502 from Nginx | API not ready — check `docker compose logs api` |
| DB connection refused | Use hostname `db`, wait for healthcheck |
| Permission denied | Check USER and chown in Dockerfile |
| Port 80 in use | Change nginx ports to `"8080:80"` in compose |

---

## Grading Yourself

| Score | Criteria |
|-------|----------|
| **Pass** | Stack runs, CRUD works, persistence proven, README complete |
| **Strong** | All must-haves + clean Dockerfiles you can explain line-by-line |
| **Expert** | Stretch goals + can debug failures in under 5 minutes |

---

## Next Weeks

- **Week 2:** Deploy TaskFlow infra to AWS with Terraform (ECS, RDS, ElastiCache)
- **Week 3:** GitHub Actions — test, build images, push to ECR, deploy

Tell me when you start building — I'll review your Dockerfile and compose file as you go.
