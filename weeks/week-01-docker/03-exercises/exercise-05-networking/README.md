# Exercise 05 — Fix Networking

The API cannot connect to the database. Fix the stack.

Error in logs:
```
could not connect to server: Connection refused
    Is the server running on host "localhost"?
```

Files: `docker-compose.yml`, `api/app.py`

After fix:
```bash
docker compose up -d --build
curl http://localhost:8000/health  # db: healthy
```

Write `FIX.md` explaining the root cause.
