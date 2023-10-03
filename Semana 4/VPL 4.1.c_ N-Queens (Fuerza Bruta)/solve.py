from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    def check_solution(c):

        # Itero por índices la lista pasada como parámetro (una combinaicón)
        for queen_pos in range(len(c)):
            # Manteniendo la posición de la reina, itero nuevamente el resto de reinas posteriores
            for other_q_pos in range(queen_pos + 1, len(c)):
                # Compruebo que la reina2 no esté en la misma columna o diagonal que la reina1
                if c[queen_pos] == c[other_q_pos] or\
                abs(c[queen_pos] - c[other_q_pos]) == other_q_pos - queen_pos:
                    # Las reinas están en la misma columna o en la misma diagonal, retorno False
                    return False

        # He acabado de iterar las reinas y no he tenido ningún problema, itero True
        return True
            
    solutions_list = []

    combination_iterator = My_Iterator(num_queens, num_queens)

    # solve it here!    
    # Iteramos todas las combinaciones posibles
    for combination in combination_iterator.next():
        # Llamo a check_solution() para verificar el resultado
        if check_solution(combination):
            # Comprobamos si la solución tiene un tamaño adecuado (no es necesario)
            if len(set(combination)) == num_queens:
                # Añado la combinación al resto de soluciones
                solutions_list.append(combination)

    return solutions_list
