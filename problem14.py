from Problem import AbsProblem


class Problem14(AbsProblem):
    details = "Project Euler. Problem 14:\n" \
              "The following iterative sequence is defined for the set of positive integers:\n" \
              "n → n/2 (n is even)\n" \
              "n → 3n + 1 (n is odd)\n" \
              "Using the rule above and starting with 13, we generate the following sequence:\n" \
              "13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1\n" \
              "It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. \n" \
              "Although it has not been proved yet (Collatz Problem), \n" \
              "it is thought that all starting numbers finish at 1.\n" \
              ">>Which starting number, under one million, produces the longest chain?\n" \
              "NOTE: Once the chain starts the terms are allowed to go above one million."

    @property
    def getinfo(self):
        return self.details

    def result(self):
        maxLen = 0
        Number = 0
        for i in range(1, 1000000):
            CurrSeq = self.__getCollatzSequense(i)
            CurrLen = len(CurrSeq)
            if CurrLen > maxLen:
                maxLen = CurrLen
                Number = i
                # print("num: %d len %s" % (Number, maxLen))
        return Number

    def __getCollatzSequense(self, num):
        seq = [num]
        while num != 1:
            if num % 2 == 0:
                num /= 2
                seq.append(num)
            else:
                num = 3 * num + 1
                seq.append(num)
        return seq
