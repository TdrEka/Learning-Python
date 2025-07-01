inventario = [
    {"producto": "Laptop", "precio": 800, "stock": 5, "categoria": "Electrónicos"},
    {"producto": "Ratón", "precio": 20, "stock": 50, "categoria": "Electrónicos"},
    {"producto": "Libro Python", "precio": 35, "stock": 15, "categoria": "Libros"},
    {"producto": "Monitor", "precio": 200, "stock": 8, "categoria": "Electrónicos"},
    {"producto": "Teclado", "precio": 60, "stock": 25, "categoria": "Electrónicos"}
]

# Tareas:
# 1. Filtrar productos de categoría "Electrónicos"
# 2. Ordenar por precio descendente
# 3. Calcular valor total del inventario electrónico
# 4. Encontrar el producto más caro

electronicos = [item for item in inventario if item["categoria"] == "Electrónicos"]
descendente_precio = sorted(inventario, key=lambda item: item["precio"], reverse=True)
total_value = sum(product["precio"] * product["stock"] for product in inventario)
most_expensive = max(inventario, key=lambda product: product["precio"])
