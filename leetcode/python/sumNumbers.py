# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        stack, summation = [[root]], 0
        if root.right:
            stack[-1].append(root.right)
        if root.left:
            stack[-1].append(root.left)
        while stack:
            if len(stack[-1]) > 1:
                temp = stack[-1].pop()
                stack.append([temp])
                if temp.right:
                    stack[-1].append(temp.right)
                if temp.left:
                    stack[-1].append(temp.left)
            elif stack[-1][0].left or stack[-1][0].right:
                stack.pop()
            else:
                slen = len(stack)
                factor = 10 ** (slen - 1)
                for p in stack:
                    summation += p[0].val * factor
                    factor //= 10
                stack.pop()
        return summation
