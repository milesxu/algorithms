class Solution:

    # @return an integer
    def romanToInt(self, s):
        n, i = 0, 1000
        rmap = {1000: ['MMM', 'MM', 'M'],
                100: ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C'],
                10: ['XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X'],
                1: ['IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']}
        while i:
            for j, p in enumerate(rmap[i]):
                if s.find(p) == 0:
                    n, s = n + (len(rmap[i]) - j) * i, s[len(p):]
                    break
            i //= 10
        return n
