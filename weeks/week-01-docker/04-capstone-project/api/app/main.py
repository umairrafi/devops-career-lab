from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
import os
import redis

from app.database import engine, get_db, Base
from app.routes import tasks, projects

app = FastAPI(
    title="TaskFlow API",
    description="Week 1 Docker Capstone — Task Management Platform",
    version="1.0.0",
)

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


def get_redis():
    return redis.from_url(REDIS_URL, decode_responses=True)


@app.get("/health")
def health(db: Session = Depends(get_db)):
    status = {
        "status": "healthy",
        "service": "taskflow-api",
        "env": os.getenv("APP_ENV", "unknown"),
        "db": "unknown",
        "redis": "unknown",
    }

    try:
        db.execute(text("SELECT 1"))
        status["db"] = "healthy"
    except Exception as e:
        status["db"] = f"unhealthy: {e}"
        status["status"] = "degraded"

    try:
        get_redis().ping()
        status["redis"] = "healthy"
    except Exception as e:
        status["redis"] = f"unhealthy: {e}"
        status["status"] = "degraded"

    if status["status"] != "healthy":
        from fastapi.responses import JSONResponse
        return JSONResponse(content=status, status_code=503)
    return status


@app.get("/api/stats")
def stats(db: Session = Depends(get_db)):
    r = get_redis()
    cache_key = "taskflow:stats"

    cached = r.get(cache_key)
    if cached:
        import json
        return {"source": "cache", **json.loads(cached)}

    from app.models import Task
    total = db.query(Task).count()
    todo = db.query(Task).filter(Task.status == "todo").count()
    done = db.query(Task).filter(Task.status == "done").count()

    result = {"total": total, "todo": todo, "done": done}
    import json
    r.setex(cache_key, 60, json.dumps(result))
    return {"source": "db", **result}


app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
