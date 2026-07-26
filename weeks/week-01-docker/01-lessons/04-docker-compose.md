# Lesson 4: Docker Compose

**Reading time:** 20 minutes  
**After this lesson you'll understand:** How to run multi-container applications with one command.

---

## The Problem Compose Solves

Your app needs:
- API container
- PostgreSQL container
- Redis container

Without Compose:

```bash
docker network create mynet
docker run -d --network mynet --name db -e POSTGRES_PASSWORD=secret postgres:16
docker run -d --network mynet --name redis redis:7-alpine
docker run -d --network mynet --name api -e DATABASE_URL=... -p 8000:8000 my-api
# ... 20 more flags, wrong order = broken app
```

With Compose — one file, one command:

```bash
docker compose up -d
```

---

## docker-compose.yml Structure

```yaml
services:          # Define containers
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:secret@db:5432/myapp
    depends_on:
      - db
      - redis

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

volumes:           # Named volumes (persistent storage)
  pgdata:

networks:          # Optional — default network created automatically
  default:
    name: myapp-network
```

---

## Key Concepts

### Service names = DNS hostnames

Inside the Compose network, services reach each other by **service name**:

```
API connects to: postgresql://postgres:secret@db:5432/myapp
                                              ^^
                                         service name, NOT localhost
```

**Common beginner bug:** Using `localhost` inside a container refers to **that container itself**, not the host or sibling containers.

### depends_on

```yaml
depends_on:
  - db
```

Starts `db` before `api`. **Does NOT wait for db to be ready** — only for container to start. For readiness, use healthchecks:

```yaml
db:
  image: postgres:16-alpine
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U postgres"]
    interval: 5s
    timeout: 5s
    retries: 5

api:
  depends_on:
    db:
      condition: service_healthy
```

### build vs image

```yaml
# Build from Dockerfile in current directory
api:
  build:
    context: .
    dockerfile: Dockerfile

# Or use pre-built image
api:
  image: myregistry.com/my-api:v1.0
```

### Environment variables

```yaml
environment:
  APP_ENV: production
  DATABASE_URL: postgresql://postgres:secret@db:5432/myapp

# Or from file
env_file:
  - .env
```

### Port mapping

```yaml
ports:
  - "8000:8000"      # host:container
  - "127.0.0.1:8000:8000"  # bind to localhost only
```

### Volumes

```yaml
volumes:
  - pgdata:/var/lib/postgresql/data    # Named volume (persistent)
  - ./config.yml:/app/config.yml:ro    # Bind mount (host file, read-only)
```

---

## Essential Compose Commands

```bash
# Start all services in background
docker compose up -d

# Build images before starting
docker compose up -d --build

# View logs (all services)
docker compose logs -f

# Logs for one service
docker compose logs -f api

# List running services
docker compose ps

# Stop all (containers remain)
docker compose stop

# Stop and remove containers, networks
docker compose down

# Also remove volumes (⚠️ deletes database data)
docker compose down -v

# Run one-off command in a service
docker compose exec api python manage.py migrate
docker compose run api pytest   # New temporary container

# Validate compose file
docker compose config
```

---

## Multiple Compose Files (Dev vs Prod)

```bash
# docker-compose.yml — base
# docker-compose.override.yml — auto-loaded for local dev
# docker-compose.prod.yml — production overrides

docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

Example override for dev (hot reload):

```yaml
# docker-compose.override.yml
services:
  api:
    volumes:
      - ./src:/app/src    # Mount code for live reload
    command: python -m flask run --debug --host=0.0.0.0
```

---

## Full Stack Example (Preview)

```yaml
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/app
      REDIS_URL: redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d app"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7-alpine

volumes:
  pgdata:
```

---

## Compose vs Kubernetes

| | Docker Compose | Kubernetes |
|---|----------------|------------|
| **Scale** | Single host, dev/small prod | Multi-node clusters |
| **Use case** | Local dev, CI, small deployments | Production at scale |
| **Complexity** | Low | High |
| **Your path** | Week 1 | Week 4 |

**Interview line:** "I use Compose for local development and integration tests. Production workloads go to ECS or Kubernetes with similar service definitions."

---

## Check Your Understanding

1. Why can't the API use `localhost` to reach Postgres in Compose?
2. What does `depends_on` NOT guarantee?
3. What's the difference between `docker compose down` and `docker compose down -v`?
4. How do services find each other on the network?

<details>
<summary>Answers</summary>

1. `localhost` inside the API container is the API container itself. Postgres runs in a separate container with hostname `db` (the service name).
2. It doesn't guarantee the dependency is **ready** (e.g., Postgres accepting connections) — only that the container started. Use healthchecks + `condition: service_healthy`.
3. `down -v` also removes named volumes — **deletes database data**.
4. Docker's embedded DNS resolves service names to container IPs on the Compose network.

</details>

---

## Next Lesson

👉 **[Lesson 5: Networking and Volumes](05-networking-and-volumes.md)**

Then run **[Hands-on Example 4: Compose Stack](../02-hands-on/example-04-compose-stack/)**
