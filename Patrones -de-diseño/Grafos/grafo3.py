def dfs(grafo, inicio):
    visitados = set()

    def dfs_recursivo(nodo):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs_recursivo(vecino)

    dfs_recursivo(inicio)
    return list(visitados)

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
resultado = dfs(grafo, inicio)
print("Recorrido DFS desde el nodo", inicio + ":", resultado)
