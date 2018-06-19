"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from Problem7 import is_prime
from itertools import permutations


for first_term in range(1000, 9998):
    for arith_increase in range(1, 4500):
        terms = [first_term, first_term + arith_increase, first_term + 2 * arith_increase]
        print(first_term, arith_increase)
        if all([i < 10000 for i in terms]) and all(is_prime(i) for i in terms) and all([tuple(str(i)) in permutations(str(first_term)) for i in terms]):
            if not (first_term == 1487 and arith_increase == 3330):
                print(str(first_term) + str(first_term + arith_increase) + str(first_term + 2 * arith_increase))
                exit(0)

