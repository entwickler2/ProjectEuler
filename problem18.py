# problem 18/67
from abc import ABC
from Problem import AbsProblem
from io import open


class Problem18(AbsProblem, ABC):
    details = "Project Euler. Problem 18:\n" \
              "By starting at the top of the triangle below and moving to adjacent numbers on the row below, " \
              "the maximum total from top to bottom is 23. \n" \
              "               3 \n" \
              "              7 4 \n" \
              "             2 4 6 \n" \
              "            8 5 9 3 \n" \
              "That is, 3 + 7 + 4 + 9 = 23.\n" \
              "Find the maximum total from top to bottom of the triangle below:\n" \
              "                75 \n" \
              "              95 64 \n" \
              "             17 47 82 \n" \
              "            18 35 87 10 \n" \
              "           20 04 82 47 65 \n" \
              "          19 01 23 75 03 34 \n" \
              "         88 02 77 73 07 63 67 \n" \
              "        99 65 04 28 06 16 70 92 \n" \
              "       41 41 26 56 83 40 80 70 33 \n" \
              "      41 48 72 33 47 32 37 16 94 29 \n" \
              "     53 71 44 65 25 43 91 52 97 51 14 \n" \
              "    70 11 33 28 77 73 17 78 39 68 17 57 \n" \
              "   91 71 52 38 17 14 91 43 58 50 27 29 48 \n" \
              "  63 66 04 68 89 53 67 30 73 16 69 87 40 31 \n" \
              "04 62 98 27 23 09 70 98 73 93 38 53 60 04  23 \n" \
              "NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. \n" \
              "However, Problem 67, is the same challenge with a triangle containing one-hundred rows; \n" \
              "it cannot be solved by brute force, and requires a clever method! ;o)\n"

    triangle = \
        [[75],
         [95, 64],
         [17, 47, 82],
         [18, 35, 87, 10],
         [20, 4, 82, 47, 65],
         [19, 1, 23, 75, 3, 34],
         [88, 2, 77, 73, 7, 63, 67],
         [99, 65, 4, 28, 6, 16, 70, 92],
         [41, 41, 26, 56, 83, 40, 80, 70, 33],
         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
         [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
         [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    @property
    def getinfo(self):
        return self.details

    def result(self):
        return self.traverse_triangle_bottom_up(self.triangle)

    @staticmethod
    def parse_file(fpath):
        return [[int(i) for i in l.strip('\n').split()] for l in open(fpath, "r").readlines()]

    @staticmethod
    def process_row(lower, upper):
        results = []
        for i in range(0, len(upper)):
            results.append(upper[i] + max(lower[i], lower[i + 1]))
        return results

    def traverse_triangle_bottom_up(self, triangle):
        triangle.reverse()
        results = triangle.pop(0)
        for row in triangle:
            results = self.process_row(results, row)
        return results[0]

    # triangle = parse_file("p067_triangle.txt")
