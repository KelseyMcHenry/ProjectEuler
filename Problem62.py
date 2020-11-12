"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from HelperFunctions import *
from itertools import permutations

solved = False

index = 101
while not solved:
    initial_cube = index ** 3
    permutation_cube_count_list = set()
    permutation_cube_count_list.add(initial_cube)
    digits = digits_in_int_unsorted(initial_cube)
    permutation_generator = permutations(digits)
    for candidate_permutation in permutation_generator:
        cube_check_number = flatten_number_list(candidate_permutation)
        if is_cube(cube_check_number):
            permutation_cube_count_list.add(cube_check_number)
            if len(permutation_cube_count_list) > 5:
                break
    print(f'index: {index} | cube: {initial_cube} | permutation_count: {len(permutation_cube_count_list)}')
    if len(permutation_cube_count_list) == 3:
        print('-----------')
        print('DONE')
        print(f'{initial_cube}')
        print(f'{permutation_cube_count_list}')
        print('-----------')
        break
    index += 1