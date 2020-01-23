"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


from HelperFunctions import prime_factorization


def main():
    print(prime_factorization(600851475143))
    print(max(prime_factorization(600851475143)))


if __name__ == '__main__':
    main()
