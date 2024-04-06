""" Tipo de Grafo: Utilizaremos un grafo dirigido, ya que las acciones de restauración pueden tener una dirección específica de una área a otra.

Pesos en las Aristas: Los pesos en las aristas podrían representar el costo de las acciones de restauración, la efectividad estimada de la restauración en cada área, o cualquier otro factor relevante para la restauración del ecosistema.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de áreas de recuperación en el ecosistema y la cantidad de acciones de restauración entre ellas. En un ecosistema con muchas áreas de recuperación y acciones de restauración, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todas las áreas de recuperación estén conectadas a través de acciones de restauración. Esto es fundamental para coordinar y planificar eficazmente la restauración del ecosistema degradado.

Escalabilidad: A medida que se agregan más áreas de recuperación y se realizan más acciones de restauración, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de áreas de recuperación clave para la restauración del ecosistema, la planificación de acciones de restauración efectivas y la evaluación del progreso de la restauración en todo el ecosistema. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad de la red de áreas de recuperación. """

# Grafo representando la red de áreas de recuperación y acciones de restauración
red_recuperacion = {
    'Área A': {'Área B': 5, 'Área C': 8},
    'Área B': {'Área D': 6},
    'Área C': {'Área D': 7},
    'Área D': {}
}

# Mostrar el grafo
for area, acciones in red_recuperacion.items():
    for accion, costo in acciones.items():
        print(f"{area} -> {accion} (Costo de la acción: {costo})")
