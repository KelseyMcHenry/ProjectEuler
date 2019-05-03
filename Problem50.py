"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from Problem7 import is_prime

primes = [i for i in range(2, 1000000) if is_prime(i)]
print(primes)

# truncate down the primes list
sum_val = 0
largest_prime = 0
for prime in primes:
    sum_val += prime
    if sum_val >= 1000000:
        sum_val -= prime
        largest_prime = prime
        break
primes = primes[:primes.index(largest_prime)]


# coming from bottom up
max_len = 0
value = 0

for i in range(1, len(primes) + 1):
    sub_list = primes[i:]
    val = sum(sub_list)
    if is_prime(val):
        max_len = len(sub_list)
        value = val
        break

for i in range(1, len(primes) + 1):
    sub_list = primes[:-i]
    val = sum(sub_list)
    if is_prime(val) and len(sub_list) > max_len:
        value = val
        break

print(value)