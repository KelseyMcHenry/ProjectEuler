"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# (Right, Down, Left, Up, Right)
unmapped_movements = [(1, i-2, i-1, i-1, i-1) for i in range(3, 1003, 2)]
mapped_movements = list()

print(unmapped_movements)

for move in unmapped_movements:
    mapped_movements.append((0, move[0]))
    mapped_movements.append((move[1], 0))
    mapped_movements.append((0, -1 * move[2]))
    mapped_movements.append((-1 * move[3], 0))
    mapped_movements.append((0, move[4]))

print(mapped_movements)

current_value = 1
solution = 1

for movement in mapped_movements:
    current_value += max(abs(movement[0]), abs(movement[1]))
    print(current_value)
    if movement != (0, 1):
        solution += current_value

print(solution)
