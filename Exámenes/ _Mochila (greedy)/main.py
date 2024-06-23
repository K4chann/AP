from solve import *

first_line   = input().split()
items_count  = int(first_line[0])
capacity     = int(first_line[1])

items = []

for j in range(items_count):
   parts  = input().split()
   value  = int(parts[0])
   weight = int(parts[1])
   items.append( (value, weight) )

taken, value = solve(items, capacity)

if taken:
   print(f'{sorted(taken)}:{value}')
else:
   print('No solution')
