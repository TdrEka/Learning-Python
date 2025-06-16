# Crear una funcion que dada una lista de usuarios conectados y un usuario se añade el usuario a la lista de
# conectados en caso de que no lo estuviese previamente

usuario1 = "Charlie"
usuario2 = "Mike"
usuario3 = "Octavia"
usuarios_conectados = []

def añadir_usuario(lista_conectados, usuario):
    """Añade un usuario a una lista de usuarios conectados"""
    if usuario not in lista_conectados:
        lista_conectados.append(usuario)
        print(f" {usuario} se ha conectado. Total conectados: {len(lista_conectados)}")
        return True
    else:
        print(f" {usuario} ya estaba conectado.")
        return False

añadir_usuario(usuarios_conectados, usuario1)
añadir_usuario(usuarios_conectados, usuario2)
añadir_usuario(usuarios_conectados, usuario3)
print(f"Usuarios en linea: {usuarios_conectados}")
añadir_usuario(usuarios_conectados, usuario2)
print(f"Usuarios en linea: {usuarios_conectados}")
