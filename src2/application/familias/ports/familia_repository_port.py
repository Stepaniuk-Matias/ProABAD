from abc import ABC, abstractmethod
from uuid import UUID
from domain.familias.entities.familia import Familia
from domain.familias.entities.atributo import Atributo

class IFamiliaRepository(ABC):

    @abstractmethod
    def _row_to_familia(self, row) -> Familia:
        pass

    @abstractmethod
    def create(self, familia: Familia) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Familia | None:
        pass

    @abstractmethod
    def list_all(self) -> list[Familia]:
        pass

    @abstractmethod
    def update(self, id: UUID) -> Familia:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass

    @abstractmethod
    def get_atributos(self, id: UUID) -> list[Atributo]:
        pass
