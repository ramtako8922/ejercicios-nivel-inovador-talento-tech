def bfs(grafo, inicio):
    visitados = set()
    cola = [inicio]
    recorrido = []

    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in grafo[nodo]:
                cola.append(vecino)

    return recorrido

# Grafo dado
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

inicio = 'A'
resultado = bfs(grafo, inicio)
print("Recorrido BFS desde el nodo", inicio + ":", resultado)
