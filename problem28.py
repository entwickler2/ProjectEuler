# problem 28
from abc import ABC

from Problem import AbsProblem


class Problem28(AbsProblem, ABC):
    details = "Project Euler. Problem 28:\n" \
              "Starting with the number and moving to the right in a clockwise direction a 5 by 5 spiral is formed " \
              "as follows: \n" \
              "21    22    23    24    25 \n" \
              "20    7     8     9     10 \n" \
              "19    6     1     2     11 \n" \
              "18    5     4     3     12 \n" \
              "17    16    15    14    13 \n" \
              "It can be verified that the sum of the numbers on the diagonals is 101. \n" \
              ">>What is the sum of the numbers on the diagonals in a by spiral formed in the same way?\n"
    __max_spiral_length = 1001
    __spiral_range = list(range(1, __max_spiral_length * __max_spiral_length + 1))

    # To solve the problem find diagonal numbers from spiral range and sum them

    @property
    def getinfo(self):
        return self.details

    def result(self):
        diagonal_1 = self.diagonal_1(max(self.__spiral_range))  # diagonal values: 1, 5, 9, 17, 25, ...
        diagonal_2 = self.diagonal_2(max(self.__spiral_range))  # diagonal values: 1, 3, 7, 13, 21, ...
        diagonal_values = set(diagonal_1 + diagonal_2)
        return sum(diagonal_values)

    @staticmethod
    def diagonal_1(max_length):
        i_1 = 0
        i = 1
        ind = [0]
        while True:
            i_1 = i_1 + i * 2
            i += 1
            if i_1 < max_length:
                ind.append(i_1 + 1)
            else:
                break
        return ind

    @staticmethod
    def diagonal_2(max_length):
        i = 1
        ind = []
        while True:
            out = i * i - i % 2
            if out < max_length:
                ind.append(out + 1)
                i += 1
            else:
                break
        return ind
