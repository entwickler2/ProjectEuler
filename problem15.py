import math
from Problem import AbsProblem


class Problem15(AbsProblem):
    details = "Project Euler. Problem 15:\n" \
              "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, " \
              "there are exactly 6 routes to the bottom right corner.\n" \
              ">>How many such routes are there through a 20×20 grid?"

    __gridNodeSide = 20

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = math.factorial(self.__gridNodeSide * 2) / \
                 (math.factorial(self.__gridNodeSide) * math.factorial(self.__gridNodeSide * 2 - self.__gridNodeSide))
        return int(result)

