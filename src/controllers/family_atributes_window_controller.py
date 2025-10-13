from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QModelIndex

from views.Ui_family_atributes_window_view import Ui_FamilyAtributeWindowForm
from models.family_atribute_tree import FamilyAtributeTreeModel
from utils.combo_box_delegate import ComboBoxDelegate

from database.connection import create_connection

from repositories.family_repo import FamilyRepository
from repositories.mappers.family_mapper import FamilyMapper
from services.family_service import FamilyService
from adapters.family_tree_adapter import FamilyTreeAdapter


class FamilyAtributeWindow(QWidget, Ui_FamilyAtributeWindowForm):
    """
    Controlador principal de la vista de Familias y Atributos.
    Responsable solo de conectar UI ↔ Servicio.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inyección de dependencias
        repository = FamilyRepository(create_connection, FamilyMapper)
        self.service = FamilyService(repository)
        self.model = FamilyAtributeTreeModel()
        self.adapter = FamilyTreeAdapter(["int", "float", "bool", "list"])

        self.tree_view.setItemDelegateForColumn(1, ComboBoxDelegate(self.adapter.tipos_validos))
        self.model.dataChanged.connect(self.on_model_data_changed)

        self._load_tree()

    def _load_tree(self):
        try:
            familias = self.service.get_families()
            self.adapter.build_model(self.model, familias)
            self.tree_view.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las familias:\n{e}")

    # --------------------------------------------------------------------
    # EVENTOS DE CAMBIO EN EL MODELO
    # --------------------------------------------------------------------

    def on_model_data_changed(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles=None):
        """
        Detecta cambios en el modelo y actualiza los datos persistidos.
        """
        for row in range(topLeft.row(), bottomRight.row() + 1):
            for col in range(topLeft.column(), bottomRight.column() + 1):
                idx = topLeft.sibling(row, col)
                parent = idx.parent()

                if parent.isValid():  # Atributo
                    self._handle_attribute_edit(idx, row, col)

                else:  # Familia
                    self._handle_family_edit(idx)
    
    def _handle_family_edit(self, idx):
        id_fam = idx.data(Qt.UserRole)
        if not id_fam:
            return
        new_name = idx.data(Qt.EditRole)
        try:
            self.service.update_family(id_fam, new_name)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo actualizar la familia:\n{e}")

    def _handle_attribute_edit(self, idx, row, col):
        id_attr = idx.sibling(row, 0).data(Qt.UserRole)
        if not id_attr:
            return
        try:
            self.service.update_attribute_from_ui(id_attr, col, idx)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo actualizar el atributo:\n{e}")
