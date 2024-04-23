# Subsistema de clases
class Motor:
    def encender(self):
        print("Motor encendido")

    def apagar(self):
        print("Motor apagado")

class Luces:
    def encender(self):
        print("Luces encendidas")

    def apagar(self):
        print("Luces apagadas")

class Radio:
    def encender(self):
        print("Radio encendida")

    def apagar(self):
        print("Radio apagada")

# Facade
class CocheFacade:
    def __init__(self):
        self.motor = Motor()
        self.luces = Luces()
        self.radio = Radio()

    def arrancar_coche(self):
        self.motor.encender()
        self.luces.encender()
        self.radio.encender()

    def apagar_coche(self):
        self.motor.apagar()
        self.luces.apagar()
        self.radio.apagar()

# Uso del patrón Facade
coche = CocheFacade()
coche.arrancar_coche()
print("------")
coche.apagar_coche()
