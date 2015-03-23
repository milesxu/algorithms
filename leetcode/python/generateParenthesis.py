class Solution:

    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        combinations, result = [[0], [1]], []
        while len(combinations[0]) < n - 1:
            m, temp = len(combinations[0]) + 1, []
            for p in combinations:
                tsum = sum(p)
                for i in range(m + 1):
                    if tsum + i > m:
                        break
                    else:
                        temp.append(p + [i])
                # temp = [p + [i] for p in combinations for i in range(m + 1)
                #         if sum(p) <= m - i]
            combinations = temp
        for p in combinations:
            temp = p + [n - sum(p)]
            result.append(''.join(['(' + ')' * q for q in temp]))
        return result
