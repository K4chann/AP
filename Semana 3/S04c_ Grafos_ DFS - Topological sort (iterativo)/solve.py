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
        nonlocal N # Es necesario definir N como "nonlocal", ya que a la hora de usar una varibale con su mismo nombre, ésta se reinicializa
        #  1. Añade código aqui # No es necesario definir el resto de variables utilizadas como "s" (Stack()) u "order" (dict()) ya que solo estamos usando métodos en ellas, no asignando valores
        s.push(u)
        
        while not s.isEmpty():
            
            node = s.peek() # Usamos peek() para no sacar el elemento de la pila todavía, sino cuando sea absolutamente necesaria su asignación en el orden topológico
            visibleNodes.add(node)

            # Si el nodo visualizado tiene sucesores no visualizados, se añaden a la pila
            for neighbor in G.successors(node):
                if neighbor not in visibleNodes:
                    s.push(neighbor)

            # Si el último elemento de la pila es el mismo elemento que hemos mirado al principio de la iteración,
            # significa que ese nodo no tiene más sucesores, por lo que podemos asignarle un orden
            if s.peek() == node:
                order[s.pop()] = N
                N -= 1

    #  2. Añade código también aqui
    s = Stack()
    # Recorremos todos los nodoa del grafo y llamamos a la función dfs_iterative(node) para procesarlo
    for node in G:
        if node not in visibleNodes:
            dfs_iterative(node)
    
    return order
