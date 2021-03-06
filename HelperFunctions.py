import math
from math import factorial, sqrt, ceil
import operator as op
from functools import reduce, lru_cache
import time

# TODO: Classify all of the helper functions

# ================================================= CONSTANTS =================================================


LETTERS_IN_ENGLISH_NUMBERS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                              9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                              20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
                              80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}


# ================================================= GENERATORS =================================================


def fibonacci_generator(n=None, max_value=None):
    """
    Returns a fibonacci number generator
    :param n: if provided, the generator will stop at the nth fibonacci number, otherwise it will continue indefinitely.
    :param max_value if provided, the generator will stop at the first value to exceed this value
    :return: generator
    """
    a, b = 0, 1
    if n is None:
        # infinite mode
        while True:
            yield a
            a, b = b, a + b
            if max_value and a > max_value:
                break
    else:
        # finite mode
        for _ in range(n):
            yield a
            a, b = b, a + b
            if max_value and a > max_value:
                break


def prime_generator(n=None, max_value=None):
    """
    Returns a prime number generator
    :param n: if provided, the generator will stop at the nth prime number, otherwise it will continue indefinitely.
    :param max_value if provided, the generator will stop at the first value to exceed this value
    :return: generator
    """
    x = 2
    if n is None:
        # infinite mode
        while True:
            if is_prime(x):
                yield x
                x += 1
            else:
                x += 1
            if max_value and x > max_value:
                break
    else:
        # finite mode
        for _ in range(n):
            while not is_prime(x):
                x += 1
            if max_value and x > max_value:
                break
            yield x
            x += 1


def triangle_number_generator(n=None, max_value=None):
    """
    Returns a triangle number generator
    :param n: if provided, the generator will stop at the nth triangle number, otherwise it will continue indefinitely.
    :param max_value if provided, the generator will stop at the first value to exceed this value
    :return: generator
    """
    # FORMULA FOR TRIANGULAR NUMBER = n(n+1)/2
    i = 1
    if n is None:
        # infinite mode
        while True:
            triangle = i * (i + 1) / 2
            yield int(triangle)
            i += 1
            if max_value and triangle > max_value:
                break
    else:
        # finite mode
        while i <= n:
            triangle = i * (i + 1) / 2
            yield int(triangle)
            i += 1
            if max_value and triangle > max_value:
                break


def square_number_generator(n=None, max_value=None):
    """
    Returns a square number generator
    :param n: if provided, the generator will stop at the nth square number, otherwise it will continue indefinitely.
    :param max_value if provided, the generator will stop at the first value to exceed this value
    :return: generator
    """

    i = 1
    if n is None:
        # infinite mode
        while True:
            square = i ** 2
            yield square
            i += 1
            if max_value and square > max_value:
                break
    else:
        # finite mode
        while i <= n:
            square = i ** 2
            yield square
            i += 1
            if max_value and square > max_value:
                break


def pentagonal_number_generator(n=None, max_value=None):
    """
    Returns a pentagonal number generator
    :param n: if provided, the generator will stop at the nth pentagonal number, otherwise it will continue indefinitely.
    :param max_value if provided, the generator will stop at the first value to exceed this value
    :return: generator
    """
    # FORMULA FOR TRIANGULAR NUMBER = n(n+1)/2
    i = 1
    if n is None:
        # infinite mode
        while True:
            pentagonal = (i * (i + 1) / 2) + (i * (i + 1))
            yield int(pentagonal)
            i += 1
            if max_value and pentagonal > max_value:
                break
    else:
        # finite mode
        while i <= n:
            pentagonal = (i * (i + 1) / 2) + (i * (i + 1))
            yield int(pentagonal)
            i += 1
            if max_value and pentagonal > max_value:
                break


def composite_number_generator(n=None, max_value=None):
    """
        Returns a composite number generator
        :param n: if provided, the generator will stop at the nth composite number, otherwise it will continue indefinitely.
        :param max_value if provided, the generator will stop at the first value to exceed this value
        :return: generator
        """
    x = 2
    if n is None:
        # infinite mode
        while True:
            if not is_prime(x):
                yield x
                x += 1
            else:
                x += 1
            if max_value and x > max_value:
                break
    else:
        # finite mode
        for _ in range(n):
            while is_prime(x):
                x += 1
            if max_value and x > max_value:
                break
            yield x
            x += 1

# ============================================= BOOLEAN CLASSIFIERS =============================================


