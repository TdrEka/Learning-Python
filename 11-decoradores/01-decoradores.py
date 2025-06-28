# Los decoradores, son las anotaciones de otros lenguajes. y se inicializan con un '@' Ej= @mi_decorador
# Se pueden agregar a funciones, clases o sobre otros decoradores.
# Modifican aquello que decoran
# Son funciones que reciben otras funciones como parametro (las que estan decorando)
# Crean dentro de si mismos una funcion extra que acepta los argumentos (en caso de tenerlos) y  returnean la nueva funcion.
import time


#decorador
def log(fn_decorada):
    def wrapper(*args, **kwargs):
        pass

    return wrapper






#decorando la funcion suma con el decorador log
@log
def suma(n1, n2):
    return n1 + n2



@log
def resta(n1, n2):
    return n1 - n2


def measure_execution_time(fn):
    def watercolour(*args, **kwargs):
        rn = time.time()
        print(f"Start: {rn}")
        result = fn(*args, **kwargs)
        aftertime = time.time()
        print(f"End: {aftertime}")
        print(f"Running {fn.__name__} took just about {aftertime - rn}")
        return result
    return watercolour



class DecoratorLog:
    def __init__(self, fn_d):
        self.fn = fn_d

    def __call__(self, *args, **kwargs):
        pass