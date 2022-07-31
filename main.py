from ProjectEuler import ProjectEuler

pe = ProjectEuler()

for problem in pe.suite:
    print("---------------------------")
    problemDesc = problem.getinfo
    print(problemDesc)
    problemResult = problem.result()
    print("RESULT: " + str(problemResult))
