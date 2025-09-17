import psycopg2

#TODO: pasar config a un archivo .txt

config = {
    'host': 'localhost',
    'database': 'recipes_db',
    'user': 'postgres',
    'password': '1234',
}

def create_connection():
    """Establece y devuelve una conexión a la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(**config)
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    return conn