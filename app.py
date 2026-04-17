from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    smiles = data.get("smiles")

    # TEMP (replace later with your model)
    return jsonify({"prediction": f"Predicted value for {smiles}"})
