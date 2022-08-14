from Problem import AbsProblem


class Problem1(AbsProblem):
    details = "Project Euler. Problem 1:\n" \
              "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.\n" \
              "The sum of these multiples is 23.\n" \
              ">>Find the sum of all the multiples of 3 or 5 below 1000."

    @property
    def getinfo(self):
        return self.details

    def result(self):
        result = 0
        for i in range(1, 1000):
            if (i % 3 == 0) or (i % 5 == 0):
                result += i
        return result
