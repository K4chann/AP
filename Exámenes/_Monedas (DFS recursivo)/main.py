from solve import *

first_line = input().split()
num_coins  = int(first_line[0])
change     = int(first_line[1])

coins      = []
for j in range(1, num_coins+1):
   parts = input().split()
   coin  = int(parts[0])
   coins.append(coin)

solutions = solve(coins, change)

if solutions:
   print(sorted(solutions))
   
   if len(solutions) == 1:
      print('1 solución')
   else:
      print(len(solutions), 'soluciones')

else:
   print('No hay solucion')
