"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

palindromic = list()
for i in range(1, 1000000):
    string_i = str(i)
    binary_string = bin(i)[2:]
    if string_i == string_i[::-1] and binary_string == binary_string[::-1]:
        palindromic.append(i)

print(sum(palindromic))
