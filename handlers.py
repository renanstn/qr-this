import os
import uuid
from io import BytesIO

import qrcode
from flask import request
from werkzeug.utils import secure_filename

from bucket import create_bucket_if_not_exist, get_minio_path, upload_file


def handle_file_upload(file):
    file_id = uuid.uuid4()
    file_name_id = uuid.uuid4().hex
    original_filename = secure_filename(file.filename)
    _, ext = os.path.splitext(original_filename)
    file_name = f"{file_name_id}{ext}"
    create_bucket_if_not_exist()
    upload_file(file, file_name)
    return file_name


def handle_load_image(file_id):
    file_url = get_minio_path(file_id)
    return file_url


def handle_qr_code_generation(file_name):
    link = f"{request.url_root}show/{file_name}"
    image = qrcode.make(link)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
