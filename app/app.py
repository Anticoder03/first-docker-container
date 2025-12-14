from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/journey")
def journey():
    return render_template("journey.html")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/health-ui")
def health_ui():
    return render_template("health.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
