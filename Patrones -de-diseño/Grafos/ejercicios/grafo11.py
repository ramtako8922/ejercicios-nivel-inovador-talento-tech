""" Tipo de Grafo: Utilizaremos un grafo dirigido, ya que el flujo de agua entre los cuerpos de agua tiene una dirección específica, desde fuentes más altas hacia fuentes más bajas.

Pesos en las Aristas: Los pesos en las aristas podrían representar la cantidad de agua que fluye entre los cuerpos de agua en un período de tiempo determinado. Estos pesos pueden ayudar a estimar la cantidad de contaminantes transportados o la capacidad de dilución de un cuerpo de agua.

Densidad del Grafo: La densidad del grafo dependerá de la cantidad de cuerpos de agua y la complejidad de las conexiones entre ellos. En un ecosistema acuático complejo, el grafo podría ser más denso.

Conectividad: Es importante que el grafo sea conexo para garantizar que todos los cuerpos de agua estén conectados a través del flujo de agua. Esto es fundamental para comprender cómo los contaminantes pueden moverse a través del ecosistema acuático.

Escalabilidad: A medida que se agregan más cuerpos de agua y se recopilan más datos sobre el flujo de agua, la complejidad del grafo aumentará. Es importante utilizar estructuras de datos eficientes y algoritmos escalables para manejar la información de manera efectiva.

Eficiencia en Búsquedas: Las operaciones de búsqueda frecuentes en este contexto podrían incluir 
la identificación de las fuentes de contaminación más críticas, la evaluación del impacto de diferentes medidas de gestión en la calidad del agua y la predicción de la dispersión de contaminantes en el ecosistema acuático. Algoritmos como Dijkstra o BFS pueden ser útiles para encontrar rutas óptimas y evaluar la conectividad del sistema acuático. """

# Grafo representando el flujo de agua en un ecosistema acuático
flujo_agua = {
    'Río': {'Lago': 10, 'Estanque': 5},
    'Lago': {'Estanque': 3},
    'Estanque': {}
}

# Mostrar el grafo
for cuerpo_agua, conexiones in flujo_agua.items():
    for conexion, flujo in conexiones.items():
        print(f"{cuerpo_agua} -> {conexion} (Flujo de agua: {flujo})")
