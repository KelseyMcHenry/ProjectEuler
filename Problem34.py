"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial


def sum_of_factorial_of_digits(number):
    sum = 0
    for i in [int(digit) for digit in str(number)]:
        sum += factorial(i)
    return sum


print(sum([i for i in range(10, 999999) if sum_of_factorial_of_digits(i) == i]))
