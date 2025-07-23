#!/bin/sh
set -e

sleep 5

mc alias set local http://localhost:9000 "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD"
mc mb --ignore-existing local/qr-app
mc anonymous set download local/qr-app

exec minio server /data --console-address ":9001"
