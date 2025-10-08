from abc import ABC, abstractmethod
from typing import List
from database.connection import create_connection
from database.unit_of_work import UnitOfWork
from models.schema_familia import Familia, Atributo

class IFamilyRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Familia]:
        pass

    @abstractmethod
    def update_family_name(self, id_fam: int, new_name: str) -> None:
        pass

    @abstractmethod
    def update_attribute_field(self, id_attr: int, field: str, new_val) -> None:
        pass

class FamilyRepository(IFamilyRepository):
    def __init__(self, connection, mapper):
        self.connection = connection
        self.mapper = mapper


    def get_all(self) -> List[Familia]:
        with self.connection() as conn:
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
                return self.mapper.map_rows_to_objects(rows)

    def update_family_name(self, id_fam, new_name):
        with self.connection() as conn:
            with UnitOfWork(conn) as cur:
                query = f"""UPDATE familias SET "nombre" = %s WHERE id_familia = %s;"""
                cur.execute(query, (new_name, id_fam))

    def update_attribute_field(self, id_attr, field, new_val):

        allowed_fields = {"nombre_atributo", "tipo_dato", "unidad", "es_obligatorio", "orden", "opciones_atributos"}
        if field not in allowed_fields:
            raise ValueError(f"Campo no permitido: {field}")

        with self.connection() as conn:
            with UnitOfWork(conn) as cur:
                query = f"""UPDATE atributos SET {field} = %s WHERE id_atributo = %s;"""
                cur.execute(query, (new_val, id_attr))
