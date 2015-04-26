from collections import defaultdict


class NodeChain:

    """docstring for NodeChain"""

    def __init__(self, nodes, dists, pnode=-1, parent=None):
        self._subBlue = 0
        self._nodes = tuple(nodes)
        self._dists = tuple(dists)
        self._pnode = pnode
        self._parent = parent
        self._bnblue = [0] * len(nodes)
        self._dyed = set()
        self._distSum = (0, 0)
        self._dsums = dict()
        self._clen = [i for i in [10000, 1000, 100, 10] if i <= len(nodes)]
        # self._bdists = 0
        self._ddists = self._dTreeInit(len(nodes))
        self._dblues = self._dTreeInit(len(nodes))

    def _initItem(self, clen):
        if clen == 10:
            return [0]
        else:
            temp = [self._initItem(clen // 10) for i in range(10)]
            return [0] + temp

    def _dTreeInit(self, nodeLen):
        tree = [0]
        temp, rlen = tree, nodeLen
        for i in self._clen:
            n, r = divmod(rlen, i)
            temp += [self._initItem(i) for j in range(n)]
            if r:
                rlen = r
                if n:
                    temp.append([0])
                temp = temp[-1]
            else:
                break
        return tree

    def _getLoopArray(self, idx):
        cblen, tlen, temp = [], len(self._nodes), idx
        for j, i in enumerate(self._clen):
            m, l = divmod(tlen, i)
            n, k = divmod(temp, i)
            if n < m:  # it is impossible that n > m.
                cblen += self._clen[j:]
                break
            elif m:
                cblen.append(i)
            tlen, temp = l, k
        return cblen

    def _treeUpdate(self, tree, index, n):
        tree[0] += n
        cblen, temp = self._getLoopArray(index), index
        for i in cblen:
            m, r = divmod(temp, i)
            tidx = m + 1
            tree[tidx][0] += n
            temp, tree = r, tree[tidx]

    def registerNode(self, chainArray):
        for i in self._nodes:
            chainArray[i] = self

    def blueUpdate(self, node, bdist, inBranch=False):
        self._subBlue += 1
        idx = self._nodes.index(node)
        self._treeUpdate(self._dblues, idx, 1)
        d = self._dists[idx] - self._dists[0]
        self._treeUpdate(self._ddists, idx, d)
        if inBranch:
            self._bnblue[idx] += 1
            # self._bdists += bdist
        else:
            self._dyed.add(node)
        if self._parent:
            bdist += self._dists[idx]
            self._parent.blueUpdate(self._pnode, bdist, True)
        else:
            tdist = self._distSum[1]
            self._distSum = (self._subBlue, tdist + bdist + self._dists[idx])
            # self._distSum = (self._subBlue, self._ddists[0] + self._bdists)

    def _pdistSum(self, index, nblue):
        if index in self._dsums and self._dsums[index][0] == nblue:
            return self._dsums[index][1]
        cblen = self._getLoopArray(idx)
        rcblen = cblen
        idx, stack, miss = index, [], False
        while rcblen:
            dvnd = rcblen.pop()

    def toggle(self, i):
        if i not in self._dyed:
            self.blueUpdate(i, 0)

    def distSum(self, node, nblue):
        if self._distSum[0] < nblue:
            tdist = self._parent.distSum(self._pnode, nblue)
            tdist += (nblue - 2 * self._subBlue) * self._dists[0]
            self._distSum = (nblue, tdist)
        tdist = self._distSum[1]
        preDist, preBlue = tdist - self._ddists[0], nblue - self._subBlue
        idx = self._nodes.index(node)
        cblen = self._getLoopArray(idx)
        itemp, dtree, btree = idx, self._ddists, self._dblues
        snode, preChainDist, preChainBlue = 0, 0, 0
        for i in cblen:
            n, r = divmod(itemp, i)
            snode += n * i
            tidx = n + 1
            for j in range(1, tidx):
                preChainDist += dtree[j][0]
                preChainBlue += btree[j][0]
            itemp = r
            dtree, btree = dtree[tidx], btree[tidx]
        for i in range(snode, idx):
            node = self._nodes[i]
            n = self._bnblue[i] + (node in self._dyed)
            preChainBlue += n
            preChainDist += n * (self._dists[i] - self._dists[0])
        subChainDist = self._ddists[0] - preChainDist
        subChianBlue = self._dblues[0] - preChainBlue
        chainD = self._dists[idx] - self._dists[0]
        redundance, compensate = subChianBlue * chainD, preChainBlue * chainD
        chainDistSum = compensate - preChainDist + subChainDist - redundance
        return chainDistSum + preDist + preBlue * chainD


class TreeColoring:

    """Single Round Match 624 Round 1 - Division I, Level Three:
    TreeColoring"""

    def __init__(self):
        self._curValue = 0
        self._totalDist = 0
        self._distance = []
        self._parent = []
        self._blue = set()
        # self._subBlue = Counter()
        self.chains = []

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

    def _preProcess(self, N):
        inNodes, level, self.chains = set(), [0], [None] * N
        for j in self._parent:
            level.append(level[j] + 1)
            inNodes.add(j)
        leafNodes = defaultdict(list)
        for i in (set(range(N)) - inNodes):
            leafNodes[level[i]].append(i)
        keys = sorted(leafNodes)
        while keys:
            endNodes = leafNodes.pop(keys.pop())
            while endNodes:
                node, chain, dist, pchain = endNodes.pop(), [], [], None
                while node:
                    chain.insert(0, node)
                    dist.insert(0, self._distance[node - 1])
                    node = self._parent[node - 1]
                    if self.chains[node] is not None:
                        pchain = self.chains[node]
                        break
                if not (node or pchain):
                    chain.insert(0, 0)
                    dist.insert(0, 0)
                for i in range(1, len(dist)):
                    dist[i] += dist[i - 1]
                if node or pchain:
                    nchain = NodeChain(chain, dist, node, pchain)
                else:
                    nchain = NodeChain(chain, dist)
                nchain.registerNode(self.chains)
        print('pre process complete!')

    def color(self, N, Q, startSeed, threshold, maxDist):
        self._curValue, dxor, blue = startSeed, 0, set()
        self._generateInput(N, Q, threshold, maxDist)
        self._preProcess(N)
        for i in range(Q):
            qtype = self._genNextRandom() % 2 + 1
            qnode = self._genNextRandom() % N
            if qtype == 1:
                blue.add(qnode)
                self.chains[qnode].toggle(qnode)
            else:
                dxor ^= self.chains[qnode].distSum(qnode, len(blue))
        return dxor

if __name__ == '__main__':
    tc = TreeColoring()
    # print(tc.color(100000, 100000, 123456, 500000, 474747))
    # print(tc.color(4, 5, 2, 9, 10))
    # print(tc.color(8, 8, 3, 5, 7))
    # print(tc.color(14750, 50, 29750, 1157, 21610))
    print(tc.color(100000, 100000, 654321, 1000003, 1000003))
    # print(tc.color(100000, 10, 654321, 1000003, 1000003))
