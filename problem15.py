import math
from Problem import AbsProblem


class Problem15(AbsProblem):
    details = "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, " \
              "there are exactly 6 routes to the bottom right corner.\n" \
              ">>How many such routes are there through a 20×20 grid?"

    gridNodeSide = 20

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = math.factorial(self.gridNodeSide*2)/\
                 (math.factorial(self.gridNodeSide)*math.factorial(self.gridNodeSide*2-self.gridNodeSide))
        return int(result)

