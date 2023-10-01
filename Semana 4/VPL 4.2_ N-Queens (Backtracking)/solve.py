
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!   
    solution = [-1] * num_queens

    def is_valid_solution(solution, level):
    
        for i in range(level):
            for j in range(i + 1, level):
                if solution[i] == solution[j] or \
                abs(solution[i] - solution[j]) == j - i:
                    return False
            
        return True

    def dfs(level: int = 0):
        # Si la solución que tengo construída hasta este nivel
        # no es válida subimos al nivel anterior ('backtack')
        if not is_valid_solution(solution, level):
            return
        
        # Si tengo todos los dígitos de una solución, la proceso
        # y continúo el recorrido DFS.
        elif level == num_queens:
            # ... (código que guarda o imprime esta solución)
            solutions_list.append(solution.copy())
            return
        
        else:
            # Continúo con el recorrido en profundidad
            for digit in range(num_queens):
                solution[level] = digit # Coloco un dígito
                dfs(level + 1)          # Llamada recursiva
            
            solution[level] = -1        # Quito el dígito
            return

    dfs()

    return solutions_list
