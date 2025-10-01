class Familia:
    def __init__(self, id_familia, nombre):
        self.id = id_familia
        self.nombre = nombre
        self.atributos = []  # lista de objetos Atributo

    def agregar_atributo(self, atributo):
        self.atributos.append(atributo)


class Atributo:
    def __init__(self, id_atributo, nombre, tipo_dato, unidad, obligatorio, orden, opciones_atributos):
        self.id = id_atributo
        self.nombre = nombre
        self.tipo_dato = tipo_dato
        self.unidad = unidad
        self.obligatorio = obligatorio
        self.orden = orden
        self.opciones_atributos = opciones_atributos