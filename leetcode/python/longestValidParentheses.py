class Solution:

    # @param s, a string
    # @return an integer

    def longestValidParentheses(self, s):
        left, right = [], []
        for i, p in enumerate(s):
            if p == '(':
                left.append(i)
            elif left:
                left.pop()
            else:
                right.append(i)
        breakpoint = sorted(left + right)
        if not breakpoint:
            return len(s)
        if breakpoint[0]:
            breakpoint.insert(0, -1)
        if breakpoint[-1] < len(s):
            breakpoint.append(len(s))
        return max([breakpoint[i] - breakpoint[i - 1] - 1
                    for i in range(1, len(breakpoint))])

    def longestValidParentheses1(self, s):
        stack, left, result = [], -1, 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif not stack:
                left = i
            else:
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    result = max(result, i - left)
        return result

    def longestValidParentheses2(self, s):
        stack = []
        for i, p in enumerate(s):
            if p == '(' or not stack or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
        if not stack:
            return len(s)
        stack.insert(0, -1)
        stack.append(len(s))
        return max([stack[i] - stack[i - 1] - 1 for i in range(1, len(stack))])

    def longestValidParentheses3(self, s):
        validleft, stack, result = [], [], 0
        for i, p in enumerate(s):
            validleft.append(i)
            if p == '(':
                stack.append(i)
            elif stack:
                validleft[i] = stack.pop()
                if validleft[validleft[i] - 1] < validleft[i] - 1:
                    validleft[i] = validleft[validleft[i] - 1]
                result = max(result, i - validleft[i] + 1)
        return result

    def longestValidParentheses4(self, s):
        valid, result = [0] * len(s), 0
        for i, p in enumerate(s):
            if i and p == ')':
                if s[i - 1] == '(':
                    valid[i] += 2
                elif valid[i - 1] and i - 1 >= valid[i - 1] \
                        and s[i - valid[i - 1] - 1] == '(':
                    valid[i] = valid[i - 1] + 2
                if i > valid[i] and valid[i] and valid[i - valid[i]]:
                    valid[i] += valid[i - valid[i]]
                result = max(result, valid[i])
        print(valid)
        return result


if __name__ == '__main__':
    p = Solution()
    print(p.longestValidParentheses4("(()))())("))
