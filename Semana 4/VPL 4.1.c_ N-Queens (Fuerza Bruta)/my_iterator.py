# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    # ...
    next_digits = digits.copy()

    carry = 1

    for digit in range(len(next_digits) - 1, -1, -1):
        next = next_digits[digit] + carry

        carry = next // base

        if carry == 0:
            next_digits[digit] = next
            return next_digits
        else:
            next_digits[digit] = 0
    
# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        # ...
        self.num_digits = num_digits
        self.base = base

    def next(self):
        # 2.2 Añade código aqui
        # ...
        d = [0] * self.num_digits
        d[-1] = -1

        while d != ([self.base - 1] * self.num_digits):
            d = next_number(d, self.base)
            yield d
        
        # Cuando no quedan valores simplemente retornamos
        return
