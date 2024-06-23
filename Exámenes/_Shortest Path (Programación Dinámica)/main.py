import networkx  as nx
from solve       import *

first_line = input().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
from_node  = int(first_line[2])
to_node    = int(first_line[3])

graph     = nx.DiGraph()
graph.add_nodes_from(range(1,num_nodes+1))
for j in range(1, num_edges+1):
   parts = input().split()
   u = int(parts[0])
   v = int(parts[1])
   w = int(parts[2])
   graph.add_edge(u, v, weight=w)

min_d, taken = solve(graph, from_node, to_node)
print(min_d)
print(taken)
