# problem 24
from abc import ABC
from Problem import AbsProblem
from itertools import permutations


class Problem24(AbsProblem, ABC):
    details = "Project Euler. Problem 24:\n" \
              "A permutation is an ordered arrangement of objects. For example, \n" \
              "3124 is one possible permutation of the digits 1, 2, 3 and 4. \n" \
              "If all of the permutations are listed numerically or alphabetically, \n" \
              "we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:\n" \
              "012   021   102   120   201   210 \n" \
              ">>What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?\n"

    __initial_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = ""
        # Generate permutations
        permutations_obj = permutations(self.__initial_seq)
        c = 0
        for i in list(permutations_obj):
            c += 1
            if c == 1000000:
                result = str(i).replace(", ", "").replace("(", "").replace(")", "")
        return result
