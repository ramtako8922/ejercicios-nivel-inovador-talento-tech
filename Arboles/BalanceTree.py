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

    def is_balanced(self):
        """
        Verifica si el árbol binario está balanceado.
        Devuelve True si está balanceado, False en caso contrario.
        """
        return self._is_balanced_recursive(self.root) != -1

    def _is_balanced_recursive(self, node):
        """
        Función auxiliar recursiva para verificar el balance del árbol.
        Devuelve la altura del árbol si está balanceado, -1 si no lo está.
        """
        if node is None:
            return 0
        
        left_height = self._is_balanced_recursive(node.left)
        right_height = self._is_balanced_recursive(node.right)
        
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
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
tree.insert(9)

# Verificar si el árbol está balanceado
if tree.is_balanced():
    print("El árbol está balanceado.")
else:
    print("El árbol no está balanceado.")
