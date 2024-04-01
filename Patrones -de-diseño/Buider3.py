# Clase que representa un automóvil
class Automovil:
    def __init__(self):
        self.opciones = []

    def agregar_opcion(self, opcion):
        self.opciones.append(opcion)

    def mostrar_opciones(self):
        for opcion in self.opciones:
            print(f"Opción: {opcion}")

# Clase Builder para construir un automóvil
class AutomovilBuilder:
    def __init__(self):
        self.automovil = Automovil()

    def agregar_opcion(self, opcion):
        self.automovil.agregar_opcion(opcion)
        return self  # Devuelve el propio builder para permitir la construcción encadenada

    def obtener_automovil(self):
        return self.automovil

# Uso
builder = AutomovilBuilder()
automovil = builder.agregar_opcion("Asientos de cuero").agregar_opcion("Sistema de sonido premium").obtener_automovil()
automovil.mostrar_opciones()
