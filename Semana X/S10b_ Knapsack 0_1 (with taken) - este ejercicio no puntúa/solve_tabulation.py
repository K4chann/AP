
import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        
        for index in range(1, len(items) + 1):
            for weight in range(1, len(table[0])):
                if (wi := items[index - 1].weight) <= weight:
                    table[index][weight] = max(
                        table[index - 1][weight],
                        table[index - 1][weight - wi] + items[index - 1].value
                    )
                else:
                    table[index][weight] = table[index - 1][weight]
        return table[-1][-1]

    def fill_taken():
        index = len(table) - 1
        weight = len(table[0]) - 1
        
        while index > 0 and weight > 0:
            if table[index][weight] != table[index - 1][weight]:
                taken.insert(0, index)
                index, weight = index - 1, weight - items[index - 1].weight
            else:
                index -= 1

    max_benefit = fill_table()
    fill_taken()
    return max_benefit, taken
