from typing import List
from PySide6.QtCore import Qt

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

    def get_families(self) -> List[Familia]:
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

    def update_attribute_from_ui(self, id_attr: int, col: int, idx):
        """
        Recibe un cambio en una celda del modelo (columna, índice Qt)
        y se encarga de traducirlo a un campo y valor válido.
        """
        field_map = {0: 'nombre_atributo', 1: 'tipo_dato', 2: 'unidad', 3: 'es_obligatorio'}
        field = field_map.get(col)

        new_val = idx.data(Qt.EditRole) if col != 3 else (idx.data(Qt.CheckStateRole) == Qt.Checked)

        if field == "tipo_dato" and new_val not in ["int", "float", "bool", "list"]:
            raise ValueError(f"Tipo de dato '{new_val}' no permitido.")
        if field:
            self.repository.update_attribute_field(id_attr, field, new_val)
