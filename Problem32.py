"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from HelperFunctions import is_pandigital_triplet

# 4 digit limit because 1 * (some 4 digit number) = (4 digit number); 4 + 4 + 1 = 9
products = set([i*j for i in range(9999) for j in range(9999) if is_pandigital_triplet(i, j, i * j)])
print(sum(products))
