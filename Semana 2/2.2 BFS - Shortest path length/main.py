import networkx  as nx

from graph_utils import *
from solve       import *

# Añade al fichero graph_utils.py la rutina que has creado
# en el ejercicio anterior para crear el grafo: build_graph().

with open("input.txt", mode="r", encoding="utf-8") as fr:
    input = fr.read().strip().split("\n")

graph = build_graph(input)

first_node = 0
distances = bfs_path_length(graph, first_node)

ordered_distances = dict(sorted(distances.items()))
print(ordered_distances)
