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

