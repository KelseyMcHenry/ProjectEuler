"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from HelperFunctions import is_prime
from math import sqrt, ceil
from itertools import product


prime_cache = list()


def next_odd_composite_number(number):
    number += 1
    while number % 2 == 0 or is_prime(number):
        number += 1
    return number


odd_composite = 2
for i in range(1, 1000000):
    print(odd_composite)
    odd_composite = next_odd_composite_number(odd_composite)
    primes = [i for i in range(1, odd_composite) if is_prime(i)]
    twice_squares = [2 * (i ** 2) for i in range(1, int(ceil(sqrt(odd_composite / 2))))]
    sum_candidates = product(primes, twice_squares)
    sums = [s for s in sum_candidates if s[0] + s[1] == odd_composite]
    if len(sums) == 0:
        print(sums)
        print(odd_composite)
        break

