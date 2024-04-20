class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# Construir el árbol
raiz = Node("Administrador del Sistema")
raiz.left = Node("Gestor de Áreas Protegidas")
raiz.right = Node("Gestor de Especies")
raiz.right.left = Node("Gestor de Actividades")
