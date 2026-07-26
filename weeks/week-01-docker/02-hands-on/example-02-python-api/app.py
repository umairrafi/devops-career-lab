from flask import Flask, jsonify
import os

app = Flask(__name__)

ITEMS = [
    {"id": 1, "name": "Learn Docker"},
    {"id": 2, "name": "Build TaskFlow"},
]


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "env": os.getenv("APP_ENV", "production"),
    })


@app.route("/api/items")
def list_items():
    return jsonify({"items": ITEMS})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
