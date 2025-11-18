from dataclasses import dataclass
from uuid import UUID

from ..value_objects.unidad import Unidad
from ..value_objects.tipo_dato import TipoDato

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
        
        # regla 1: Si el tipo_dato es OPCIONES, entonces si o si hay que ingresar opciones
        if self.tipo_dato == 'OPCIONES' and self.opciones is None:
            raise ValueError(f"El atributo '{self.nombre}' es de tipo OPCIONES pero no se pasaron opciones.")
        
        # regla 2: Si el tipo_dato no es OPCIONES, no se pueden ingresar opciones
        if self.tipo_dato != 'OPCIONES' and self.opciones is not None:
            raise ValueError(f"El atributo '{self.nombre}' no acepta 'opciones', porque no es de tipo OPCIONES.")
        
        # regla 3: Si el tipo_dato no es OPCIONES, debe tener unidad
        if self.tipo_dato != 'OPCIONES' and self.unidad is None:
            raise ValueError(f"El atributo '{self.nombre}' debe llevar unidad")
