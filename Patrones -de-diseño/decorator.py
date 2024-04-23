# Componente base
class Cafe:
    def get_precio(self):
        pass

    def get_descripcion(self):
        pass

# Componente concreto
class CafeSimple(Cafe):
    def get_precio(self):
        return 100

    def get_descripcion(self):
        return "Café simple"

# Decorador base
class DecoradorCafe(Cafe):
    def __init__(self, cafe):
        self.cafe = cafe

    def get_precio(self):
        return self.cafe.get_precio()

    def get_descripcion(self):
        return self.cafe.get_descripcion()

# Decorador concreto
class Leche(DecoradorCafe):
    def __init__(self, cafe):
        super().__init__(cafe)

    def get_precio(self):
        return super().get_precio() + 20

    def get_descripcion(self):
        return super().get_descripcion() + ", con leche"

# Uso del patrón Decorator
cafe_simple = CafeSimple()
print(f"Descripción: {cafe_simple.get_descripcion()}, Precio: {cafe_simple.get_precio()}")

cafe_con_leche = Leche(cafe_simple)
print(f"Descripción: {cafe_con_leche.get_descripcion()}, Precio: {cafe_con_leche.get_precio()}")
