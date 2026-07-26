# Hands-on Example 2: Python Flask API

**Time:** 45 minutes  
**Goal:** Containerize a real API with proper Dockerfile patterns, health checks, and non-root user.

---

## What You'll Build

A minimal Flask API with:
- `/health` endpoint
- `/api/items` CRUD stub
- Production-style Dockerfile

---

## Project Structure

```
example-02-python-api/
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── app.py
└── README.md
```

---

## Step 1: Review the Application

Open `app.py` — a simple Flask API with health check.

Key line for Docker:
```python
app.run(host='0.0.0.0', port=5000)  # Must bind 0.0.0.0, not 127.0.0.1
```

---

## Step 2: Build the Image

```bash
cd weeks/week-01-docker/02-hands-on/example-02-python-api

docker build -t flask-api:1.0 .
```

Watch the build output — notice layer caching:
- Run build again without changes → "CACHED" on most steps
- Change `app.py` only → only last layers rebuild

---

## Step 3: Run the Container

```bash
docker run -d -p 5000:5000 --name flask-api flask-api:1.0

# Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/api/items
```

---

## Step 4: Pass Environment Variables

```bash
docker stop flask-api && docker rm flask-api

docker run -d -p 5000:5000 \
  -e APP_ENV=development \
  -e LOG_LEVEL=DEBUG \
  --name flask-api \
  flask-api:1.0

docker exec flask-api env | grep APP
```

---

## Step 5: Check Health and Logs

```bash
docker ps                    # STATUS should show (healthy) after ~30s
docker logs flask-api
docker exec flask-api whoami # Should print: appuser (not root)
```

---

## Step 6: Debug Exercise

Stop container, run interactively:

```bash
docker run -it --entrypoint /bin/sh flask-api:1.0
$ python -c "from app import app; print(app.config)"
$ exit
```

---

## Step 7: Clean Up

```bash
docker stop flask-api
docker rm flask-api
# Keep image for later or: docker rmi flask-api:1.0
```

---

## Dockerfile Walkthrough

Read the Dockerfile line by line and match to Lesson 3:

1. `FROM python:3.11-slim` — pinned base
2. `ENV PYTHONUNBUFFERED=1` — logs appear immediately
3. `COPY requirements.txt` before `COPY . .` — cache optimization
4. `USER appuser` — security
5. `HEALTHCHECK` — orchestration readiness

---

## Experiment

1. Remove `host='0.0.0.0'` from app.py, rebuild, run — curl fails. Why?
2. Add a new route `/api/version` — rebuild and verify only later layers changed
3. Check image size: `docker images flask-api`

---

## Next

👉 **[Example 3: Multi-stage Go](../example-03-multi-stage-go/README.md)**
