from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []
    
    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...

    node0 = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(node0)

    # Mientras haya nodos en la lista de nodos vivos
    # ...
    while alive:  #sustituir el True por la condición que considere más adecuada
        
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        if current.index == len(items):
            continue
        
        right = Node(current.index + 1, [], current.value, current.room)
        left = Node(current.index + 1, [], current.value, current.room)
        alive.append(right)
        alive.append(left)

    return 0, [], visiting_order