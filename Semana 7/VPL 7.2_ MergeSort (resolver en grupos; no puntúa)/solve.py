def solve(items: list):
    """
    Sort the given list of items in ascending order
    """
    def merge(left, mid, right):
        # solve it here!
        first_half = [items[index] for index in range(left, mid + 1)]
        second_half = [items[index] for index in range(mid + 1, right + 1)]

        first_end = len(first_half)
        second_end = len(second_half)

        index_first_half = 0
        index_second_half = 0
        items_index = left

        while index_first_half < first_end and index_second_half < second_end:
            item1 = first_half[index_first_half]
            item2 = second_half[index_second_half]

            if (item1 < item2):
                index_first_half += 1
                items[items_index] = item1
            else:
                index_second_half += 1
                items[items_index] = item2
            items_index += 1
        
        while index_first_half < first_end:
            items[items_index] = first_half[index_first_half]
            index_first_half += 1
            items_index += 1

        while index_second_half < second_end:
            items[items_index] = second_half[index_second_half]
            index_second_half += 1
            items_index += 1
    
    def merge_sort(left, right):
        # solve it here!
        if left < right:
            mid = left + (right - left) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

    merge_sort(0, len(items) - 1)
    return
