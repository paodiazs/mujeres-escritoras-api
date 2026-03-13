import os
import psycopg2
from psycopg2.extras import RealDictCursor # Para que devuelva diccionarios
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    # PostgreSQL usa 'dbname' en lugar de 'database'
    return psycopg2.connect(
        host=os.getenv("BD_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT", 5432) # Puerto por defecto de Postgres
    )