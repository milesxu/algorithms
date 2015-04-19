class Solution:

    # @return a string
    def countAndSay(self, n):
        nstr = str(1)
        for i in range(n - 1):
            cur, m, temp = None, 0, []
            for p in nstr:
                if cur is None:
                    cur, m = p, 1
                elif cur == p:
                    m += 1
                else:
                    temp, cur, m = temp + [str(m), cur], p, 1
            temp += [str(m), cur]
            nstr = ''.join(temp)
        return nstr
