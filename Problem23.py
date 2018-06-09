"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from Problem21 import d
from itertools import product


def is_abundant(number):
    return d(number) > number


subset_abundant_numbers = [i for i in range(1, 28124) if is_abundant(i)]

pairs_abundant_number_subset = product(subset_abundant_numbers, subset_abundant_numbers)

can_be_written_as_sum = set([i + j for i, j in pairs_abundant_number_subset if i + j < 28124])

larger_set = set(range(1, max(can_be_written_as_sum) + 1))

cannot_be_written = larger_set - can_be_written_as_sum

print(sum(cannot_be_written))

