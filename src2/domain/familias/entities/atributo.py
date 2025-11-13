from dataclasses import dataclass
from uuid import UUID

from value_objects.unidad import Unidad
from value_objects.tipo_dato import TipoDato

@dataclass
class Atributo:
    id: UUID
    nombre: str
    tipo_dato: TipoDato
    unidad: Unidad
    es_obligatorio: bool
    orden: int
    opciones: list[str] | None = None

    def __post_init__(self):
        if self.tipo_dato.name == 'OPCIONES' and self.opciones is None:
            raise ValueError("Si el atributo es tipo opción, debe ingresar por lo menos una opción")
        
        if self.tipo_dato.name != 'OPCIONES' and self.opciones is not None:
            raise ValueError("No se pueden ingresar opciones si el atributo no es de tipo opción")

        if self.tipo_dato.name != 'OPCIONES' and self.unidad is None:
            raise ValueError("Falta unidad")
