import os

from minio import Minio

MINIO_BUCKET_NAME = "qr-app"


minio_client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)


def create_bucket_if_not_exist():
    found = minio_client.bucket_exists(MINIO_BUCKET_NAME)
    if not found:
        minio_client.make_bucket(MINIO_BUCKET_NAME)


def upload_file(file, file_name):
    object_size = os.fstat(file.fileno()).st_size
    minio_client.put_object(
        MINIO_BUCKET_NAME,
        file_name,
        file,
        object_size,
    )


def load_file(file_name):
    stored_file = minio_client.get_object(MINIO_BUCKET_NAME, file_name)
    return stored_file


def get_minio_path(file_name):
    base_url = os.getenv("MINIO_ENDPOINT")
    return f"http://{base_url}/{MINIO_BUCKET_NAME}/{file_name}"
