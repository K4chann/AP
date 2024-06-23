def solve(items, capacity):
    taken = []
    value = 0
    
    items = sorted(
        enumerate(items), key=lambda x: x[1][0] / x[1][1], reverse=True
    )
    
    for index, (v, w) in items:
        if w <= capacity:
            capacity -= w
            value += v
            taken.append(index + 1)
    
    return taken, value
