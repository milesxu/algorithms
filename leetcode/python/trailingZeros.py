class Solution:

    # @return an integer
    def trailingZeroes(self, n):
        zeros = 0
        while n:
            n //= 5
            zeros += n
        return zeros
