from PySide6.QtWidgets import QWidget

# TODO: Cambiar nombre de Ui_Form a Ui_MainWindow
from views.Ui_main_window_view import Ui_Form

from controllers.family_atributes_window_controller import FamilyAtributeWindow

from views.tree_view import TreeView
from models.tree_model import TreeModel
from utils.tree_item import TreeItem

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Se crea root item y modelo para el árbol

        self.root_item = TreeItem(["Familia","Atributo","Tipo de dato"]).cargar_datos()
        self.model = TreeModel(self.root_item)

        # Se crea tree view y se vincula con el modelo

        self.tree_view = TreeView()
        self.tree_view.setModel(model=self.model)

        self.familys_button.clicked.connect(self.open_family_window)
        self.toolButton.clicked.connect(self.tree_view.show)

    def open_family_window(self):
        self.w = FamilyAtributeWindow()
        self.w.show()
