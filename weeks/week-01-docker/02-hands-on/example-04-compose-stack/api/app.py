from flask import Flask, jsonify, request
import os
import time
import psycopg2
import redis

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:secret@db:5432/appdb")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


def get_db():
    return psycopg2.connect(DATABASE_URL)


def get_redis():
    return redis.from_url(REDIS_URL)


def wait_for_db(max_retries=30, delay=2):
    for i in range(max_retries):
        try:
            conn = get_db()
            conn.close()
            print(f"Database ready after {i + 1} attempt(s)")
            return True
        except Exception as e:
            print(f"Waiting for database... ({i + 1}/{max_retries}): {e}")
            time.sleep(delay)
    return False


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.route("/health")
def health():
    status = {"status": "healthy", "db": "unknown", "redis": "unknown"}
    try:
        conn = get_db()
        conn.close()
        status["db"] = "healthy"
    except Exception:
        status["db"] = "unhealthy"
        status["status"] = "degraded"

    try:
        get_redis().ping()
        status["redis"] = "healthy"
    except Exception:
        status["redis"] = "unhealthy"
        status["status"] = "degraded"

    code = 200 if status["status"] == "healthy" else 503
    return jsonify(status), code


@app.route("/api/counter")
def counter():
    r = get_redis()
    count = r.incr("page_views")
    return jsonify({"count": count})


@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, created_at FROM tasks ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    tasks = [{"id": r[0], "title": r[1], "created_at": r[2].isoformat()} for r in rows]
    return jsonify({"tasks": tasks})


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "title required"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s) RETURNING id", (title,))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": task_id, "title": title}), 201


if __name__ == "__main__":
    if wait_for_db():
        init_db()
        app.run(host="0.0.0.0", port=8000)
    else:
        print("Failed to connect to database. Exiting.")
        exit(1)
