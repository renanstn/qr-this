FROM minio/minio:latest

WORKDIR /data

COPY init_minio.sh .
RUN chmod +x init_minio.sh
EXPOSE 9000
EXPOSE 9001

ENTRYPOINT ["./init_minio.sh"]
