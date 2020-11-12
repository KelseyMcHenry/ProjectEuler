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
}

class TestProblems(unittest.TestCase):

    def test_all_problems(self):
        for function, solution in problems_and_solutions.items():
            tick = time.perf_counter()
            answer = function()
            tock = time.perf_counter()
            self.assertEqual(answer, solution)
            self.assertLess(tock - tick, 60)
            print(f'Solution for {function.__name__}: {answer} in {tock - tick:.2f} sec')
        time.sleep(1)
