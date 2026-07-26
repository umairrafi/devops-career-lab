# Exercise 01 — Fix the Broken Dockerfile

## Issues to find (don't read until you've tried!)

1. `host='127.0.0.1'` — must be `0.0.0.0`
2. `USER nobody` without `chown` — app.py not readable
3. `CMD python app.py` shell form — use exec form `CMD ["python", "app.py"]`
4. Missing HEALTHCHECK (bonus fix)
5. Use slim base image (bonus)

## Verify

```bash
docker build -t exercise-01 .
docker run -d -p 5000:5000 exercise-01
curl http://localhost:5000/health
```
