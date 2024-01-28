# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        # Primera fase: Rellenamos la lista 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        if len(items) < 0:
            return 0
            
        for n in range(len(items)):
            if n == 0:
                table.append(items[n])
            elif n == 1:
                table.append(max(items[n], table[n - 1]))
            else:
                table.append(max(table[n - 2] + items[n], table[n - 1]))
        
        return table[-1]
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        i = len(items) - 1
        b = max_benefit
        
        while i > -1 and b > 0:
            if (table[i] <= b and (i == 0 or table[i] != table[i - 1])):
                taken.insert(0, i + 1)
                b -= items[i]
            i -= 1
            
        return
        
    max_benefit = fill_table()
    fill_taken()
    return max_benefit, taken
