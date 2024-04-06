class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        xr, yr = self.encontrar(x), self.encontrar(y)
        if xr == yr:
            return False
        if self.rango[xr] < self.rango[yr]:
            xr, yr = yr, xr
        self.padre[yr] = xr
        if self.rango[xr] == self.rango[yr]:
            self.rango[xr] += 1
        return True

def arbol_expansion_minima(grafo):
    nodos = {nodo: indice for indice, nodo in enumerate(grafo)}
    aristas = []
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            aristas.append((peso, nodos[nodo], nodos[vecino]))
    aristas.sort()

    arbol = {}
    union_find = UnionFind(len(grafo))
    for peso, u, v in aristas:
        if union_find.unir(u, v):
            if u not in arbol:
                arbol[u] = {}
            arbol[u][v] = peso
            if v not in arbol:
                arbol[v] = {}
            arbol[v][u] = peso

    return arbol

# Uso del algoritmo
grafo_ponderado = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
arbol = arbol_expansion_minima(grafo_ponderado)
print("Árbol de Expansión Mínima:", arbol)
