"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

from HelperFunctions import digits_in_int

max_val = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum_of_digits = sum(digits_in_int(a ** b))
        if sum_of_digits > max_val:
            max_val = sum_of_digits

print(max_val)

