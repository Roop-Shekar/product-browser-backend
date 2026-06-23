import os

from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

load_dotenv()

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    sslmode="require"
)


def get_connection():
    return pool.getconn()


def release_connection(conn):
    pool.putconn(conn)