# Ejercicio 1
# Dada una lista con grados Centigrados ([16, 21, 25, 27, 32, 30, 28, 29)]
# Obtener la lista con los grados en Fahrenheit
# obtener otra con los grados Kelvin

centigrados = [16, 21, 25, 27, 32, 30, 28, 29]

fahrenheit = [(temperature * 9) / 5 + 32 for temperature in centigrados]

kelvin = [temperature + 273.15 for temperature in centigrados]


print('-'*70, '\n'*2)
print(centigrados, "Centigrados")
print(fahrenheit, "Fahrenheit")
print(kelvin, "Kelvin")
print("\n\n" + "-"*70)
