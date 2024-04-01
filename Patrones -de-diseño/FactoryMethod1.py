from abc import ABC, abstractmethod

# Clase base para definir un producto
class Producto(ABC):
    @abstractmethod
    def descripcion(self):
        pass

# Clases concretas que representan diferentes productos
class ProductoDigital(Producto):
    def descripcion(self):
        return "Descarga del producto digital"

class ProductoFisico(Producto):
    def descripcion(self):
        return "Envío del producto físico"

# Clase fábrica abstracta para crear productos
class FabricaProductos(ABC):
    @abstractmethod
    def crear_producto(self):
        pass

# Clases concretas de fábrica que crean productos específicos
class FabricaProductosDigitales(FabricaProductos):
    def crear_producto(self):
        return ProductoDigital()

class FabricaProductosFisicos(FabricaProductos):
    def crear_producto(self):
        return ProductoFisico()

# Uso
fabrica_digital = FabricaProductosDigitales()
producto_digital = fabrica_digital.crear_producto()
print(producto_digital.descripcion())  # Output: Descarga del producto digital

fabrica_fisica = FabricaProductosFisicos()
producto_fisico = fabrica_fisica.crear_producto()
print(producto_fisico.descripcion())  # Output: Envío del producto físico
