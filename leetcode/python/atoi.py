class Solution:

    # @return an integer
    def atoi(self, str):
        negative, bit, symb, strcp = False, [], 0, str.strip()
        for p in strcp:
            if not p.isalnum():
                symb += 1
                if symb > 1:
                    return 0
                if bit:
                    break
                if p == '-':
                    negative = True
            elif p.isdigit():
                bit.append(int(p))
            else:
                if len(bit) > 0:
                    break
                else:
                    return 0
        result, factor, bound, radix, overflow = 0, 1, 2 ** 31, 10, False
        while bit:
            temp = factor * bit.pop()
            if bound - temp <= result:
                overflow = True
                break
            result += temp
            factor *= radix
        if negative:
            if overflow:
                return -bound
            return -result
        if overflow:
            return bound - 1
        return result
