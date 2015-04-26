lnull, rnull = 0, 0


class TreeNode:

    """Node clas of Link-Cut Tree"""

    def __init__(self, nilNode=None, parent=None, distance=0):
        self._reset(nilNode, parent, distance)

    def _reset(self, nilNode, parent, distance):
        self.parent = parent     # parent node
        self.left = nilNode      # left son node
        self.right = nilNode     # right son node
        self.nblue = 0           # number of blue nodes in subtree
        self.sdist = distance    # self distance to initial parent
        self.ddist = distance    # duplicate path distance
        self.ldist = 0           # duplicate path distance of left subtree
        self.rdist = 0           # duplicate path distance of right subtree
        self.vblue = 0           # number of blue nodes in virtual subtree
        self.vldist = 0          # sum of ldist of virtual subtree
        self.dyed = False        # color of self is blue or not

    def isNull(self):
        return self.parent is None

    def update(self):
        # global lnull, rnull
        # if self.left.isNull():
        #     lnull += 1
        # if self.right.isNull():
        #     rnull += 1
        self.nblue = self.dyed + self.vblue + \
            self.left.nblue + self.right.nblue
        self.ddist = self.sdist + self.left.ddist + self.right.ddist
        self.ldist = self.vldist + self.left.ldist + self.right.ldist + \
            (self.sdist + self.left.ddist) * (self.nblue - self.left.nblue)
        self.rdist = self.vldist + self.left.rdist + self.right.rdist + \
            self.right.ddist * (self.nblue - self.right.nblue) + \
            self.sdist * self.left.nblue

    def sign(self):
        if self.isNull():
            return -1
        if self.parent.right == self:
            return 1
        elif self.parent.left == self:
            return 0
        else:
            return -1

    def getSub(self, pos):
        if pos:
            return self.right
        else:
            return self.left

    def setSub(self, pos, node):
        if pos:
            self.right = node
        else:
            self.left = node
        if not node.isNull():
            node.parent = self

    # move to the link-cut tree class
    def rotate(self, pos):
        pnode = self.parent
        gparent = pnode.parent
        if pnode.sign() >= 0:
            gparent.setSub(pnode.sign(), self)
        else:
            self.parent = gparent
        pnode.setSub(pos, self.getSub(not pos))
        self.setSub(not pos, pnode)
        pnode.update()

    def splay(self):
        a = self.sign()
        while a >= 0:
            b = self.parent.sign()
            if b >= 0:
                if a == b:
                    self.parent.rotate(a)
                else:
                    self.rotate(a)
                self.rotate(b)
            else:
                self.rotate(a)
            a = self.sign()
        self.update()

    def expose(self, default):
        node, temp = self, default
        while True:
            node.splay()
            if not temp.isNull():
                node.vblue -= temp.nblue
                node.vldist -= temp.ldist
            if not node.right.isNull():
                node.vblue += node.right.nblue
                node.vldist += node.right.ldist
            node.right = temp
            node.update()
            temp = node
            node = node.parent
            if node.isNull():
                break
        self.splay()


class LinkCutTree:

    """docstring for LinkCutTree"""

    def __init__(self, parents, distance):
        self.default = TreeNode()
        zero = TreeNode(self.default, self.default)
        self._Nodes = [zero]
        N = len(parents)
        for i in range(N):
            pnode = self._Nodes[parents[i]]
            self._Nodes.append(TreeNode(self.default, pnode, distance[i]))

    def toggle(self, i):
        if not self._Nodes[i].dyed:
            self._Nodes[i].expose(self.default)
            self._Nodes[i].dyed = True

    def distSum(self, i):
        if not self._Nodes[i].parent.isNull():
            self._Nodes[i].expose(self.default)
        return self._Nodes[i].rdist


class TreeColoring:

    """Single Round Match 624 Round 1 - Division I, Level Three:
    TreeColoring
    http://www.shuizilong.com/house/archives/srm-624/"""

    def __init__(self):
        self._curValue = 0
        self._distance = []
        self._parent = []
        self._queryType = []
        self._queryNode = []

    def _genNextRandom(self):
        self._curValue = (self._curValue * 1999 + 17) % 1000003
        return self._curValue

    def _generateInput(self, N, Q, threshold, maxDist):
        for i in range(N - 1):
            self._distance.append(self._genNextRandom() % maxDist)
            temp = self._genNextRandom()
            if temp < threshold:
                self._parent.append(i)
            else:
                self._parent.append(temp % (i + 1))
        for i in range(Q):
            self._queryType.append(self._genNextRandom() % 2 + 1)
            self._queryNode.append(self._genNextRandom() % N)

    def color(self, N, Q, startSeed, threshold, maxDist):
        self._curValue = startSeed
        self._generateInput(N, Q, threshold, maxDist)
        lct = LinkCutTree(self._parent, self._distance)
        dxor = 0
        # result = open("D:/tcresult2.txt", 'w')
        for i in range(Q):
            qtype, qnode = self._queryType[i], self._queryNode[i]
            if qtype == 1:
                lct.toggle(qnode)
            else:
                temp = lct.distSum(qnode)
                dxor ^= temp
                # result.write("{}  {}\n".format(qnode, temp))
        # result.close()
        return dxor


if __name__ == '__main__':
    tc = TreeColoring()
    # print(tc.color(100000, 100000, 123456, 500000, 474747))
    # print(tc.color(4, 5, 2, 9, 10))
    # print(tc.color(8, 8, 3, 5, 7))
    # print(tc.color(14750, 50, 29750, 1157, 21610))
    print(tc.color(100000, 100000, 654321, 1000003, 1000003))
    print(lnull, rnull)
