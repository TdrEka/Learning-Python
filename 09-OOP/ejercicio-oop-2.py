# Ejercicio 2
# Implementar la clase producto (id, titulo, precio)
# Implementar un carrito de la compra (clase CarritoCompra)
# Las funcionalidades del carrito tienen que ser:
# - añadir producto (si se añade un producto con cantidad 0, se elimina del carrito)
# - quitar producto
# - mostrar precio total €
# - pagar compra (son 2 acciones, la de mostrar el ticket y luego vaciar el carrito)

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if quantity == 0:
            if product.id in self.items:
                del self.items[product.id]
        else:
            if product.id in self.items:
                self.items[product.id]['quantity'] += quantity
            else:
                self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def total_price(self):
        total = 0
        for item_data in self.items.values():
            total += item_data['product'].price * item_data['quantity']
        return total

    def pay(self):
        print("=== TICKET ===")
        for item_data in self.items.values():
            product = item_data['product']
            quantity = item_data['quantity']
            print(f"{product.name} x{quantity} - {product.price * quantity}€")
        print(f"TOTAL: {self.total_price()}€")
        print("=== PAID ===")
        self.items = {}
