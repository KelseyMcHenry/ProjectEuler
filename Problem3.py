"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# prime factorization
def prime_factorization(number):
    running_amt = number
    prime_factors = []

    for i in range(2, number):
        while running_amt % i == 0:
            running_amt /= i
            prime_factors.append(i)
            if running_amt == 1:
                break
            i = 2
        if running_amt == 1:
            break

    return prime_factors


def main():
    print(prime_factorization(600851475143))
    print(max(prime_factorization(600851475143)))

if __name__ == '__main__':
    main()