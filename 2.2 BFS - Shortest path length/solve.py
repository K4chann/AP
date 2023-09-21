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
    visited = set()                  # (visited) Este conjunto nos permitirá saber los nodos que hemos visitado
    visibles = set()                 # (visibles) Este conunto nos permitirá saber los nodos que hemos podido ver,
    q.enqueue(first_node)            # sin necesidad de que hayan sido visitados.
    
    while not q.isEmpty():
         
        node = q.dequeue()
        visited.add(node)
         
        for neighbor in graph.neighbors(node):
            current_distance = distance[node]
            
            if neighbor not in visited and neighbor not in visibles: # Aunque esta comprobación de not in visited & not in visibles parezca innecesaria,
                t_distance = current_distance + 1                    # para un grafo de 8 nodos y 14 aristas pasa de 25 iteraciones a sólo 8 iteraciones.

                if t_distance < distance[neighbor]:                  # Calculamos una distancia tentativa, aunque se pueda hacer solo comprobando si distance[neighbor] == 'inf'
                    distance[neighbor] = t_distance                  # así podremos dejar el código enfocado para expandirlo al algoritmo de Dijkstra.
                
                q.enqueue(neighbor)
                visibles.add(neighbor)
    

    return dict(sorted(distance.items()))
