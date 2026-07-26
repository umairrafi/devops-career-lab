# Hands-on Example 4: Full Stack with Docker Compose

**Time:** 60 minutes  
**Goal:** Run API + PostgreSQL + Redis together — the pattern you'll use in the capstone and at work.

---

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   API       │────▶│  PostgreSQL │     │    Redis    │
│  (Python)   │     │   (db)      │     │   (cache)   │
│  :8000      │────▶│   :5432     │     │   :6379     │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲
       │ localhost:8000
   Your browser/curl
```

---

## Step 1: Review Files

```
example-04-compose-stack/
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── README.md
```

The API:
- Connects to Postgres using hostname `db`
- Connects to Redis using hostname `redis`
- Waits for DB before starting (simple retry loop)

---

## Step 2: Start the Stack

```bash
cd weeks/week-01-docker/02-hands-on/example-04-compose-stack

docker compose up -d --build
```

Watch logs:
```bash
docker compose logs -f
```

Wait until you see API ready messages.

---

## Step 3: Test Endpoints

```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/counter
curl http://localhost:8000/api/counter   # Increment — watch count go up
curl http://localhost:8000/api/tasks
```

---

## Step 4: Explore the Network

```bash
docker compose ps
docker network ls | grep compose
docker compose exec api ping -c 2 db
docker compose exec api ping -c 2 redis
```

---

## Step 5: Database Persistence Test

```bash
# Create a task
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Docker Compose"}'

curl http://localhost:8000/api/tasks

# Restart stack (NOT down -v)
docker compose restart

curl http://localhost:8000/api/tasks
# Task still there — volume persisted
```

---

## Step 6: Simulate DB Not Ready

```bash
docker compose stop db
curl http://localhost:8000/health
# Should show db: unhealthy

docker compose start db
# Wait for healthy, then retry
```

---

## Step 7: Run Migrations Manually

```bash
docker compose exec api python -c "from app import init_db; init_db()"
```

---

## Step 8: Tear Down

```bash
# Stop, keep data
docker compose down

# Stop, DELETE database data
docker compose down -v
```

---

## Compose File Highlights

Study `docker-compose.yml`:

- `healthcheck` on db with `pg_isready`
- `depends_on` with `condition: service_healthy`
- Named volume `pgdata` for Postgres
- No port mapping on db/redis (internal only) — **production pattern**

---

## Experiment

1. Change API to use `localhost` for db — watch it fail. Fix back to `db`.
2. Add `docker compose logs db` when healthcheck fails
3. Scale API: `docker compose up -d --scale api=2` — what breaks? (port conflict — learn why)

---

## Next

👉 **[Practice Exercises](../../03-exercises/README.md)**
