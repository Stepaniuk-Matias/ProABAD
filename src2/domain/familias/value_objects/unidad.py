from dataclasses import dataclass

@dataclass(frozen=True)
class Unidad:
    nombre: str

    def __post_init__(self):
        if not self.nombre or not self.nombre.strip():
            raise ValueError("La unidad no puede estar vacía")

    def __str__(self):
        return self.nombre
