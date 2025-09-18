import psycopg2

#TODO: pasar config a un archivo .txt

config = {
    'host': '192.168.20.6',
    'database': 'proabad_app',
    'user': 'postgres',
    'password': 'Proabad1213',
}

def create_connection():
    """Establece y devuelve una conexión a la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(**config)
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    return conn