# Lesson 8: Debugging and Troubleshooting

**Reading time:** 20 minutes  
**After this lesson you'll understand:** A systematic approach to fixing Docker problems — essential for DevOps interviews and on-the-job.

---

## The Debugging Mindset

When something fails, ask in order:

1. **Did the image build?** → Build logs, Dockerfile syntax
2. **Did the container start?** → `docker ps -a`, exit codes
3. **Is the process running inside?** → `docker logs`, `docker exec`
4. **Can it reach dependencies?** → Network, DNS, env vars
5. **Are ports correct?** → Mapping, EXPOSE, firewall

---

## Problem: Container Exits Immediately

```bash
docker ps -a
# STATUS: Exited (1) 2 seconds ago
```

**Diagnose:**

```bash
docker logs my-container          # See error output
docker inspect my-container       # Check ExitCode, Error, Cmd
```

**Common causes:**

| Cause | Fix |
|-------|-----|
| CMD points to wrong path | Fix Dockerfile CMD |
| App crashes on startup | Read logs, missing env var |
| Script not executable | `RUN chmod +x script.sh` |
| Running as wrong user | Permission denied — fix ownership |

**Override CMD to debug:**

```bash
docker run -it --entrypoint /bin/sh my-app
# Now you're in shell — run commands manually
```

---

## Problem: Can't Connect to App on localhost

```bash
curl http://localhost:8000
# Connection refused
```

**Checklist:**

```bash
docker ps                           # Is container running?
docker port my-container            # Port mapping correct?
docker logs my-container            # App actually listening?
docker exec my-container netstat -tlnp   # Or ss -tlnp
```

**Common mistakes:**

- App listens on `127.0.0.1` inside container → must listen on `0.0.0.0`
- Wrong port mapping: `-p 8000:5000` but app on 8000
- Forgot `-p` entirely

```python
# Flask — must bind all interfaces in container
app.run(host='0.0.0.0', port=5000)
```

---

## Problem: Database Connection Refused

```
sqlalchemy.exc.OperationalError: could not connect to server: Connection refused
```

**Checklist:**

1. Using service name (`db`) not `localhost`?
2. Is db container running? `docker compose ps`
3. Is db healthy? `docker compose ps` shows `(healthy)`
4. Correct credentials in DATABASE_URL?
5. Is API starting before db is ready? → Add healthcheck + depends_on condition

```bash
# Test from API container
docker compose exec api ping db
docker compose exec api nc -zv db 5432
```

---

## Problem: Build Fails or Is Slow

```bash
docker build -t my-app .
# ERROR or takes forever
```

**Fixes:**

```bash
docker build --progress=plain -t my-app .   # Verbose output
docker build --no-cache -t my-app .         # Ignore bad cache
```

- Check `.dockerignore` — is `node_modules` being sent?
- Network issues during `RUN apt-get` or `pip install`?
- Typo in COPY path?

```bash
docker history my-app:latest    # Which layer is huge?
```

---

## Problem: Out of Disk Space

```bash
docker system df
# Images: 45GB, Containers: 2GB, Volumes: 10GB

docker system prune -a --volumes   # Careful — removes unused everything
```

---

## Useful Debug Commands Cheat Sheet

```bash
# Lifecycle
docker ps -a
docker logs -f --tail=50 CONTAINER
docker inspect CONTAINER
docker events

# Inside container
docker exec -it CONTAINER /bin/sh
docker exec CONTAINER env              # See environment variables
docker exec CONTAINER cat /etc/hosts   # DNS entries

# Network
docker network inspect NETWORK
docker compose exec api ping db
docker compose exec api curl -v http://api:8000/health

# Images
docker history IMAGE
docker image inspect IMAGE

# Compose
docker compose config                  # Validate and render final YAML
docker compose ps
docker compose top                     # Processes in each service
```

---

## Interview: "Walk me through debugging a failing container in production"

**Strong answer structure:**

1. Check orchestrator events (ECS/K8s) or `docker ps -a`
2. Pull logs: `docker logs` or CloudWatch
3. Check recent deploy — new image tag? config change?
4. Verify health endpoint and resource limits (OOM?)
5. Exec into container if needed (or debug sidecar in distroless)
6. Check connectivity to dependencies
7. Roll back to last known good image if critical
8. Post-incident: add healthcheck, improve logging, fix root cause

---

## Practice: Break Things on Purpose

Learning Docker means breaking things deliberately:

1. Remove `host='0.0.0.0'` from Flask — see connection refused
2. Use `localhost` for db hostname — see connection error
3. Remove HEALTHCHECK — see unhealthy status in Compose
4. Run as root vs non-root — see permission errors on files
5. Fill disk with `docker run` loops — practice prune

---

## Week 1 Lessons Complete

You now have the conceptual foundation. Time to **build muscle memory**:

1. 👉 **[Hands-on Examples](../02-hands-on/)** — run all 4
2. 👉 **[Exercises](../03-exercises/)** — solve 6 problems
3. 👉 **[Capstone: TaskFlow](../04-capstone-project/)** — portfolio project

---

## Next Step

👉 **[Hands-on Example 1: Hello World](../02-hands-on/example-01-hello-world/README.md)**
