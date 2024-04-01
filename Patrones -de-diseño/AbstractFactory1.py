# Interfaz para la fábrica abstracta de productos
class FabricaProductos:
    def crear_producto_digital(self):
        pass

    def crear_producto_fisico(self):
        pass

# Interfaz para productos digitales
class ProductoDigital:
    def descripcion(self):
        pass

# Interfaz para productos físicos
class ProductoFisico:
    def descripcion(self):
        pass

# Clases concretas que implementan la fábrica abstracta y los productos
class FabricaProductosEstandar(FabricaProductos):
    def crear_producto_digital(self):
        return ProductoDigitalEstandar()

    def crear_producto_fisico(self):
        return ProductoFisicoEstandar()

class ProductoDigitalEstandar(ProductoDigital):
    def descripcion(self):
        return "Descarga del producto digital estándar"

class ProductoFisicoEstandar(ProductoFisico):
    def descripcion(self):
        return "Envío del producto físico estándar"

# Uso
fabrica = FabricaProductosEstandar()
producto_digital = fabrica.crear_producto_digital()
producto_fisico = fabrica.crear_producto_fisico()

print(producto_digital.descripcion())  # Output: Descarga del producto digital estándar
print(producto_fisico.descripcion())    # Output: Envío del producto físico estándar
