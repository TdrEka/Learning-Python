lista_nums = [1, 2, 3, 4, 5, 6]

#uno, dos, tres, cuatro, cinco, seis = lista_nums
#print(cuatro)
#print(tres)

#uno, dos, tres, *resto = lista_nums

persona = {
    "nombre": "Charlie",
    "apellido": "Sheen",
    "email": "charlie@gmail.com"
}

#nombre, apellidos, email = persona (devuelve solo la clave)
#nombre, apellidos, email = persona.values() (devuelve el valor)
nombre, apellidos, email = persona.items() # (devuelve el par clave valor en forma de tuple)
print(nombre)



