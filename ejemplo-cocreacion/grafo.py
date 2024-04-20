import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Añadir nodos
G.add_node("Área Protegida")
G.add_node("Especie")
G.add_node("Actividad")

# Añadir aristas
G.add_edge("Actividad", "Área Protegida")
G.add_edge("Especie", "Área Protegida")

# Dibujar el grafo
nx.draw(G, with_labels=True)
plt.show()
