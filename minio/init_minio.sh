#!/bin/sh

set -e
minio server /data --console-address ":9001" &
MINIO_PID=$!
sleep 10

mc alias set local http://localhost:9000 "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD"
mc mb --ignore-existing local/qr-app
mc anonymous set download local/qr-app

wait $MINIO_PID
