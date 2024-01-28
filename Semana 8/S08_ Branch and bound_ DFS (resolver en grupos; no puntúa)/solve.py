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

    # 1) Creamos el nodo raiz.
    # ...
    node0 = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(node0)
    
    best_value = 0
    best_taken = []

    # Mientras haya nodos en la lista de nodos vivos
    # ...
    while alive:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.
        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        # Condiciones de poda
        # ...
        if current.room <= 0:
            continue

        if current.estimate(items) < best_value:
            continue

        if current.value > best_value:
            best_value = current.value
            best_taken = current.taken

        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        if current.index != len(items):
            right = Node(current.index + 1, current.taken, current.value, current.room)
            left_taken = current.taken.copy()
            left_taken.append(current.index + 1)
            left_value = current.value + items[current.index].value
            left_room = current.room - items[current.index].weight
            left = Node(current.index + 1, left_taken, left_value, left_room)
            alive.append(right)
            alive.append(left)

    return best_value, best_taken, visiting_order