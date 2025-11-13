from dataclasses import dataclass, field
from uuid import UUID
from typing import List
from .atributo import Atributo

@dataclass
class Familia:
    id: UUID
    name: str
    attributes: List[Atributo] = field(default_factory = True)

    def add_atributo(self, atributo: Atributo):
        if any(a.nombre == atributo.nombre for a in self.atributos):
            raise ValueError(f"Atributo '{atributo.nombre}' duplicado en familia '{self.nombre}'")
        self.atributos.append(atributo)

