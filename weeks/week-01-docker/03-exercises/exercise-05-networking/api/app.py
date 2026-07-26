from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# BUG: localhost should be the service name
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:secret@localhost:5432/appdb")

@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return jsonify({"status": "healthy", "db": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "db": str(e)}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
