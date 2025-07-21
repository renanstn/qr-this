from flask import Flask, render_template, request
from bucket import (
    MINIO_BUCKET_NAME,
    minio_client,
    create_bucket_if_not_exist,
    upload_file,
    get_minio_path,
)


app = Flask(__name__)


@app.route("/ping")
def ping():
    return "<p>Pong!</p>"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["formFile"]
        create_bucket_if_not_exist()
        upload_file(file)
        return "<p>Image uploaded!</p>"
    else:
        return render_template("index.html")
