from fastapi import FastAPI, Request
from database import get_connection
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/escritoras")
def obtener_escritoras(
    nombre: str | None = None, 
    apellidos: str | None = None, 
    pais_nacimiento: str | None = None, 
):
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        sql = "SELECT * FROM escritoras WHERE 1=1"
        parametros = []

        if nombre:
            sql += " AND nombre = %s"
            parametros.append(nombre)

        if apellidos:
            sql += " AND apellidos = %s"
            parametros.append(apellidos)   
        
        if pais_nacimiento:
            sql += " AND pais_nacimiento = %s"
            parametros.append(pais_nacimiento)
        
        cursor.execute(sql,parametros)
        escritoras = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return escritoras
        
    except Exception as e:
        return {"error": f"No se pudieron obtener las escritoras: {str(e)}"}

@app.get("/libros")
def obtener_libros(
    titulo: str | None = None, 
    genero: str | None = None, 
    anio_publicacion: str | None = None):
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        sql = "SELECT * FROM libros WHERE 1=1"
        parametros = []
        
        if titulo:
            sql += " AND titulo = %s"
            parametros.append(titulo)


        if genero:
            sql += " AND genero = %s"
            parametros.append(genero)
        
        if anio_publicacion:
            sql += " AND anio_publicacion = %s"
            parametros.append(anio_publicacion)

        
        cursor.execute(sql,parametros)
        libros = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return libros
        
    except Exception as e:
        print(f"Error en SQL: {e}")
        return {"error": f"No se pudieron obtener los libros: {str(e)}"}

@app.get("/frases")
def obtener_frases():
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        sql = """
            SELECT * 
            FROM frases
        """
        
        cursor.execute(sql)
        frases = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return frases
        
    except Exception as e:
        return {"error": f"No se pudieron obtener las frases: {str(e)}"}

@app.get("/premios")
def obtener_premios():
    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        sql = """
            SELECT * 
            FROM premios
        """
        
        cursor.execute(sql)
        premios = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return premios
        
    except Exception as e:
        return {"error": f"No se pudieron obtener los premios: {str(e)}"}

