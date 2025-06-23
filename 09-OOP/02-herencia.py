class Animal:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hacer_sonido(self):
        print(f"{self.nombre} dice AAH")



class Perro(Animal):
    pass