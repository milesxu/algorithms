class Solution:

    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        reverse, factor, number = s[::-1], 1, 0
        for p in reverse:
            number += (ord(p) - ord('A') + 1) * factor
            factor *= 26
        return number
