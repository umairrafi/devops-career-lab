# Lesson 7: Security and Production Practices

**Reading time:** 20 minutes  
**After this lesson you'll understand:** How to run containers safely in production — what interviewers expect from a DevOps-minded engineer.

---

## Security Principles for Containers

### 1. Don't run as root

```dockerfile
# Debian/Ubuntu slim
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Alpine
RUN adduser -D appuser
USER appuser
```

If container is compromised, attacker has limited privileges.

```bash
# Verify at runtime
docker exec api whoami   # Should NOT be root
```

### 2. Never bake secrets into images

```dockerfile
# ❌ NEVER
ENV AWS_SECRET_KEY=sk-live-xxxxx
COPY .env .
```

```yaml
# ✅ Pass at runtime
environment:
  DATABASE_URL: ${DATABASE_URL}
env_file:
  - .env   # .env in .gitignore and .dockerignore
```

Production: AWS Secrets Manager, Parameter Store, Kubernetes secrets — injected at deploy time.

### 3. Use .dockerignore aggressively

```
.env
.env.*
*.pem
*.key
secrets/
.git
```

### 4. Pin base image versions

```dockerfile
# ❌ Unpredictable
FROM python:latest

# ✅ Reproducible
FROM python:3.11.9-slim-bookworm
```

Update deliberately, scan after updates.

### 5. Scan images for vulnerabilities

```bash
# Docker Scout (built into Docker Desktop)
docker scout quickview my-app:1.0

# Trivy (CI-friendly — you'll use in Week 3)
trivy image my-app:1.0
```

Fix or upgrade base images when critical CVEs appear.

### 6. Read-only filesystem (when possible)

```bash
docker run --read-only -v /tmp tmpfs my-app
```

```yaml
services:
  api:
    read_only: true
    tmpfs:
      - /tmp
```

### 7. Drop unnecessary capabilities

```yaml
services:
  api:
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
```

---

## Production Dockerfile Checklist

```dockerfile
FROM python:3.11-slim-bookworm          # ✅ Pinned version
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1                  # ✅ Proper logging
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser                            # ✅ Non-root
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "..." || exit 1         # ✅ Health check
CMD ["python", "app.py"]                # ✅ Exec form
```

---

## Logging Best Practices

- Log to **stdout/stderr** — Docker captures automatically
- Use structured JSON logs in production
- Don't log secrets or PII

```python
import json, logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(message)s')
logger = logging.getLogger(__name__)
logger.info(json.dumps({"event": "request", "path": "/health", "status": 200}))
```

View logs:

```bash
docker logs api
docker compose logs -f --tail=100 api
```

In AWS: CloudWatch Logs driver, Fluent Bit, Datadog agent.

---

## Resource Limits

Prevent one container from consuming entire host:

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          memory: 256M
```

```bash
docker run -m 512m --cpus=0.5 my-api
```

**Interview:** "Without limits, a memory leak in one container can OOM-kill the host."

---

## Graceful Shutdown

Docker sends **SIGTERM** on stop, waits 10s (default), then **SIGKILL**.

Your app must handle SIGTERM:

```python
import signal, sys
def shutdown(signum, frame):
    print("Shutting down gracefully...")
    # close DB connections, finish requests
    sys.exit(0)
signal.signal(signal.SIGTERM, shutdown)
```

```yaml
services:
  api:
    stop_grace_period: 30s
```

---

## Production vs Development Compose

| Concern | Development | Production |
|---------|-------------|------------|
| Code mount | Bind mount for hot reload | Baked in image |
| Secrets | `.env` file | Secret manager |
| Ports | Expose all for debugging | Only public services |
| Database | Port mapped to host | Internal network only |
| Restart | Manual | `restart: unless-stopped` |
| Images | `build:` locally | Pull from ECR with pinned tag |

```yaml
# Production snippet
services:
  api:
    image: 123456789.dkr.ecr.me-south-1.amazonaws.com/taskflow-api:v1.0.0
    restart: unless-stopped
    # no build:, no bind mounts
```

---

## Check Your Understanding

1. Why shouldn't secrets be in Dockerfile ENV?
2. What signal does Docker send when you `docker stop`?
3. Why run containers as non-root?
4. What's the purpose of HEALTHCHECK?

<details>
<summary>Answers</summary>

1. Images are stored in registries and layers persist — secrets become extractable via `docker history` or image inspection.
2. SIGTERM first (graceful shutdown window), then SIGKILL if process doesn't exit.
3. Limits blast radius if container is compromised; principle of least privilege.
4. Lets orchestrators detect and restart unhealthy containers; load balancers can route away from unhealthy instances.

</details>

---

## Next Lesson

👉 **[Lesson 8: Debugging and Troubleshooting](08-debugging-troubleshooting.md)**
