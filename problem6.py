from abc import ABC
from Problem import AbsProblem


class Problem6(AbsProblem, ABC):
    details = 'Project Euler. Problem 6:\n' \
              'The sum of the squares of the first ten natural numbers is, \n' \
              '1^2+2^2+...+10^2=385 \n' \
              'The square of the sum of the first ten natural numbers is,\n ' \
              '(1+2+...+10)^2=55^2=3025\n' \
              'Hence the difference between the sum of the squares of the first ten natural numbers \n' \
              'and the square of the sum is. \n' \
              '3025-385=2640\n' \
              'Find the difference between the sum of the squares of the first one hundred natural numbers ' \
              'and the square of the sum.'

    NUM = 100

    @property
    def getinfo(self):
        return self.details

    def result(self):
        r = range(1, self.NUM + 1)
        a = 0
        b = 0
        for i in r:
            a += i ** 2
            b += i
        b = b ** 2
        result = b - a
        return result




