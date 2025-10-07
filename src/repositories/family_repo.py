from database.connection import create_connection
from database.unit_of_work import UnitOfWork
class FamilyRepository:
    def get_family_and_attributes(self):
        with create_connection() as conn:
            with UnitOfWork(conn) as cur:
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

    def update_family_name(self, id_fam, new_name):
        with create_connection() as conn:
            with UnitOfWork(conn) as cur:
                query = f"""UPDATE familias SET "nombre" = %s WHERE id_familia = %s;"""
                cur.execute(query, (new_name, id_fam))
                print("update_family_name")

    def update_attribute_field(self, id_attr, field, new_val):
        with create_connection() as conn:
            with UnitOfWork(conn) as cur:
                query = f"""UPDATE atributos SET %s = %s WHERE id_atributo = %s;"""
                cur.execute(query, (field, new_val, id_attr))
                print("update_atribute_field")
