import sys
from time import time
from ProjectEuler import ProjectEuler


def main(problemid=-1):
    pe = ProjectEuler(problemid)
    print("---------------------------")
    print("Project Euler")
    print("selected problems: %d" % len(pe.suite))
    print("---------------------------")
    totalStart = time()
    for prob in pe.suite:
        problemDesc = prob.getinfo
        print(problemDesc)
        start = time()
        problemResult = prob.result
        print("RESULT: " + str(problemResult))
        print("Elapsed time: %f seconds" % (time() - start))
        print("---------------------------")
    print("TOTAL ELAPSED TIME: %f seconds" % (time() - totalStart))


if __name__ == "__main__":
    argLen = len(sys.argv)
    if argLen == 1:
        print("No arguments, the full suite is selected for running")
        main()
    elif argLen == 2:
        argument = sys.argv[1]
        print("Problem%s is selected for running" % argument)
        main(int(argument))
    else:
        print(f"Wrong argument")



