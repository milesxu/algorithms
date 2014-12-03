class Solution:

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result, rs = [], s[::-1]

        def palindrome(start, end):
            rend, rstart = len(s) - start, len(s) - end
            if s[start:end] == rs[rstart:rend]:
                return True
            return False

        stack = [[0, len(s)]]
        while stack:
            i, j = stack[-1]
            if i == len(s):
                temp = []
                for i in range(1, len(stack)):
                    temp.append(s[stack[i - 1][0]:stack[i][0]])
                result.append(temp)
                stack.pop()
            elif j <= i:
                stack.pop()
            else:
                end = s.rfind(s[i], i, j)
                stack[-1][1] = end
                if palindrome(i, end + 1):
                    stack.append([end + 1, len(s)])
        return result

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        icache, rs = dict(), s[::-1]

        def palindrome(start, end):
            rend, rstart = len(s) - start, len(s) - end
            if s[start:end] == rs[rstart:rend]:
                return True
            return False

        for i, p in enumerate(s):
            if p in icache:
                icache[p].append(i)
            else:
                icache[p] = [i]

        cut = [-1] * len(s)
        cut[0] = 0
        for i in range(len(cut)):
            temp = 0
            if i:
                temp = cut[i - 1] + 1
                if cut[i] == -1 or cut[i] > temp:
                    cut[i] = temp
            p = s[i]
            candidate = len(icache[p]) - 1
            while i < icache[p][candidate]:
                end = icache[p][candidate]
                if (cut[end] == -1 or cut[end] > temp) \
                        and palindrome(i, end + 1):
                    cut[end] = temp
                candidate -= 1
        return cut[-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.partition('a'))
    # print(s.partition('bb'))
    print(s.minCut('cbbbcc'))
    print(s.minCut('cbb'))
    print(s.minCut('bb'))
    print(s.minCut('a'))
    print(s.minCut(
        'fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbha\
        fehieabbdfeigbiaggchaeghaijfbjhi'))
    print(s.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaa"))
