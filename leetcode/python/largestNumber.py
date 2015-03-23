class Solution:

    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):

        def substrcmp(stra, strb):
            temp, maxa = len(stra), max(stra[0], stra[-1])
            while temp < len(strb) and maxa == strb[temp]:
                    temp += 1
            if temp == len(strb):
                return 0
            if maxa > strb[temp]:
                return 1
            return -1

        def stringcmp(stra, strb):
            if stra == strb:
                return 0
            if len(stra) < len(strb) and stra == strb[:len(stra)]:
                return substrcmp(stra, strb)
            if len(stra) > len(strb) and stra[:len(strb)] == strb:
                return -substrcmp(strb, stra)
            if stra > strb:
                return 1
            return -1

        string = [str(p) for p in num]
        string.sort(cmp=stringcmp, reverse=True)
        result = ''.join(string)
        if result[0] == '0':
            return '0'
        return result
