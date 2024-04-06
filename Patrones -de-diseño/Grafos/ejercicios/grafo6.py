""" Tipo de Grafo: En este caso, podemos considerar un grafo no dirigido, ya que las relaciones entre los elementos del ecosistema (plantas y animales) no necesariamente son unidireccionales. Por ejemplo, una planta puede ser consumida por un animal, pero también puede haber interacciones simbióticas donde ambas se benefician mutuamente.

Pesos en las Aristas: Para representar la intensidad de las relaciones, como la dependencia alimentaria o la importancia ecológica, es importante asignar pesos a las aristas. Estos pesos pueden representar la cantidad de energía transferida, la frecuencia de interacción, la importancia en la cadena alimentaria, etc.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de relaciones entre las especies. En un ecosistema complejo, es probable que 
haya muchas relaciones, lo que haría que el grafo sea más denso. Sin embargo, también puede haber relaciones más específicas que resulten en un grafo más disperso.

Conectividad: En un ecosistema real, es posible que existan componentes desconectados, como diferentes 
hábitats separados geográficamente. Sin embargo, para este ejercicio, podríamos considerar un grafo conexo para simplificar el análisis de las relaciones entre las especies.

Escalabilidad: A medida que se agregan más nodos (especies) y aristas (relaciones), la complejidad del grafo aumentará. Para manejar la escalabilidad, es importante utilizar estructuras de datos eficientes y algoritmos optimizados para realizar operaciones en el grafo.

Eficiencia en Búsquedas: En el contexto de la gestión ambiental, las operaciones de búsqueda comunes pueden incluir la identificación de cadenas alimenticias, la detección de especies clave en el ecosistema y la evaluación de la vulnerabilidad del ecosistema a perturbaciones. Para optimizar estas operaciones, se pueden utilizar algoritmos de búsqueda eficientes, como DFS o BFS. """

# Grafo representando un ecosistema simple
ecosistema = {
    'Planta A': {'Herbívoro 1', 'Herbívoro 2'},
    'Planta B': {'Herbívoro 2', 'Herbívoro 3'},
    'Herbívoro 1': {'Carnívoro 1'},
    'Herbívoro 2': {'Carnívoro 1', 'Carnívoro 2'},
    'Herbívoro 3': {'Carnívoro 2'}
}

# Mostrar el grafo
for especie, relaciones in ecosistema.items():
    print(f"{especie} -> {', '.join(relaciones)}")
