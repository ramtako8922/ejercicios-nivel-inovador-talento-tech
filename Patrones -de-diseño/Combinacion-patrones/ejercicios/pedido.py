from typing import List

# Clase que representa un pedido
class Order:
    def __init__(self):
        self.products = []
        self.delivery_address = ""

    def add_product(self, product_name: str, quantity: int):
        self.products.append({"product_name": product_name, "quantity": quantity})

    def set_delivery_address(self, address: str):
        self.delivery_address = address

    def __str__(self):
        products_str = "\n".join([f"Product: {item['product_name']}, Quantity: {item['quantity']}" for item in self.products])
        return f"Order details:\n{products_str}\nDelivery Address: {self.delivery_address}"



# Clase Builder para construir un pedido paso a paso
class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, product_name: str, quantity: int):
        self.order.add_product(product_name, quantity)

    def set_delivery_address(self, address: str):
        self.order.set_delivery_address(address)

    def get_order(self):
        return self.order
# Clase Singleton para gestionar la creación de pedidos
class OrderManager:
    _instance = None

    @staticmethod
    def get_instance():
        if not OrderManager._instance:
            OrderManager._instance = OrderManager()
        return OrderManager._instance

    def __init__(self):
        self.order_builder = None

    def create_order_builder(self):
        self.order_builder = OrderBuilder()

    def get_order_builder(self):
        return self.order_builder



# Ejemplo de uso
order_manager = OrderManager.get_instance()
order_manager.create_order_builder()

order_builder = order_manager.get_order_builder()
order_builder.add_product("Product 1", 2)
order_builder.add_product("Product 2", 1)
order_builder.set_delivery_address("123 Main St, City, Country")

order = order_builder.get_order()
print(order)