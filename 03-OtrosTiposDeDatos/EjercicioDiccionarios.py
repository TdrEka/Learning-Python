# Crear una lista de Diccionarios que representan los Sugus y recorrerla mostrando la relacion entre sabor y color
# de cada Sugus

sugus = [
    {"color": "rojo", "sabor": "fresa"},
    {"color": "azul", "sabor": "mirtilla"},
    {"color": "amarillo", "sabor": "limon"},
    {"color": "naranja", "sabor": "naranja"}
]

print("=== RELACIÓN COLOR Y SABOR DE SUGUS ===\n")

for sugus_item in sugus:
    print(f"El Sugus de color {sugus_item['color']} tiene sabor a {sugus_item['sabor']}")


usuario = {
    "userID": "TdrEka",
    "password": "1234"
}
infoUsuario = {
    "nombre": "Charlie",
    "apellidos": "Stones",
    "edad": "28",
    "userID": "eka.pk"
}

usuario.update(infoUsuario)
print(usuario)
