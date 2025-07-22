import os
import uuid
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from bucket import (
    MINIO_BUCKET_NAME,
    minio_client,
    create_bucket_if_not_exist,
    upload_file,
    get_minio_path,
)
from database import connection_pool, insert_file


app = Flask(__name__)


@app.route("/ping")
def ping():
    return "<p>Pong!</p>"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file_id = uuid.uuid4()
        file_name_id = uuid.uuid4().hex
        file = request.files["formFile"]
        original_filename = secure_filename(file.filename)
        _, ext = os.path.splitext(original_filename)
        file_name = f"{file_name_id}{ext}"
        create_bucket_if_not_exist()
        upload_file(file, file_name)
        connection = connection_pool.getconn()
        try:
            with connection.cursor() as cursor:
                insert_file(cursor, file_id, file_name)
                connection.commit()
        finally:
            connection_pool.putconn(connection)
        return f"File name: {file_name}"
    else:
        return render_template("index.html")


@app.route("/load/<file_id>")
def load_file(file_id):
    file_url = get_minio_path(file_id)
    return render_template("show.html", file_url=file_url)
