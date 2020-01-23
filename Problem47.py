"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from HelperFunctions import prime_factorization

start_num = 130000
done = False
while not done:
    if len(set(prime_factorization(start_num))) == 4 and len(set(prime_factorization(start_num + 1))) == 4 and len(set(prime_factorization(start_num + 2))) == 4 and len(set(prime_factorization(start_num + 3))) == 4:
        done = True
    else:
        start_num += 1

print(start_num)