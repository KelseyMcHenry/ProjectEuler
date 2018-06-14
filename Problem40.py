"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

big_string = ""
for i in range(1, 1000001):
    big_string += str(i)

print(int(big_string[0]) * int(big_string[9]) * int(big_string[99]) * int(big_string[999]) * int(big_string[9999]) * int(big_string[99999]) * int(big_string[999999]))