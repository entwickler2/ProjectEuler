# Problem 20
from Problem import AbsProblem
import math


class Problem20(AbsProblem):
    details = "Project Euler. Problem 20:\n" \
              "n! means n × (n − 1) × ... × 3 × 2 × 1\n" \
              "For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,\n" \
              "and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.\n" \
              ">>Find the sum of the digits in the number 100!\n"

    @property
    def getinfo(self):
        return self.details

    def result(self):
        sum_num = 0
        a = str(math.factorial(100))
        for i in a:
            sum_num += int(i)
        return sum_num
