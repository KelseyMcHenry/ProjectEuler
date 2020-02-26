"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from HelperFunctions import is_prime, concatenate_numbers, primes_under_x
from itertools import combinations, permutations

import time
from operator import itemgetter

start_time = time.time()

set_size = 1
primes_cache = primes_under_x(10000)
index_combinations = combinations(range(len(primes_cache)), 1)
index_combinations = [list(entry) for entry in index_combinations]
combinations = []

while set_size < 5:
    set_size += 1
    for index_combination in index_combinations:
        for index in range(len(primes_cache)):
            index_combo = index_combination.__add__([index])
            combo = itemgetter(*index_combo)(primes_cache)
            permutations_of_primes = permutations(combo, 2)
            all_prime = True
            for pair in permutations_of_primes:
                if not is_prime(concatenate_numbers(pair)):
                    all_prime = False
                    break
            if all_prime and set(index_combo) not in combinations:
                combinations.append(set(index_combo))
    print(set_size)
    print(combinations)
    index_combinations = [list(combination) for combination in combinations]
    combinations = []


for combination in index_combinations:
    combo = itemgetter(*combination)(primes_cache)
    print(combo)
    print(sum(combo))




