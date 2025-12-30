from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_logs():
    start_time = time.time()
    data = request.json

    # Placeholder for Gemini analysis
    analysis_result = {
        "attack_type": "Brute Force",
        "severity": "High",
        "recommendation": "Block IP and rotate credentials"
    }

    latency = time.time() - start_time

    return jsonify({
        "analysis": analysis_result,
        "latency_seconds": latency
    })

if __name__ == "__main__":
    app.run()
