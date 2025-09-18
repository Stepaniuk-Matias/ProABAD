from database.connection import create_connection
import psycopg2

def select_family_and_atributes():
    conn = create_connection()
    cur = conn.cursor()
    query = """
            SELECT 
                f.id_familia,
                f.nombre AS familia,
                a.id_atributo,
                a.nombre_atributo,
                a.tipo_dato,
                a.unidad,
                a.es_obligatorio,
                a.orden
            FROM familias f
            LEFT JOIN atributos a 
                ON f.id_familia = a.id_familia
            ORDER BY f.nombre, a.orden;
            """
    cur.execute(query)
    rows = cur.fetchall()
    return rows