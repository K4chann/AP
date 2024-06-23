from sys import maxsize as infinite

def solve(coins, change):
    """
    Solve function that returns the list of unique solutions that use the same number of coins
    and no coin value is repeated.
    
    :param coins: A list containing all available coins.
    :param change: The objective amount of change.
    :rtype: List[List[int]]
    :return: A list containing all the unique possible solutions.
    """
    solutions_list = [] # Lista de soluciones
    solutions_set = [] # Lista de soluciones donde las mismas son conjuntos.
                       # Se usará para una mejor búsqueda de soluciones dentro de ella.
    min_num_coins = infinite
    
    def is_valid(solution, level):
        """
        Inner function that validadtes wheter the solution at the specified
        level is valid or not and wheter that solution is a final solution or not.
        
        :param solution: A list of the current solution.
        :param level: The reached level of the current solution.
        :rtype: tuple(bool, bool)
        :return: A tuple with a boolean that determines the described statements.
        """
        current_change = 0
        current_coins = set()
        
        for index in range(level):
            current_change += coins[solution[index] - 1]
            current_coins.add(coins[solution[index] - 1])
        
        return (
            current_change <= change and \
            len(solution[:level]) == len(current_coins)
            ), current_change == change

    def dfs(solution=[-1]*len(coins), level=0):
        """
        Inner function that recursively looks for solutions of the described
        change problem.
        
        :param solution: A list with the coins that are taken at this level.
        :param level: The current level of the current solution.
        """
        nonlocal min_num_coins # Número mínimo de monedas que se usará para que todas las soluciones tengan la misma cantidad de monedas.
        
        # Validamos la solución a la vez que validamos si se ha llegado al final.
        valid, is_solution = is_valid(solution, level)
        
        if not valid or level == len(coins):
            return
        
        if is_solution:
            solution = solution[:level] # Trunco la solución hasta el nivel que he llegado.
            if (solution_set := set(solution)) not in solutions_set:
                # Si la solución no se encuentra entre las ya validadas, compruebo si la puedo coger.
                if level < min_num_coins:
                    # Si el nivel en el que estoy se ha quedado por debajo del número mínimo de monedas, reinicio las soluciones.
                    min_num_coins = level # Establezco el nuevo número mínimo de monedas.
                    solutions_list.clear()
                    solutions_set.clear()
                if level == min_num_coins:
                    # Si el nivel en el que estoy coincide con el número mínimo de monedas para formar una solución, la añado al resto.
                    solutions_list.append(solution)
                    solutions_set.append(solution_set)
            return
        
        # Voy asignando un dígito a cada nivel para ir formando las soluciones.
        for digit in range(1, len(coins) + 1):
            solution[level] = digit
            dfs(list(solution), level + 1)
            
        solution[level] = -1 # Reinicio el nivel
        
    dfs()
    
    return solutions_list if solutions_list else None
