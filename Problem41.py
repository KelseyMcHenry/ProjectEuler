"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from Problem7 import is_prime

for n in range(9, 2, -1):
    digits = [str(i) for i in range(1, n)]
    pandigital_intermediates = permutations(digits)
    pandigitals = [''.join(intermediate) for intermediate in pandigital_intermediates]
    pandigitals.sort(reverse=True)

    for pandigital in pandigitals:
        if is_prime(int(pandigital)):
            print(pandigital)
            exit(0)
