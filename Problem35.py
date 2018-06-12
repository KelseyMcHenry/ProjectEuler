"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from Problem7 import is_prime


def get_rotations(number):
    results = list()
    results.append(number)
    digits = [int(digit) for digit in str(number)]
    for _ in range(1, len(str(number))):
        temp = digits.pop()
        digits.insert(0, temp)
        n = 0
        for digit in digits:
            n *= 10
            n += int(digit)
        results.append(n)

    return results


circular_primes = list()

for i in range(1, 1000000):
    rotations = get_rotations(i)
    is_circular_prime = True
    for rotation in rotations:
        if not is_prime(rotation):
            is_circular_prime = False
            break
    if is_circular_prime:
        circular_primes.append(i)

print(circular_primes)
print(len(circular_primes))