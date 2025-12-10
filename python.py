# app.py

from flask import Flask, request, jsonify
from transformers import pipeline

# ------------------------------
# Initialize Flask app
# ------------------------------
app = Flask(__name__)

# ------------------------------
# Load Hugging Face sentiment analysis model
# Explicitly specify model to avoid warnings
# ------------------------------
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)

# ------------------------------
# Health check endpoint
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    return "Sentiment Analysis API is running!"

# ------------------------------
# Main sentiment analysis endpoint
# ------------------------------
@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = sentiment_pipeline(text)[0]
        return jsonify({
            "text": text,
            "label": result["label"],
            "score": float(result["score"])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------
# Run the app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)

