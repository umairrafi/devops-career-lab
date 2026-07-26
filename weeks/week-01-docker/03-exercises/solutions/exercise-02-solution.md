# Solution: Exercise 02 — Image Optimization

## Changes made

| Change | Size impact |
|--------|-------------|
| `python:3.11-slim` instead of full | ~800MB → ~150MB base |
| Remove build-essential, vim, git | Major savings |
| Combine apt RUN + cleanup | Fewer layers |
| Add .dockerignore (exclude tests, docs) | Smaller context |
| `pip install --no-cache-dir` | No pip cache in layer |
| Copy requirements before app | Better cache (not size, but best practice) |

## Optimized Dockerfile

```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
```

## .dockerignore

```
.git
tests/
docs/
*.md
Dockerfile.bloated
__pycache__
```

## Expected result

~120-180MB depending on platform.
