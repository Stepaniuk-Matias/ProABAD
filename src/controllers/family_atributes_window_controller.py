from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QPoint, QModelIndex
from PySide6.QtGui import QStandardItem

from views.Ui_family_atributes_window_view import Ui_FamilyAtributeWindowForm
from models.family_atribute_tree import FamilyAtributeTreeModel
from utils.combo_box_delegate import ComboBoxDelegate

from database.connection import create_connection
from repositories.family_repo import FamilyRepository
from repositories.mappers.family_mapper import FamilyMapper
from services.family_service import FamilyService
from adapters.family_tree_adapter import FamilyTreeAdapter


# -------------------------------------------------------------------------
# CONTROLADOR DE INTERACCIÓN CON EL ÁRBOL
# -------------------------------------------------------------------------
class TreeController:
    """
    Controla operaciones sobre el QTreeView:
    creación de nuevos ítems, persistencia y reordenamiento.
    """
    def __init__(self, tree_view, factory, service):
        self.tree_view = tree_view
        self.factory = factory
        self.service = service


        # Habilitar arrastrar y soltar dentro del árbol
        # self.tree_view.setDragDropMode(self.tree_view.InternalMove)
        # self.tree_view.setDefaultDropAction(Qt.MoveAction)
        # self.tree_view.setDragEnabled(True)
        # self.tree_view.setAcceptDrops(True)
        # self.tree_view.setDropIndicatorShown(True)

    # ---------------------------------------------------------------------
    # Crear nuevo ítem según contexto
    # ---------------------------------------------------------------------
    def add_item(self):
        model = self.tree_view.model()
        index = self.tree_view.currentIndex()

        try:
            if not index.isValid():
                # --- Crear familia ---
                new_family_id = self.service.create_family("Nueva Familia")
                item = self.factory.create_family("Nueva Familia")[0]
                item.setData(new_family_id, Qt.UserRole)
                model.appendRow([item])
                return

            item = model.itemFromIndex(index)
            parent = item.parent()

            if parent is None:
                # --- Crear atributo en la familia seleccionada ---
                id_fam = item.data(Qt.UserRole)
                new_attr_id = self.service.create_attribute(
                    id_familia=id_fam,
                    nombre="Nuevo Atributo",
                    tipo="int",
                    unidad="",
                    es_obligatorio=False,
                    orden=item.rowCount() + 1
                )
                items = self.factory.create_attribute("Nuevo Atributo")
                items[0].setData(new_attr_id, Qt.UserRole)
                items[3].setData(new_attr_id, Qt.UserRole)
                item.appendRow(items)
            elif parent.parent() is None:
                # --- Crear opción de atributo ---
                id_attr = item.data(Qt.UserRole)
                new_option = "Nueva Opción"
                self.service.add_option_to_attribute(id_attr, new_option)

                items = self.factory.create_option(new_option)
                item.appendRow(items)
            else:
                # --- Si seleccionó una opción, crear otra al mismo nivel ---
                parent.appendRow(self.factory.create_option("Nueva Opción"))

        except Exception as e:
            QMessageBox.critical(self.tree_view, "Error", f"No se pudo crear el elemento:\n{e}")


# -------------------------------------------------------------------------
# CONTROLADOR PRINCIPAL DE LA VISTA
# -------------------------------------------------------------------------
class FamilyAtributeWindow(QWidget, Ui_FamilyAtributeWindowForm):
    """
    Controlador principal de la vista de Familias y Atributos.
    Responsable de conectar UI ↔ Servicio y delegar comportamiento del árbol.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inyección de dependencias
        repository = FamilyRepository(create_connection, FamilyMapper)
        self.service = FamilyService(repository)
        self.model = FamilyAtributeTreeModel()
        self.adapter = FamilyTreeAdapter(["int", "float", "bool", "list"])

        # Configurar UI
        self.tree_view.setItemDelegateForColumn(1, ComboBoxDelegate(self.adapter.tipos_validos))
        self.model.dataChanged.connect(self.on_model_data_changed)
        self._load_tree()

        # Controlador del árbol
        self.tree_controller = TreeController(self.tree_view, self.adapter, self.service)
        self.create_button.clicked.connect(self.tree_controller.add_item)

    # --------------------------------------------------------------------
    # CARGA INICIAL
    # --------------------------------------------------------------------
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

    def keyPressEvent(self, event):
        """Intercepta presionar tecla Escape para limpiar selección."""
        if event.key() == Qt.Key_Escape:
            self.tree_view.clearSelection()
        else:
            super().keyPressEvent(event)

