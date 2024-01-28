
def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n, w):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools

        if (key := (n, w)) in mem:
            return mem[key]

        if n <= 0:
            return 0
        
        if (wn := items[n].weight) <= w:
            r = max(t(n - 1, w), (t(n - 1, w - wn) + items[n].value))
        else:
            r = t(n - 1, w)
            
        mem[(n, w)] = r
        return r

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        
        
        return

    n = len(items)-1

    max_benefit = t(n,capacity)
    print(mem)
    fill_taken()

    return max_benefit, taken
    