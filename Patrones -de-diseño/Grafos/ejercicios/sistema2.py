import networkx as nx
import matplotlib.pyplot as plt
import random

# Creamos un grafo no dirigido para representar la red de hogares
G = nx.Graph()

# Creamos un diccionario para almacenar los datos de cada hogar
hogares = {
    "Hogar A": {"consumo_agua": random.randint(1, 100), "consumo_electricidad": random.randint(1, 100)},
    "Hogar B": {"consumo_agua": random.randint(1, 100), "consumo_electricidad": random.randint(1, 100)},
    "Hogar C": {"consumo_agua": random.randint(1, 100), "consumo_electricidad": random.randint(1, 100)},
    "Hogar D": {"consumo_agua": random.randint(1, 100), "consumo_electricidad": random.randint(1, 100)},
    "Hogar E": {"consumo_agua": random.randint(1, 100), "consumo_electricidad": random.randint(1, 100)},
}

# Agregamos los nodos y sus atributos al grafo
for hogar, datos in hogares.items():
    G.add_node(hogar, consumo_agua=datos["consumo_agua"], consumo_electricidad=datos["consumo_electricidad"])

# Calculamos las similitudes entre los hogares basadas en sus atributos
for hogar1 in hogares.keys():
    for hogar2 in hogares.keys():
        if hogar1 != hogar2:
            similitud = abs(hogares[hogar1]["consumo_agua"] - hogares[hogar2]["consumo_agua"]) + \
                        abs(hogares[hogar1]["consumo_electricidad"] - hogares[hogar2]["consumo_electricidad"])
            G.add_edge(hogar1, hogar2, similitud=similitud)

# Dibujamos el grafo
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'similitud')
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Red de Consumo de Recursos por Hogares")
plt.axis("off")
plt.show()
