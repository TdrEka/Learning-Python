# Problema del diamante.

class Animal:
    def __init__(self, nombre, tipo, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"{self.nombre} goes {self.sonido}")

    def __str__(self):
        return f"Animal(nombre={self.nombre}, tipo={self.tipo}, sonido={self.sonido}"

class AnimalVolador(Animal):
    def volar(self):
        print("puede volar.")

    def __str__(self):
        str_animal = super().__str__()
        return f"{str_animal} es (AnimalVolador)"

class AnimalNadador(Animal):
    def nadar(self):
        print("puede nadar.")
        
    def __str__(self):
        str_animal = super().__str__()
        return f"{str_animal} es (AnimalNadador)"

class Pato(AnimalVolador, AnimalNadador):
    def __init__(self, nombre):
        super().__init__(nombre, "pato", "cuac cuac")

    def __str__(self):
        str_animal = super().__str__()
        return f"{str_animal} (es un pato)"

willix = Pato("Willix")

willix.volar()
willix.nadar()
willix.hacer_sonido()

print(willix)


# Pinguino

