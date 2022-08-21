from problem1 import Problem1
from problem2 import Problem2
from problem3 import Problem3
from problem4 import Problem4
from problem5 import Problem5
from problem6 import Problem6
from problem7 import Problem7
from problem8 import Problem8
from problem9 import Problem9
from problem10 import Problem10
from problem11 import Problem11
from problem15 import Problem15


class ProjectEuler:
    suite = []

    def __init__(self):
        self.suite.append(Problem1())
        self.suite.append(Problem2())
        self.suite.append(Problem3())
        self.suite.append(Problem4())
        self.suite.append(Problem5())
        self.suite.append(Problem6())
        self.suite.append(Problem7())
        self.suite.append(Problem8())
        self.suite.append(Problem9())
        self.suite.append(Problem10())
        self.suite.append(Problem11())
        #
        self.suite.append(Problem15())
