from PySide6.QtWidgets import QWidget

from views.Ui_family_atributes_window_view import Ui_Form

# TODO: Cambiar el nombre de Ui Form a Ui_FamilyAtributeWindow

class FamilyAtributeWindow (QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)