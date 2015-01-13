class Solution:

    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        integer, residue = divmod(abs(numerator), abs(denominator))
        if numerator * denominator < 0:
            negative = '-'
        else:
            negative = ''
        if residue:
            quotient, rqmap, n = [], {}, 0
            while residue:
                residue *= 10
                if residue in rqmap:
                    n = rqmap[residue]
                    return negative + str(integer) + '.' + \
                        ''.join(map(str, quotient[:n])) + '(' + \
                        ''.join(map(str, quotient[n:])) + ')'
                rqmap[residue] = n
                temp, residue = divmod(residue, abs(denominator))
                quotient.append(temp)
                n += 1
            return negative + str(integer) + '.' + ''.join(map(str, quotient))
        return negative + str(integer)
