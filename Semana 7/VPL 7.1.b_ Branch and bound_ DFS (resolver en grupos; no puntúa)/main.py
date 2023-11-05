from collections import namedtuple

from node import *
from solve import *

first_line = input().split()
item_count = int(first_line[0])
capacity = int(first_line[1])
    
items = []
for i in range(1, item_count+1):
    line = input()
    parts = line.split()
    items.append(Item(i-1, int(parts[0]), int(parts[1])))

_, _, visiting_order = solve_branch_and_bound_DFS(capacity, items, True)
print(visiting_order)