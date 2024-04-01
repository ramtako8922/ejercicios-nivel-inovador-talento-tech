from abc import ABC, abstractmethod

# Clase base para definir un personaje
class Personaje(ABC):
    @abstractmethod
    def habilidades(self):
        pass

# Clases concretas que representan diferentes tipos de personajes
class Guerrero(Personaje):
    def habilidades(self):
        return "Ataque fuerte y defensa alta"

class Mago(Personaje):
    def habilidades(self):
        return "Magia poderosa y poca resistencia física"

# Clase fábrica abstracta para crear personajes
class FabricaPersonajes(ABC):
    @abstractmethod
    def crear_personaje(self):
        pass

# Clases concretas de fábrica que crean personajes específicos
class FabricaGuerreros(FabricaPersonajes):
    def crear_personaje(self):
        return Guerrero()

class FabricaMagos(FabricaPersonajes):
    def crear_personaje(self):
        return Mago()

# Uso
fabrica_guerreros = FabricaGuerreros()
guerrero = fabrica_guerreros.crear_personaje()
print(guerrero.habilidades())  # Output: Ataque fuerte y defensa alta

fabrica_magos = FabricaMagos()
mago = fabrica_magos.crear_personaje()
print(mago.habilidades())  # Output: Magia poderosa y poca resistencia física
