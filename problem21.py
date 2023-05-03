from Problem import AbsProblem


class Problem21(AbsProblem):
    details = "Project Euler. Problem 21:\n" \
              "Let d(n) be defined as the sum of proper divisors of n " \
              "(numbers less than n which divide evenly into n).\n" \
              "If d(a) = b and d(b) = a, where a ≠ b, " \
              "then a and b are an amicable pair and each of a and b are called amicable numbers.\n" \
              "For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; " \
              "therefore d(220)=284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.\n" \
              ">>Evaluate the sum of all the amicable numbers under 10000.\n"

    OFFSET = 15
    N = 10000
    friendNumLis = []

    @property
    def getinfo(self):
        return self.details

    def result(self):
        num_list, sum_list = self.__find_friends(list(range(2, self.N)))
        num_list_from_sum_list, sum_list_from_sum_list = self.__find_friends(sum_list)

        for i, v in enumerate(num_list):
            if num_list[i] == sum_list_from_sum_list[i] and num_list[i] != 0 and num_list[i] != sum_list[i]:
                self.friendNumLis.append(num_list[i])
            else:
                pass

        return sum(self.friendNumLis)

    @staticmethod
    def __check_divider(num):
        for y in range(2, num):
            if num % y == 0:
                return True
        return False

    @staticmethod
    def __get_dividers(num):
        dividers = [1]
        for y in range(2, num):
            if num % y == 0:
                dividers.append(y)
        return dividers

    def __find_friends(self, n_list):
        nums = []
        sums = []
        for i in n_list:
            if self.__check_divider(i):
                sums.append(sum(self.__get_dividers(i)))
                nums.append(i)
            else:
                nums.append(0)
                sums.append(0)
        return nums, sums
