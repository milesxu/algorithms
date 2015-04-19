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

        def recursion(i, j):
            if i < len(s) and j == len(p):
                return False
            if i == len(s):
                return p.count('*', j) * 2 == len(p) - j

            def star(k): return k < len(p) - 1 and p[k + 1] == '*'

            temp = star(j)
            if temp and star(j + 2) and p[j] == p[j + 2]:
                return recursion(i, j + 2)
            if s[i] == p[j] or p[j] == '.':
                if temp:
                    return recursion(i, j + 2) or recursion(i + 1, j)
                return recursion(i + 1, j + 1)
            if temp:
                return recursion(i, j + 2)
            return False

        return recursion(0, 0)

    def isMatchr1(self, s, p):
        p1, star = [], []
        for q in p:
            if q == '*':
                star[-1] = 1
            else:
                star.append(0)
                p1.append(q)
        legal = [0] * len(p1)
        for i in range(len(p1) - 1, -1, -1):
            if star[i]:
                legal[i] = 1
            else:
                break
        # print(p1, star, legal)

        def recursion(i, j):
            if i < len(s) and j == len(p1):
                return False
            if i == len(s):
                return j == len(p1) or bool(legal[j])
            if j < len(p1) - 1 and p1[j] == p1[j + 1] \
                    and star[j] and star[j + 1]:
                return recursion(i, j + 1)
            if s[i] == p1[j] or p1[j] == '.':
                if star[j]:
                    return recursion(i, j + 1) or recursion(i + 1, j)
                return recursion(i + 1, j + 1)
            if star[j]:
                return recursion(i, j + 1)
            return False

        return recursion(0, 0)

    def isMatchr2(self, s, p):
        p1, star, i = [], [], 0
        while i < len(p):
            if i < len(p) - 1 and p[i + 1] == '*':
                if not (p1 and star[-1] and (p1[-1] == '.' or p1[-1] == p[i])):
                    p1.append(p[i])
                    star.append(True)
                i += 2
            else:
                p1.append(p[i])
                star.append(False)
                i += 1
        legal = [False] * len(p1)
        for i in range(len(p1) - 1, -1, -1):
            if star[i]:
                legal[i] = True
            else:
                break
        fail = set()

        def recursion(i, j):
            if (i, j) in fail:
                return False
            if i < len(s) and j == len(p1):
                temp = False
            elif i == len(s):
                temp = j == len(p1) or legal[j]
            elif s[i] == p1[j] or p1[j] == '.':
                temp = (recursion(i, j + 1) or recursion(i + 1, j)) if \
                    star[j] else recursion(i + 1, j + 1)
            else:
                temp = recursion(i, j + 1) if star[j] else False
            if temp:
                return True
            fail.add((i, j))
            return False

        return recursion(0, 0)

    def isMatchi(self, s, p):
        p1, star = [], []
        for q in p:
            if q == '*':
                star[-1] = True
            else:
                star.append(False)
                p1.append(q)
        legal = [False] * len(p1)
        for i in range(len(p1) - 1, -1, -1):
            if star[i]:
                legal[i] = True
            else:
                break

        i, j, stack = 0, 0, []
        while True:
            if i < len(s) and j == len(p1):
                if stack:
                    i, j = stack.pop()
                else:
                    return False
            elif i == len(s):
                if j == len(p1) or legal[j]:
                    return True
                elif stack:
                    i, j = stack.pop()
                else:
                    return False
            elif j < len(p1) - 1 and p1[j] == p1[j + 1] \
                    and star[j] and star[j + 1]:
                j += 1
            elif s[i] != p1[j] and p1[j] != '.':
                if star[j]:
                    j += 1
                elif stack:
                    i, j = stack.pop()
                else:
                    return False
            elif star[j]:
                stack.append([i + 1, j])
                j += 1
            else:
                i, j = i + 1, j + 1
        return i == len(s)

    def isMathcAutomaton(self, s, p):
        p1, star, i = [], [], 0
        while i < len(p):
            if i < len(p) - 1 and p[i + 1] == '*':
                if not (p1 and star[-1] and (p1[-1] == '.' or p1[-1] == p[i])):
                    p1.append(p[i])
                    star.append(True)
                i += 2
            else:
                p1.append(p[i])
                star.append(False)
                i += 1

        def prefixtable():
            temp = [0] * len(p1) + 1
            temp[0], k = -1, -1
            for i in range(1, len(p1)):
                while k > -1 and (p1[k + 1] not in p1[i] + '.'):
                    k = temp[k]
                if p1[k + 1] == p1[i]:
                    k += 1
                temp[i] == k
            return temp

        prefix, q = prefixtable(), 0
        for c in s:
            if star[q]:
                q = prefix[q]
            if q < len(p1) and p1[q] == '.' or p1[q] == c:
                q += 1
            else:
                pass

    # @return a boolean
    # use a matrix, where the value of [i, j] represents whether
    # s[0:i] can be matched by p[0:j]
    # prow is initialized so that can correctly compute matches table for s[0]
    # there are three cases for q == '*':
    # s[:i + 1] can match p[:j - 1], then must return true
    # s[:i + 1] cannot match p[:j - 1], but
    # s[:i] can match p[:j + 1] or p[:j - 1], then if l match p[j - 1: j + 1],
    # also return true
    # it is a kind of transmission. "." always transmit the last match result
    # which is match of string just before it. "*" always transmit the match
    # result two chars before it. all transmission are from one row to the
    # other.
    # each row only one char in s is matched, but the results of early matched
    # chars are accumulated to the next rows.
    # in each row, the length of p is increased one by one. can design a table
    # to implement some rules, make each row represent match result so far.
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

    def isMatch1(self, s, p):
        star, i, si = [], 0, 0
        while i < len(p):
            if si == len(s) or (p[i].isalpha() and p[i] != s[si]):
                if not star:
                    return False
                star[-1][2] -= 1
                si, i = star[-1][2], star[-1][0] + 1
                if star[-1][1] == star[-1][2]:
                    star.pop()
            elif p[i] == '*':
                star.append([i, si, len(s)])
                i, si = i + 1, len(s)
            else:
                i, si = i + 1, si + 1
        return True

    def isMatch2(self, s, p):
        if '**' in p:
            pl = []
            for q in p:
                if not pl or q != '*' or (q == '*' and pl[-1] != '*'):
                    pl.append(q)
            p = ''.join(pl)
            print(p)
        ns = p.count('*')
        na = len(p) - ns
        if len(s) < na:
            return False
        star, i, si, ai = [], 0, 0, 0
        while i < len(p):
            if p[i] not in '?*' and p[i] != s[si]:
                if not star:
                    return False
                star[-1][3] -= 1
                i, ai, si = star[-1][0] + 1, star[-1][1], star[-1][3]
                if star[-1][2] > star[-1][3]:
                    star.pop()
            elif p[i] == '*':
                temp = len(s) - (na - ai)
                if temp >= si:
                    star.append([i, ai, si, temp])
                    si = temp
                i += 1
            else:
                i, ai, si = i + 1, ai + 1, si + 1
        return True

    def isMatch3(self, s, p):
        print(s)
        pl = []
        for q in p:
            if pl and ((q.isalpha() and pl[-1].isalpha()) or
                       q == pl[-1] == '?'):
                pl[-1] += q
            elif pl and q == pl[-1] == '*':
                continue
            else:
                pl.append(q)
        p = ''.join(pl)
        print(p)
        ns = p.count('*')
        na = len(p) - ns
        if len(s) < na or (pl[0].isalpha() and not s.startswith(pl[0])) or \
                (pl[-1].isalpha() and not s.endswith(pl[-1])):
            return False
        print(pl)
        stack, i, si, ai, back, prestar = [], 0, 0, 0, False, False
        while i < len(pl):
            # if si > len(s):
            #     print(i, si, ai, pl[i])
            if back:
                if not stack:
                    return False
                i, ai, si, end = stack[-1]
                idx = s.rfind(pl[i], si, end)
                print('back', i, si, end, idx)
                if idx > -1:
                    stack[-1][3], si = idx + len(pl[i]) - 1, idx + len(pl[i])
                    i, prestar, back = i + 1, False, False
                else:
                    stack.pop()
            elif pl[i] == '*':
                if i == len(pl) - 1:
                    return True
                i, prestar = i + 1, True
            elif '?' in pl[i]:
                si, ai, i = si + len(pl[i]), ai + len(pl[i]), i + 1
            elif not prestar:
                if s.startswith(pl[i], si):
                    si, ai, i = si + len(pl[i]), ai + len(pl[i]), i + 1
                else:
                    back = True
            else:
                ai += len(pl[i])
                end = len(s) - (na - ai)
                idx = s.rfind(pl[i], si, end)
                print('advance', i, si, end, idx)
                if idx > -1:
                    stack.append([i, ai, si, idx + len(pl[i]) - 1])
                    si, i, prestar = idx + len(pl[i]), i + 1, False
                else:
                    back = True
        print(ai, si, len(pl), len(p), len(s), na)
        if len(s) == si:
            return True
        return False

    def isMatch4(self, s, p):
        pl = []
        for q in p:
            if pl and ((q.isalpha() and pl[-1].isalpha()) or
                       q == pl[-1] == '?'):
                pl[-1] += q
            elif pl and q == pl[-1] == '*':
                continue
            else:
                pl.append(q)
        p = ''.join(pl)
        ns = p.count('*')
        na = len(p) - ns
        if len(s) < na or (pl and pl[-1].isalpha() and not s.endswith(pl[-1])):
            return False
        stack, i, j, ai, si, back, prestar = [], 0, 0, 0, 0, False, False
        while i < len(pl):
            if back and j > -1:
                ti, ta, te = stack[j]
                if j < len(stack) - 1:
                    li, la, le = stack[j + 1]
                    temp = le - (la - ta + len(pl[li]) - len(pl[ti]))
                    if temp >= te:
                        j = -1
                        continue
                    te = temp + 1
                idx = s.rfind(pl[ti], ta, te)
                if idx == -1:
                    return False
                stack[j][2] = idx + len(pl[ti]) - 1
                j -= 1
            elif j == -1:
                ai, si = stack[j][1] + len(pl[stack[j][0]]), stack[j][2] + 1
                i, prestar, j, back = stack[j][0] + 1, False, len(stack), False
            elif pl[i] == '*':
                if i == len(pl) - 1:
                    return True
                i, prestar = i + 1, True
            elif '?' in pl[i]:
                if prestar and i == len(pl) - 1:
                    return True
                si, ai, i = si + len(pl[i]), ai + len(pl[i]), i + 1
            elif not prestar:
                if s.startswith(pl[i], si):
                    si, ai, i = si + len(pl[i]), ai + len(pl[i]), i + 1
                elif not stack:
                    return False
                else:
                    back, j = True, len(stack) - 1
            else:
                end = len(s) - (na - ai - len(pl[i]))
                idx = s.rfind(pl[i], ai, end)
                if idx == -1:
                    return False
                stack.append([i, ai, idx + len(pl[i]) - 1])
                back, j = True, len(stack) - 2
        if si == len(s):
            print(stack)
            return True
        return False

    def isMatch5(self, s, p):
        pl = []
        for q in p:
            if pl and ((q.isalpha() and pl[-1].isalpha()) or
                       q == pl[-1] == '?'):
                pl[-1] += q
            elif pl and q == pl[-1] == '*':
                continue
            else:
                pl.append(q)
        p = ''.join(pl)
        if len(p) - p.count('*') > len(s):
            return False
        prow = [True] + [False] * len(p)
        if p and p[0] == '*':
            prow[1] = True
        for i, c in enumerate(s):
            trow = [False]
            for j, l in enumerate(p):
                if l == '*':
                    trow.append(prow[j] or prow[j + 1] or trow[j])
                elif l == '?':
                    trow.append(prow[j])
                else:
                    trow.append(prow[j] and c == l)
            prow = trow
        return prow[-1]

    def isMatch6(self, s, p):
        pl = []
        for q in p:
            if pl and ((q.isalpha() and pl[-1].isalpha()) or
                       q == pl[-1] == '?'):
                pl[-1] += q
            elif pl and q == pl[-1] == '*':
                continue
            else:
                pl.append(q)
        p = ''.join(pl)
        ns = p.count('*')
        na = len(p) - ns
        if na > len(s) or (ns == 0 and len(s) != len(p)):
            return False
        stack, ai, prestar, end, si = [], 0, False, len(s), 0
        k, l = 0, len(pl) - 1
        while k < len(pl) and pl[k] != '*':
            if pl[k].isalpha() and not s.startswith(pl[k], si):
                return False
            k, si, ai = k + 1, si + len(pl[k]), ai + len(pl[k])
        while l >= k and pl[l] != '*':
            end -= len(pl[l])
            if pl[l].isalpha() and not s.startswith(pl[l], end):
                return False
            l -= 1
        for i, q in enumerate(pl[k: l + 1]):
            if q == '*':
                prestar = True
            elif '?' in q or not prestar:
                ai += len(q)
            else:
                stack.append([i + k, ai])
                ai, prestar = ai + len(q), False
        te = end
        while stack:
            i, start = stack[-1]
            idx = s.rfind(pl[i], start, te)
            if idx == -1:
                return False
            temp = idx + len(pl[i])
            while i < l:
                i += 1
                if pl[i] == '*':
                    te = end = idx
                    l = stack[-1][0]
                    stack.pop()
                    break
                elif pl[i].isalpha() and not s.startswith(pl[i], temp) or \
                        temp >= end:
                    te = idx + len(pl[i]) - 1
                    break
                else:
                    temp += len(pl[i])
        return True

    # solution from http://yucoding.blogspot.com/2013/02/leetcode-question-123-
    # wildcard-matching.html
    # if j reaches end of p first, then j will be back to star + 1, if no star,
    # return false.
    # if a substring without *, then start from the minimum possible i index to
    # find the first match. then other substrings can have more to match, star
    # will also be the next index of * after current substring.
    def isMatch7(self, s, p):
        i, j, si, star = 0, 0, None, None
        while i < len(s):
            # print(i, j)
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i, j = i + 1, j + 1
            elif j < len(p) and p[j] == '*':
                si, star, j = i, j, j + 1
            elif star is not None:
                i, j, si = si + 1, star + 1, si + 1
            else:
                return False
        if p[j:] == '*' * (len(p) - j):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch("aaaaaaaaaaaaac", "a*a*a*a*a*a*a*a*a*a*aaaaac"))
    # print(s.isMatchr("ccbbabbbabababa", ".*.ba*c*c*aab.a*b*"))
    # print(s.isMatchr("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
    # print(s.isMatchr("ab", ".*.."))
    # print(s.isMatchr("bbbba", ".*a*a"))
    # print(s.isMatchr("aaa", "aaaa"))
    # print(s.isMatchr("ab", ".*c"))
    # print(s.isMatchr("a", ""))
    # print(s.isMatchr('aa', 'a'))
    # print(s.isMatchr('aa', 'aa'))
    # print(s.isMatchr("aaa", "aa"))
    # print(s.isMatchr("aab", "c*a*b"))
    print(s.isMatchi("aa", "a*"))
    # print(s.isMatch7("aa", "*"))
    # print(s.isMatch6("ab", "?*"))
    # print(s.isMatch7('a.cccccbb', '?*b'))
    # print(s.isMatch6("hi", "*?"))
    # print(s.isMatch7(
    #     "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
    #     "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"))
    # print(s.isMatch7(
    #     "baabbabababaabbabababbaabbbbaaabaaabbbbaaaaaabbbbaaabaaabbbbbabaabbbbbbbbabbbabbabbbbabbbbabbbbbbabababbaaaabbbbaabaaababbbabaaaabaabbbabbaabbabbbbabaababbbbbbbabbaaaabaaabbaaabaaaaababbbaaaabbbbbabbabb",
    #     "ba*ba*bb*a********abaa*bb**abb**b***ab**b*b*babb***a*bb*aaabb*****b*aabb**aa**b*a***b*bb*b*bb*a*bbbbb**"))
    # print(s.isMatch7("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))
    # print(s.isMatch7("mississippi", "m*iss*iss*"))
