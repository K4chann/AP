from solve import *

first_line   = input().split()
num_digits = int(first_line[0])
base       = int(first_line[1])

obj = My_Iterator(num_digits, base)
for c in obj.next():
     print(c)
