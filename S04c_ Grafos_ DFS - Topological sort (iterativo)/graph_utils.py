import networkx as nx

def build_digraph_with_weights():
    """ 
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear grafo direcional con num_nodes
    G = nx.DiGraph()

    for node in range(1, num_nodes + 1):
        G.add_node(node)
        
    for _ in range(num_edges):
        data = input().split()
        G.add_edge(int(data[0]), int(data[1]), weight=data[2])

    return G
