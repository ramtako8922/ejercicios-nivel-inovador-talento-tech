class Node:
    def __init__(self, value):
        # Inicializa un nuevo nodo con el valor dado
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # Inicializa un nuevo árbol binario con la raíz nula
        self.root = None

    def insert(self, value):
        # Inserta un nuevo nodo en el árbol
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Inserta recursivamente un nuevo nodo en el árbol
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

    def height(self):
        # Calcula la altura del árbol
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # Calcula recursivamente la altura del árbol
        if node is None:
            return 0
        else:
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return max(left_height, right_height) + 1

# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Calcula la altura del árbol
tree_height = tree.height()
print("La altura del árbol es:", tree_height)
