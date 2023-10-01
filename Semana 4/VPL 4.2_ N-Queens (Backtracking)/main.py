from solve import *

first_line = input().split()
num_queens = int(first_line[0])

solutions_list = solve(num_queens)

for solution in solutions_list:
    print(solution)