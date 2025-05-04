# problem 31
from abc import ABC
from Problem import AbsProblem



class Problem31(AbsProblem, ABC):
    details = "Project Euler. Problem 31:\n" \
              "In the United Kingdom the currency is made up of pound (£) and pence (p). " \
              "There are eight coins in general circulation:\n" \
              "1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).\n" \
              "It is possible to make £2 in the following way:\n" \
              "1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p\n" \
              ">> How many different ways can £2 be made using any number of coins?"
    __COIN_SUM = 200

    @property
    def getinfo(self):
        return self.details

    def result(self):
        ways = [0] * (self.__COIN_SUM+1)
        ways[0] = 1
        # print(ways)
        for x in [1, 2, 5, 10, 20, 50, 100, 200]:
            for i in range(x, self.__COIN_SUM+1):
                # print(f"x: {x} i:{i} >> WAYS FOR n={i}: ways[{i}]({ways[i]})+ways[{i - x}]({ways[i - x]})")
                ways[i] += ways[i - x]
                # print(ways)
        # print(ways)
        return ways[self.__COIN_SUM]
