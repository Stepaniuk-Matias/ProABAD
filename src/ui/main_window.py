from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QWidget, QLabel, QMainWindow, QLineEdit, 
                               QVBoxLayout, QHBoxLayout, QDial, QProgressBar, QPushButton,
                               QMenu, QToolBar, QStackedLayout)

from views.tree_view import TreeView
from models.tree_model import TreeModel
from utils.tree_item import TreeItem

# Ventana principal de la aplicación, contiene menu de opciones
# TODO: Implementar funcionalidades de los menús y acciones
# TODO: Hacer un dashboard con info util
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("ProABAD")
        self.setWindowIcon(QIcon(r".\src\assets\LOGO MIGUEL ABAD.png"))
        self.setMinimumSize(QSize(800, 600))

        self.stacked_layout = QStackedLayout()


        self.central_widget = QWidget()
        self.central_widget.setWindowTitle("Ventana Principal")
        self.setCentralWidget(self.central_widget)

        # Se crea root item y modelo para el árbol

        self.root_item = TreeItem(["Familia","Atributo","Tipo de dato"]).cargar_datos()
        self.model = TreeModel(self.root_item)

        # Se crea tree view y se vincula con el modelo

        self.tree_view = TreeView()
        self.tree_view.setModel(model=self.model)

        self.stacked_layout.addWidget(self.central_widget)
        self.stacked_layout.addWidget(self.tree_view)

        
        #Menu bar y acciones

        menu_bar = self.menuBar()

        familias_y_atributos = menu_bar.addMenu("Familias y Atributos")

        accion_crear_familia = QAction("Crear", self) 
        familias_y_atributos.addAction(accion_crear_familia)


        accion_ver_familias = QAction("Ver y editar", self)
        accion_ver_familias.triggered.connect(lambda: self.stacked_layout.setCurrentIndex(1))

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




