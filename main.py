from time import time
from ProjectEuler import ProjectEuler

pe = ProjectEuler()
print("---------------------------")
print("Project Euler")
print("solved problems: %d" % len(pe.suite))
print("---------------------------")
for prob in pe.suite:
    problemDesc = prob.getinfo
    print(problemDesc)
    start = time()
    problemResult = prob.result()
    print("RESULT: " + str(problemResult))
    print("Elapsed time: %f seconds" % (time() - start))
    print("---------------------------")
