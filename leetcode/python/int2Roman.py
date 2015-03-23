class Solution:

    # @return a string
    def intToRoman(self, num):
        temp, num = divmod(num, 1000)
        roman = 'M' * temp
        rmap = {100: 'CDM', 10: 'XLC', 1: 'IVX'}
        i = 100
        while i:
            temp, num = divmod(num, i)
            if temp == 9:
                roman += (rmap[i][0] + rmap[i][2])
            elif temp >= 5:
                roman += (rmap[i][1] + rmap[i][0] * (temp - 5))
            elif temp == 4:
                roman += (rmap[i][0] + rmap[i][1])
            else:
                roman += rmap[i][0] * temp
            i //= 10
        return roman
