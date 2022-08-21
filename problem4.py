from Problem import AbsProblem

class Problem4(AbsProblem):
    details = "Project Euler. Problem 4:\n" \
              "A palindromic number reads the same both ways. " \
              "The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\n" \
              ">>Find the largest palindrome made from the product of two 3-digit numbers."

    __refNum1 = [999, 100]
    __refNum2 = [999, 100]
    __palindromes = []

    @property
    def getinfo(self):
        return self.details

    def result(self):
        self.__findMults(self.__refNum1, self.__refNum2)
        result = max(self.__palindromes)
        return result

    def __checkForPalindrome(self, num):
        str1 = str(num)
        str2 = str1[::-1]
        if str1 == str2:
            return True
        else:
            return False

    def __findMults(self, num1,num2):
        arr1 = range(num1[0],num1[1],-1)
        arr2 = range(num2[0],num2[1],-1)
        for a in arr1:
            for b in arr2:
                c = a*b
                if self.__checkForPalindrome(c):
                    self.__palindromes.append(c)
                    #print("POLINDROM: %d number 1: %d  number 2: %d" % (c,a,b))
                    # return c
        return 0

