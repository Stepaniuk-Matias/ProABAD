import sqlite3

familias = [
    {
        "nombre": "Ruedas",
        "atributos": [
            {"nombre_atributo": "Diámetro", "tipo_dato": "REAL", "obligatorio": 1, "orden": 1},
            {"nombre_atributo": "Ancho", "tipo_dato": "REAL", "obligatorio": 1, "orden": 2}
        ]
    },
    {
        "nombre": "Ejes de polea",
        "atributos": [
            {"nombre_atributo": "Diámetro", "tipo_dato": "REAL", "obligatorio": 1, "orden": 1},
            {"nombre_atributo": "Largo", "tipo_dato": "REAL", "obligatorio": 1, "orden": 2}
        ]
    }
]

conn = sqlite3.connect(r".\src\database\ProABAD_test.db")
cursor = conn.cursor()

for familia in familias:
    cursor.execute("INSERT INTO Familia (nombre) VALUES (?)", (familia["nombre"],))
    id_familia = cursor.lastrowid
    for atributo in familia["atributos"]:
        cursor.execute(
            "INSERT INTO Atributo (id_familia, nombre_atributo, tipo_dato, obligatorio, orden) VALUES (?, ?, ?, ?, ?)",
            (id_familia, atributo["nombre_atributo"], atributo["tipo_dato"], atributo["obligatorio"], atributo["orden"])
        )

conn.commit()
conn.close()