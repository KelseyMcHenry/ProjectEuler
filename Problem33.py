"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from HelperFunctions import fraction_in_lowest_common_terms

fractions = list()

for i in range(10, 100):
    for j in range(10, 100):
        if i < j:
            digits_in_i = [int(digit) for digit in str(i)]
            digits_in_j = [int(digit) for digit in str(j)]
            for digit in digits_in_i:
                if digit in digits_in_j and i != j and digit != 0:
                    digits_in_i.remove(digit)
                    reconstructed_i = digits_in_i[0]
                    digits_in_j.remove(digit)
                    reconstructed_j = digits_in_j[0]
                    if j != 0 and reconstructed_j != 0:
                        if i / j == reconstructed_i / reconstructed_j:
                            fractions.append((i, j))

print(fractions)
fractions_lct = list()

for fraction in fractions:
    fractions_lct.append(fraction_in_lowest_common_terms(fraction[0], fraction[1]))

numerator_product = 1
denominator_product = 1
for fraction in fractions_lct:
    numerator_product *= fraction[0]
    denominator_product *= fraction[1]

print(fraction_in_lowest_common_terms(numerator_product, denominator_product)[1])