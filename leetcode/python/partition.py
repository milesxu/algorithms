class Solution:

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result, stack = [], [0]

        def palindrome(string):
            start, end, n = 0, -1, (len(string) - 1) // 2
            while start <= n:
                if string[start] != string[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        def testInsert(end):
            for i in range(end, stack[-1], -1):
                if palindrome(s[stack[-1]:i]):
                    stack.append(i)
                    return True
            return False

        j = len(s)
        while True:
            while stack[-1] < len(s):
                while not testInsert(j):
                    j = stack.pop()
                    if not j:
                        return result
                    j -= 1
                j = len(s)
            temp = []
            for i in range(1, len(stack)):
                temp.append(s[stack[i - 1]:stack[i]])
            result.append(temp)
            j = stack.pop() - 1

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        result, stack, cache = len(s) + 1, [0], set()

        def palindrome(string):
            if string in cache:
                # print('hit!')
                return True
            start, end, n = 0, -1, (len(string) - 1) // 2
            while start <= n:
                if string[start] != string[end]:
                    return False
                start, end = start + 1, end - 1
            cache.add(string)
            return True

        def testInsert(end):
            for i in range(end, stack[-1], -1):
                if palindrome(s[stack[-1]:i]):
                    stack.append(i)
                    return True
            return False

        j = len(s)
        while True:
            while stack[-1] < len(s) and len(stack) < result:
                # print(result)
                while not testInsert(j):
                    j = stack.pop()
                    if not j:
                        return result - 2
                    j -= 1
                j = len(s)
            if stack[-1] == len(s):
                # result = min(result, len(stack))
                result = len(stack)
                print(result)
            j = stack.pop() - 1

if __name__ == '__main__':
    s = Solution()
    # print(s.partition('a'))
    # print(s.partition('bb'))
    print(s.minCut(
        'fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbha\
        fehieabbdfeigbiaggchaeghaijfbjhi'))
