# Number letter counts
# Problem 17
from abc import ABC
from Problem import AbsProblem


class Problem17(AbsProblem, ABC):
    details = "Project Euler. Problem 17:\n" \
              "If the numbers 1 to 5 are written out in words: one, two, three, four, five, \n" \
              "then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.\n" \
              ">>If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, \n" \
              "how many letters would be used? \n" \
              "NOTE: Do not count spaces or hyphens. \n" \
              "For example, 342 (three hundred and forty-two) contains 23 letters and \n" \
              "115 (one hundred and fifteen) contains 20 letters. The use of \"and\" \n" \
              "when writing out numbers is in compliance with British usage. \n"

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = 0
        for i in range(1, 1000 + 1):
            s = str(i)
            number_string = ''
            if len(s) == 1:
                word_unit = self.__decode_units(s)
                number_string = word_unit
            elif len(s) == 2:
                word_dozens = self.__decode_dozens(s)
                number_string = word_dozens
            elif len(s) == 3:
                word_hundreds = self.__decode_hundreds(s)
                number_string = word_hundreds
            elif len(s) == 4:
                word_thousands = self.__decode_thousands(s)
                number_string = word_thousands
            length = len(number_string.replace(' ', ''))
            # print("%s - %s %s" % (s, number_string, length))
            result += length
        return result

    @staticmethod
    def __decode_units(string):
        word_num = ''
        if '1' in string:
            word_num = 'one'
        elif '2' in string:
            word_num = 'two'
        elif '3' in string:
            word_num = 'three'
        elif '4' in string:
            word_num = 'four'
        elif '5' in string:
            word_num = 'five'
        elif '6' in string:
            word_num = 'six'
        elif '7' in string:
            word_num = 'seven'
        elif '8' in string:
            word_num = 'eight'
        elif '9' in string:
            word_num = 'nine'
        return word_num

    def __decode_dozens(self, string):
        word_num = ''
        if '10' in string:
            word_num = 'ten'
        elif '11' in string:
            word_num = 'eleven'
        elif '12' in string:
            word_num = 'twelve'
        elif '13' in string:
            word_num = 'thirteen'
        elif '14' in string:
            word_num = 'fourteen'
        elif '15' in string:
            word_num = 'fifteen'
        elif '16' in string:
            word_num = 'sixteen'
        elif '17' in string:
            word_num = 'seventeen'
        elif '18' in string:
            word_num = 'eighteen'
        elif '19' in string:
            word_num = 'nineteen'
        elif '2' in string[0]:
            word_num = 'twenty' + self.__decode_units(string[1])
        elif '3' in string[0]:
            word_num = 'thirty' + self.__decode_units(string[1])
        elif '4' in string[0]:
            word_num = 'forty' + self.__decode_units(string[1])
        elif '5' in string[0]:
            word_num = 'fifty' + self.__decode_units(string[1])
        elif '6' in string[0]:
            word_num = 'sixty' + self.__decode_units(string[1])
        elif '7' in string[0]:
            word_num = 'seventy' + self.__decode_units(string[1])
        elif '8' in string[0]:
            word_num = 'eighty' + self.__decode_units(string[1])
        elif '9' in string[0]:
            word_num = 'ninety' + self.__decode_units(string[1])
        elif '0' in string[0]:
            word_num = self.__decode_units(string[1])
        return word_num

    def __decode_hundreds(self, string):
        if '100' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '200' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '300' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '400' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '500' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '600' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '700' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '800' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        elif '900' in string:
            word_num = self.__decode_units(string[0]) + ' hundred'
        else:
            word_num = self.__decode_units(string[0]) + ' hundred and ' + self.__decode_dozens(string[1:])
        return word_num

    def __decode_thousands(self, string):
        word_num = ''
        if '1000' in string:
            word_num = self.__decode_units(string[0]) + ' thousand'
        return word_num
