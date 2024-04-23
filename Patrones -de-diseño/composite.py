# Componente base
class ComponenteMenu:
    def mostrar(self):
        pass

# Componente hoja
class ElementoMenu(ComponenteMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre} - ${self.precio}")

# Componente compuesto
class Menu(ComponenteMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def mostrar(self):
        print(f"== {self.nombre} ==")
        for elemento in self.elementos:
            elemento.mostrar()

# Uso del patrón Composite
cafe = ElementoMenu("Café", 100)
te = ElementoMenu("Té", 80)

menu_bebidas = Menu("Bebidas")
menu_bebidas.agregar_elemento(cafe)
menu_bebidas.agregar_elemento(te)

sandwich = ElementoMenu("Sandwich", 200)
ensalada = ElementoMenu("Ensalada", 150)

menu_comidas = Menu("Comidas")
menu_comidas.agregar_elemento(sandwich)
menu_comidas.agregar_elemento(ensalada)

menu_principal = Menu("Menú Principal")
menu_principal.agregar_elemento(menu_bebidas)
menu_principal.agregar_elemento(menu_comidas)

menu_principal.mostrar()
