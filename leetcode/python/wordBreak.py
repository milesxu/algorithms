class Solution:

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak3(self, s, dict):
        leafStack, stringLst = [], []
        sets, setd = set(list(s)), set(list("".join(dict)))
        if len(sets) > len(setd):
            return stringLst
        # previous, next nodes, start strings, invalid strings, valid strings
        # key string the node represent
        cur = [None, [], set(), set(),
               sorted(list(dict), key=len, reverse=True), ""]

        def iterate(string, node):
            child = None
            for p in node[4][:]:
                if p in node[2]:
                    continue
                i = string.find(p)
                if i == -1:
                    node[3].add(p)
                    node[4].remove(p)
                elif i == 0:
                    node[2].add(p)
                    child = [node, [], set(), set(), list(node[4]), p]
                    node[1].append(child)
                    break
            return child

        ss = s
        while cur:
            temp = iterate(ss, cur)
            if temp is None:
                cur, ss = cur[0], cur[5] + ss
            elif temp[5] == ss:
                leafStack.append(temp)
            else:
                ss, cur = ss[len(temp[5]):], temp

        while leafStack:
            leaf, temp = leafStack.pop(), []
            while leaf[5]:
                temp.insert(0, leaf[5])
                leaf = leaf[0]
            stringLst.append(" ".join(temp))
        return stringLst

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak2(self, s, dict):
        sets, setd = set(list(s)), set(list("".join(dict)))
        if len(sets) > len(setd):
            return False
        # previous, next nodes, start strings, invalid strings, valid strings
        # key string the node represent
        cur = [None, [], set(), set(),
               sorted(list(dict), key=len, reverse=True), ""]

        def iterate(string, node):
            child = None
            for p in node[4][:]:
                if p in node[2]:
                    continue
                i = string.find(p)
                if i == -1:
                    node[3].add(p)
                    node[4].remove(p)
                elif i == 0:
                    node[2].add(p)
                    child = [node, [], set(), set(), list(node[4]), p]
                    node[1].append(child)
                    break
            return child

        ss = s
        while cur:
            temp = iterate(ss, cur)
            if temp is None:
                cur, ss = cur[0], cur[5] + ss
            elif temp[5] == ss:
                return True
            else:
                ss, cur = ss[len(temp[5]):], temp
        return False

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak1(self, s, dict):
        sets, setd = set(list(s)), set(list("".join(dict)))
        if len(sets) > len(setd):
            return False
        i, j, stack = 0, len(s), []
        while j:
            if s[i:j] in dict:
                if j == len(s):
                    return True
                stack.append([i, j])
                i, j = j, len(s)
            else:
                j -= 1
                while j == i and stack:
                    i, j = stack.pop()
                    j -= 1
        return False

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        stringLst = []
        sets, setd = set(list(s)), set(list("".join(dict)))
        if len(sets) > len(setd):
            return stringLst
        i, j, stack = 0, len(s), []
        while j:
            if s[i:j] in dict and j != len(s):
                    stack.append([i, j])
                    i, j = j, len(s)
            else:
                if s[i:j] in dict:
                    temp = [s[p[0]:p[1]] for p in stack]
                    temp.append(s[i:])
                    stringLst.append(" ".join(temp))
                j -= 1
                while j == i and stack:
                    i, j = stack.pop()
                    j -= 1
        return stringLst


if __name__ == '__main__':
    s = Solution()
    # print(s.wordBreak("abcd", ["a", "abc", "b", "cd"]))
    # print(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
    # print(s.wordBreak("aaaaaaa", ["aaaa", "aa"]))
    print(s.wordBreak("a", ["a"]))
    # print(s.wordBreak("ab", ["a", "b"]))
    # print(s.wordBreak("bb", ["a", "b", "bbb", "bbbb"]))
