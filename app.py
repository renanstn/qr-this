import os

from flask import Flask, render_template, request, send_file, Response

from handlers import (
    handle_file_upload,
    handle_load_image,
    handle_qr_code_generation,
)
from bucket import load_file

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "Pong!"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["formFile"]
        file_name = handle_file_upload(file)
        qr_code = handle_qr_code_generation(file_name)
        return send_file(qr_code, mimetype="image/png")
    else:
        return render_template("index.html")


@app.route("/show/<file_id>")
def load_file(file_id):
    # file_url = handle_load_image(file_id)
    # return render_template("show.html", file_url=file_url)
    stored_file = load_file(file_id)
    return Response(stored_file, mimetype='image/png')
