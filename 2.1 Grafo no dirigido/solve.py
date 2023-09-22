import networkx as nx

def build_graph():
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """

    # Sabemos que el formato de los ficheros de entrada es el siguiente: "int1 int2"
    # Pedimos la primera línea, que contendrá el número de nodos y el número de aristas
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Creamos un grafo para posteriormente añadirle los nodos
    G = nx.Graph()
    # Paso 1: Crear el grafo no-dirigido con sus vértices
    for node in range(1, num_nodes + 1):   # El rango es de 1 a el último nodo mas 1, ya que nuestros nodos tienen que empezar en el 1, y no en el 0
        G.add_node(node) # En cada iteración vamos añadiendo el nodo al GRAFO

    # Ahora le añadimos las aristas, sabemos que el formato ("int1 int2") indica que int1 se une con int2 o viceversa, eso no es relevante ya que es un GRAFO NO DIRIIGDO
    for edge in range(num_edges):
        # Paso 2: Añadirle las aristas
        line = input().split() # Pedimos la línea que indica qué nodo se une con qué nodo y la spliteamos, teniendo ["int1", "int2"]
        G.add_edge(int(line[0]), int(line[1])) # Finalmente vamos añadiendo éstas aristas, pero convertidas a int(), ya que los nodos los añadimos de tipo int() al iterar un range()

    # En este punto el GRAFO ya está creado con sus nodos y aristas correspondientes, simplemente lo retornamos
    return G
    