def is_palindromic(number):
    """
    Returns if the number provided is the same forward as backwards
    """
    return str(number)[::-1] == str(number)


@lru_cache(maxsize=None)
def is_prime(num):
    """
    returns True or False if num is prime or not
    :param num:
    :return:
    """
    # account for negative input
    num = abs(num)
    # 1 and 2 are special cases
    if num == 1:
        return False
    if num == 2:
        return True
    # throw out odd numbers
    if num % 2 == 0:
        return False
    # starting at 3 and checking every odd number up to the sqrt of the number, check if it has any factors.
    for i in range(3, int(ceil(sqrt(num)) + 1), 2):
        if num % i == 0:
            return False
    return True


def is_amicable(number):
    """
    returns a boolean if a number is amicable
    (Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.)
    """
    value = sum(proper_divisors(number))
    if sum(proper_divisors(value)) == number and value != number:
        return True
    else:
        return False


def is_abundant(number):
    """
    returns if a number is abundant
    (A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.)
    """
    return sum(proper_divisors(number)) > number


def is_pandigital_triplet(a, b, c):
    """
    returns a boolean if a triplet of numbers contains only 1 instance of each digit across all 3 numbers
    """
    concat = str(a) + str(b) + str(c)
    if len(concat) != 9:
        return False
    for i in range(1, 10):
        if concat.count(str(i)) != 1:
            return False
    # print((a, b, c))
    return True


def is_truncatable_prime(number):
    """
    given a number, returns a boolean saying if it is a truncatable prime from left to right and right to left.
    (Being prime itself, it is possible to continuously remove digits from
    left to right, and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.)
    """
    if number in [2, 3, 5, 7]:
        return False
    slicesLR = [int(str(number)[i:]) for i in range(0, len(str(number)))]
    slicesRL = [int(str(number)[:i]) for i in range(1, len(str(number)) + 1)]
    return all([is_prime(slice) for slice in slicesLR]) and all([is_prime(slice) for slice in slicesRL])


def is_pandigital(number):
    """
    Given a number, returns a boolean indicating whether or not it is pandigital, IE it contains all digits 1-9
    once and only once
    """
    if len(str(number)) > 9:
        return False
    for i in range(1, len(str(number)) + 1):
        if str(number).count(str(i)) != 1:
            return False
    return True


def is_triangle_number(number):
    """
    given a number returns a boolean if it is a triangle number
    """
    try:
        value = (1 + sqrt(1 + 4 * (2 * number))) / 2
        return value % 1 == 0
    except ValueError:
        return False


def is_square(number):
    """
    given a number returns a boolean if it is a square number
    """
    return sqrt(number) % 1.0 == 0


def is_pentagonal(number):
    """
    given a number returns a boolean if it is a pentagonal number
    """
    return ((1 + sqrt(1 + (4 * 3 * 2 * number))) / 6) % 1 == 0


def is_hexagonal(number):
    """
    given a number returns a boolean if it is a hexagonal number
    """
    return ((1 + sqrt(1 + 8 * number)) / 4) % 1 == 0


def is_heptagonal(number):
    """
    given a number returns a boolean if it is a heptagonal number
    """
    return ((3 + sqrt(9 + 4 * 5 * 2 * number)) / 10) % 1 == 0


def is_octagonal(number):
    """
    given a number returns a boolean if it is a octagonal number
    """
    return ((2 + sqrt(4 + 4 * 3 * number)) / 6) % 1 == 0


# ================================================= MATHEMATICAL =================================================
# ================================================= MISCELLANEOUS =================================================

def primes_under_x(x):
    """
    Returns a list of all prime numbers with a value less than the number provided
    """
    # start at 3 and skip all even numbers, adding the rest to the list
    primes_list = [i for i in range(3, x, 2) if is_prime(i)]
    # add 2 since it is prime but the even number count skips it
    primes_list.append(2)
    return primes_list


@lru_cache(maxsize=None)
def prime_factorization(number):
    """
    returns a list containing all the digits in the prime factorization of number

    :param number:
    :return:
    """
    running_amt = number
    prime_factors = []

    # start checking factors at 2 since everything is divisible by 1
    i = 2
    # check all factors up to the number itself, since all numbers are divisible by themselves, it will terminate there in the case that it is prime.
    while i <= number:
        while running_amt % i == 0:
            # if the number you are checking is a factor, add it to the list and divide the current number by that value.
            running_amt /= i
            prime_factors.append(i)
            if running_amt == 1:
                break
            # restart the counting again, there can be multiple instances of a factor during prime factorization.
            i = 2
        if running_amt == 1:
            break
        i += 1

    return prime_factors


