from solve_tsp import *

string1= input()
parent1 = [int(k) for k in string1.split(',')]

string2= input()
parent2 = [int(k) for k in string2.split(',')]

lower_bound = int(input())
upper_bound = int(input())

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)
8 
print(solution)