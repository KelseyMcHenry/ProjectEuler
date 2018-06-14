"""
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from math import sqrt


def word_score(word):
    score = 0
    for letter in word:
        score += (ord(letter) - 64)
    return score


def is_triangle_number(number):
    try:
        value = (1 + sqrt(1 + 4 * (2 * number))) / 2
        return value % 1 == 0
    except ValueError:
        return False


with open("p042_words.txt", "r") as words:
    for line in words:
        word_list = (line.replace('"', '').split(','))

triangle_word_count = 0
for word in word_list:
    if is_triangle_number(word_score(word)):
        triangle_word_count += 1

print(triangle_word_count)

