from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QWidget, QLabel, QMainWindow, QLineEdit, 
                               QVBoxLayout, QHBoxLayout, QDial, QProgressBar, QPushButton,
                               QMenu, QToolBar)

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("ProABAD")
        self.setWindowIcon(QIcon(r".\src\ui\LOGO MIGUEL ABAD.png"))
        self.setMinimumSize(QSize(800, 600))