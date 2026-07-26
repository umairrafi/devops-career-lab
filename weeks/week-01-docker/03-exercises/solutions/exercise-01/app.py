from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "env": os.getenv("APP_ENV", "unknown")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
