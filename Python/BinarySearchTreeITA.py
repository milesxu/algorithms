class BinarySearchTreeNode:

    """docstring for BinarySearchTreeNode"""

    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:

    """docstring for BinarySearchTree"""

    def __init__(self):
        self.Root = None

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def maximum(self, node):
        while node.right:
            node = node.right
        return node

    def toSortedList(self, nd):
        """output tree as a sorted list"""

        def stackAppend(stack, node):
            while node:
                stack.append(node)
                node = node.left

        lst, tStack = [], []
        stackAppend(tStack, nd)
        while tStack:
            pNode = tStack.pop()
            lst.append(pNode.key)
            if pNode.right:
                stackAppend(tStack, pNode.right)
        return lst

    def search(self, node, key):
        while node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        tNode = node.parent
        while tNode and node == tNode.right:
            node, tNode = tNode, tNode.parent
        return tNode

    def predecessor(self, node):
        if node.left:
            return self.maximum(node.left)
        tNode = node.parent
        while tNode and node == tNode.left:
            node, tNode = tNode, tNode.parent
        return tNode

    def insert(self, node):
        pNode, tNode = None, self.Root
        while tNode:
            pNode = tNode
            if node.key < tNode.key:
                tNode = tNode.left
            else:
                tNode = tNode.right
        node.parent = pNode
        if pNode is None:
            self.Root = node
        elif node.key < pNode.key:
            pNode.left = node
        else:
            pNode.right = node

    def _transplant(self, nodeu, nodev):
        if nodeu.parent is None:
            self.Root = nodev
        elif nodeu == nodeu.parent.left:
            nodeu.parent.left = nodev
        else:
            nodeu.parent.right = nodev
        if nodev:
            nodev.parent = nodeu.parent

    def delete(self, node):
        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        # tNode is the successor of node, so it must have no left subnode.
        else:
            tNode = self.minimum(node.right)
            if tNode.parent != node:
                self._transplant(tNode, tNode.right)
                tNode.right = node.right
                tNode.right.parent = tNode
            self._transplant(node, tNode)
            tNode.left = node.left
            tNode.left.parent = tNode
