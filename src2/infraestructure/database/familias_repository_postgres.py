from domain.familias.entities.familia import Familia
from domain.familias.entities.atributo import Atributo
from domain.familias.value_objects.tipo_dato import TipoDato
from domain.familias.value_objects.unidad import Unidad
from application.familias.ports.familia_repository_port import IFamiliaRepository

class FamiliaRepositoryPostgres(IFamiliaRepository):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def _row_to_familia(self, row):
        if row is None:
            return None
        id, nombre, atributos = row
        return Familia(id, nombre, atributos)
        

    def save(self, familia:Familia):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO familias (nombre)
                VALUES (%s)
                RETURNING id_familia
            """, (familia.nombre,))
        new_id = cur.fetchone()[0]
        self.conn.commit()
        return new_id

    def get_by_id(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id_familia, nombre, atributos
                FROM familias
                WHERE id_familia = %s
            """, (id,))
            row = cur.fetchone()
        return self._row_to_familia(row)
    
    def list_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
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
            """)
            rows = cur.fetchall()
        familias = [self._row_to_familia(row) for row in rows]
        return familias
    
    def update(self, id):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE familias SET nombre")

