class Solution:

    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        negative = False
        if num1[0] == '-':
            negative = not negative
            num1 = num1[1:]
        if num2[0] == '-':
            negative = not negative
            num2 = num2[1:]
        dot = 0
        temp = num1.find('.')
        if temp > -1:
            num1 = num1[: temp] + num1[temp + 1:]
            dot += len(num1) - temp
        temp = num2.find('.')
        if temp > -1:
            num2 = num2[: temp] + num2[temp + 1:]
            dot += len(num2) - temp
        a = [int(p) for p in reversed(num1)]
        b = [int(p) for p in reversed(num2)]
        rarr = [0] * (len(a) + len(b))
        for i, p in enumerate(a):
            carry = 0
            for j, q in enumerate(b):
                carry, rarr[i + j] = divmod(p * q + carry + rarr[i + j], 10)
            if carry:
                rarr[i + len(b)] = carry
        while rarr and not rarr[-1]:
            rarr.pop()
        if not rarr:
            return '0'
        result = ''.join([str(p) for p in reversed(rarr)])
        if dot:
            result = result[: len(result) - dot + 1] + '.' + \
                result[len(result) - dot + 1:]
        if negative:
            result = '-' + result
        return result


if __name__ == '__main__':
    m = Solution()
    print(m.multiply('0', '0'))
