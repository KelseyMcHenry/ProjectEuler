"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from HelperFunctions import digits_in_int

solved = False
x = 1
while not solved:
    values = [2 * x, 3 * x, 4 * x, 5 * x, 6 * x]
    digits_in_values = [digits_in_int(val) for val in values]
    if all(digit_list == digits_in_values[0] for digit_list in digits_in_values):
        print(x)
        solved = True
    x += 1
