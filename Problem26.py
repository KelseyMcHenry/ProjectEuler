"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


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


max_len = 0
answer = 0
for i in range(1, 1000):
    cycle_len = recurring_cycle_length(i)
    if cycle_len > max_len:
        answer = i
        max_len = cycle_len

print(answer)