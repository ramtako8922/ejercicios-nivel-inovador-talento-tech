# Interfaz para la fábrica abstracta de personajes
class FabricaPersonajes:
    def crear_guerrero(self):
        pass

    def crear_mago(self):
        pass

# Interfaz para guerreros
class Guerrero:
    def habilidades(self):
        pass

# Interfaz para magos
class Mago:
    def habilidades(self):
        pass

# Clases concretas que implementan la fábrica abstracta y los personajes
class FabricaPersonajesFantasia(FabricaPersonajes):
    def crear_guerrero(self):
        return GuerreroFantasia()

    def crear_mago(self):
        return MagoFantasia()

class GuerreroFantasia(Guerrero):
    def habilidades(self):
        return "Ataque fuerte y defensa alta (Fantasía)"

class MagoFantasia(Mago):
    def habilidades(self):
        return "Magia poderosa y poca resistencia física (Fantasía)"

# Uso
fabrica_fantasia = FabricaPersonajesFantasia()
guerrero = fabrica_fantasia.crear_guerrero()
mago = fabrica_fantasia.crear_mago()

print(guerrero.habilidades())  # Output: Ataque fuerte y defensa alta (Fantasía)
print(mago.habilidades())      # Output: Magia poderosa y poca resistencia física (Fantasía)
