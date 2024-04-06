""" Tipo de Grafo: Utilizaremos un grafo no dirigido, ya que las rutas de migración pueden ser bidireccionales y las especies pueden moverse en ambas direcciones.

Pesos en las Aristas: Los pesos en las aristas podrían representar la importancia de las rutas de migración para diferentes especies, la distancia entre las áreas geográficas o la facilidad de migración a lo largo de cada ruta.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de áreas geográficas y la frecuencia y variedad de las rutas de migración entre ellas. En áreas con una gran diversidad de especies y hábitats conectados, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todas las áreas geográficas estén conectadas a través de rutas de migración. Esto es fundamental para facilitar el flujo genético y la dispersión de especies en el paisaje.

Escalabilidad: A medida que se agregan más áreas geográficas y se recopilan más datos sobre las rutas de migración, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de rutas de migración clave para especies en peligro, la evaluación del impacto de la fragmentación del hábitat en la conectividad del paisaje y la planificación de corredores biológicos para conservar la biodiversidad. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad del paisaje. """
# Grafo representando las rutas de migración de especies
grafo_migracion = {
    'Reserva A': {'Reserva B': 5, 'Reserva C': 8},
    'Reserva B': {'Reserva A': 5, 'Reserva D': 6, 'Reserva E': 7},
    'Reserva C': {'Reserva A': 8, 'Reserva F': 9},
    'Reserva D': {'Reserva B': 6, 'Reserva G': 10},
    'Reserva E': {'Reserva B': 7, 'Reserva G': 11},
    'Reserva F': {'Reserva C': 9, 'Reserva H': 12},
    'Reserva G': {'Reserva D': 10, 'Reserva E': 11},
    'Reserva H': {'Reserva F': 12}
}

# Mostrar el grafo
for area, migraciones in grafo_migracion.items():
    for migracion, distancia in migraciones.items():
        print(f"{area} <-> {migracion} (Distancia: {distancia})")
