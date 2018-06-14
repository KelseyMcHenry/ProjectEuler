"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

def find_right_angle_triangle_lengths(number):
    solutions = list()
    upper_limit = (number // 2) + 1
    for a in range(1, upper_limit):
        for b in range(1, upper_limit):
            if a + b < number and a + b + sqrt(a**2 + b**2) == number:
                solutions.append((a, b, sqrt(a**2 + b**2)))
    return solutions


max_length = 0
solution = 0
for p in range(1, 1001):

    length = len(find_right_angle_triangle_lengths(p))
    if length > max_length:
        max_length = length
        solution = p
    print(p)


print(solution)
