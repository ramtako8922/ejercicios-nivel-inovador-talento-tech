# Clase que representa un menú de comida rápida
class MenuRapido:
    def __init__(self):
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def mostrar_menu(self):
        for plato in self.platos:
            print(f"Plato: {plato}")

# Clase Builder para construir un menú de comida rápida
class MenuRapidoBuilder:
    def __init__(self):
        self.menu = MenuRapido()

    def agregar_plato(self, plato):
        self.menu.agregar_plato(plato)
        return self  # Devuelve el propio builder para permitir la construcción encadenada

    def obtener_menu(self):
        return self.menu

# Uso
builder = MenuRapidoBuilder()
menu = builder.agregar_plato("Hamburguesa").agregar_plato("Papas Fritas").obtener_menu()
menu.mostrar_menu()
