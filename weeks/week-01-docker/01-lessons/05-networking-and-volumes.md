# Lesson 5: Networking and Volumes

**Reading time:** 20 minutes  
**After this lesson you'll understand:** How containers communicate and how data persists.

---

## Docker Networking Models

### Default: Bridge network

When you `docker run`, containers join a **bridge network**. Each container gets its own IP. Port mapping (`-p`) exposes ports to the host.

```
Host Machine (your laptop)
├── docker0 bridge (172.17.0.1)
│   ├── Container A (172.17.0.2) — api
│   ├── Container B (172.17.0.3) — db
│   └── Container C (172.17.0.4) — redis
└── localhost:8000 ──maps──▶ Container A:8000
```

### Custom networks

```bash
docker network create myapp-net
docker run -d --network myapp-net --name db postgres:16
docker run -d --network myapp-net --name api -e DB_HOST=db my-api
```

Containers on same network can ping each other by **name** (Docker DNS).

### Network drivers

| Driver | Use case |
|--------|----------|
| `bridge` | Default, single host |
| `host` | Container uses host network directly (no isolation) |
| `none` | No networking |
| `overlay` | Multi-host (Swarm, some K8s setups) |

**Compose** creates a bridge network automatically for the project.

---

## Port Mapping Deep Dive

```bash
docker run -p 8000:8000 my-api
#            │     │
#            │     └── Port inside container
#            └── Port on host (your machine)
```

Variations:

```bash
-p 8000:8000              # All interfaces (0.0.0.0)
-p 127.0.0.1:8000:8000    # Localhost only (more secure for dev)
-p 8000:8000/udp          # UDP port
-P                        # Publish ALL exposed ports to random host ports
```

**Interview question:** "What's the difference between EXPOSE and -p?"

**Answer:** EXPOSE is documentation in Dockerfile. `-p` (or Compose `ports:`) actually publishes to the host.

---

## Container-to-Container Communication

```python
# Inside API container — CORRECT
DATABASE_URL = "postgresql://user:pass@db:5432/myapp"
#                                  ^^ service name

# WRONG — this points to API container itself
DATABASE_URL = "postgresql://user:pass@localhost:5432/myapp"
```

```python
# WRONG — host.docker.internal works on Docker Desktop for reaching HOST
# but NOT for reaching other containers
REDIS_URL = "redis://host.docker.internal:6379"  # Only if Redis on host
```

---

## Volumes — Persistent Data

Container filesystem is **ephemeral**. Delete container = data gone.

### Named volumes (recommended for databases)

```bash
docker volume create pgdata
docker run -v pgdata:/var/lib/postgresql/data postgres:16
```

```yaml
# Compose
volumes:
  pgdata:

services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
```

Data survives `docker compose down`. Deleted only with `docker compose down -v`.

### Bind mounts (dev hot-reload)

```yaml
services:
  api:
    volumes:
      - ./src:/app/src   # Host dir mounted into container
```

Changes on host appear instantly in container. Perfect for development; use named volumes for production database data.

### tmpfs mounts (in-memory, no persist)

```yaml
tmpfs:
  - /tmp
```

---

## Volume Commands

```bash
docker volume ls
docker volume inspect pgdata
docker volume rm pgdata
docker volume prune    # Remove unused volumes
```

---

## Networking Commands

```bash
docker network ls
docker network inspect myapp_default
docker network rm myapp-net

# Test connectivity from inside container
docker exec -it api ping db
docker exec -it api curl http://redis:6379
# or
docker compose exec api wget -qO- http://db:5432  # may fail but DNS resolves
```

---

## Real-World Pattern: Init and Migrations

Database must exist before API connects. Pattern:

```yaml
api:
  depends_on:
    db:
      condition: service_healthy
  command: >
    sh -c "python wait_for_db.py &&
           python migrate.py &&
           python app.py"
```

Or run migrations as one-off:

```bash
docker compose run api python migrate.py
docker compose up -d api
```

---

## Security: Don't Expose Database Ports

```yaml
# Bad for production — exposes Postgres to host/internet
db:
  ports:
    - "5432:5432"

# Good — db only reachable by other containers on internal network
db:
  # no ports section — internal only
  expose:
    - "5432"   # optional documentation
```

API connects via `db:5432` on internal network. No host port mapping needed.

---

## Check Your Understanding

1. How do containers on the same Compose network find each other?
2. What's the difference between a bind mount and a named volume?
3. Why shouldn't you map Postgres port 5432 to host in production?
4. What happens to named volume data when you `docker compose down`?

<details>
<summary>Answers</summary>

1. Docker's internal DNS — service name resolves to container IP.
2. Bind mount = specific host directory synced; named volume = Docker-managed storage, portable, better for DB data.
3. Exposes database to host network — security risk. Internal network access is enough for app containers.
4. Data **persists**. Only `docker compose down -v` removes volumes.

</details>

---

## Next Lesson

👉 **[Lesson 6: Multi-Stage Builds and Optimization](06-multi-stage-builds.md)**
