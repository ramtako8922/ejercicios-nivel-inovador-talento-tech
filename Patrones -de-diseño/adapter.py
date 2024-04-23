# Interfaz antigua
class ViejaInterfaz:
    def hacer_algo_antiguo(self):
        print("Haciendo algo de la manera antigua...")

# Clase que implementa la interfaz antigua
class ImplementacionVieja(ViejaInterfaz):
    def hacer_algo_antiguo(self):
        print("Haciendo algo de la manera antigua...")

# Interfaz nueva
class NuevaInterfaz:
    def hacer_algo_nuevo(self):
        pass

# Adaptador de interfaz
class AdaptadorDeInterfaz(NuevaInterfaz):
    def __init__(self, vieja_interfaz):
        self.vieja_interfaz = vieja_interfaz

    def hacer_algo_nuevo(self):
        print("Adaptando la interfaz antigua a la interfaz nueva...")
        self.vieja_interfaz.hacer_algo_antiguo()

# Uso del adaptador
vieja_interfaz = ImplementacionVieja()
adaptador = AdaptadorDeInterfaz(vieja_interfaz)
adaptador.hacer_algo_nuevo()
