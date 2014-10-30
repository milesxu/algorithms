class RBNode:

    """docstring for RBNode"""

    def __init__(self, key=None, red=None, parent=None):
        self.red = red
        self.key = key
        self.parent = parent
        self.child = [None, None]


class RedBlackTree:

    """docstring for RedBlackTree"""

    def __init__(self):
        self.Root = None

    @staticmethod
    def makeNode(self, key):
        return RBNode(key, 1)

    @staticmethod
    def isRed(self, node):
        return node and node.red

    def _extremum(self, root, idx):
        while root.child[idx]:
            root = root.child[idx]
        return root

    def minimum(self, root):
        return self._extremum(root, 0)

    def maximum(self, root):
        return self._extremum(root, 1)

    def search(self, key):

        def recursion(root, key):
            if root is None or root.key == key:
                return root
            return recursion(root.child[root.key < key], key)

        return recursion(self.Root, key)

    def _adjacent(self, node, idx):
        if node.child[idx]:
            return self._extremum(node.child[idx], not idx)
        while node.parent and node == node.parent.child[idx]:
            node = node.parent
        return node.parent

    def successor(self, node):
        return self._adjacent(node, 1)

    def predecessor(self, node):
        return self._adjacent(node, 0)

    def toSortedList(self):
        """output tree keys as a sorted list, use inorder tree walk."""

        def recursion(root):
            lst = []
            if root:
                lst += self.toSortedList(root.child[0])
                lst.append(root.key)
                lst += self.toSortedList(root.child[1])
            return lst

        return recursion(self.Root)

    def _rotate(self, root, idx):
        newr = root.child[not idx]

        root.child[not idx] = newr.child[idx]
        root.child[not idx].parent = root

        newr.parent, newr.child[idx] = root.parent, root
        if root.parent:
            root.parent.child[root.parent.child[0] == root] = newr
        root.parent = newr

        root.red = 1
        newr.red = 0
        return newr

    def _doubleRotate(self, root, idx):
        # directions of two rotate are opposite, the ultimate root is
        # root.child[not idx].child[idx]
        root.child[not idx] = self._rotate(root.child[not idx], not idx)
        # root.child[not idx].parent = root
        return self._rotate(root, idx)

    def bottomupInsert(self, key):

        def recursion(rt, key):
            if rt is None:
                return self.makeNode(key)
            idx = rt.key <= key
            rt.child[idx] = recursion(rt.child[idx], key)
            rt.child[idx].parent = rt
            # rt.child[idx] cannot be None
            if rt.child[idx].red:
                if self.isRed(rt.child[not idx]):
                    rt.child[idx].red = 0
                    rt.child[not idx].red = 0
                    rt.red = 1
                else:
                    if self.isRed(rt.child[idx].child[idx]):
                        rt = self._rotate(rt, not idx)
                    elif self.isRed(rt.child[idx].child[not idx]):
                        rt = self._doubleRotate(rt, not idx)
            return rt

        self.Root = recursion(self.Root, key)
        self.Root.red = 0

    def bottomupDelete(self, key):

        def deletionBalance(root, idx):
            p, s, done = root, root.child[not idx], False
            # s cannot is None, otherwise black violation will happen.
            if s.red:
                p = self._rotate(p, idx)
                s = p.child[not idx]
            if s:
                if not self.isRed(s.child[0]) and not self.isRed(s.child[1]):
                    if p.red:
                        done = True
                    p.red, s.red = 0, 1
                else:
                    temp, newr = p.red, p == root
                    if self.isRed(s.child[not idx]):
                        p = self._rotate(p, idx)
                    else:
                        p = self._doubleRotate(p, idx)
                    p.child[0].red, p.child[1].red = 0, 0
                    p.red, done = temp, True
                    if newr:
                        root = p
                    else:
                        root.child[idx] = p
            return root, done

        def recursion(root, key):
            if root is None:
                return root, True
            if root.key == key:
                if root.child[0] is None or root.child[1] is None:
                    temp = root.child[root.child[0] is None]
                    if root.red:
                        done = True
                    elif self.isRed(temp):
                        temp.red, done = 0, True
                    else:
                        done = False
                    return temp, done
                else:
                    temp = self.successor(root)
                    root.key, key = temp.key, temp.key

            idx = root.key <= key
            root.child[idx], done = recursion(root.child[idx], key)
            if root.child[idx]:
                root.child[idx].parent = root
            if not done:
                return deletionBalance(root, idx)

        self.Root = recursion(self.Root, key)
        if self.Root:
            self.Root.red = 0

    def topdownInsert(self, key):
        if self.Root is None:
            self.Root = self.makeNode(key)
        else:
            nd, p, g = self.Root, None, None
            idx, last, inserted = 0, None, False
            while True:
                if nd is None:
                    p.child[idx] = nd = self.makeNode(key)
                    nd.parent, inserted = p, True
                elif self.isRed(nd.child[0]) and self.isRed(nd.child[1]):
                    nd.red, nd.child[0].red, nd.child[1].red = 1, 0, 0
                # the root is black, so the parent of p cannot be None.
                # the loop has run more than twice, last also cannot be None.
                if self.isRed(p) and nd.red:
                    if g:
                        idx2 = g.child[1] == p.parent
                    if nd == p.child[last]:
                        temp = self._rotate(p.parent, not last)
                    else:
                        temp = self._doubleRotate(p.parent, not last)
                    if g is None:
                        self.Root = temp
                    else:
                        g.child[idx2], temp.parent = temp, g

                if inserted:
                    break
                last, idx = idx, nd.key <= key
                p, nd = nd, nd.child[idx]
                if p.parent:
                    g = p.parent.parent

        self.Root.red = 0

    def topdownDelete(self, key):
        if self.Root:
            nd, idx = self.makeNode(0), 1
            nd.child[idx], head, f = self.Root, nd, None
            while nd.child[idx]:
                last, g, p, nd = idx, nd.parent, nd, nd.child[idx]
                idx = nd.key <= key
                if nd.key == key:
                    f = nd

                if not nd.red and not self.isRed(nd.child[idx]):
                    if self.isRed(nd.child[not idx]):
                        p = p.child[last] = self._rotate(nd, idx)
                    else:
                        s = p.child[not last]
                        if s:
                            if not self.isRed(s.child[0]) and \
                                    not self.isRed(s.child[1]):
                                p.red, s.red, nd.red = 0, 1, 1
                            else:
                                idx2 = g.child[1] == p
                                if self.isRed(s.child[last]):
                                    g.child[idx2] = self._doubleRotate(p, last)
                                elif self.isRed(s.child[not last]):
                                    g.child[idx2] = self._rotate(p, last)
                                g.child[idx2].parent = g
                                nd.red, g.child[idx2].red = 1, 1
                                g.child[idx2].child[0].red = 0
                                g.child[idx2].child[1].red = 0

            if f:
                f.key = nd.key
                p.child[p.child[1] == nd] = nd.child[nd.child[0] is None]
            self.Root = head.child[1]
            if self.Root:
                self.Root.red = 0


def RBTreeAssert(tree):

    def recursion(root):
        lh, rh = 0, 0

        if root is None:
            return 1
        ln, rn = root.child[0], root.child[1]
        if root.red:
            if tree.isRed(ln) or tree.isRed(rn):
                print("red violation")
                return 0

        lh, rh = recursion(ln), recursion(rn)
        if (ln and ln.key >= root.key) or (rn and rn.key < root.key):
            print("binary tree violation")
            return 0

        if lh and rh:
            if lh != rh:
                print("black violation")
                return 0
            else:
                return lh + (not root.red)
        else:
            return 0
