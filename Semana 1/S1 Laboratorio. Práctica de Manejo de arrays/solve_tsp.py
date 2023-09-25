def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = parent1[lower_bound:upper_bound]
    index = upper_bound
    search_index = upper_bound
    parents_len = len(parent2)
    parent_gens = set(child1)

    while index < parents_len:
        if search_index == parents_len:
            search_index = 0
            
        child_item = parent2[search_index]

        if child_item not in parent_gens:
            child1.insert(index, child_item)
            index += 1
            
        search_index += 1

    index = 0

    while index < lower_bound:
        child_item = parent2[search_index]

        if child_item not in parent_gens:
            child1.insert(index, child_item)
            index += 1

        search_index += 1
            
    return child1
