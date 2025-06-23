class Dog:
    def __init__(self, name, legs = 4):
        self.legs = legs
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

class User:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    def get_full_name(self):
        return f"{self.name} {self.last_name}"


my_dog = Dog("Fluffy")
scraps = Dog("Scraps", 3)

print(my_dog.bark())
usuario1 = User("Eka", "Izquierdo")
print(usuario1.get_full_name())
print(f"{scraps.name} is a dog and has {scraps.legs} legs...")




class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    @staticmethod
    def suma(n1, n2):
        return n1 + n2



class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni
        self.__telefono = telefono

    def get_dni(self):
        return self.__dni

    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    dni = property(get_dni, set_dni)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono


    def __str__(self):
        return f"{self.nombre} {self.apellido} es un humano, su dni es {self.dni}, lo puedes llamar en {self.telefono}"

    def __repr__(self):
        return f"<{self.nombre} {self.apellido} es un humano, su dni es {self.dni}, lo puedes llamar en {self.telefono}.>"

ekaitz = Persona("Ekaitz", "Izquierdo", "51299693X", "+34 747499755")

print(ekaitz)