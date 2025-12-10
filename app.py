from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face model
sentiment = pipeline("sentiment-analysis")

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    result = sentiment(text)[0]
    return jsonify({
        "text": text,
        "label": result["label"],
        "score": float(result["score"])
    })

@app.route("/", methods=["GET"])
def home():
    return "Sentiment Analysis API is running!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face model
sentiment = pipeline("sentiment-analysis")

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    result = sentiment(text)[0]
    return jsonify({
        "text": text,
        "label": result["label"],
        "score": float(result["score"])
    })

@app.route("/", methods=["GET"])
def home():
    return "Sentiment Analysis API is running!"

if __name__ == "__main__":
    app.run(debug=True)

