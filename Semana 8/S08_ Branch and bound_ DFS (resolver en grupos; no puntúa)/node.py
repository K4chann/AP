from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room

    def estimate(self, items):
        if self.room < 0:
            return 0
            
        rs = 0
        
        for item in items:
            rs += item.value
        
        for index in range(1, self.index + 1):
            if index not in self.taken:
                rs -= items[index - 1].value
        
        return rs
