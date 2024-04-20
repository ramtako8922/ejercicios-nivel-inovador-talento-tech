import random


class Nodo:
    def __init__(self, nombre, consumo_agua, consumo_electricidad):
        self.nombre = nombre
        self.consumo_agua = consumo_agua
        self.consumo_electricidad = consumo_electricidad
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# Creamos los nodos para representar los hogares y sus atributos
hogar_a = Nodo("Hogar A", consumo_agua=random.randint(1, 100), consumo_electricidad=random.randint(1, 100))
hogar_b = Nodo("Hogar B", consumo_agua=random.randint(1, 100), consumo_electricidad=random.randint(1, 100))
hogar_c = Nodo("Hogar C", consumo_agua=random.randint(1, 100), consumo_electricidad=random.randint(1, 100))
hogar_d = Nodo("Hogar D", consumo_agua=random.randint(1, 100), consumo_electricidad=random.randint(1, 100))
hogar_e = Nodo("Hogar E", consumo_agua=random.randint(1, 100), consumo_electricidad=random.randint(1, 100))

# Creamos la jerarquía de los hogares
hogar_a.agregar_hijo(Nodo("Cocina", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))
hogar_a.agregar_hijo(Nodo("Baño", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))

hogar_b.agregar_hijo(Nodo("Cocina", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))
hogar_b.agregar_hijo(Nodo("Baño", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))

hogar_c.agregar_hijo(Nodo("Cocina", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))
hogar_c.agregar_hijo(Nodo("Baño", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))

hogar_d.agregar_hijo(Nodo("Cocina", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))
hogar_d.agregar_hijo(Nodo("Baño", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))

hogar_e.agregar_hijo(Nodo("Cocina", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))
hogar_e.agregar_hijo(Nodo("Baño", consumo_agua=random.randint(1, 50), consumo_electricidad=random.randint(1, 50)))

# Mostramos la jerarquía de hogares
def mostrar_arbol(nodo, nivel=0):
    print("   " * nivel + "|--", nodo.nombre, "- Consumo de agua:", nodo.consumo_agua, "Consumo de electricidad:", nodo.consumo_electricidad)
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)

mostrar_arbol(hogar_a)
mostrar_arbol(hogar_b)
mostrar_arbol(hogar_c)
mostrar_arbol(hogar_d)
mostrar_arbol(hogar_e)
