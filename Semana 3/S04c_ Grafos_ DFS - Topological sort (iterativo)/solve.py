import networkx as nx
from simple_stack import Stack

def dfs_topological_sort(G: nx.DiGraph):
    """
    Compute one topological sort of the given G.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = G.number_of_nodes()
    
    visibleNodes = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------

    def dfs_iterative(u):
        nonlocal N
        #  1. Añade código aqui
        s.push(u)
        
        while not s.isEmpty():
            
            node = s.peek()
            visibleNodes.add(node)
            
            for neighbor in G.successors(node):
                if neighbor not in visibleNodes:
                    s.push(neighbor)
            
            if s.peek() == node:
                order[s.pop()] = N
                N -= 1

    #  2. Añade código también aqui
    s = Stack()
    for node in G:
        if node not in visibleNodes:
            dfs_iterative(node)
    
    return order
