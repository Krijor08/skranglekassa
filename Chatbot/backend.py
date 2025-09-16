from flask import Flask, jsonify, request
from flask_cors import CORS
import ai_logic as ai

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    userInput = data.get("userInput", "")

    if not userInput:
        return jsonify({"error": "No input provided"}), 400
    AIOutput = ai.get_ai_response(userInput)
    return jsonify({"aiOutput": AIOutput})

if __name__ == "__main__":
    app.run(port="5000", debug=True)