from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "<p>Pong!</p>"

@app.route("/home")
def home():
    return render_template("index.html")
