import networkx as nx
from solve import *

graph = build_digraph_with_weights()

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges(data=True))

# Paso 3 (Opcional): Utilizando PyCharm añade aqui el código
#         necesario para mostrar gráficamente el grafo.
# ...
