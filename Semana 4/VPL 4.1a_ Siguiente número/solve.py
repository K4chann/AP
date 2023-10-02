
def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number 
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()

    # Añade tu código aqui
    # ...
    
    carry = 1

    for digit in range(len(next_digits) - 1, -1, -1):
        next = next_digits[digit] + carry

        carry = next // base

        if carry == 0:
            next_digits[digit] = next
            return next_digits
            
        next_digits[digit] = 0
        
    return next_digits
