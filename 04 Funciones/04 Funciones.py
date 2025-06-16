def suma(n1, n2):
    """ returns the sum of two numbers"""
    return n1 + n2

numero1 = 10
numero2 = 10
print(suma(10, 10))


def AddElement(item, lista = None):
    """agrega un elemento a una lista"""
    if not lista:
        lista = []
    lista.append(item)
    return lista

l1 = [1, 2]

l2 = AddElement(2)
print(l2)
AddElement(3, l1)
print(l1)

def get_ticket_loteria(sorteo, *nums):
    lista_nums = []
    for n in nums:
        lista_nums.append(str(n))
    return(f"""
        Boleto para {sorteo}  -  {lista_nums}
    """)


boleto = get_ticket_loteria("bonoloto", 1, 17, 34, 56, 39, 11)
print(boleto)

lista_productos = [
    {"nombre": "Nintendo Switch", "precio": 8, "stock": 300},
{"nombre": "Juego1", "precio": 1, "stock": 150},
{"nombre": "juego2", "precio": 1, "stock": 100},
{"nombre": "juego3", "precio": 2, "stock": 80}
]

def filtrar_productos(nombre=None, precio_max=None, stock=None):
    lista_productos_filtrados = []
    if nombre:
        for producto in lista_productos:
            if nombre.lower() in producto["nombre"].lower():
                lista_productos_filtrados.append(producto)
    if precio_max:
        for producto in lista_productos:
            if producto["precio"] <= precio_max and producto not in lista_productos_filtrados:
                lista_productos_filtrados.append(producto)
    if stock:
        for producto in lista_productos:
            if producto["stock"] <= stock and producto not in lista_productos_filtrados:
                lista_productos_filtrados.append(producto)

    return lista_productos_filtrados

print(filtrar_productos(precio_max=10, nombre="Nintendo Switch"))