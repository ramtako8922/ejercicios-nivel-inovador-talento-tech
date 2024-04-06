""" Para representar la gestión de residuos en una ciudad mediante un grafo, podemos utilizar un grafo dirigido. Cada nodo del grafo representará un punto importante en la gestión de residuos, como puntos de recolección, centros de reciclaje, vertederos y puntos de generación de residuos. Las aristas del grafo representarán las rutas de recolección y transporte de residuos entre estos puntos.

Tipo de Grafo: Utilizaremos un grafo dirigido, ya que las rutas de recolección y transporte de residuos tienen una dirección específica.

Pesos en las Aristas: Los pesos en las aristas podrían representar la distancia entre los puntos, el tiempo estimado de transporte de residuos, la capacidad de manejo de residuos de cada punto, o cualquier otro factor relevante para la eficiencia en la gestión de residuos.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de puntos de recolección, centros de reciclaje, vertederos y puntos de generación de residuos en la ciudad, así como de la complejidad de las rutas de recolección y transporte entre ellos.

Conectividad: Es importante que el grafo sea conexo para garantizar que todos los puntos de la gestión de residuos estén conectados a través de rutas de recolección y transporte. Esto es fundamental para optimizar la eficiencia en la gestión de residuos y minimizar los costos y el impacto ambiental.

Escalabilidad: A medida que se agregan más puntos de gestión de residuos y se optimizan las rutas, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de rutas óptimas para recolección y transporte de residuos, la planificación de rutas para minimizar costos y tiempos, y la identificación de puntos críticos en la gestión de residuos. Algoritmos como Dijkstra o BFS pueden ser útiles para optimizar la eficiencia en la gestión de residuos. """
# Grafo representando la gestión de residuos en una ciudad
grafo_residuos = {
    'Punto de Generación 1': {'Punto de Recolecta 1': 5, 'Punto de Recolecta 2': 8},
    'Punto de Generación 2': {'Punto de Recolecta 2': 6, 'Punto de Recolecta 3': 7},
    'Punto de Recolecta 1': {'Centro de Reciclaje 1': 4, 'Vertedero 1': 10},
    'Punto de Recolecta 2': {'Centro de Reciclaje 1': 3, 'Centro de Reciclaje 2': 5},
    'Punto de Recolecta 3': {'Centro de Reciclaje 2': 2, 'Vertedero 2': 8},
    'Centro de Reciclaje 1': {'Vertedero 1': 6},
    'Centro de Reciclaje 2': {'Vertedero 2': 4},
    'Vertedero 1': {},
    'Vertedero 2': {}
}

# Mostrar el grafo
for punto, conexiones in grafo_residuos.items():
    for conexion, distancia in conexiones.items():
        print(f"{punto} -> {conexion} (Distancia: {distancia})")
