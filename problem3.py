from Problem import AbsProblem


class Problem3(AbsProblem):
    details = "PROJECT EULER, Problem 3: \n" \
              "The prime factors of 13195 are 5, 7, 13 and 29. \n" \
              ">>What is the largest prime factor of the number 600851475143 ?"

    refNum = 600851475143
    dividers = []

    @property
    def getinfo(self):
        return self.details

    def result(self):
        self.__findDividers(self.refNum)
        result = self.__checkDividersForSimple()
        return result

    def __checkNum(self, num):
        if (num % 2 == 0) or (num % 3 == 0):
            return False
        else:
            for i in range(2, num):
                if (num % i == 0):
                    return False
        return True

    def __findDividers(self, num):
        arr = range(2, num)
        for a in arr:
            if (num % a == 0):
                print(a)
                self.dividers.append(a)
                if (len(self.dividers) > 0):
                    if (num / a == self.dividers[0]):
                        print("end")
                        return 1
        return 1

    def __checkDividersForSimple(self):
        for a in self.dividers[::-1]:
            if self.__checkNum(a):
                return a
        return -1
