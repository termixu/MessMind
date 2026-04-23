from flask import Flask, request, jsonify
import torch
import io

app = Flask(__name__)
node = None  # будет проставлен при инициализации

@app.route('/weights', methods=['POST'])
def receive_weights():
    data = request.get_json()
    weights = torch.load(io.BytesIO(bytes(data['weights'])))
    node.received_weights.append(weights)
    return jsonify({"status": "ok"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "alive", "round": node.round})
