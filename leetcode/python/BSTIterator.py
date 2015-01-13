# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self._root = root
        self._parent = []
        self._cur = None

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self._cur:
            return self._cur.right or self._parent
        else:
            return self._root

    def _setleft(self, top):
        while top.left:
            self._parent.append(top)
            top = top.left
        return top

    # @return an integer, the next smallest number
    def next(self):
        if self._cur:
            if self._cur.right:
                self._cur = self._setleft(self._cur.right)
            else:
                self._cur = self._parent.pop()
        else:
            self._cur = self._setleft(self._root)
        return self._cur.val



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
