from Problem import AbsProblem


class Problem5(AbsProblem):
    details = "Project Euler. Problem 5:\n" \
              "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any " \
              "remainder.\n" \
              ">>What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

    __NUM = 20

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = 0
        while 1:
            result += self.__NUM
            if self.__check_num(result):
                break
        return result

    def __check_num(self, result):
        y = 0
        for i in range(2, self.__NUM+1):
            if result % i == 0:
                pass
            else:
                return False
        return True

# for i in range(1,NUM):
#    print("%d/%d = %f" %(result, i, result/i))
