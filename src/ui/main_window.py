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

        menu_bar = self.menuBar()

        familias_y_atributos = menu_bar.addMenu("Familias y Atributos")

        accion_crear_familia = QAction("Crear", self) 
        familias_y_atributos.addAction(accion_crear_familia)

        accion_ver_familias = QAction("Ver y editar", self)
        familias_y_atributos.addAction(accion_ver_familias)

        productos = menu_bar.addMenu("Productos")
        accion_crear_producto = QAction("Crear", self)
        productos.addAction(accion_crear_producto)
        accion_ver_productos = QAction("Ver y editar", self)
        productos.addAction(accion_ver_productos)

        procesos = menu_bar.addMenu("Procesos")

        accion_crear_proceso = QAction("Crear", self)
        procesos.addAction(accion_crear_proceso)

        accion_ver_procesos = QAction("Ver y editar", self)
        procesos.addAction(accion_ver_procesos)

        accion_comparar_procesos = QAction("Comparar procesos", self)
        procesos.addAction(accion_comparar_procesos)
