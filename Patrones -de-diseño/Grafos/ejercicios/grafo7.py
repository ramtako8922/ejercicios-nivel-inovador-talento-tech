""" Tipo de Grafo: En este caso, utilizaremos un grafo dirigido, ya que las rutas de contaminación tienen una dirección específica, desde las fuentes de emisión hacia las áreas afectadas.

Pesos en las Aristas: Es importante asignar pesos a las aristas para representar la intensidad de la contaminación en cada ruta. Estos pesos podrían representar la cantidad de contaminantes emitidos, la distancia recorrida por los contaminantes, la sensibilidad del área afectada, etc.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de fuentes de emisión, puntos de monitoreo y áreas afectadas, así como de la complejidad de las rutas de contaminación entre ellos.

Conectividad: En este caso, es importante que el grafo sea conexo para garantizar que todas las áreas afectadas estén conectadas a al menos una fuente de emisión o punto de monitoreo.

Escalabilidad: A medida que se agregan más fuentes de emisión, puntos de monitoreo y áreas afectadas, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos optim{izados para manejar la escalabilidad del grafo.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de las rutas de contaminación más críticas, la evaluación del impacto de diferentes estrategias de mitigación y la identificación de las áreas más vulnerables. Para optimizar estas operaciones, se pueden utilizar algoritmos de búsqueda eficientes, como Dijkstra o BFS. """

# Grafo representando las rutas de contaminación
grafo_contaminacion = {
    'Fuente A': {'Punto Monitoreo 1': 5, 'Punto Monitoreo 2': 8},
    'Fuente B': {'Punto Monitoreo 2': 6, 'Punto Monitoreo 3': 7},
    'Fuente C': {'Punto Monitoreo 1': 3, 'Punto Monitoreo 3': 4},
    'Punto Monitoreo 1': {'Area A': 10, 'Area B': 12},
    'Punto Monitoreo 2': {'Area B': 9, 'Area C': 11},
    'Punto Monitoreo 3': {'Area A': 7, 'Area C': 8}
}

# Mostrar el grafo
for origen, destinos in grafo_contaminacion.items():
    for destino, peso in destinos.items():
        print(f"{origen} -> {destino} (Peso: {peso})")
