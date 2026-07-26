# Hands-on Example 1: Hello World

**Time:** 15 minutes  
**Goal:** Run your first custom Docker image and learn basic commands.

---

## What You'll Do

1. Write a minimal Dockerfile
2. Build an image
3. Run a container
4. Inspect and clean up

---

## Step 1: Create the Dockerfile

Already provided in this folder:

```dockerfile
FROM alpine:3.19
CMD ["echo", "Hello from Docker! My first custom image."]
```

**What each line does:**
- `FROM alpine:3.19` — Start from tiny Linux (~7MB)
- `CMD [...]` — Run echo when container starts

---

## Step 2: Build the Image

```bash
cd weeks/week-01-docker/02-hands-on/example-01-hello-world

docker build -t hello-docker:1.0 .
```

Expected output ends with:
```
Successfully tagged hello-docker:1.0
```

```bash
docker images hello-docker
# REPOSITORY     TAG   IMAGE ID       CREATED          SIZE
# hello-docker   1.0   abc123...      2 seconds ago    7.5MB
```

---

## Step 3: Run the Container

```bash
docker run hello-docker:1.0
# Output: Hello from Docker! My first custom image.
```

Container runs, prints message, exits. Check:

```bash
docker ps -a | head -5
# STATUS: Exited (0) — exit code 0 = success
```

---

## Step 4: Override the Command

CMD is overridable:

```bash
docker run hello-docker:1.0 echo "I overridden the CMD!"
docker run -it hello-docker:1.0 /bin/sh
# Inside shell:
/ # cat /etc/os-release
/ # exit
```

---

## Step 5: Inspect

```bash
docker history hello-docker:1.0
docker inspect hello-docker:1.0
```

---

## Step 6: Clean Up

```bash
docker rm $(docker ps -aq --filter ancestor=hello-docker:1.0)
docker rmi hello-docker:1.0
```

---

## Experiment (Do This)

1. Change `alpine:3.19` to `ubuntu:22.04` — rebuild. How does image size change?
2. Add `LABEL author="your-name"` — rebuild and `docker inspect`
3. Add a `RUN apk add curl` before CMD — what happens to image size?

---

## What You Learned

- `docker build -t name:tag .`
- `docker run` creates and starts a container
- CMD is the default process
- Images have layers (`docker history`)

---

## Next

👉 **[Example 2: Python Flask API](../example-02-python-api/README.md)**
