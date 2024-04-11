""" Tipo de Grafo: Utilizaremos un grafo no dirigido, ya que la comunicación entre sensores es bidireccional.

Pesos en las Aristas: En este caso, los pesos en las aristas podrían representar la calidad de la conexión entre los sensores adyacentes, como la intensidad de la señal o la fiabilidad de la comunicación.

Densidad del Grafo: La densidad del grafo dependerá de la distancia entre los sensores y la frecuencia de comunicación entre ellos. En una red densa, cada sensor estaría conectado a muchos otros sensores, mientras que en una red dispersa, los sensores tendrían menos conexiones.

Conectividad: Para monitorear cambios ambientales de manera efectiva, es importante que la red de sensores sea conectada, 
de modo que la información pueda fluir libremente entre los sensores.

Escalabilidad: A medida que se agregan más sensores a la red, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos y algoritmos eficientes para manejar la escalabilidad de la red.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir la identificación de rutas óptimas para transmitir información entre sensores, la detección de sensores defectuosos o la identificación de áreas con mayor concentración de sensores. Para optimizar estas operaciones, se pueden utilizar algoritmos 
de búsqueda eficientes, como Dijkstra o BFS. """
# Grafo representando la red de sensores ambientales
red_sensores = {
    'Sensor 1': {'Sensor 2': 5, 'Sensor 3': 8},
    'Sensor 2': {'Sensor 1': 5, 'Sensor 4': 6, 'Sensor 5': 7},
    'Sensor 3': {'Sensor 1': 8, 'Sensor 6': 9},
    'Sensor 4': {'Sensor 2': 6, 'Sensor 7': 10},
    'Sensor 5': {'Sensor 2': 7, 'Sensor 8': 11},
    'Sensor 6': {'Sensor 3': 9, 'Sensor 9': 12},
    'Sensor 7': {'Sensor 4': 10, 'Sensor 10': 13},
    'Sensor 8': {'Sensor 5': 11, 'Sensor 10': 14},
    'Sensor 9': {'Sensor 6': 12},
    'Sensor 10': {'Sensor 7': 13, 'Sensor 8': 14}
}

# Mostrar el grafo
for sensor, conexiones in red_sensores.items():
    for conexion, distancia in conexiones.items():
        print(f"{sensor} <-> {conexion} (Distancia: {distancia})")