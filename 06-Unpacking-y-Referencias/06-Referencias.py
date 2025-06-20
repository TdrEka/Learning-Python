# Hay estructuras de datos que funcionan por referencias (Diccionarios, Listas) == mutables

json = {
    "nombre": "Jason",
    "apellido": "Statham",
    "edad": 50
}

yaml = {**json, "nombre": "Yaml"}  #esto apunta al mismo bloque de memoria que json por lo que si muto yaml muto json

# Copia/Fusion

lista1 = [1, 2, 3]
lista3 = [*lista1]
lista1.append(5)
lista3.append(4)
print(lista1)
print(lista3)


# Diccionarios

toml = {**json}
toml["nombre"] = "Tommel"


print(yaml)
print(json)
print(toml)

credenciales_toml = {
    "email": "toml@gmail.com",
    "contraseña": "123456"
}

toml_completo = {**toml, **credenciales_toml, "edad": 40}
print(toml_completo)