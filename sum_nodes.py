# Definición de la clase Node para representar un nodo en el árbol
class Node:
    def __init__(self, value):
        # Cada nodo tiene un valor y referencias a los nodos izquierdo y derecho
        self.value = value
        self.left = None
        self.right = None

# Definición de la clase BinaryTree para representar un árbol binario
class BinaryTree:
    def __init__(self):
        # Inicialización de la raíz del árbol como None
        self.root = None

    def insert(self, value):
        # Función para insertar un nuevo nodo en el árbol
        if self.root is None:
            # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
            self.root = Node(value)
        else:
            # Si el árbol no está vacío, se llama a la función de inserción recursiva
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Función recursiva para insertar un nuevo nodo en el árbol
        if value < current_node.value:
            # Si el valor es menor que el valor del nodo actual, se inserta en el subárbol izquierdo
            if current_node.left is None:
                # Si el subárbol izquierdo es None, se crea un nuevo nodo
                current_node.left = Node(value)
            else:
                # Si el subárbol izquierdo no es None, se llama a la función recursiva con el nodo izquierdo como nodo actual
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            # Si el valor es mayor que el valor del nodo actual, se inserta en el subárbol derecho
            if current_node.right is None:
                # Si el subárbol derecho es None, se crea un nuevo nodo
                current_node.right = Node(value)
            else:
                # Si el subárbol derecho no es None, se llama a la función recursiva con el nodo derecho como nodo actual
                self._insert_recursive(current_node.right, value)

    def sum_nodes(self, node):
        """
        Función recursiva que suma los valores de todos los nodos del árbol.
        """
        if node is None:
            # Si el nodo es None, la suma es 0
            return 0
        # Se suma el valor del nodo actual con las sumas recursivas de los subárboles izquierdo y derecho
        return node.value + self.sum_nodes(node.left) + self.sum_nodes(node.right)

# Creación de un árbol binario de ejemplo
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

# Suma de los nodos del árbol
total_sum = tree.sum_nodes(tree.root)
print("La suma de los nodos es:", total_sum)
