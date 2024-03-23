class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izquierdo) + contar_nodos(nodo.derecho)

# Crear un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

# Contar los nodos del árbol
num_nodos = contar_nodos(raiz)
print("Número de nodos del árbol:", num_nodos)
