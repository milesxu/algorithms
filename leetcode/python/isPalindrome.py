class Solution:

    # @return a boolean
    def isPalindrome(self, x):
        bound = 2 ** 31 - 1
        factor, y = 1, abs(x)
        if x >= 0 and x < 10:
            return True
        while factor < y:
            factor *= 10
            if factor == y:
                return False
        factor //= 10
        n = 0
        while factor > 1:
            y, temp = divmod(y, 10)
            temp *= factor
            if bound - temp <= n:
                return False
            n += temp
            factor //= 10
        n += y
        if n == x:
            return True
        return False
