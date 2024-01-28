from solve_memoization import *
from solve_tabulation  import *

first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

# Comenzamos programando la recurrencia mediante tabulation
value1, taken1 = solve_tabulation(items)
print(value1)
print(taken1)

# Cuando termines tabulation, comenta el código anterior
# para desactivarlo (la llamada a solve_tabulation y los
# dos print) y descomenta las siguientes lineas para que
# programes la recurrencia mediante memoization.
# 
value2, taken2 = solve_memoization(items)
print(value2)
print(taken2)

# Cuando termines los dos ejercicios puedes activar estas
# lineas para comprobar que los dos dan exactamente los
# mismos resultados.
#
#assert value1 == value2
#assert taken1 == taken2
