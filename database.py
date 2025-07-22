import os
from psycopg2 import pool

DATABASE_URL = os.getenv("DATABASE_URL")
connection_pool = pool.SimpleConnectionPool(
    minconn=1, maxconn=10, dsn=DATABASE_URL
)


def insert_file(cursor, file_id, file_name):
    cursor.execute(
        "INSERT INTO qr_links (id, filename) VALUES (%s, %s)",
        (str(file_id), file_name),
    )
