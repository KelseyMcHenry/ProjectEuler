"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


from HelperFunctions import find_right_angle_triangle_lengths


max_length = 0
solution = 0
for p in range(1, 1001):

    length = len(find_right_angle_triangle_lengths(p))
    if length > max_length:
        max_length = length
        solution = p
    print(p)


print(solution)
