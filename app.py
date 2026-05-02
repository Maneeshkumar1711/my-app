import os
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Azure 🚀"})

@app.route("/health")
def health():
    return "OK", 200

# Only for local development
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)