from abc import ABC
from Problem import AbsProblem


class Problem7(AbsProblem, ABC):
    details = 'Project Euler. Problem 7:\n' \
              'By listing the first six prime numbers: \n' \
              '2, 3, 5, 7, 11, and 13, \n' \
              'we can see that the 6th prime is 13.\n' \
              '>>What is the 10 001st prime number?'

    __NUM = 10001

    @property
    def getinfo(self):
        return self.details

    @staticmethod
    def __checkNum(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def result(self):
        number = 1
        simpleNumCounter: int = 0
        while 1:
            number += 1
            if self.__checkNum(number):
                simpleNumCounter += 1
                # print("%d: %d" % (SimpleNumCounter, number))
                if simpleNumCounter == self.__NUM:
                    break
        result = number
        return result
