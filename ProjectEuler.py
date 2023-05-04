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
from problem12 import Problem12
from problem13 import Problem13
from problem14 import Problem14
from problem15 import Problem15
from problem16 import Problem16
from problem17 import Problem17

from problem20 import Problem20
from problem21 import Problem21
from problem22 import Problem22

__indexList = [sub.replace('Problem', '') for sub in list(filter(lambda obj: 'Problem' in obj, dir()))]
_sortedProblemIndexes = sorted([int(i) for i in __indexList], key=int)


class ProjectEuler:
    suite = []

    def __init__(self, problem=-1):

        if problem == -1:
            for prIndex in _sortedProblemIndexes:
                className = 'Problem' + str(prIndex)
                self.suite.append(globals()[className]())
        else:
            if problem in _sortedProblemIndexes:
                className = 'Problem' + str(problem)
                self.suite.append(globals()[className]())
