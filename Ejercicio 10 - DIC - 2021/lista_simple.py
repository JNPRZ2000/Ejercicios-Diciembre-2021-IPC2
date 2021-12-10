from os import system
from nodo import Nodo
class ListaSimple:
    def __init__(self):
        self.head = None
        self.lenght = 0
    def append(self, nombre, telefono):
        nuevo = Nodo(nombre, telefono, self.lenght)
        if self.head == None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.lenght += 1
    def __str__(self):
        cadena = "Contactos:"
        actual = self.head
        while actual != None:
            cadena += "\n{}".format(actual)
            actual = actual.siguiente
        return cadena
if __name__ == "__main__":
    lista = ListaSimple()
    def menu():
        print("""
        1- Ingresar Contacto
        2- Ver Contactos
        3- Salir
        """)
        op = int(input("\nSeleccione su opción: "))
        if op == 1:
            ingresar()
        elif op == 2:
            print(lista)
            menu()
        elif op == 3:
            print("Terminado")
        else:
            print("Opción incorrecta...")
            menu()
    def ingresar():
        nombre = (input("\nIngrese su nombre: "))
        telefono = int(input("\nIngrese su teléfono: "))
        lista.append(nombre, telefono) 
        menu()
    menu()


            