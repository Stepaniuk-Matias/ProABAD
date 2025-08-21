import sqlite3

class TreeItem:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def append_child(self, child):
        self.children.append(child)
        child.parent = self

    def child(self, row):
        return self.children[row]

    def child_count(self):
        return len(self.children)

    def column_count(self):
        return len(self.data)

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0

    def cargar_datos(self):
        conn = sqlite3.connect(r".\src\database\ProABAD_test.db")
        cursor = conn.cursor()

        self.root_item = TreeItem(data=["Familia", "Atributo"])

        cursor.execute("SELECT id_familia, nombre FROM Familia")
        for familia_id, familia_nombre in cursor.fetchall():
            familia_item = TreeItem([familia_nombre, ""])
            self.root_item.append_child(familia_item)

            cursor.execute("SELECT nombre_atributo, tipo_dato FROM Atributo WHERE id_familia=?", (familia_id,))
            for atr_nombre, atr_tipo_dato in cursor.fetchall():
                atr_item = TreeItem([atr_nombre, f"Tipo de dato: {atr_tipo_dato}"])
                familia_item.append_child(atr_item)

        conn.close()
        return self.root_item
