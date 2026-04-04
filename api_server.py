from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome API"

@app.route("/data")
def data():
    return jsonify({"name": "Python", "level": "Medium"})

if __name__ == "__main__":
    app.run(debug=True)
