"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

letters_in_english = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                      10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                      17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                      60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}


def num_letters_in_number(number):
    if number <= 20:
        print(letters_in_english[number])
        return len(letters_in_english[number])
    else:
        english = ''
        thousands_digit = number // 1000
        if thousands_digit> 0:
            # thousands digit aka 'one thousand, 5 thousand' etc
            english += letters_in_english[number // 1000] + ' ' + letters_in_english[1000] + ' '
        if (number // 100 > 0) and (number // 100 < 10):
            # hundreds digit aka 'one hundred, 5 hundred' etc
            english += letters_in_english[number // 100] + ' ' + letters_in_english[100] + ' '
        if (number // 1000 > 0 or number // 100 > 0) and number % 100 > 0:
            # 'British' usage and
            english += 'and '
        tens_digit = number % 100 - number % 10
        if  > 0:
            if
            # 10s place
            english += letters_in_english[(number % 100) - (number % 10)]
        if ((number % 100) - (number % 10) != 10) and number % 10 > 0:
            english += ' ' + letters_in_english[number % 10]

        print(english)
        return len(english)

result = 0
for i in range(1, 1001):
    result += num_letters_in_number(i)

print(result)