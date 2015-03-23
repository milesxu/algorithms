class Solution:

    # @return an integer
    def reverse(self, x):
        y, result = abs(x), 0
        while y:
            y, temp = divmod(y, 10)
            result = result * 10 + temp
        if result >> 31:
            return 0
        if x < 0:
            return -result
        return result
