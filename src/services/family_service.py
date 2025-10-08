from typing import List

from models.schema_familia import Familia, Atributo
from repositories.family_repo import IFamilyRepository
class FamilyService:
    """
    Capa de negocio para manejar Familias y Atributos.
    Orquesta el flujo de datos entre UI/controlador y el repositorio.
    """

    def __init__(self, repository: IFamilyRepository):
        # Inyección de dependencia
        self.repository = repository

    # -----------------------------
    # Métodos de lectura
    # -----------------------------

    def obtener_familias(self) -> List[Familia]:
        """
        Devuelve una lista de objetos Family con sus atributos.
        """
        familias = self.repository.get_all()
        # ordenar por nombre:
        familias.sort(key=lambda f: f.nombre.lower())
        return familias

    # -----------------------------
    # Métodos de escritura
    # -----------------------------

    def update_family(self, id_fam, new_name):
        """
        Valida el nombre y actualiza la familia.
        """
        if not new_name.strip():
            raise ValueError("El nombre de la familia no puede estar vacío.")

        # Evitar nombres duplicados en memoria:
        familias = self.repository.get_all()
        if any(f.nombre.lower() == new_name.lower() for f in familias):
            raise ValueError(f"Ya existe una familia llamada '{new_name}'.")
        
        self.repository.update_family_name(id_fam, new_name)

    def update_attribute(self, id_attr: int, field: str, new_val):
        """
        Actualiza un field específico del atributo.
        Se puede incluir lógica adicional de validación.
        """
        # Validaciones de negocio
        if field == "tipo_dato" and new_val not in ["int", "float", "bool", "list"]:
            raise ValueError(f"Tipo de dato '{new_val}' no permitido.")
        if field == "unidad" and len(new_val) > 10:
            raise ValueError("Unidad demasiado larga (máx. 10 caracteres).")

        self.repository.update_attribute_field(id_attr, field, new_val)