@lru_cache(maxsize=None)
def number_of_distinct_prime_factors_with_prime_cache(number, primes_cache):
    """
    returns a list containing all the digits in the prime factorization of number

    :param number:
    :return:
    """
    distinct_prime_factors_count = 0
    upper_limit = int(ceil(sqrt(number)))

    for i in primes_cache:
        if (distinct_prime_factors_count == 0 and i > upper_limit) or i > number:
            return distinct_prime_factors_count
        if number % i == 0:
            distinct_prime_factors_count += 1
            if distinct_prime_factors_count > 4:
                return []

    return distinct_prime_factors_count


def prime_factors_counts(number):
    """
    returns dict with all the individual digits in the prime factorization and their counts
    """
    factors = prime_factorization(number)
    return {i: factors.count(i) for i in factors}


def product_of_list(input_list):
    """
    Returns the product of a list of numbers
    """
    result = 1
    for number in input_list:
        result *= number
    return result


def divisors(number):
    """
    returns a list of numbers that divide evenly into num
    """
    if number == 1:
        return [1]
    divisor_list = list()
    for i in range(1, int(math.ceil(math.sqrt(number)) + 1)):
        if number % i == 0:
            divisor_list.append(i)
            divisor_list.append(int(number / i))
    return list(set(divisor_list))


def collatz_chain_length(number):
    """
    returns the length of the collatz chain for the given number
    """
    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        count += 1
    return count


