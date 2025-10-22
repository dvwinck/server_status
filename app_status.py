#!/usr/bin/env python3
import os
import socket
import platform
import datetime
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Helpers
def now_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Endpoints
@app.route("/", methods=["GET"])
def root_forbidden():
    return Response("Forbidden", status=403, mimetype="text/plain")

@app.route("/health", methods=["GET"])
def health():
    return Response("OK!", status=200, mimetype="text/plain")

@app.route("/info", methods=["GET"])
def info():
    data = {
        "hostname": socket.gethostname(),
        "sistema": platform.system(),
        "versao_python": platform.python_version(),
        "data_hora": now_str(),
    }
    return jsonify(data), 200

# Main
if __name__ == "__main__":
    port = int(os.getenv("PORT", "8081"))
    app.run(host="0.0.0.0", port=port)
