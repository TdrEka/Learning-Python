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