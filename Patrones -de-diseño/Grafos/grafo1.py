def detectar_ciclo(grafo):
    visitados = set()
    en_proceso = set()

    def dfs(nodo):
        if nodo in en_proceso:
            return True  # Ciclo detectado
        if nodo in visitados:
            return False  # Nodo ya visitado, no hay ciclo

        en_proceso.add(nodo)
        #Revisa los nodos con lo cuales conecta
        for vecino in grafo[nodo]:
            if dfs(vecino):
                return True  # Ciclo detectado en el subárbol
        en_proceso.remove(nodo)
        visitados.add(nodo)
        return False

    for nodo in grafo:
        if dfs(nodo):
            return True  # Ciclo detectado
    return False  # No hay ciclo

# Ejemplo de uso
grafo_con_ciclo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['A'],
    'E': []
}

grafo_sin_ciclo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(detectar_ciclo(grafo_con_ciclo))  # True
print(detectar_ciclo(grafo_sin_ciclo))  # False
