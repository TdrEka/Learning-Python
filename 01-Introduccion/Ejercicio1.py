# Ejercicio 1: Upper, Operadores.

variable = input("Dime algo: ")
is_upper = variable.isupper()


if not is_upper:
    print(f"Tu palabra: {variable}. No esta en mayusculas")
else:
    print("Tu palabra esta en mayusculas")


