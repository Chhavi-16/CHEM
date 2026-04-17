from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # ✅ check if JSON is sent
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # ✅ check if smiles exists
        smiles = data.get("smiles")
        if not smiles:
            return jsonify({"error": "Missing 'smiles'"}), 400

        # 🔥 replace this later with your real model
        prediction = f"Predicted value for {smiles}"

        return jsonify({
            "input": smiles,
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ IMPORTANT for Render (port binding)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
