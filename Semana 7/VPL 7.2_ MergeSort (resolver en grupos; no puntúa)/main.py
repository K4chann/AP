from solve import *
"""
first_line = input().split()
numValues  = int(first_line[0])
"""

with open("input.txt", mode = "r", encoding = "utf-8") as fr:
    first_line = fr.read().split()

items = []
"""
for j in range(1, numValues+1):
    parts      = input().split()
    items.append (int(parts[0]))
"""

for item in first_line:
    items.append(int(item))

rs = solve(items)

print(items)