from PySide6.QtGui import QStandardItem
from PySide6.QtCore import Qt, QModelIndex

class ItemFactory:
    def create_family(self, nombre="Nueva Familia"):
        item = QStandardItem(nombre)
        item.setData(None, Qt.UserRole)  # ID aún no asignado en DB
        return [item]

    def create_atributo(self, nombre="Nuevo Atributo"):
        nombre_item = QStandardItem(nombre)
        nombre_item.setData(None, Qt.UserRole)

        tipo_item = QStandardItem("int")
        unidad_item = QStandardItem("")

        obligatorio_item = QStandardItem()
        obligatorio_item.setFlags(obligatorio_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        obligatorio_item.setCheckState(Qt.Unchecked)
        obligatorio_item.setData(None, Qt.UserRole)

        return [nombre_item, tipo_item, unidad_item, obligatorio_item]

    def create_opcion(self, valor="Nueva Opción"):
        filler = QStandardItem()  # para mantener columnas
        opcion_item = QStandardItem(valor)
        opcion_item.setFlags(opcion_item.flags() | Qt.ItemIsEditable | Qt.ItemIsDragEnabled)
        return [filler, opcion_item]