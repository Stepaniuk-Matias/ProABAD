from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from services.family_service import FamilyService
from PySide6.QtWidgets import QMessageBox

class FamilyAtributeTreeModel(QStandardItemModel):
    def __init__(self, parent = None, family_service: FamilyService = None):
        super().__init__(parent)
        self.family_service = family_service

        self.setHorizontalHeaderLabels(["Nombre","Tipo","Unidad","Obligatorio"])
        
    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return super().setData(index, value, role)

        item = self.itemFromIndex(index)
        entity_type = item.data(Qt.UserRole + 1)  # ej: "familia", "atributo", etc.
        entity_id = item.data(Qt.UserRole)        # id en la BD

        try:
            if entity_type == "familia":
                self.family_service.update_family_name(entity_id, value)
            
            # si no hay error → actualiza en la vista
            return super().setData(index, value, role)

        except Exception as e:
            QMessageBox.warning(None, "Error al guardar", str(e))
            return False  # evita que se aplique el cambio visual