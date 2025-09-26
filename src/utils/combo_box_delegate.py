from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        cb = QComboBox(parent)
        cb.addItems(self.items)
        return cb

    def setEditorData(self, editor, index):
        value = index.data(Qt.DisplayRole) or ""
        pos = editor.findText(value)
        editor.setCurrentIndex(pos if pos >= 0 else 0)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)
