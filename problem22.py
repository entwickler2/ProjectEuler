# problem 22
from abc import ABC
from io import open
from Problem import AbsProblem


class Problem22(AbsProblem, ABC):
    details = "Project Euler. Problem 22:\n" \
              "Using names.txt (right click and 'Save Link/Target As...'), \n" \
              "a 46K text file containing over five-thousand first names, begin by sorting \n" \
              "it into alphabetical order. Then working out the alphabetical value for each name, \n" \
              "multiply this value by its alphabetical position in the list to obtain a name score.\n" \
              "For example, when the list is sorted into alphabetical order, COLIN, \n" \
              "which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. \n" \
              "So, COLIN would obtain a score of 938 × 53 = 49714.\n" \
              ">>What is the total of all the name scores in the file?\n"

    __ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
             "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = 0
        scores = []
        names = self.__parse_file("p022_names.txt")
        for index, name in enumerate(names):
            scores.append(self.__convert_to_scores(name))
            result += sum(scores[index]) * (index + 1)
        return result

    @staticmethod
    def __parse_file(fpath):
        sorted_names = []
        for line in open(fpath, "r").readlines():
            sorted_names = line.replace('"', '').split(',')
            sorted_names.sort()
        return sorted_names

    def __convert_to_scores(self, n):
        for index, letter in enumerate(self.__ABC):
            n = n.replace(letter, str(index + 1) + ',')
        n = n.split(',')
        n.remove('')
        sc = [int(s) for s in n]
        return sc
