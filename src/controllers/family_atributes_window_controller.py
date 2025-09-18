from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem

from views.Ui_family_atributes_window_view import Ui_FamilyAtributeWindow
from models.family_atribute_tree import FamilyAtributeTreeModel
from database.queries import select_family_and_atributes

# TODO: Cambiar el nombre de Ui Form a Ui_FamilyAtributeWindow

class FamilyAtributeWindow (QWidget, Ui_FamilyAtributeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = FamilyAtributeTreeModel()

        familia_items = {}

        rows = select_family_and_atributes()

        for id_fam, nombre_fam, id_attr, nom_attr, tipo, unidad, obligatorio, orden in rows:
            if id_fam not in familia_items:
                # Nodo padre
                familia_item = QStandardItem(nombre_fam)
                self.model.appendRow([familia_item])
                familia_items[id_fam] = familia_item

            # Si tiene atributo, lo agregamos como hijo
            if id_attr:
                attr_items = [
                    QStandardItem(nom_attr),
                    QStandardItem(tipo),
                    QStandardItem(unidad),
                    QStandardItem("Sí" if obligatorio else "No")
                ]
                familia_items[id_fam].appendRow(attr_items)
        
        self.tree_view.setModel(self.model)