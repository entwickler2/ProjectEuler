from Problem import AbsProblem


class Problem2(AbsProblem):
    details = "PROJECT EULER, Problem 2: \n" \
              "Each new term in the Fibonacci sequence is generated " \
              "by adding the previous two terms. \n" \
              "By starting with 1 and 2, the first 10 terms will be:\n" \
              "1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n" \
              ">>By considering the terms in the Fibonacci sequence " \
              "whose values do not exceed four million, " \
              "find the sum of the even-valued terms."

    @property
    def getinfo(self):
        return self.details

    def result(self):
        f_numbers = [1, 2]
        count = 0
        while 1:
            count += 1
            a = f_numbers[len(f_numbers) - 1]
            b = f_numbers[len(f_numbers) - 2]
            f = a + b
            if f < 4000000:
                f_numbers.append(f)
                # print("Count: %d current num %d current" % (count, f))
            else:
                break

        # print(f_numbers)
        # print("Fibonacci even nums less 4000000")
        even_fib = []
        for i in f_numbers:
            if i % 2 == 0:
                even_fib.append(i)

        result = sum(even_fib)

        # print(even_fib)
        # print("Sum of Fibonacci even nums less 4000000:  %d" % result)
        return result
