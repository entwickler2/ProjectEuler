from problem1 import Problem1
from problem2 import Problem2
from problem3 import Problem3
from problem4 import Problem4
from problem5 import Problem5

class ProjectEuler:
    suite = []

    def __init__(self):
        self.suite.append(Problem1())
        self.suite.append(Problem2())
        self.suite.append(Problem3())
        self.suite.append(Problem4())
        self.suite.append(Problem5())
