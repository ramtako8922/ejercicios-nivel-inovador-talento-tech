# Manejador base
class Manejador:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def manejar(self, solicitud):
        if self.siguiente:
            self.siguiente.manejar(solicitud)

# Manejadores concretos
class ManejadorConcretoA(Manejador):
    def manejar(self, solicitud):
        if solicitud == "A":
            print("ManejadorConcretoA maneja la solicitud")
        else:
            super().manejar(solicitud)

class ManejadorConcretoB(Manejador):
    def manejar(self, solicitud):
        if solicitud == "B":
            print("ManejadorConcretoB maneja la solicitud")
        else:
            super().manejar(solicitud)

class ManejadorConcretoC(Manejador):
    def manejar(self, solicitud):
        if solicitud == "C":
            print("ManejadorConcretoC maneja la solicitud")
        else:
            super().manejar(solicitud)

# Uso del patrón Chain of Responsibility
manejador_a = ManejadorConcretoA()
manejador_b = ManejadorConcretoB(manejador_a)
manejador_c = ManejadorConcretoC(manejador_b)

manejador_c.manejar("A")
manejador_c.manejar("B")
manejador_c.manejar("C")
manejador_c.manejar("D")
