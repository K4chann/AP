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

        for queen_pos in range(len(c)):
            for other_q_pos in range(queen_pos + 1, len(c)):
                if c[queen_pos] == c[other_q_pos] or\
                abs(c[queen_pos] - c[other_q_pos]) == other_q_pos - queen_pos:
                    return False
                
        return True
            
    solutions_list = []

    combination_iterator = My_Iterator(num_queens, num_queens)

    # solve it here!    
    for combination in combination_iterator.next():
        if check_solution(combination):
            if len(set(combination)) == num_queens:
                solutions_list.append(combination)

    return solutions_list
