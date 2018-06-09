"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Least common multiple

def prime_factors(number):
    factors = []
    running_amt = number

    for i in range(2, number):
        while running_amt % i == 0:
            running_amt /= i
            factors.append(i)
            if running_amt == 1:
                return {i: factors.count(i) for i in factors}

    return {number: 1}


LCD_nums_and_powers = {}

for i in range(1, 20):
    temp = prime_factors(i)
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