from flask import Flask

app = Flask(__name__)

@app.route('/')
def chat():
    import ai_logic as ai
    return ai.output

if __name__ == '__main__':
    app.run(debug=True) 