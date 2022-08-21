from abc import ABC
from Problem import AbsProblem


class Problem10(AbsProblem, ABC):
    details = "Project Euler. Problem 10:\n" \
              "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\n" \
              ">>Find the sum of all the primes below two million."

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = self.__sumPrime(2000000)
        print(result)
        return result

    def __sumPrime(self, Num):
        primes = list(range(0, Num))
        primes[0:2] = [0, 0]
        p = 2
        while p*p < Num:
            if primes[p]:
                removeIndexes = [0 for _ in range(p * p, Num, p)]
                primes[p*p:Num:p] = removeIndexes
            p += 1
        return sum(primes)

#pr = Problem10()
#print(pr.getinfo)