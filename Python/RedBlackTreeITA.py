from enum import Enum


class Color(Enum):

    """docstring for Color"""

    black, red = 0, 1


class RedBlackTreeNode:

    """docstring for RedBlackTreeNode"""

    def __init__(self,
                 key=None, parent=None, left=None, right=None, color=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color


class RedBlackTree:

    """docstring for RedBlackTree"""

    def __init__(self):
        self.NIL = RedBlackTreeNode()
        self.Root = self.NIL

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def search(self, node, key):
        if node == self.NIL or node.key == key:
            return key
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def successor(self, node):
        if node.right != self.NIL:
            return self.minimum(node.right)
        tNode = node.parent
        while tNode != self.NIL and node == tNode.right:
            node, tNode = tNode, tNode.parent
        return tNode

    def predecessor(self, node):
        if node.left != self.NIL:
            return self.maximum(node.left)
        tNode = node.parent
        while tNode != self.NIL and node == tNode.left:
            node, tNode = tNode, tNode.parent
        return tNode

    def toSortedList(self, node):
        """output tree keys as a sorted list, use inorder tree walk."""
        lst = []
        if node != self.NIL:
            lst += self.toSortedList(node.left)
            lst.append(node.key)
            lst += self.toSortedList(node.right)
        return lst

    def leftRotate(self, node):
        tNode = node.right
        node.right = tNode.left
        if tNode.left != self.NIL:
            tNode.left.parent = node
        tNode.parent = node.parent
        if node.parent == self.NIL:
            self.Root = tNode
        elif node == node.parent.left:
            node.parent.left = tNode
        else:
            node.parent.right = tNode
        node.parent = tNode
        tNode.left = node

    def rightRotate(self, node):
        tNode = node.left
        node.left = tNode.right
        if tNode.right != self.NIL:
            tNode.right.parent = node
        tNode.parent = node.parent
        if node.parent == self.NIL:
            self.Root = tNode
        elif node == node.parent.left:
            node.parent.left = tNode
        else:
            node.parent.right = tNode
        node.parent, tNode.right = tNode, node

    def _insertFixup(self, node):
        # only the color of node is assigned to red, colors of other nodes
        # are not changed. so if color of parent of node is red, then it
        # cannot be root, which must have black color.
        while node.parent.color == Color.red:
            if node.parent == node.parent.parent.left:
                tNode = node.parent.parent.right
                if tNode.color == Color.red:
                    tNode.color, node.parent.color = Color.black, Color.black
                    node.parent.parent.color = Color.red
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = Color.black
                    node.parent.parent.color = Color.red
                    self.rightRotate(node.parent.parent)
            else:
                tNode = node.parent.parent.left
                if tNode.color == Color.red:
                    tNode.color, node.parent.color = Color.black, Color.black
                    node.parent.parent.color = Color.red
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = Color.black
                    node.parent.parent.color = Color.red
                    self.leftRotate(node.parent.parent)
        self.Root.color = Color.black

    def insert(self, node):
        pNode, tNode = self.NIL, self.Root
        while tNode != self.NIL:
            pNode = tNode
            if node.key < tNode.key:
                tNode = tNode.left
            else:
                tNode = tNode.right
        node.parent = pNode
        if pNode == self.NIL:
            self.Root = node
        elif node.key < pNode.key:
            pNode.left = node
        else:
            pNode.right = node
        node.left, node.right, node.color = self.NIL, self.NIL, Color.red
        self._insertFixup(node)

    def _transplant(self, nodeu, nodev):
        if nodeu.parent == self.NIL:
            self.Root = nodev
        elif nodeu == nodeu.parent.left:
            nodeu.parent.left = nodev
        else:
            nodeu.parent.right = nodev
        nodev.parent = nodeu.parent

    def _deleteFixup(self, node):
        # the most important thing to solve is double black on node
        while node != self.Root and node.color == Color.black:
            if node == node.parent.left:
                sNode = node.parent.right
                if sNode.color == Color.red:
                    sNode.color, node.parent.color = Color.black, Color.red
                    self.leftRotate(node.parent)
                    sNode = node.parent.right
                # in case below, the color of sNode must be black
                if sNode.left.color == Color.black and \
                        sNode.right.color == Color.black:
                    sNode.color, node = Color.red, node.parent
                else:
                    if sNode.right.color == Color.black:
                        sNode.color, sNode.left.color = Color.red, Color.black
                        self.rightRotate(sNode)
                        sNode = node.parent.right
                    sNode.color = node.parent.color
                    node.parent.color = Color.black
                    sNode.right.color = Color.black
                    self.leftRotate(node.parent)
                    node = self.Root
            else:
                sNode = node.parent.left
                if sNode.color == Color.red:
                    sNode.color, node.parent.color = Color.black, Color.red
                    self.rightRotate(node.parent)
                    sNode = node.parent.left
                if sNode.right.color == Color.black and \
                        sNode.left.color == Color.black:
                    sNode.color, node = Color.red, node.parent
                else:
                    if sNode.left.color == Color.black:
                        sNode.color = Color.red
                        sNode.right.color = Color.black
                        self.leftRotate(sNode)
                        sNode = node.parent.left
                    sNode.color = node.parent.color
                    node.parent.color = Color.black
                    sNode.left.color = Color.black
                    self.rightRotate(node.parent)
                    node = self.Root
        node.color = Color.black

    def delete(self, node):
        pNode, originColor = node, node.color
        if node.left == self.NIL:
            tNode = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            tNode = node.left
            self._transplant(node, node.left)
        else:
            pNode = self.minimum(node.right)
            originColor = pNode.color
            tNode = pNode.right
            if pNode.parent == node:
                tNode.parent = pNode  # is this assignment redundant?
            else:
                self._transplant(pNode, pNode.right)
                pNode.right = node.right
                pNode.right.parent = pNode
            self._transplant(node, pNode)
            pNode.left = node.left
            pNode.left.parent = pNode
            pNode.color = node.color
        if originColor == Color.black:
            self._deleteFixup(tNode)