def num_letters_in_number(number):
    """
    for a given int, determines the number of letters in the written form
    """
    english = ''
    thousands_digit = number // 1000
    if thousands_digit > 0:
        # thousands digit aka 'one thousand, 5 thousand' etc
        english += LETTERS_IN_ENGLISH_NUMBERS[number // 1000] + ' ' + LETTERS_IN_ENGLISH_NUMBERS[1000] + ' '
    hundreds_digit = number // 100
    if (hundreds_digit > 0) and (hundreds_digit < 10):
        # hundreds digit aka 'one hundred, 5 hundred' etc
        english += LETTERS_IN_ENGLISH_NUMBERS[number // 100] + ' ' + LETTERS_IN_ENGLISH_NUMBERS[100] + ' '
    less_than_hundreds = number % 100
    if (thousands_digit > 0 or hundreds_digit > 0) and less_than_hundreds > 0:
        # 'British' usage and
        english += 'and '
    tens_digit = number % 100 - number % 10
    ones_digit = number % 10
    if (less_than_hundreds < 20) and less_than_hundreds != 0:
        english += LETTERS_IN_ENGLISH_NUMBERS[less_than_hundreds]
    else:
        if tens_digit > 0:
            english += LETTERS_IN_ENGLISH_NUMBERS[tens_digit] + ' '
        if ones_digit > 0:
            english += LETTERS_IN_ENGLISH_NUMBERS[ones_digit]

    # print(str(number) + " : " + english)
    return len(english.replace(' ', ''))


def proper_divisors(number):
    """
    returns the list of divisors which are strictly less than the input number
    """
    divisor_list = divisors(number)
    if len(divisor_list) > 1:
        divisor_list.remove(number)
    return divisor_list


def recurring_cycle_length(number):
    """
    for a given number, returns the length of the longest repeating cycle of digits in 1/number
    """
    # checks 2000 digits out, using integer division so no floating point rounding issues come up.
    unit_fraction = str(1*(10 ** 2000) // number)
    max_repetitions = 0
    cycle_length = 0
    for i in range(1, len(unit_fraction)):
        count = unit_fraction.count(unit_fraction[0:-i])
        if count > max_repetitions and count > 1:
            if unit_fraction[unit_fraction.index(unit_fraction[0:-i]) + len(unit_fraction[0:-i]): unit_fraction.index(unit_fraction[0:-i]) + 2 * len(unit_fraction[0:-i])] == unit_fraction[0:-i]:
                max_repetitions = count
                cycle_length = len(unit_fraction) - i
    return cycle_length


def fraction_in_lowest_common_terms(numerator, denominator):
    """
    # given a numerator and denominator of a fraction, returns a tuple containing the
    # numerator and denominator of the fraction in lowest common terms
    """
    for i in range(max(numerator, denominator), 1, -1):
        if denominator % i == 0 and numerator % i == 0:
            numerator /= i
            denominator /= i

    return int(numerator), int(denominator)


def sum_of_factorial_of_digits(number):
    """
    retuns the sum of all digits of the factorial of a number
    """
    running_sum = 0
    for i in digits_in_int_unsorted(number):
        running_sum += factorial(i)
    return running_sum


def get_rotations(number):
    """
    given a number, returns a list of all of the "rotations" of a number, ie for 123 -> 123, 231, 312
    """
    results = [number]
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


def word_score(word):
    """
    Returns the "score" for a given string by summing the indices of the letters wihthin the alphabet.
    EG: SKY = 19 + 11 + 25 = 55
    """
    score = 0
    for letter in word:
        score += (ord(letter) - 64)
    return score


def digits_in_int(number):
    """
    given an integer, returns a sorted list containing all the digits
    """
    val_str = str(number)
    vals = list(val_str)
    values_int = [int(v) for v in vals]
    values_int.sort()
    return values_int


def digits_in_int_unsorted(number):
    """
    given an integer, returns an unsorted list containing all the digits
    """
    val_str = str(number)
    vals = list(val_str)
    values_int = [int(v) for v in vals]
    return values_int


def len_n_choose_r(n, r):
    """
    returns how many ways there are to choose r items from a group of n
    """
    return factorial(n) / (factorial(r) * factorial(n - r))


def flip_number(n):
    return int(str(n)[::-1])


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


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def homebrew_combinations_to_file(list_to_choose_from, combo_size, file_handle):
    total = ncr(len(list_to_choose_from), combo_size)
    count_processed = 0
    if len(list_to_choose_from) < combo_size:
        raise ValueError('list length must be greater than or equal to the combo size')
    indices = list(range(0, combo_size))
    while indices != reversed(list(range(len(list_to_choose_from) - 1, len(list_to_choose_from) - combo_size, -1))):
        combo = []
        for index in indices:
            combo.append(list_to_choose_from[index])
        file_handle.write(str(combo) + '\n')
        count_processed += 1
        print(f'{count_processed}/{total} = {count_processed * 100 / total}%')
        try:
            increment_indices(indices, -1, len(list_to_choose_from) - 1)
        except ValueError:
            return


def increment_indices(indices, position, rollover_value):
    # try to simply add 1 to the current value
    try:
        number_to_use = indices[position] + 1
    except IndexError:
        # if position goes out of bounds, we are at the maximum
        raise ValueError('Indices is at its max value, can no longer increment')
    # if trying to add one causes it to rollover, we need to increment the next position, and once it is done, we need to come back to this position
    if number_to_use == rollover_value + 1 + (position + 1):
        number_to_use = 0
        indices[position] = number_to_use
        increment_indices(indices, position - 1, rollover_value)
    # if we are on the most significant digit, we dont have to worry about it being less than anything.
    if len(indices) == abs(position):
        while number_to_use in indices:
            number_to_use += 1
    else:
        while number_to_use in indices or number_to_use <= indices[position - 1]:
            number_to_use += 1

    indices[position] = number_to_use


@lru_cache(maxsize=None)
def concatenate_numbers(pair):
    return int(str(pair[0]) + str(pair[1]))


def is_cyclic_4dig(num_set):
    end_numbers = [number % 100 for number in num_set]
    if any([number < 10 for number in end_numbers]):
        return False
    for number in num_set:
        if number // 100 not in end_numbers:
            return False
    for i in range(len(num_set) - 1):
        if num_set[i] % 100 != num_set[i + 1] // 100:
            return False
    # check that the last digit wraps around to the first digit
    print(num_set)
    if num_set[-1] % 100 != num_set[0] // 100:
        return False
    return True


def polygonal_number_generator(s):
    num = 1
    while True:
        yield int(((s-2)*(num ** 2) - (s - 4)*(num)) / 2)
        num += 1


def cube_root(x):
    return x**(1./3.)


def is_cube(number):
    factors = prime_factorization(number)
    if len(factors) == 0:
        return False
    for factor in set(factors):
        if factors.count(factor) != 3:
            return False
    return True


def flatten_number_list(number_list):
    number_list = list(number_list)
    number_list.reverse()
    value = 0
    for i in range(0, len(number_list)):
        value += (10 ** i) * number_list[i]
    return value

