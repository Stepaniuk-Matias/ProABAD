from connection import create_connection

familias = [
    {
        "nombre": "Ruedas",
        "atributos": [
            {"nombre_atributo": "Diámetro", "tipo_dato": "float", "unidad": "mm", "es_obligatorio": True, "orden": 1},
            {"nombre_atributo": "Ancho", "tipo_dato": "float", "unidad": "mm", "es_obligatorio": True, "orden": 2}
        ]
    },
    {
        "nombre": "Ejes de polea",
        "atributos": [
            {"nombre_atributo": "Diámetro", "tipo_dato": "float", "unidad": "mm", "es_obligatorio": True, "orden": 1},
            {"nombre_atributo": "Largo", "tipo_dato": "float", "unidad": "mm", "es_obligatorio": True, "orden": 2}
        ]
    }
]

conn = create_connection()
cursor = conn.cursor()

for familia in familias:
    cursor.execute(
        "INSERT INTO familias (nombre) VALUES (%s) RETURNING id_familia;",
        (familia["nombre"],)
    )
    id_familia = cursor.fetchone()[0]
    for atributo in familia["atributos"]:
        cursor.execute(
            """
            INSERT INTO atributos (id_familia, nombre_atributo, tipo_dato, unidad, es_obligatorio, orden)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                id_familia, 
                atributo["nombre_atributo"], 
                atributo["tipo_dato"],
                atributo["unidad"],
                atributo["es_obligatorio"], 
                atributo["orden"]
            )
        )

conn.commit()
conn.close()