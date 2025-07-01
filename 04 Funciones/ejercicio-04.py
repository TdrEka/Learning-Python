# Quiero sumar dos numeros con dos invocaciones a funciones, es decir

# para obtener el 8 tengo que ejecutar sum(5)(3).

# Escribir el código con una función tradicional de python y con lambdas

def sum_sum(a):
    def inner(b):
        return a + b
    return inner

sum_lambda = lambda a: lambda b: a + b