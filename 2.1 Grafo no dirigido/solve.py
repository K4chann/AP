import networkx as nx

def build_graph():
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    G = nx.Graph()
    # Paso 1: Crear el grafo no-dirigido con sus vértices
    for node in range(1, num_nodes + 1):
        G.add_node(node)
    
    # Paso 2: Añadirle las aristas
    for edge in range(num_edges):
        line = input().split()
        G.add_edge(int(line[0]), int(line[1]))


    return G
    