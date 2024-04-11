""" Tipo de Grafo: Utilizaremos un grafo no dirigido, ya que los corredores verdes permiten la migración en ambas direcciones entre los parques y áreas verdes.

Pesos en las Aristas: Los pesos en las aristas podrían representar la longitud de los corredores verdes, la calidad del hábitat a lo largo de los corredores, la presencia de obstáculos naturales o artificiales, o cualquier otro factor relevante para la migración de especies.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de parques y áreas verdes en la ciudad, así como de la complejidad de los corredores verdes entre ellos. En una ciudad con una red extensa de corredores verdes, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todos los 
parques y áreas verdes estén conectados a través de corredores verdes. Esto es fundamental para facilitar la migración de especies y fomentar la biodiversidad en la ciudad.

Escalabilidad: A medida que se agregan más parques y áreas verdes a la red de corredores verdes, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de corredores verdes clave para la migración de especies, la evaluación del impacto de la urbanización en la conectividad de la biodiversidad y la planificación de nuevas 
áreas verdes y corredores verdes. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad de la red de corredores verdes. """

# Grafo representando la red de corredores verdes entre parques y áreas verdes
corredores_verdes = {
    'Parque A': {'Área Verde 1': 5, 'Área Verde 2': 8},
    'Área Verde 1': {'Parque A': 5, 'Área Verde 2': 6, 'Área Verde 3': 7},
    'Área Verde 2': {'Parque A': 8, 'Área Verde 1': 6},
    'Área Verde 3': {'Área Verde 1': 7}
}

# Mostrar el grafo
for area_verde, conexiones in corredores_verdes.items():
    for conexion, longitud in conexiones.items():
        print(f"{area_verde} <-> {conexion} (Longitud del corredor verde: {longitud})")
