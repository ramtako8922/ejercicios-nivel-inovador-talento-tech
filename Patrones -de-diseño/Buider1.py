# Clase que representa un pedido
class Pedido:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_pedido(self):
        for producto in self.productos:
            print(f"Producto: {producto}")

# Clase Builder para construir un pedido
class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def agregar_producto(self, producto):
        self.pedido.agregar_producto(producto)
        return self  # Devuelve el propio builder para permitir la construcción encadenada

    def obtener_pedido(self):
        return self.pedido

# Uso
builder = PedidoBuilder()
pedido = builder.agregar_producto("Laptop").agregar_producto("Mouse").obtener_pedido()
pedido.mostrar_pedido()
