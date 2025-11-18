from dataclasses import dataclass, field
from uuid import UUID
from .atributo import Atributo

@dataclass
class Familia:
    id: UUID
    nombre: str
    atributos: list[Atributo] = field(default_factory = list)

    def add_atributo(self, atributo: Atributo):
        if any(a.nombre == atributo.nombre for a in self.atributos):
            raise ValueError(f"Atributo '{atributo.nombre}' duplicado en familia '{self.nombre}'")
        self.atributos.append(atributo)