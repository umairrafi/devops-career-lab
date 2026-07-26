# Exercise 03 — Health Checks

Starter compose stack missing healthchecks and restart policies.

Fix `docker-compose.yml` and `api/Dockerfile` so all services show `(healthy)`.

```bash
cd exercise-03-healthchecks
docker compose up -d --build
docker compose ps
```

All services should be healthy within 60 seconds.
