from flask import Flask, render_template, request
import ai_logic as ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def chat():
    userInput = request.form["userInput"]
    AIOutput = ai.get_ai_response(userInput)
    return render_template("index.html", aiOutput=AIOutput)

if __name__ == "__main__":
    app.run(debug=True)