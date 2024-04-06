import heapq

def dijkstra(grafo, inicio):
    distancia = {nodo: float('infinity') for nodo in grafo}
    distancia[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        if distancia_actual > distancia[nodo_actual]:
            continue
        for vecino, peso in grafo[nodo_actual].items():
            distancia_total = distancia_actual + peso
            if distancia_total < distancia[vecino]:
                distancia[vecino] = distancia_total
                heapq.heappush(cola, (distancia_total, vecino))

    return distancia

# Uso del algoritmo
grafo_ponderado = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
inicio = 'A'
distancias = dijkstra(grafo_ponderado, inicio)
print("Distancias desde el nodo", inicio + ":", distancias)