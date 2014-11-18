class Solution:
    # @param tokens, a list of string
    # @return an integer

    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif i[1:].isdigit() and i[0] == '-':
                stack.append(-int(i[1:]))
            else:
                suc = stack.pop()
                pre = stack.pop()
                if i == '+':
                    temp = pre + suc
                elif i == '-':
                    temp = pre - suc
                elif i == '*':
                    temp = pre * suc
                elif i == '/':
                    temp = pre // suc
                    if temp < 0 and (pre % suc != 0):
                        temp += 1
                stack.append(temp)
        return stack.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
