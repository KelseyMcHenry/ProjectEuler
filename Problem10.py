"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from HelperFunctions import is_prime

print(sum([i for i in range(3, 2000000, 2) if is_prime(i)]) + 2)
