__author__ = 'aloneranger'


class Solution:

    # @return a boolean, recursive version
    def isMatchr(self, s, p):

        def recursion1(i, j):
            if i == len(s) and j == len(p):
                return True
            if j + 1 < len(p) and p[j + 1] == '*':
                if p[j] == '.' or p[j] == s[i]:
                    return recursion1(i + 1, j) or recursion1(i + 1, j + 2)
                else:
                    return recursion1(i, j + 2)
            elif p[j] == s[i] or p[j] == '.':
                return recursion1(i + 1, j + 1)
            else:
                return False

        def recursion(i, j, pm=True):
            if i == len(s) and j == len(p):
                return True
            if p[j] == '*':
                temp = pm and (p[j - 1] == '.' or p[j - 1] == s[i])
                return \
                    (temp and (recursion(i + 1, j) or recursion(i, j + 1))) \
                    or (not temp and recursion(i, j + 1))
            temp = p[j] == '.' or p[j] == s[i]
            return pm and recursion(i + temp, j + 1, temp)

        return recursion(0, 0)

    # @return a boolean
    # use a matrix, where the value of [i, j] represents whethert
    # s[0:i] can be matched by p[0:j]
    # prow is initialized so that can correctly compute matches table for s[0]
    # there are three cases for q == '*':
    # s[:i + 1] can match p[:j - 1], then must return true
    # s[:i + 1] cannot match p[:j - 1], but
    # s[:i] can match p[:j + 1] or p[:j - 1], then if l match p[j - 1: j + 1],
    # also return true
    def isMatch(self, s, p):
        prow = [True] + [False] * len(p)
        for i, m in enumerate(p):
            if m == '*':
                prow[i + 1] = prow[i - 1]
        for i, l in enumerate(s):
            trow = [False]
            for j, q in enumerate(p):
                if q == '.':
                    trow.append(prow[j])
                elif q == '*':
                    trow.append(
                        trow[-2] or ((prow[j - 1] or prow[j + 1]) and
                                     (p[j - 1] == '.' or p[j - 1] == l)))
                else:
                    trow.append(prow[j] and l == q)
            prow = trow
        return prow[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('aa', 'a'))
