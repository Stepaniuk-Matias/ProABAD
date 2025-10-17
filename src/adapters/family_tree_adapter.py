from PySide6.QtGui import QStandardItem, QColor
from PySide6.QtCore import Qt


class FamilyTreeAdapter:
    def __init__(self, tipos_validos):
        self.tipos_validos = tipos_validos

    # -----------------------------------------------------------------
    # Construcción del modelo a partir de entidades
    # -----------------------------------------------------------------
    def build_model(self, model, familias: list):
        familia_items = {}
        atributo_items = {}

        for familia in familias:
            # --- Familia ---
            familia_item = QStandardItem(familia.nombre)
            familia_item.setData(familia.id_familia, Qt.UserRole)
            familia_item.setFlags(familia_item.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
            model.appendRow([familia_item])
            familia_items[familia.id_familia] = familia_item

            # --- Atributos ---
            for atributo in familia.atributos:
                attr_nombre = QStandardItem(atributo.nombre)
                attr_nombre.setData(atributo.id_atributo, Qt.UserRole)
                attr_nombre.setFlags(attr_nombre.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)

                attr_tipo = QStandardItem(atributo.tipo)
                attr_unidad = QStandardItem(atributo.unidad)

                attr_obligatorio = QStandardItem()
                attr_obligatorio.setFlags(attr_obligatorio.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                attr_obligatorio.setCheckState(Qt.Checked if atributo.es_obligatorio else Qt.Unchecked)
                attr_obligatorio.setData(atributo.id_atributo, Qt.UserRole)

                familia_item.appendRow([
                    attr_nombre,
                    attr_tipo,
                    attr_unidad,
                    attr_obligatorio
                ])
                atributo_items[atributo.id_atributo] = attr_nombre

                # --- Opciones ---
                for opcion in atributo.opciones:
                    opcion_item = QStandardItem(opcion)
                    opcion_item.setFlags(opcion_item.flags() | Qt.ItemIsEditable | Qt.ItemIsDragEnabled)
                    opcion_item.setBackground(QColor('#ff6e40'))
                    atributo_items[atributo.id_atributo].appendRow([opcion_item])

    # -----------------------------------------------------------------
    # Creación de nuevos ítems (usados por TreeController)
    # -----------------------------------------------------------------
    def create_family(self, nombre="Nueva Familia"):
        item = QStandardItem(nombre)
        item.setData(None, Qt.UserRole)
        item.setFlags(item.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        return [item]

    def create_attribute(self, nombre="Nuevo Atributo"):
        nombre_item = QStandardItem(nombre)
        nombre_item.setData(None, Qt.UserRole)
        nombre_item.setFlags(nombre_item.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)

        tipo_item = QStandardItem(self.tipos_validos[0])
        unidad_item = QStandardItem("")

        obligatorio_item = QStandardItem()
        obligatorio_item.setFlags(obligatorio_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        obligatorio_item.setCheckState(Qt.Unchecked)
        obligatorio_item.setData(None, Qt.UserRole)

        return [nombre_item, tipo_item, unidad_item, obligatorio_item]

    def create_option(self, valor="Nueva Opción"):
        opcion_item = QStandardItem(valor)
        opcion_item.setFlags(opcion_item.flags() | Qt.ItemIsEditable | Qt.ItemIsDragEnabled)
        opcion_item.setBackground(QColor('#ff6e40'))
        return [opcion_item]
