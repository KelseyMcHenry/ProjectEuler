"""

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

2–√=1+12+12+12+…
By expanding this for the first four iterations, we get:

1+1/2=32=1.5
1+12+12=75=1.4
1+12+12+12=1712=1.41666…
1+12+12+12+12=4129=1.41379…

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

"""

from HelperFunctions import digits_in_int
from sys import setrecursionlimit


def recursive_infinite_fraction_bottom_part(stop_depth, numerator=5, denominator=2):
    if stop_depth == 1:
        return numerator, denominator
    if stop_depth == 2:
        return numerator + denominator, numerator
    else:
        return recursive_infinite_fraction_bottom_part(stop_depth - 1, ((2 * numerator) + denominator), numerator)


setrecursionlimit(1001)
count = 0
for i in range(1, 1001):
    numerator, denominator = recursive_infinite_fraction_bottom_part(i)
    if len(digits_in_int(numerator)) > len(digits_in_int(denominator)):
        count += 1

print(count)