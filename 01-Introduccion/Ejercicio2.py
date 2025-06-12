# Ejercicio 2:
# Un usuario introduce un numero (oculto)
# le da una pista al siguiente usuario: la longitud del numero es <rellenar esto>
# Otro usuario tiene que adivinar el numero (introduciendolo)
# Mostrar True si acierta, False si no

import getpass

secret_number = getpass.getpass("Enter your secret number: ")

print(f"Hint: The length of the number is {len(secret_number)}")

guess = input("Enter your guess: ")

result = guess == secret_number
print(result)