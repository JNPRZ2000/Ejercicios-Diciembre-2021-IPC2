class Nodo:
    def __init__(self, nombre, telefono, id):
        self.nombre = nombre
        self.telefono = telefono
        self.id = id
        self.siguiente = None
    def __str__(self):
        return "{}. Nombre: {}  -   Teléfono: {}".format((self.id+1), self.nombre, self.telefono)