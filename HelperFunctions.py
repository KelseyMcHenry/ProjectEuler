import math
from math import factorial, sqrt


letters_in_english = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                      17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                      60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}


# returns a list containing all the digits in the prime factorization of number
def prime_factorization(number):
    running_amt = number
    prime_factors = []

    for i in range(2, number):
        while running_amt % i == 0:
            running_amt /= i
            prime_factors.append(i)
            if running_amt == 1:
                break
            i = 2
        if running_amt == 1:
            break

    return prime_factors


# returns dict with all the individual digits in the prime factorization and their counts
def prime_factors_counts(number):
    factors = []
    running_amt = number

    for i in range(2, number):
        while running_amt % i == 0:
            running_amt /= i
            factors.append(i)
            if running_amt == 1:
                return {i: factors.count(i) for i in factors}

    return {number: 1}


# returns True or False if num is prime or not
def is_prime(num):
    num = abs(num)
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)) + 1), 2):
        if num % i == 0:
            return False
    return True


# returns a list of numbers that divide evenly into num
def divisors(num):
    if num == 1:
        return [1]
    divisor_list = list()
    for i in range(1, int(math.ceil(math.sqrt(num)) + 1)):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(int(num / i))
    return list(set(divisor_list))


# returns the nth triangle number
def nth_triangle_number(index):
    return sum(range(1, index+1))


