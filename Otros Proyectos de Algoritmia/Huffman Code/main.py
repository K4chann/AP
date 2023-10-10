from node import Node


def solve_huffman_code(input_text: str) -> dict:
    """Solves the Huffman Code of every character in the given text.

    Parameters:
        input_text (str): the text given to assign a Huffman code to every character
    
    Returns:
        dict: a dictionarie containing every character with its Huffman Code
    """

    # Delcaración de variables requeridas
    input_text = list(input_text.lower().replace(" ", ""))
    letres = dict()
    nodes = []
    tree_root = None

    # Calculamos las frecuencias de cada carácter
    for letre in input_text:
        if letre not in letres.keys():
            letres[letre] = input_text.count(letre)

    # letres = {"a": 12, "b": 2, "c": 7, "d": 13, "e": 14, "f": 85}

    # Creamos los nodos con cada carácter
    for letre, freq in letres.items():
        nodes.append(Node(freq, letre))

    # Ordenamos los nodos de mayor a menor frecuencia
    nodes.sort(key=lambda item:item.freq, reverse=True)

    while bool(nodes):
        items = [nodes.pop(), nodes.pop()]                           # Obtenemos los dos nodos de menor frecuencia                 
        new_freq = items[0].freq + items[1].freq                     # Calculamos la nueva frecuencia del nodo raíz
        root = Node(new_freq, None, children=[items[0], items[1]])   # Creamos el nuevo nodo raízcon los dos nodos de menos frecuencia
        tree_root = root                                             # Dicho nodo raíz, será ahora la raíz del árbol

        # Si nodes no está vacía, añadimos el nuevo nodo raíz para su procesamiento
        if bool(nodes):
            nodes.append(root)
            # Volvemos a ordenar los nodos de mayor a menor frecuencia
            nodes.sort(key=lambda item:item.freq, reverse=True)

    # Creamos una cola para generar los códigos de Huffman y añadimos el nodo raíz con un 'prefijo' por defecto
    queue = []
    queue.append([tree_root, ""])
    rs = dict() # En ésta variable se almacenarán los resultados
    
    # Mientras la cola no esté vacía...
    while queue:
        item = queue.pop()                  # Obtenemos el último item de la cola
        prefix = item[1] + "0"              # Al prefijo, le añadimos "0", ya que el primer elemento será el nodo izquierdo
        node = item[0]                      # Añadimos a node el nodo

        # Recorremos los hijos del nodo
        for kid in node.children:
            if kid.letre is not None:       # Si el nodo tiene un carácter asignado...
                rs[kid.letre] = prefix      # Añadimos a los resultados el carácter con su código Huffman (prefijo)

            queue.append([kid, prefix])     # Añadimos a la cola el nodo hijo con su prefijo hasta ahora
            prefix = prefix[:-1] + "1"      # Cambiamos el último dígito del prefijo por el del nodo derecho (1) para su posterior asignación
        
    return dict(sorted(rs.items()))


##############################################################################################
# ÉSTE BLOQUE DE CÓDIGO SERÁ USADO PARA REALIZAR PRUEBAS. CÁMBIESE A DISPOSICIÓN DEL USUARIO #
##############################################################################################
if __name__ == "__main__":
    with open("input/huffman.txt", mode="r", encoding="utf-8") as fr:
        print(
            solve_huffman_code(fr.read())
        )
##############################################################################################
# ÉSTE BLOQUE DE CÓDIGO SERÁ USADO PARA REALIZAR PRUEBAS. CÁMBIESE A DISPOSICIÓN DEL USUARIO #
##############################################################################################
