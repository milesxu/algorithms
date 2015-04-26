class Solution:

    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        candidate, selected, total = [list(range(n))], set(), set(range(n))
        while candidate:
            if not candidate[-1]:
                candidate.pop()
                if candidate:
                    selected.remove(candidate[-1].pop())
            elif len(candidate) < n:
                a, tset = candidate[-1][-1], set([candidate[-1][-1]])
                if a > 0:
                    tset.add(a - 1)
                if a < n - 1:
                    tset.add(a + 1)
                clist = list(total - selected - tset)
                if not clist:
                    candidate[-1].pop()
                else:
                    candidate.append(clist)
                    selected.add(a)
            else:
                temp = []
                for i in range(n):
                    q = candidate[i][-1]
                    queen = ''.join(['.' * q, 'Q', '.' * (n - q - 1)])
                    temp.append(queen)
                result.append(temp)
                candidate.pop()
                if candidate:
                    selected.remove(candidate[-1].pop())
        return result


if __name__ == '__main__':
    snq = Solution()
    print(snq.solveNQueens(5))
