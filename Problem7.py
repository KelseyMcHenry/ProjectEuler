"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from HelperFunctions import is_prime


def main():
    primes = list()
    value = 2

    while len(primes) < 10001:
        if is_prime(value):
            primes.append(value)
        value += 1

    print(primes[-1])


if __name__ == '__main__':
    main()
