from networkx import *

def solve(graph, from_node, to_node):
    value = 0
    taken = []
    # Inicializo la memoria con el nodo de comienzo, el formato es el siguiente:
    # ((nodo procedente, nodo al que se dirige la arista), valor mínimo hasta el momento)
    mem = {7: ((None, 7), 0)}
    
    def dist(u, v):
        # Aquí se guardarán todas las distancias de los nodos predecesores a v.
        solutions = []
        
        # Si v (el nodo al que se quiere ir), es el mismo que el nodo de comienzo, se entiende
        # que su distancia mínima es 0.
        if v == from_node:
            return 0

        for predecessor in graph.predecessors(v):
            solutions.append(
                (
                    (predecessor, v),
                    dist(v, predecessor) + graph[predecessor][v]['weight']      # Ecuación de la recurrencia: dist(u) + l(u, v)
                )
            )
        
        # Si solutions está vacía, hemos llegado a un nodo sin predecesores pero no se trata
        # del nodo de comienzo.
        if not solutions:
            mem[v] = [(v, u), graph[v][u]['weight']]
            return mem[v][1]
        
        # Se obtiene la solución cuyo valor de distancia hasta el momento es mínimo.
        minimum = min(solutions, key=lambda item:item[1])
        # Se guarda el la memoria y se retorna el valor de la distancia.
        mem[v] = minimum
        
        return minimum[1]
        
    dist(to_node, to_node)
    
    # Se extrae de la memoria la información asociada al nodo destino,
    # la cual contendrá el nodo del que se viene y la distancia mínima conseguida hasta el nodo final.
    data = mem[to_node]
    taken.append(data[0][1]) # Añadimos el nodo destino a los taken
    value = data[1] # Establecemos como solución el valor mínimo final obtenido en el nodo destino.
    
    # En bucle, estaremos yendo hacia atrás visitando los nodos de los que se
    # proviene e introduciéndolos en los taken.
    while True:
        u, v = data[0]
        taken.insert(0, u)
        
        # Si el nodo del que se proviene ha sido el nodo de comienzo, se acaba el bucle.
        if u == from_node:
            break
        
        data = mem[u]
    
    return value, taken
