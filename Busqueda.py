class Node:
    def __init__(self, value):
        """
        Inicializa un nuevo nodo con el valor dado.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Inicializa un árbol binario vacío.
        """
        self.root = None

    def insert(self, value):
        """
        Inserta un nuevo nodo con el valor dado en el árbol.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """
        Función auxiliar recursiva para insertar un nuevo nodo en el árbol.
        """
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        """
        Busca un valor específico en el árbol.
        Devuelve True si el valor se encuentra en el árbol, False en caso contrario.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Función auxiliar recursiva para buscar un valor en el árbol.
        """
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

# Buscar un valor en el árbol
value_to_find = 4
if tree.search(value_to_find):
    print(f"El valor {value_to_find} se encuentra en el árbol.")
else:
    print(f"El valor {value_to_find} no se encuentra en el árbol.")
