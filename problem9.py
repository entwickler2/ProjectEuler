from abc import ABC
from Problem import AbsProblem


class Problem9(AbsProblem, ABC):
    details = "Project Euler. Problem 9:\n" \
              "A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\n" \
              "a^2 + b^2 = c^2\n" \
              "For example, 32 + 42 = 9 + 16 = 25 = 52.\n" \
              ">>There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = self.__calc()
        # print(result)
        # print("RESULT: %d" % (result[0]*result[1]*result[2]))
        return result[0] * result[1] * result[2]

    __a = range(1, 1000)
    __b = range(1, 1000)
    __c = range(1, 1000)

    def __calc(self):
        for A in self.__a:
            # print(A)
            for B in self.__b:
                for C in self.__c:
                    if (A < B < C) and ((A ** 2) + (B ** 2) == C ** 2) and ((A + B + C) == 1000):
                        # print("a = %d\nb = %d\nc = %d" % (A, B, C))
                        return [A, B, C]
