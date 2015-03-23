class Solution:

    # @return an integer
    def divide(self, dividend, divisor):
        quotient, absd, absv = 0, abs(dividend), abs(divisor)
        while absd > absv:
            k, n = absv, 0
            while absd > k:
                k <<= 1
                n += 1
            quotient += (1 << (n - 1))
            absd -= (absv << (n - 1))
        if absd == absv:
            quotient += 1
            absd = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            # if absd:
            #     return -quotient - 1
            # else:
                return -quotient
        return min(quotient, (1 << 31) - 1)


if __name__ == '__main__':
    dv = Solution()
    print(dv.divide(10, 3))