# returns the length of the collatz chain for the given number
def collatz_chain_length(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        count += 1
    return count


# for a given int, determines the number of letters in the written form
def num_letters_in_number(number):
    english = ''
    thousands_digit = number // 1000
    if thousands_digit > 0:
        # thousands digit aka 'one thousand, 5 thousand' etc
        english += letters_in_english[number // 1000] + ' ' + letters_in_english[1000] + ' '
    hundreds_digit = number // 100
    if (hundreds_digit > 0) and (hundreds_digit < 10):
        # hundreds digit aka 'one hundred, 5 hundred' etc
        english += letters_in_english[number // 100] + ' ' + letters_in_english[100] + ' '
    less_than_hundreds = number % 100
    if (thousands_digit > 0 or hundreds_digit > 0) and less_than_hundreds > 0:
        # 'British' usage and
        english += 'and '
    tens_digit = number % 100 - number % 10
    ones_digit = number % 10
    if (less_than_hundreds < 20) and less_than_hundreds != 0:
        english += letters_in_english[less_than_hundreds]
    else:
        if tens_digit > 0:
            english += letters_in_english[tens_digit] + ' '
        if ones_digit > 0:
            english += letters_in_english[ones_digit]

    print(str(number) + " : " + english)
    return len(english.replace(' ', ''))


# returns the list of divisors which are less than the input number
def proper_divisors(number):
    divisor_list = divisors(number)
    if len(divisor_list) > 1:
        divisor_list.remove(number)
    return divisor_list


# returns a boolean if a number is amicable
def is_amicable(number):
    value = sum(proper_divisors(number))
    if sum(proper_divisors(value)) == number and value != number:
        return True
    else:
        return False


# returns if a number is abundant
def is_abundant(number):
    return sum(proper_divisors(number)) > number


# for a given number, returns the length of the longest repeating cycle of digits in 1/number
def recurring_cycle_length(number):
    # checks 10000 digits out, using integer division so no floating point rounding issues come up.
    unit_fraction = str(1*(10 ** 10000) // number)
    max_repetitions = 0
    cycle_length = 0
    for i in range(1, len(unit_fraction)):
        count = unit_fraction.count(unit_fraction[0:-i])
        if count > max_repetitions and count > 1:
            if unit_fraction[unit_fraction.index(unit_fraction[0:-i]) + len(unit_fraction[0:-i]): unit_fraction.index(unit_fraction[0:-i]) + 2 * len(unit_fraction[0:-i])] == unit_fraction[0:-i]:
                max_repetitions = count
                cycle_length = len(unit_fraction) - i
    return cycle_length


# returns a boolean if a triplet of numbers contains only 1 instance of each digit across all 3 numbers
def is_pandigital_triplet(a, b, c):
    concat = str(a) + str(b) + str(c)
    if len(concat) != 9:
        return False
    for i in range(1, 10):
        if concat.count(str(i)) != 1:
            return False
    # print((a, b, c))
    return True


# given a numerator and denominator of a fraction, returns a tuple containing the
# numerator and denominator of the fraction in lowest common terms
def fraction_in_lowest_common_terms(numerator, denominator):
    for i in range(max(numerator, denominator), 1, -1):
        if denominator % i == 0 and numerator % i == 0:
            numerator /= i
            denominator /= i

    return int(numerator), int(denominator)


# retuns the sum of all digits of the factorial of a number
def sum_of_factorial_of_digits(number):
    running_sum = 0
    for i in [int(digit) for digit in str(number)]:
        running_sum += factorial(i)
    return running_sum


# given a number, returns a list of all of the "rotations" of a number, ie for 123 -> 123, 231, 312
def get_rotations(number):
    results = []
    results.append()
    digits = [int(digit) for digit in str(number)]
    for _ in range(1, len(str(number))):
        temp = digits.pop()
        digits.insert(0, temp)
        n = 0
        for digit in digits:
            n *= 10
            n += int(digit)
        results.append(n)

    return results


# for a decimal number input return a string representation of the number in binary
def dec_to_binary(number):
    print(number)
    binary_string = ''
    while number // 2 > 0:
        binary_string = str(number % 2) + binary_string
        number //= 2
        print(number)
    binary_string = str(number % 2) + binary_string
    return binary_string


# given the perimeter of a right angle triangle, returns a list of tuples containing
# all possible integer length combinations of the sides
def find_right_angle_triangle_lengths(number):
    solutions = list()
    upper_limit = (number // 2) + 1
    for a in range(1, upper_limit):
        for b in range(1, upper_limit):
            if a + b < number and a + b + sqrt(a**2 + b**2) == number:
                solutions.append((a, b, sqrt(a**2 + b**2)))
    return solutions


# given a number returns a boolean if it is a triangle number
def is_triangle_number(number):
    try:
        value = (1 + sqrt(1 + 4 * (2 * number))) / 2
        return value % 1 == 0
    except ValueError:
        return False


# given a number returns a boolean if it is a pentagonal number
def is_pentagonal(number):
    return ((1 + sqrt(1 + (4 * 3 * 2 * number))) / 6) % 1 == 0


# given a number returns a boolean if it is a hexagonal number
def is_hexagonal(number):
    return ((1 + sqrt(1 + 8 * number)) / 4) % 1 == 0


# given an integer, returns a list containing all the digits
def digits_in_int(number):
    val_str = str(number)
    vals = list(val_str)
    values_int = [int(v) for v in vals]
    values_int.sort()
    return values_int


# returns how many ways there are to choose r items from a group of n
def len_n_choose_r(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def flip_number(n):
    return int(str(n)[::-1])


def is_palindromic(n):
    return n == flip_number(n)


def square_spiral(side_length, direction='clockwise'):
    if side_length % 2 == 0:
        raise ValueError('side_length must be odd')

    # (Right, Down, Left, Up, Right)
    unmapped_movements = [(1, i - 2, i - 1, i - 1, i - 1) for i in range(3, side_length + 2, 2)]
    mapped_movements = list()

    if direction == 'counterclockwise':
        for move in unmapped_movements:
            mapped_movements.append((0, move[0]))
            mapped_movements.append((-1 * move[1], 0))
            mapped_movements.append((0, -1 * move[2]))
            mapped_movements.append((move[3], 0))
            mapped_movements.append((0, move[4]))
    elif direction == 'clockwise':
        for move in unmapped_movements:
            mapped_movements.append((0, move[0]))
            mapped_movements.append((move[1], 0))
            mapped_movements.append((0, -1 * move[2]))
            mapped_movements.append((-1 * move[3], 0))
            mapped_movements.append((0, move[4]))
    else:
        raise Exception('not a direction')

    matrix = []
    for _ in range(0, side_length):
        matrix.append([0] * side_length)

    cursor = ((side_length // 2), (side_length // 2))
    current_value = 1
    matrix[cursor[0]][cursor[1]] = current_value
    current_value += 1
    for move in mapped_movements:
        if move[0] == 0:
            direction_magnitude = move[1]
            adding_index = 1
        else:
            direction_magnitude = move[0]
            adding_index = 0
        for _ in range(0, abs(direction_magnitude)):
            direction = [0, 0]
            direction[adding_index] = 1 * direction_magnitude // abs(direction_magnitude)
            cursor = tuple([sum(x) for x in zip(cursor, tuple(direction))])
            matrix[cursor[0]][cursor[1]] = current_value
            current_value += 1

    return matrix
