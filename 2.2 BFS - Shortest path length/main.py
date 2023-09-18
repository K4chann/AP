import networkx  as nx

from graph_utils import *
from solve       import *

# Añade al fichero graph_utils.py la rutina que has creado
# en el ejercicio anterior para crear el grafo: build_graph().
graph = build_graph();

first_node = 1
distances = bfs_path_length(graph, first_node)

ordered_distances = dict(sorted(distances.items()))
print(ordered_distances)