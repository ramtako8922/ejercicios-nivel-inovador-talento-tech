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

    def find_level(self, node_value):
        """
        Encuentra el nivel de un nodo específico en el árbol.
        Devuelve -1 si el nodo no se encuentra en el árbol.
        """
        return self._find_level_recursive(self.root, node_value, 0)

    def _find_level_recursive(self, node, node_value, level):
        """
        Función auxiliar recursiva para encontrar el nivel de un nodo en el árbol.
        """
        if node is None:
            return -1
        if node.value == node_value:
            return level
        left_level = self._find_level_recursive(node.left, node_value, level + 1)
        right_level = self._find_level_recursive(node.right, node_value, level + 1)
        return max(left_level, right_level)

# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

# Buscar el nivel de un nodo específico
node_value_to_find = 4
level = tree.find_level(node_value_to_find)
if level != -1:
    print(f"El nivel del nodo con valor {node_value_to_find} es: {level}")
else:
    print(f"No se encontró un nodo con valor {node_value_to_find} en el árbol.")
