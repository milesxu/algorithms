# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self, root):
        if root is None:
            return []
        lst, temp = [], [[root.left, root.right, root.val]]
        while temp:
            p = temp[-1]
            if p[0]:
                temp.append([p[0].left, p[0].right, p[0].val])
                p[0] = None
            elif p[1]:
                temp.append([p[1].left, p[1].right, p[1].val])
                p[1] = None
            else:
                lst.append(temp.pop()[2])
        return lst

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        lst, temp = [root.val], [[root.left, root.right]]
        while temp:
            p = temp[-1]
            if p[0]:
                lst.append(p[0].val)
                temp.append([p[0].left, p[0].right])
                p[0] = None
            elif p[1]:
                lst.append(p[1].val)
                temp.append([p[1].left, p[1].right])
                p[1] = None
            else:
                temp.pop()
        return lst
