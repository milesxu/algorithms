class Solution:

    # @return a boolean
    def isValid(self, s):
        left, right, stack = '([{', ')]}', []
        for p in s:
            if p in left:
                stack.append(ord(p))
            else:
                i = ord(p)
                if stack and (stack[-1] == i - 1 or stack[-1] == i - 2):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
