import numpy as np
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def api_verify():
  return "API ONLINE v1.0", 200

@app.route('/test', methods=['GET'])
def test():
  response = {"x": np.random.randint(100), "y": np.random.randint(100)}
  return jsonify(response), 200


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)