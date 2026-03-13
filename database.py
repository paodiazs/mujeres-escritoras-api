import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    url = os.getenv("DATABASE_URL")
    
    if url:
        return psycopg2.connect(url)
    else:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
