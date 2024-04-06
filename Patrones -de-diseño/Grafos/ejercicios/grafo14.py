""" Tipo de Grafo: Utilizaremos un grafo no dirigido, ya que la comunicación entre estaciones de monitoreo es bidireccional.

Pesos en las Aristas: Los pesos en las aristas podrían representar la calidad de la conexión entre las estaciones, la distancia entre ellas, la cantidad de datos transferidos o cualquier otro factor relevante para el monitoreo atmosférico.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de estaciones de monitoreo en la ciudad y la cantidad de conexiones entre ellas. En una ciudad con una red extensa de estaciones, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todas las estaciones estén conectadas entre sí. Esto es fundamental para recopilar datos de monitoreo de manera efectiva en toda la ciudad.

Escalabilidad: A medida que se agregan más estaciones de monitoreo a la red, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de estaciones más cercanas a un punto específico, la optimización de rutas de comunicación entre estaciones y la evaluación de la cobertura de la red de monitoreo. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad de la red de estaciones. """

# Grafo representando la red de estaciones de monitoreo atmosférico
red_monitoreo = {
    'Estación A': {'Estación B': 5, 'Estación C': 8},
    'Estación B': {'Estación A': 5, 'Estación D': 6},
    'Estación C': {'Estación A': 8, 'Estación D': 7},
    'Estación D': {'Estación B': 6, 'Estación C': 7}
}

# Mostrar el grafo
for estacion, conexiones in red_monitoreo.items():
    for conexion, calidad in conexiones.items():
        print(f"{estacion} <-> {conexion} (Calidad de la conexión: {calidad})")
