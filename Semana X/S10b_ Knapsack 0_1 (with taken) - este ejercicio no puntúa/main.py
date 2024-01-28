from collections       import namedtuple
from solve_memoization import *
from solve_tabulation  import *

Item = namedtuple("Item", ['index', 'value', 'weight'])
"""
first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))
"""
items = []
with open("tests.txt", mode="r", encoding="utf-8") as fr:
    first_line = fr.read().split("\n")
    capacity = int(first_line[0].split()[-1])
    for index in range(1, len(first_line)):
        line = first_line[index].split()
        items.append(Item(index, int(line[0]), int(line[1])))

# Comenzamos programando la recurrencia mediante tabulation
value1, taken1 = solve_tabulation(items, capacity)
print(value1, taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
 
value2, taken2 = solve_memoization(items, capacity)
print(value2, taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.

# assert value1 == value2
# assert taken1 == taken2
