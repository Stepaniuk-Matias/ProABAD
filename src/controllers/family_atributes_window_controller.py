from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QModelIndex

from views.Ui_family_atributes_window_view import Ui_FamilyAtributeWindowForm
from models.family_atribute_tree import FamilyAtributeTreeModel
from utils.combo_box_delegate import ComboBoxDelegate

from repositories.family_repo import FamilyRepository
from services.family_service import FamilyService
from adapters.family_tree_adapter import FamilyTreeAdapter


class FamilyAtributeWindow(QWidget, Ui_FamilyAtributeWindowForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inyección de dependencias
        repository = FamilyRepository()
        self.service = FamilyService(repository)
        self.model = FamilyAtributeTreeModel()
        self.adapter = FamilyTreeAdapter(["int", "float", "bool", "list"])

        self.tree_view.setItemDelegateForColumn(1, ComboBoxDelegate(self.adapter.tipos_validos))
        self.model.dataChanged.connect(self.on_model_data_changed)

        rows = self.service.load_tree_data()
        self.adapter.build_model(self.model, rows)
        self.tree_view.setModel(self.model)

    def on_model_data_changed(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles=None):
        for row in range(topLeft.row(), bottomRight.row() + 1):
            for col in range(topLeft.column(), bottomRight.column() + 1):
                idx = topLeft.sibling(row, col)
                parent = idx.parent()

                if parent.isValid():  # Atributo
                    id_attr = idx.sibling(row, 0).data(Qt.UserRole)
                    if not id_attr:
                        continue
                    field_map = {0: 'nombre_atributo', 1: 'tipo_dato', 2: 'unidad', 3: 'es_obligatorio'}
                    field = field_map.get(col)
                    if not field:
                        continue
                    new_val = idx.data(Qt.DisplayRole) if col != 3 else (idx.data(Qt.CheckStateRole) == Qt.Checked)
                    try:
                        self.service.update_attribute(id_attr, field, new_val)
                    except Exception as e:
                        print("Error guardando atributo:", e)

                else:  # Familia
                    id_fam = idx.data(Qt.UserRole)
                    if id_fam:
                        new_name = idx.data(Qt.DisplayRole)
                        try:
                            self.service.update_family(id_fam, new_name)
                        except Exception as e:
                            print("Error guardando familia:", e)
