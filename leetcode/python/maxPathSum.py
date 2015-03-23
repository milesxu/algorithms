# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # @param root, a tree node
    # @return an integer

    def maxPathSum(self, root):
        stack, pathSum, mpSum = [root], {}, None
        while stack:
            left, right = stack[-1].left, stack[-1].right
            if left and left not in pathSum:
                stack.append(left)
            elif right and right not in pathSum:
                stack.append(right)
            else:
                node = stack.pop()
                if left is None and right is None:
                    pathSum[node] = node.val
                    if mpSum is None or mpSum < pathSum[node]:
                        mpSum = pathSum[node]
                elif left and right:
                    pathSum[node] = max(pathSum[left], pathSum[right], 0) + \
                        node.val
                    mpSum = max(pathSum[node],
                                pathSum[left] + pathSum[right] + node.val,
                                mpSum)
                elif left:
                    pathSum[node] = node.val + max(pathSum[left], 0)
                    mpSum = max(pathSum[node], mpSum)
                else:
                    pathSum[node] = node.val + max(pathSum[right], 0)
                    mpSum = max(pathSum[node], mpSum)
        return mpSum
