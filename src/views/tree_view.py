from PySide6.QtWidgets import QTreeView

class TreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tree View")
        self.setMinimumSize(400, 300)  # Hide the header by default
        self.setUniformRowHeights(True)  # Optimize row height rendering
        self.setAlternatingRowColors(True)  # Enable alternating row colors for better readability

    def setModel(self, model):
        super().setModel(model)
        self.expandAll()  # Expand all items by default