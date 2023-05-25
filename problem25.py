# problem 25
from abc import ABC
from Problem import AbsProblem
from functools import lru_cache


class Problem25(AbsProblem, ABC):
    details = "Project Euler. Problem 25:\n" \
              "The Fibonacci sequence is defined by the recurrence relation:\n" \
              "Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.\n" \
              "Hence the first 12 terms will be:\n" \
              "F1 = 1\n" \
              "F2 = 1\n" \
              "F3 = 2\n" \
              "F4 = 3\n" \
              "F5 = 5\n" \
              "F6 = 8\n" \
              "F7 = 13\n" \
              "F8 = 21\n" \
              "F9 = 34\n" \
              "F10 = 55\n" \
              "F11 = 89\n" \
              "F12 = 144\n" \
              "The 12th term, F12, is the first term to contain three digits.\n" \
              ">>What is the index of the first term in the Fibonacci sequence to contain 1000 digits?\n"

    @property
    def getinfo(self):
        return self.details

    @property
    def result(self):
        i = 0
        while True:
            i += 1
            num = self.__fib_calc(i)
            num_len = len(str(num))
            # if i < 13:
            #     print("index: {0} len: {1} num: {2}".format(i, num_len, num))
            if num_len == 1000:
                return i

    @lru_cache()
    def __fib_calc(self, n):
        if n <= 2:
            return 1
        else:
            return self.__fib_calc(n - 1) + self.__fib_calc(n - 2)
