import os
from flask import Flask, render_template, request
from handlers import handle_file_upload, handle_load_image


app = Flask(__name__)


@app.route("/ping")
def ping():
    return "Pong!"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["formFile"]
        file_name = handle_file_upload(file)
        return f"File name: {file_name}"
    else:
        return render_template("index.html")


@app.route("/load/<file_id>")
def load_file(file_id):
    file_url = handle_load_image(file_id)
    return render_template("show.html", file_url=file_url)
