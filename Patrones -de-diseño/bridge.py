# Implementación de la interfaz
class Implementador:
    def operacion_impl(self):
        pass

# Implementación concreta A
class ImplementadorConcretoA(Implementador):
    def operacion_impl(self):
        return "Implementación A"

# Implementación concreta B
class ImplementadorConcretoB(Implementador):
    def operacion_impl(self):
        return "Implementación B"

# Abstracción
class Abstraccion:
    def __init__(self, implementador):
        self.implementador = implementador

    def operacion(self):
        return f"Abstracción usando {self.implementador.operacion_impl()}"

# Uso del patrón Bridge
implementador_a = ImplementadorConcretoA()
implementador_b = ImplementadorConcretoB()

abstraccion_a = Abstraccion(implementador_a)
abstraccion_b = Abstraccion(implementador_b)

print(abstraccion_a.operacion())
print(abstraccion_b.operacion())
