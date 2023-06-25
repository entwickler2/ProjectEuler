# problem 26
from abc import ABC
from Problem import AbsProblem
from functools import lru_cache


class Problem26(AbsProblem, ABC):
    details = "Project Euler. Problem 26:\n" \
              "A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions \n" \
              "with denominators 2 to 10 are given:\n" \
              "    1/2	= 	0.5\n" \
              "    1/3	= 	0.(3)\n" \
              "    1/4	= 	0.25\n" \
              "    1/5	= 	0.2\n" \
              "    1/6	= 	0.1(6)\n" \
              "    1/7	= 	0.(142857)\n" \
              "    1/8	= 	0.125\n" \
              "    1/9	= 	0.(1)\n" \
              "    1/10	= 	0.1\n" \
              "Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. \n" \
              "It can be seen that 1/7 has a 6-digit recurring cycle.\n" \
              "Find the value of d < 1000 for which 1/d contains the longest recurring cycle \n" \
              "in its decimal fraction part.\n"

    __upper_lim = 1000
    __recurring_cycles = {}
    __recurring_cycle_len = {}

    @property
    def getinfo(self):
        return self.details

    def result(self):
        max_len = 0
        result_den = 1
        for den in range(2, self.__upper_lim + 1):
            rec_cycle = self.__calc_recurring_cycle(1, den)
            rec_cycle_len = len(rec_cycle)
            self.__recurring_cycles[den] = str(rec_cycle)
            self.__recurring_cycle_len[den] = rec_cycle_len
            # print("den: {0} len: {1} rec_cycle: {2}".format(den, rec_cycle_len, self.__recurring_cycles[den]))
            if rec_cycle_len > max_len:
                max_len = rec_cycle_len
                result_den = int(den)
        print("den: {0} recurring_cycle len: {1}".format(result_den, max_len))
        return result_den

    @staticmethod
    def __calc_recurring_cycle(num, den):
        res = ""
        mp = {}
        # First remainder
        rem = num % den
        # Keep finding remainder until either
        # remainder becomes 0 or repeats
        while (rem != 0) and (rem not in mp):
            # Store this remainder
            mp[rem] = len(res)
            # Multiply remainder with 10
            rem = rem * 10
            # Append rem / den to result
            res_part = rem // den
            res += str(res_part)
            # Update remainder
            rem = rem % den

        if rem == 0:
            return ""
        else:
            return res[mp[rem]:]
