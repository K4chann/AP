import networkx as nx
from simple_stack import Stack
import random

def dfs_topological_sort(G):
    """
    Compute one topological sort of the given graph.
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
    
    visibles = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------
        
    s = Stack()
    order = {node: None for node in G.nodes()}
    s.push(
        list(G.nodes())[random.randint(0, len(G) - 1)]
    )
    i = 0

    while not s.is_empty():
        i += 1
        node = s.peek()
        visibles.add(node)

        for neighbor in G.successors(node):
            i += 1
            if neighbor not in visibles:
                s.push(neighbor)
            
        if s.peek() == node:
            G.remove_node(node)
            s.pop()
            order[node] = N
            N -= 1
        
        if s.is_empty() and bool(G):
            s.push(
                next(iter(G.nodes()))
            )

    return order
