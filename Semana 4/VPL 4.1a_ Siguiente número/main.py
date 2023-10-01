from solve import *

first_line = input().split()
num_values = int(first_line[0])
base       = int(first_line[1])

for j in range(num_values):
    data = input()

    # Convertimos la string en la lista que contiene
    # el número de entrada.
    digits = []
    for digit in data:
        digits.append(int(digit))

    # Mostramos la lista con el número de entrada y
    # la lista con el siguiente número.
    print(digits, '- ', end="")
    print(next_number(digits, base))
