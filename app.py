from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "API running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = data["input"]
    prediction = model.predict([[value]])
    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
