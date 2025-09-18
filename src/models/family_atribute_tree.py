from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

class FamilyAtributeTreeModel(QStandardItemModel):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setHorizontalHeaderLabels(["Nombre","Tipo","Unidad","Obligatorio"])
        
        