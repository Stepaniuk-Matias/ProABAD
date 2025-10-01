from database.connection import create_connection
import psycopg2

# class QueryExecuter():
#     def __init__(self, query):
#         self.query = query
#     try:
#         conn = create_connection()
#         cur = conn.cursor()
#         cur.execute(self.query)
#     except Exception as e:
#         print("Error con la db ", e)

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
                a.orden AS orden_atributo,
                a.opciones_atributos
            FROM familias f
            LEFT JOIN atributos a
                ON f.id_familia = a.id_familia
            """
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def update_family_name(id, new_name):
    with create_connection() as conn:
        cur = conn.cursor()
        query = f"""UPDATE familias SET "nombre" = '{new_name}' WHERE id_familia = {id};"""
        cur.execute(query)
        print("update_family_name")
        cur.close()

def update_attribute_field(id, field, value):
    with create_connection() as conn:
        cur = conn.cursor()
        query = f"""UPDATE atributos SET "{field}" = '{value}' WHERE id_atributo = {id};"""
        cur.execute(query)
        print("update_atribute_field")
        cur.close()
