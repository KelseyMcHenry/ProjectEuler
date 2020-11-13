import unittest
import time
from ProblemExecution import *

problems_and_solutions = {
    problem_1: 233168,
    problem_2: 4613732,
    problem_3: 6857,
    problem_4: 906609,
    problem_5: 232792560,
    problem_6: 25164150,
    problem_7: 104743,
    problem_8: 23514624000,
    problem_9: 31875000,
    problem_10: 142913828922,
    problem_11: 70600674,
    problem_12: 76576500,
    problem_13: 5537376230,
    problem_14: 837799,
    problem_15: 137846528820,
    problem_16: 1366,
    problem_17: 21124,
    problem_18: 1074,
    problem_19: 171,
    problem_20: 648,
    problem_21: 31626,
    problem_22: 871198282,
    problem_23: 4179871,
    problem_24: 2783915460,
    problem_25: 4782,
    problem_26: 983,
    problem_27: -59231,
    problem_28: 669171001,
    problem_29: 9183,
    problem_30: 443839,
    problem_31: 73682,
    problem_32: 45228,
    problem_33: 100,
    problem_34: 40730,
    problem_35: 55,
    problem_36: 872187
}


class TestProblems(unittest.TestCase):

    def test_all_problems(self):
        start = 33
        for func, solution in problems_and_solutions.items():
            if int(func.__name__[8:]) < start:
                continue
            tick = time.perf_counter()
            answer = func()
            tock = time.perf_counter()
            print(f'Solution for {func.__name__}: {answer} in {tock - tick:.2f} sec')
            self.assertEqual(solution, answer)
            self.assertLess(tock - tick, 60)
        time.sleep(1)