from PySide6.QtWidgets import QWidget

from views.Ui_main_window_view import Ui_MainWindowForm

from controllers.family_atributes_window_controller import FamilyAtributeWindow
from controllers.login_controller import LoginController


class MainWindow(QWidget, Ui_MainWindowForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.open_login_window()
        self.familys_button.clicked.connect(self.open_family_window)

    def open_family_window(self):
        self.w = FamilyAtributeWindow()
        self.w.show()
    
    # def open_login_window(self):
    #     self.w = LoginController(parent=self)
    #     self.w.show()
