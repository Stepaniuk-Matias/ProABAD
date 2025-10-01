from PySide6.QtGui import QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class FamilyTreeAdapter:
    def __init__(self, tipos_validos):
        self.tipos_validos = tipos_validos

    def build_model(self, model, rows):
        familia_items = {}
        atributo_items = {}

        for (id_fam, nombre_fam, id_attr, nom_attr, tipo, unidad, obligatorio, orden_attr,
             opciones_atributo) in rows:

            # Familia
            if id_fam not in familia_items:
                familia_item = QStandardItem(nombre_fam)
                familia_item.setData(id_fam, Qt.UserRole)
                model.appendRow([familia_item])
                familia_items[id_fam] = familia_item

            # Atributo
            if id_attr and id_attr not in atributo_items:
                attr_nombre = QStandardItem(nom_attr)
                attr_nombre.setData(id_attr, Qt.UserRole)

                attr_tipo = QStandardItem(tipo)
                attr_unidad = QStandardItem(unidad)

                attr_obligatorio = QStandardItem()
                attr_obligatorio.setFlags(attr_obligatorio.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                attr_obligatorio.setCheckState(Qt.Checked if obligatorio else Qt.Unchecked)
                attr_obligatorio.setData(id_attr, Qt.UserRole)

                familia_items[id_fam].appendRow([
                    attr_nombre,
                    attr_tipo,
                    attr_unidad,
                    attr_obligatorio
                ])
                atributo_items[id_attr] = attr_nombre

            # Opción
            if opciones_atributo:
                for op in opciones_atributo:
                    opcion_item = QStandardItem(op)
                    opcion_item.setFlags(opcion_item.flags() | Qt.ItemIsEditable | Qt.ItemIsDragEnabled)
                    opcion_item.setBackground(QColor('#ff6e40'))
                    opcion_item.setFont()
                    # opcion_item

                    atributo_items[id_attr].appendRow([QStandardItem(), opcion_item])
