# problem 23
from abc import ABC
from Problem import AbsProblem


class Problem23(AbsProblem, ABC):
    details = "Project Euler. Problem 23:\n" \
              "A perfect number is a number for which the sum of its proper divisors is exactly equal to the " \
              "number.\n" \
              "For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, \n" \
              "which means that 28 is a perfect number.\n" \
              "A number n is called deficient if the sum of its proper divisors is less than n and \n" \
              "it is called abundant if this sum exceeds n.\n" \
              "As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, \n" \
              "the smallest number that can be written as the sum of two abundant numbers is 24. \n" \
              "By mathematical analysis, it can be shown that all integers greater than 28123 \n" \
              "can be written as the sum of two abundant numbers. However, \n" \
              "this upper limit cannot be reduced any further by analysis even though it is known that \n" \
              "the greatest number that cannot be expressed as the sum of two abundant numbers is less \n" \
              "than this limit.\n" \
              ">>Find the sum of all the positive integers which cannot be written \n" \
              "as the sum of two abundant numbers.\n"

    __abundant_nums = []
    __non_sum_of_two = []
    __sum_of_two = set()
    __magic_num_l = 12
    __magic_num_h = 28123

    @property
    def getinfo(self):
        return self.details

    def result(self):
        self.__find_all_abundant_numbers()
        # print("len of abundant numbers: {0}: {1}".format(len(self._abundant_nums), self._abundant_nums, ))
        self.__find_all_sum_of_two()
        # print("len of possible sum of two nums: {0}\n numbers: {1}".format(len(self._sum_of_two), self._sum_of_two))
        self.__find_all_non_sum_of_two()
        # print("len of non sum of two numbers: {0} {1}".format(len(self._non_sum_of_two), self._non_sum_of_two))
        return sum(self.__non_sum_of_two)

    def __find_all_abundant_numbers(self):
        for i in range(self.__magic_num_l, self.__magic_num_h + 1):
            if self.__is_abundant_num(i):
                self.__abundant_nums.append(i)

    def __find_all_sum_of_two(self):
        for i in self.__abundant_nums:  # _magic_num
            for j in self.__abundant_nums:
                a = i + j
                if a < self.__magic_num_h:
                    self.__sum_of_two.add(a)

    def __find_all_non_sum_of_two(self):
        for i in range(1, self.__magic_num_h):
            if i not in self.__sum_of_two:
                self.__non_sum_of_two.append(i)

    @staticmethod
    def __is_abundant_num(num):
        dividers = []
        for i in range(1, num):
            if num % i == 0:
                dividers.append(i)
        if num < sum(dividers):
            # print("{0}: {1} sum: {2}".format(num, dividers, sum(dividers)))
            return True
        else:
            return False
