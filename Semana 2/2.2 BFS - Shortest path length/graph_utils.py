import networkx as nx

def build_graph(input):
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """

    first_line = input[0]
    # first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[-1])

    G = nx.Graph()
    # Paso 1: Crear el grafo no-dirigido con sus vértices
    for node in range(num_nodes):
        G.add_node(node)
    
    # Paso 2: Añadirle las aristas
    for edge in input[1:]:
        # edge = input().split()
        edge = edge.split()
        G.add_edge(int(edge[0]), int(edge[1]))

    return G