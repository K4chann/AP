import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    q = Queue()
    
    distance[first_node] = 0
    visitados = set()
    q.enqueue(first_node)
    
    while not q.isEmpty():
         
        node = q.dequeue()
        visitados.add(node)
         
        neighbors = set(graph.neighbors(node))
         
        for neighbor in neighbors:
            current_distance = distance[node]
            
            if neighbor not in visitados:
                t_distance = current_distance + 1
                if t_distance < distance[neighbor]:
                    distance[neighbor] = t_distance
                
                q.enqueue(neighbor)
    

    return distance
