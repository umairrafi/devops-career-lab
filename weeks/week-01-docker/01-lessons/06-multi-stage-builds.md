# Lesson 6: Multi-Stage Builds and Optimization

**Reading time:** 20 minutes  
**After this lesson you'll understand:** How to build tiny, secure production images — especially for Go and compiled languages.

---

## The Problem: Bloated Images

A naive Go Dockerfile:

```dockerfile
FROM golang:1.22
WORKDIR /app
COPY . .
RUN go build -o server .
CMD ["./server"]
```

**Result:** Image ~800MB — includes entire Go toolchain, source code, build cache.

Production only needs the **compiled binary** (~10–20MB).

---

## Multi-Stage Build Solution

```dockerfile
# ── Stage 1: Build ──
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server .

# ── Stage 2: Runtime ──
FROM alpine:3.19
RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /app/server .
RUN adduser -D appuser
USER appuser
EXPOSE 8080
CMD ["./server"]
```

**Result:** Image ~15MB. Only the binary and minimal runtime land in the final image.

```
Stage builder (discarded)     Stage final (pushed/deployed)
┌─────────────────────┐      ┌─────────────────┐
│ golang toolchain    │      │ alpine + binary │
│ source code         │ ──▶  │ ~15 MB          │
│ ~800 MB             │ COPY │                 │
└─────────────────────┘      └─────────────────┘
```

---

## Python Multi-Stage (Optional Pattern)

Python is interpreted — multi-stage is less dramatic but still useful to exclude dev dependencies:

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

---

## Image Size Optimization Checklist

| Technique | Impact |
|-----------|--------|
| Use `alpine` or `slim` base | High |
| Multi-stage builds | High (compiled langs) |
| `--no-cache-dir` on pip | Medium |
| Combine RUN commands + clean apt cache | Medium |
| `.dockerignore` large dirs | Medium |
| Don't install dev/test deps in prod image | Medium |
| `ldflags="-s -w"` strip Go binary symbols | Low-Medium |

```bash
# Compare sizes
docker images | grep my-app
```

---

## Distroless Images (Advanced)

Google's **distroless** images contain only your app + runtime libs — no shell, no package manager.

```dockerfile
FROM golang:1.22-alpine AS builder
# ... build ...

FROM gcr.io/distroless/static-debian12
COPY --from=builder /app/server /
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

**Tradeoff:** Can't `docker exec` into shell for debugging. Use logging and sidecar debug containers instead.

---

## Build Arguments for Flexibility

```dockerfile
ARG GO_VERSION=1.22
FROM golang:${GO_VERSION}-alpine AS builder
ARG VERSION=dev
RUN go build -ldflags="-X main.version=${VERSION}" -o server .
```

```bash
docker build --build-arg VERSION=1.2.3 -t my-api:1.2.3 .
```

---

## Layer Caching Strategy (Recap)

Order Dockerfile instructions from **least changing** to **most changing**:

```dockerfile
FROM python:3.11-slim          # 1. Base — rarely changes
COPY requirements.txt .        # 2. Deps — changes sometimes
RUN pip install ...            # 3. Install — cached with requirements
COPY . .                       # 4. Code — changes every commit
```

---

## Interview Scenarios

**Q: "Your Docker image is 2GB. How do you reduce it?"**

A:
1. Check `docker history` to find large layers
2. Switch to slim/alpine base
3. Multi-stage build — exclude build tools
4. Review `.dockerignore`
5. Remove dev dependencies from production stage
6. Combine RUN layers and clean package caches

**Q: "Why CGO_ENABLED=0 for Go?"**

A: Produces statically linked binary with no C dependencies — can use `scratch` or minimal alpine base.

---

## Check Your Understanding

1. What gets discarded in a multi-stage build?
2. Why is the builder stage named with `AS builder`?
3. What does `COPY --from=builder` do?
4. When is multi-stage less beneficial?

<details>
<summary>Answers</summary>

1. All layers from non-final stages — only the last FROM stage becomes the image.
2. So later stages can reference it with `--from=builder`.
3. Copies files from a previous build stage into current stage.
4. Interpreted languages (Python/Node) where you still need the runtime — gains are smaller unless separating dev/prod deps.

</details>

---

## Hands-on

👉 **[Example 3: Multi-stage Go](../02-hands-on/example-03-multi-stage-go/)**

---

## Next Lesson

👉 **[Lesson 7: Security and Production](07-security-production.md)**
