from PySide6.QtWidgets import QWidget

# TODO: Cambiar nombre de Ui_Form a Ui_MainWindow
from views.Ui_main_window_view import Ui_Form

from controllers.family_atributes_window_controller import FamilyAtributeWindow


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.familys_button.clicked.connect(self.open_family_window)

    def open_family_window(self):
        self.w = FamilyAtributeWindow()
        self.w.show()
