from PySide6.QtGui import QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from models.schema_familia import Familia, Atributo

class FamilyTreeAdapter:
    def __init__(self, tipos_validos):
        self.tipos_validos = tipos_validos

    def build_model(self, model, familias: list[Familia]):
        familia_items = {}
        atributo_items = {}

        for familia in familias:
            # --- Familia ---
            familia_item = QStandardItem(familia.nombre)
            familia_item.setData(familia.id_familia, Qt.UserRole)
            model.appendRow([familia_item])
            familia_items[familia.id_familia] = familia_item

            # --- Atributos ---
            for atributo in familia.atributos:
                attr_nombre = QStandardItem(atributo.nombre)
                attr_nombre.setData(atributo.id_atributo, Qt.UserRole)

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
