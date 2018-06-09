"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print(sum([i for i in range(3, 2000000, 2) if isPrime(i)]) + 2)
