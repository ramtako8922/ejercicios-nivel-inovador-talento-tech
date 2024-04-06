""" Tipo de Grafo: Utilizaremos un grafo no dirigido, ya que los senderos pueden ser recorridos en ambas direcciones entre los puntos de inicio y fin.

Pesos en las Aristas: Los pesos en las aristas podrían representar la longitud de los senderos, la dificultad del terreno, la presencia de puntos de interés o cualquier otro factor relevante para los visitantes de la reserva natural.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de senderos en la reserva natural y la complejidad de sus interconexiones. En una reserva con una red extensa de senderos, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todos los puntos de inicio y fin de los senderos estén conectados entre sí. Esto es fundamental para permitir a los visitantes explorar la reserva natural de manera efectiva.

Escalabilidad: A medida que se agregan más senderos a la red de senderos, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de senderos más cortos o más escénicos, la planificación de rutas para diferentes niveles de habilidad y la evaluación de la accesibilidad de la reserva natural. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad de la red de senderos. """

# Grafo representando la red de senderos en una reserva natural
red_senderos = {
    'Inicio Sendero 1': {'Fin Sendero 1': 5, 'Inicio Sendero 2': 8},
    'Inicio Sendero 2': {'Fin Sendero 2': 6, 'Inicio Sendero 1': 8},
    'Fin Sendero 1': {'Inicio Sendero 1': 5},
    'Fin Sendero 2': {'Inicio Sendero 2': 6}
}

# Mostrar el grafo
for punto_inicio, conexiones in red_senderos.items():
    for punto_fin, longitud in conexiones.items():
        print(f"{punto_inicio} <-> {punto_fin} (Longitud del sendero: {longitud})")
