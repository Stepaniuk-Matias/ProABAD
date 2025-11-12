from views.Ui_login_view import Ui_LoginForm

from PySide6.QtWidgets import QWidget

class LoginController(QWidget, Ui_LoginForm):
    def __init__(self, auth_service = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.auth_service = auth_service

    def handle_login(self):
        pass
        # username = self.user_lineEdit.text()
        # password = self.password_lineEdit.text()

        # if self.auth_service.authenticate(username, password):
        #     self.show_message("Login successful!")
        # else:
        #     self.show_message("Invalid username or password.")