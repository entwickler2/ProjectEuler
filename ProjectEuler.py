from problem1 import Problem1
from problem2 import Problem2


class ProjectEuler:
    suite = []

    def __init__(self):
        self.suite.append(Problem1())
        self.suite.append(Problem2())
