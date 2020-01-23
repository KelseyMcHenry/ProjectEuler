"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from HelperFunctions import is_prime
from itertools import combinations

number = 56003
max_prime_family_len = 0

value_found = False

while not value_found:
    # if the initial value is a prime...
    if is_prime(number):
        num_string = str(number)
        # for each possible amount of digits to replace...
        for num_digits_to_replace in range(1, len(num_string)):
            prime_family = []
            indices_to_replace = list(combinations(range(0, len(num_string)), num_digits_to_replace))
            # for each possible digit to replace them with...
            for index_set in indices_to_replace:
                for number_to_replace_with in range(0, 10):
                    num_string = str(number)
                    for index in index_set:
                        num_string_list = list(num_string)
                        num_string_list[index] = str(number_to_replace_with)
                        num_string = "".join(num_string_list)
                        actual_number = int(num_string)

                    prime_family.append(actual_number)

                copy = prime_family.copy()
                for candidate in copy:
                    if len(str(candidate)) < len(str(number)) or not is_prime(candidate):
                        prime_family.remove(candidate)
                # print(f'{number} :: {index_set} :: {prime_family}')
                if len(prime_family) > max_prime_family_len:
                    max_prime_family_len = len(prime_family)
                if len(prime_family) == 8 and number in prime_family:
                    print(f'base number: {number} :: indices: {index_set} :: {prime_family}')
                    exit(0)
                prime_family.clear()
    # exit(0)
    number += 1
