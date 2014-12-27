class Solution:

    # @return an integer
    def reverse(self, x):
        y = abs(x)
        bit = []
        while y:
            y, temp = divmod(y, 10)
            bit.append(temp)
        factor, result, bound = 1, 0, 2 ** 31
        while bit:
            temp = factor * bit.pop()
            if bound - temp < result:
                return 0
            result += temp
            factor *= 10
        if x < 0:
            return -result
        return result
