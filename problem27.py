# problem 27
from abc import ABC
from Problem import AbsProblem


class Problem27(AbsProblem, ABC):
    details = "Project Euler. Problem 27:\n" \
              "Euler discovered the remarkable quadratic formula: \n" \
              "n^2+n+41:\n" \
              "It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39.\n" \
              "However, when n = 40, 40^2+40+41=40(40+1)+41 is is divisible by 41, and certainly when\n" \
              "n = 41, 41^2+41+41 is clearly divisible by 41.\n" \
              "The incredible formula n^2-79n+1601 was discovered, which produces primes " \
              "for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.\n" \
              "Considering quadratics of the form:\n" \
              "n^2+an+b, where |a|<1000 and |b|<=1000 where |n| is the modulus/absolute value of n\n" \
              "e.g. |11|=11 and |-4|=4\n" \
              ">>Find the product of the coefficients, a and b, \n" \
              "for the quadratic expression " \
              "that produces the maximum number of primes for consecutive values of n, starting with 0.\n"

    __a_range = range(-999, 1000)
    __b_range = range(-1000, 1000 + 1)
    __n = 0
    __ab = {}  # key: tuple(a,b), value: max n value

    @property
    def getinfo(self):
        return self.details

    def result(self):
        for a in self.__a_range:
            for b in self.__b_range:
                pr_amount = self.get_max_prime_count(a, b)
                if pr_amount != 0:
                    self.__ab[(a, b)] = pr_amount
        max_prime_ab_values = max(zip(self.__ab.values(), self.__ab.keys()))
        product_ab = max_prime_ab_values[1][0]*max_prime_ab_values[1][1]
        # print(f"found primes: {max_prime_ab_values} a*b={product_ab}")
        return product_ab

    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                pass
        return True

    def get_max_prime_count(self, a, b):
        n = -1
        count = 0
        while True:
            n += 1
            out = n ** 2 + a * n + b
            if self.is_prime(out):
                count += 1
                # print("a {0} b {1} n {0} out {1} count {2}".format(n, out, count))
                continue
            break
        return count
