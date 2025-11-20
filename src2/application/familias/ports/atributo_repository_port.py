from abc import ABC, abstractmethod
from domain.familias.entities.atributo import Atributo

class IAtributoRepositoryPort(ABC):
    
    @abstractmethod
    def save(self, atributo: Atributo) -> Atributo:
        pass

    @abstractmethod
    def update(self, id: str, field: str, new_value) -> None:
        pass