"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


possible_ways = list()
for twolb in range(0, 2):
    if twolb == 1:
        continue
    for lb in range(0, 3):
        for fiftyp in range(0, 5):
            for twentyp in range(0, 11):
                for tenp in range(0, 21):
                    for fivep in range(0, 41):
                        for twop in range(0, 101):
                            for onep in range(201):
                                if (200 * twolb) + (100 * lb) + (50 * fiftyp) + (20 * twentyp) + (10 * tenp) + (5 * fivep) + (2 * twop) + onep == 200:
                                    possible_ways.append((twolb, lb, fiftyp, twentyp, tenp, fivep, twop, onep))


print(len(possible_ways))