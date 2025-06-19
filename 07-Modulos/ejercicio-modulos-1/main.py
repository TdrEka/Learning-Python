# Ejercicio 1
# Crear un traductor de textos
# Como primer parametro, tiene que recibir una clave que representa el texto a traducir
# Como segundo parametro tiene que recibir el lenguaje al cual queremos traducir el texto
# El lenguaje de traducción por defecto será inglés ("en")
# Las traducciones las vamos a tener en un diccionario, es decir, hola -> hello, hola -> ciao ....
# from glob import translate

# --- Ejemplo de uso:
# traduce("baile", lang="en") # dance
# traduce("hola", lang="it") # ciao
# traduce("patatas") # potatoes

import translator
print("\n" + "-"*50 + "\n")
print(translator.translate("ambulancia", "de"))
print("\n" + "-"*50)