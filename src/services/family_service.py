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
        # 🔸 Ejemplo de regla de negocio: ordenar por nombre
        familias.sort(key=lambda f: f.nombre.lower())
        return familias

    # -----------------------------
    # Métodos de escritura
    # -----------------------------
    def renombrar_familia(self, id_fam: int, nuevo_nombre: str):
        """
        Valida el nombre y actualiza la familia.
        """
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la familia no puede estar vacío.")

        # Ejemplo: Evitar nombres duplicados en memoria
        familias = self.repository.get_all()
        if any(f.nombre.lower() == nuevo_nombre.lower() for f in familias):
            raise ValueError(f"Ya existe una familia llamada '{nuevo_nombre}'.")

        self.repository.update_family_name(id_fam, nuevo_nombre)

    def actualizar_atributo(self, id_attr: int, campo: str, nuevo_valor):
        """
        Actualiza un campo específico del atributo.
        Se puede incluir lógica adicional de validación.
        """
        # 🔸 Validaciones de negocio
        if campo == "tipo_dato" and nuevo_valor not in ["int", "float", "bool", "list"]:
            raise ValueError(f"Tipo de dato '{nuevo_valor}' no permitido.")
        if campo == "unidad" and len(nuevo_valor) > 10:
            raise ValueError("Unidad demasiado larga (máx. 10 caracteres).")

        self.repository.update_attribute_field(id_attr, campo, nuevo_valor)

    def load_tree_data(self):
        familias = self.repository.get_all()
        return familias

    def update_attribute(self, id_attr, field, new_val):
        self.repository.update_attribute_field(id_attr, field, new_val)

    def update_family(self, id_fam, new_name):
        self.repository.update_family_name(id_fam, new_name)

    def load_familias(self):
        rows = self.repository.get_all()
        familias_dict = {}

        for r in rows:
            id_fam, nombre_fam, id_attr, nom_attr, tipo, unidad, obligatorio, orden, opciones = r

            if id_fam not in familias_dict:
                familias_dict[id_fam] = Familia(id_fam, nombre_fam, [])

            if id_attr:
                atributo = Atributo(
                    id_atributo=id_attr,
                    id_familia=id_fam,
                    nombre=nom_attr,
                    tipo=tipo,
                    unidad=unidad,
                    es_obligatorio=obligatorio,
                    orden=orden,
                    opciones=opciones or []
                )
                familias_dict[id_fam].atributos.append(atributo)

        return list(familias_dict.values())
    