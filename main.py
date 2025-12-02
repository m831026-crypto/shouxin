import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "shouxin backend running"

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 5000))
    except:
        port = 5000
    app.run(host="0.0.0.0", port=port)
