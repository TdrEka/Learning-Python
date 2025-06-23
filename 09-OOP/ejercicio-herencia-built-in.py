# Ejercicio 1
# Crear una lista que tenga la cuenta del numero de elementos que tiene
# No hay que hacer len(mi_lista) para obtenerlos

class ListaConCounter(list):
    def __init__(self, initial_list=None):
        super().__init__()
        self.count = 0

        if initial_list:
            for item in initial_list:
                self.append(item)

    def append(self, item):
        super().append(item)
        self.count += 1

    def __str__(self):
        return f"Count: {self.count}, Items: {list(self)}"