"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#prime factorization

running_amt = 600851475143
prime_factors = []

for i in range(2, 600851475143):
    while running_amt % i == 0:
        running_amt /= i
        prime_factors.append(i)
        if running_amt == 1:
            break
    if running_amt == 1:
        break

print(prime_factors)
print(max(prime_factors))
