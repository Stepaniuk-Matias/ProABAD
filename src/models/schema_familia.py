from typing import List

class Atributo:
    def __init__(self, id_atributo: int, id_familia: int, nombre: str, tipo: str,
                 unidad: str, es_obligatorio: bool, orden: int, opciones: List[str] = None):
        self.id_atributo = id_atributo
        self.id_familia = id_familia
        self.nombre = nombre
        self.tipo = tipo
        self.unidad = unidad
        self.es_obligatorio = es_obligatorio
        self.orden = orden
        self.opciones = opciones or []

class Familia:
    def __init__(self, id_familia: int, nombre: str, atributos: List[Atributo] = None):
        self.id_familia = id_familia
        self.nombre = nombre
        self.atributos = atributos or []
