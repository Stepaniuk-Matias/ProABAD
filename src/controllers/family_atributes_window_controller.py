from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItem
from PySide6.QtCore import Qt, QModelIndex

from views.Ui_family_atributes_window_view import Ui_FamilyAtributeWindowForm
from models.family_atribute_tree import FamilyAtributeTreeModel
from database.queries import (select_family_and_atributes, 
                              update_family_name, 
                              update_attribute_field)

class FamilyAtributeWindow (QWidget, Ui_FamilyAtributeWindowForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = FamilyAtributeTreeModel()

        self.model.dataChanged.connect(self.on_model_data_changed)

        familia_items = {}

        rows = select_family_and_atributes()

        for id_fam, nombre_fam, id_attr, nom_attr, tipo, unidad, obligatorio, orden in rows:
            if id_fam not in familia_items:
                # Nodo padre
                familia_item = QStandardItem(nombre_fam)
                familia_item.setData(id_fam, Qt.UserRole)

                self.model.appendRow([familia_item])
                familia_items[id_fam] = familia_item

            # Si tiene atributo, lo agregamos como hijo
            if id_attr:

                attr_nombre = QStandardItem(nom_attr)
                attr_nombre.setData(id_attr, Qt.UserRole)

                attr_tipo = QStandardItem(tipo)

                attr_unidad = QStandardItem(unidad)

                attr_obligatorio = QStandardItem()
                attr_obligatorio.setFlags(attr_obligatorio.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                attr_obligatorio.setCheckState(Qt.Checked if obligatorio else Qt.Unchecked)
                # opcional: guardar id también en esta columna si te resulta más cómodo
                attr_obligatorio.setData(id_attr, Qt.UserRole)

                attr_items = [
                    attr_nombre,
                    attr_tipo,
                    attr_unidad,
                    attr_obligatorio
                ]

                familia_items[id_fam].appendRow(attr_items)
        
        self.tree_view.setModel(self.model)

    
    def on_model_data_changed(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles=None):
        # recorro la región editada
        for row in range(topLeft.row(), bottomRight.row() + 1):
            for col in range(topLeft.column(), bottomRight.column() + 1):
                idx = topLeft.sibling(row, col)
                parent = idx.parent()
                # si tiene padre -> es fila de atributo
                if parent.isValid():
                    # id del atributo está en la columna 0
                    id_attr = idx.sibling(row, 0).data(Qt.UserRole)
                    if not id_attr:
                        continue
                    if col == 0:           # nombre
                        field = 'nombre_atributo'
                        new_val = idx.data(Qt.DisplayRole)
                    elif col == 1:         # tipo
                        field = 'tipo_dato'
                        new_val = idx.data(Qt.DisplayRole)
                    elif col == 2:         # unidad
                        field = 'unidad'
                        new_val = idx.data(Qt.DisplayRole)
                    elif col == 3:         # obligatorio (checkbox)
                        field = 'es_obligatorio'
                        new_val = idx.data(Qt.CheckStateRole) == Qt.Checked

                    # llamá a tu función de persistencia (definila en database.queries)
                    try:
                        update_attribute_field(id_attr, field, new_val)
                    except Exception as e:
                        print("Error guardando atributo:", e)
                else:
                    # edición sobre nodo familia (nombre de familia)
                    id_fam = idx.data(Qt.UserRole)
                    if id_fam:
                        new_name = idx.data(Qt.DisplayRole)
                        try:
                            update_family_name(id_fam, new_name)
                        except Exception as e:
                            print("Error guardando familia:", e)