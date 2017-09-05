class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        minLen = min(len(a), len(b)) - 1
        maxLen = max(len(a), len(b)) - 1
        strS = b if len(a) >= len(b) else a
        strB = a if len(a) >= len(b) else b
        c, carry = [], 0
        while minLen > -1:
            temp = int(strB[maxLen]) + int(strS[minLen]) + carry
            if temp == 0:
                c.append('0')
            elif temp == 1:
                c.append('1')
                carry = 0
            elif temp == 2:
                c.append('0')
                carry = 1
            else:
                c.append('1')
                carry = 1
            maxLen -= 1
            minLen -= 1
            
        while (maxLen > -1 and carry):
            temp = int(strB[maxLen]) + carry
            if temp == 1:
                c.append('1')
                carry = 0
            else:
                c.append('0')
                carry = 1
