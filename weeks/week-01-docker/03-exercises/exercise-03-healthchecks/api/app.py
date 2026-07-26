from flask import Flask, jsonify
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/health")
def health():
    uptime = time.time() - start_time
    return jsonify({"status": "healthy", "uptime_seconds": round(uptime, 1)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
