class Solution:

    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        m, n = 0, 0
        for p in num:
            if n == 0:
                m, n = p, n + 1
            elif m == p:
                n += 1
            else:
                n -= 1
        return m
