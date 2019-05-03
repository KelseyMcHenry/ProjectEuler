"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial
"""
formula for all possible permutations
P(n,r)=n!/(n−r)!
(n-r)! = 1 when n = r, simplified here
divided by all possible permutations of the set of 20 rights and 20 downs to account for repetitions
"""
print(int(factorial(40) / (factorial(20) * factorial(20))))

