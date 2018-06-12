"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from Problem7 import is_prime


def is_truncatable_prime_LR(number):
    slices = [int(str(number)[i:]) for i in range(0, len(str(number)))]
    # print(slices)
    return all([is_prime(slice) for slice in slices])


def is_truncatable_prime_RL(number):
    slices = [int(str(number)[:i]) for i in range(1, len(str(number)) + 1)]
    # print(slices)
    return all([is_prime(slice) for slice in slices])


truncatable_primes = list()
number = 8
while len(truncatable_primes) < 11:
    if is_truncatable_prime_LR(number) and is_truncatable_prime_RL(number):
        truncatable_primes.append(number)
        print(number)
    number += 1
    # if number % 100 == 0:
        # print(number)

print(truncatable_primes)
print(sum(truncatable_primes))

