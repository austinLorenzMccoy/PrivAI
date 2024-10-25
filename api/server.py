#server.py
from flask import Flask, request, jsonify
from train import train_model_with_dp
from infer import infer_with_gemini
from load_models import load_models

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    data = request.json['data']
    train_model_with_dp(data)
    return jsonify({"status": "Training started"})

@app.route('/infer', methods=['POST'])
def infer():
    image_data = request.json['image_data']
    result = infer_with_gemini(image_data)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

