class Solution:

    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        hexs = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        m = 0
        while n:
            m, n = m + hexs[n & 15], n >> 4
        return m
