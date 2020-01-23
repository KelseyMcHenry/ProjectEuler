"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from HelperFunctions import prime_factors_counts


LCD_nums_and_powers = {}

for i in range(1, 20):
    temp = prime_factors_counts(i)
    if temp:
        for num, power in temp.items():
            if num not in LCD_nums_and_powers.keys():
                LCD_nums_and_powers[num] = power
            elif LCD_nums_and_powers[num] < power:
                LCD_nums_and_powers[num] = power

soln = 1
for num, power in LCD_nums_and_powers.items():
    soln *= (num ** power)

print(soln)