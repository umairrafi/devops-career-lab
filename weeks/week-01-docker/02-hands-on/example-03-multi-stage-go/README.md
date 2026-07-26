# Hands-on Example 3: Multi-Stage Go Build

**Time:** 45 minutes  
**Goal:** Build a tiny production Go image using multi-stage builds — directly applies to your Go Lambda background.

---

## What You'll Build

A minimal HTTP API in Go, compiled in a builder stage, copied to a ~15MB Alpine runtime image.

---

## Step 1: Review the Code

```
example-03-multi-stage-go/
├── Dockerfile
├── go.mod
├── main.go
└── README.md
```

`main.go` — simple HTTP server with `/health` and `/api/time`.

---

## Step 2: Build Single-Stage (Compare Size)

First, see the problem. Create a temp Dockerfile:

```dockerfile
# Dockerfile.single — DO NOT USE IN PROD, for learning only
FROM golang:1.22-alpine
WORKDIR /app
COPY . .
RUN go build -o server .
CMD ["./server"]
```

```bash
docker build -f Dockerfile.single -t go-api:single .
docker images go-api:single
# ~300-400MB
```

---

## Step 3: Build Multi-Stage (Production)

```bash
docker build -t go-api:1.0 .
docker images go-api:1.0
# ~15-20MB
```

Compare:
```bash
docker images | grep go-api
```

---

## Step 4: Run and Test

```bash
docker run -d -p 8080:8080 --name go-api go-api:1.0

curl http://localhost:8080/health
curl http://localhost:8080/api/time
```

---

## Step 5: Inspect Layers

```bash
docker history go-api:1.0
docker history go-api:single
```

Notice builder stage layers don't appear in final image.

---

## Step 6: Verify Non-Root

```bash
docker exec go-api whoami   # appuser
```

---

## Step 7: Clean Up

```bash
docker stop go-api && docker rm go-api
docker rmi go-api:single go-api:1.0
```

---

## Key Takeaways for Interviews

1. Builder stage has Go toolchain; runtime only has binary
2. `CGO_ENABLED=0` = static binary, no C deps
3. `-ldflags="-s -w"` strips debug symbols
4. `COPY --from=builder` pulls artifact from previous stage

---

## Experiment

1. Build with `FROM scratch` instead of alpine (remove ca-certificates need if no HTTPS)
2. Add build arg `VERSION` and pass at build time
3. Time builds: change only a comment in main.go — multi-stage cache behavior

---

## Next

👉 **[Example 4: Full Stack Compose](../example-04-compose-stack/README.md)**
