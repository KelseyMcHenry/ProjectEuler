"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from Problem12 import divisors


def proper_divisors(number):
    divisor_list = divisors(number)
    if len(divisor_list) > 1:
        divisor_list.remove(number)
    return divisor_list


def d(number):
    return sum(proper_divisors(number))


def is_amicable(number):
    value = d(number)
    if d(value) == number and value != number:
        return True
    else:
        return False


def main():
    print(sum([i for i in range(1, 10001) if is_amicable(i)]))


if __name__ == '__main__':
    main()
