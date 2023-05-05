# Number letter counts
# Problem 19
from abc import ABC
from Problem import AbsProblem
import calendar


class Problem19(AbsProblem, ABC):
    details = "Project Euler. Problem 19:\n" \
              "You are given the following information, but you may prefer to do some research for yourself. \n" \
              "- 1 Jan 1900 was a Monday.\n" \
              "- Thirty days has September, April, June and November. All the rest have thirty-one,\n" \
              "  Saving February alone, \n" \
              "  Which has twenty-eight, rain or shine. \n" \
              "  And on leap years, twenty-nine. \n" \
              "- A leap year occurs on any year evenly divisible by 4, " \
              "but not on a century unless it is divisible by 400. \n" \
              ">>How many Sundays fell on the first of the month during the twentieth century " \
              "(1 Jan 1901 to 31 Dec 2000)?\n"

    @property
    def getinfo(self):
        return self.details

    def result(self):
        sundays = 0
        obj = calendar.Calendar(firstweekday=6)
        for year in range(1901, 2000 + 1):
            for month in range(1, 12 + 1):
                days_iterator = obj.itermonthdays2(year, month)
                for day in days_iterator:
                    if day[0] == 1 and day[1] == 6:
                        sundays += 1
                        # print("%02d.%02d.%d " % (day[0], month, year))
        return sundays
