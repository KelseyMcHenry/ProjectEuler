"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(number, upper_limit):
    if len(str(number)) != upper_limit:
        return False
    for i in range(1, upper_limit + 1):
        if str(number).count(str(i)) != 1:
            return False
    return True


def concat_prod(number, range):
    result = ''
    for i in range:
        result += str(number * i)
    return int(result)


solution = 0
for i in range(1, 9999):
    for n in range(3, 9):
        number = concat_prod(i, range(1, n))
        if is_pandigital(number, 9) and number > solution:
            solution = number

print(solution)
