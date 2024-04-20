import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido ponderado
G = nx.DiGraph()

# Agregamos los sensores y sus conexiones con el embalse
sensores = [
    {"nombre": "Sensor A", "distancia": 10},
    {"nombre": "Sensor B", "distancia": 15},
    {"nombre": "Sensor C", "distancia": 20},
    {"nombre": "Sensor D", "distancia": 25},
    {"nombre": "Sensor E", "distancia": 30},
    {"nombre": "Sensor F", "distancia": 80},
    {"nombre": "Sensor G", "distancia": 45},
    
    
]

for sensor in sensores:
    G.add_edge("Embalse", sensor["nombre"], weight=sensor["distancia"])

# Dibujamos el grafo
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, arrows=True)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Red de Sensores de Niveles de Agua en Embalse")
plt.axis("off")
plt.show()
