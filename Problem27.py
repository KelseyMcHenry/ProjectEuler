"""
Euler discovered the remarkable quadratic formula:

n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from HelperFunctions import is_prime

max_prime_run = 0
answer = (0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        last_result_was_prime = True
        prime_count = 0
        while last_result_was_prime:
            value = (n**2) + (a * n) + b
            if is_prime(value):
                last_result_was_prime = True
                prime_count += 1
            else:
                last_result_was_prime = False
            n += 1
        if prime_count > max_prime_run:
            max_prime_run = prime_count
            print(max_prime_run)
            answer = (a, b)

print(str(answer[0] * answer[1]))