from Problem import AbsProblem


class Problem16(AbsProblem):
    details = "Project Euler. Problem 16:\n" \
              "2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.\n" \
              ">>What is the sum of the digits of the number 2^1000?"

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = 0
        a = str(2 ** 1000)
        for i in a:
            result += int(i)
        return result
