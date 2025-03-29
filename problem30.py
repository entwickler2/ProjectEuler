# problem 30
from abc import ABC
from Problem import AbsProblem
from math import log10


def get_max_range(power):
    digit_range = 1
    # The sum of the digits powers is max when all digits are 9
    number_range = 9 ** power
    while digit_range < len(str(number_range)):
        # print(f"num: {num} num_range: {len(str(num))} digit_range: {digit_range}")
        digit_range += 1
        number_range += 9 ** power
    # print(f"found range: {num} with digits: {digit_range}")
    return number_range


class Problem30(AbsProblem, ABC):
    details = "Project Euler. Problem 30:\n" \
              "Surprisingly there are only three numbers " \
              "that can be written as the sum of fourth powers of their digits:\n" \
              "1634 = 1^4 + 6^4 + 3^4 + 4^4\n" \
              "8208 = 8^4 + 2^4 + 0^4 + 8^4\n" \
              "9474 = 9^4 + 4^4 + 7^4 + 4^4\n" \
              "As 1^4 = 1 is not a sum it is not included." \
              "The sum of these numbers is 1634 + 8208 + 9474\n" \
              ">> Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.\n"
    __N = 5

    @property
    def getinfo(self):
        return self.details

    def result(self):
        filtered_numbers = list()
        # print(f"max range: {max_range} for {self.__N}")
        for n in range(2, get_max_range(self.__N)+1):
            # sum of powers of all digits
            if n == sum([int(x)**self.__N for x in str(n)]):
                filtered_numbers.append(n)
                # print(f"{filtered_numbers}")
        return sum(filtered_numbers)
