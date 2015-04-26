from collections import Counter


class NodeChain:

    """docstring for NodeChian"""

    def __init__(self, nodes, dists, pnode=-1, parent=None):
        self.nblue = 0
        self.nodes = tuple()
        self._distSum = (0, 0)       # direct distance and branch distance
        self._dist = (0, 0)          # same as above
        self._dists = dict()
        self._branch = dict()
        self._bnblue = Counter()
        self._pre = 0
        self._suc = 0
        self._vbranch = []
        self._vbdist = dict()
        self._parent = parent
        self._pnode = pnode
        self._dyed = set()
        self._totalDist = (0, 0, 0, 0, 0)  # nblue, dd, bd, preblue, subblue
        self._compact(nodes, dists)

    def _split(self, nodes, dists, n):
        tnode, tdist = nodes[n:], dists[n:]
        del nodes[n:]
        del dists[n:]
        m, r = divmod(len(tnode), n)
        ntemp, dtemp = [], []
        if m:
            ntemp = [tnode[i:i + n] for i in range(0, (m - 1) * n, n)]
            dtemp = [tdist[i:i + n] for i in range(0, (m - 1) * n, n)]
        if r:
            ntemp.append(tnode[m * n:])
            dtemp.append(tnode[m * n:])
        return ntemp, dtemp

    def _compact(self, nodes, dists):
        clen = [1000, 100, 10]
        for i in clen:
            if len(nodes) > i:
                ntemp, dtemp = self._split(nodes, dists, i)
                for j, k in zip(ntemp, dtemp):
                    chain = NodeChain(j, k, nodes[0], self)
                    self._vbranch.append(chain)
                    self._vbdist[chain] = (0, 0)
        self.nodes = tuple(nodes)
        self._dists = {n: d for n, d in zip(nodes, dists)}

    def __hash__(self):
        return hash(self.nodes)

    def __eq__(self, other):
        return self.nodes == other.nodes

    def addBranch(self, node, subChain):
        if node in self._branch:
            self._branch[node].append(subChain)
        else:
            self._branch[node] = [subChain]

    def registerNode(self, chainArray):
        for i in self.nodes:
            chainArray[i] = self
        for j in self._vbranch:
            j.registerNode(chainArray)

    def blueUpdate(self, subChain, node, ddist, bdist):
        self.nblue += 1
        netd = ddist - self._dists[self.nodes[0]]
        if self == subChain:
            self.dyed.add(node)
            self._dist = (self._dist[0] + netd, self._dist[1])
        elif subChain in self._vbranch:
            dd, bd = self._vbdist[subChain]
            self._vbdist[subChain] = (dd + netd, bd + bdist)
        else:
            bdist += ddist
            ddist = self._dists[node]
            netd = ddist - self._dists[self.nodes[0]]
            self._bnblue[node] += 1
            self._dist = (self._dist[0] + netd, self._dist[1] + bdist)
        self._distSum = (self._distSum[0] + netd, self._distSum[1] + bdist)
        if self._parent:
            self._parent.blueUpdate(self, self._pnode, ddist, bdist)

    def toggle(self, i):
        if i not in self._dyed:
            self.blueUpdate(self, i, self._dists[i], 0)

    def getBlue(self, i):
        idx, pre = self._nodes.index(i), 0
        for j in self._nodes[:idx]:
            pre += self._bnblue[j] + (j in self.dyed)
        return pre, self.nblue - pre

    def disSum(self, chain, i):
        if self._parent:
            dd, bd, pre, suc = self._parent.distSum(self, self._pnode)
        else:
            dd, bd = self._distSum
            pre, suc = 0, self.nblue
        # self._totalDist = (pre + suc, dd, bd, pre, suc)
        pred, preb, nblue = 0, 0, 0
        for i in self._vbranch[:chain]:
            td, tb = self._vbdist[i]
            pred += td
            preb += tb
            nblue += i.nblue
        sucd, sucb = dd - pred, bd - preb
        # chainD = chain._dists[chain._nodes[0]] * (2 * nblue - self.nblue) - pred + sucd

    def distQuery(self, i, nblue):
        tblue, dd, bd, preb, sucb = self._totalDist
        if nblue == tblue:
            pass
        else:


class TreeColoring:

    """Single Round Match 624 Round 1 - Division I, Level Three:
    TreeColoring"""

    def __init__(self):
        self._curValue = 0
        self._totalDist = 0
        self._distance = []
        self._parent = []
        self._blue = set()
        self._subBlue = Counter()
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
        self.chains, nodes = [None] * N, set(range(N))
        while nodes:
            end = max(nodes)
            chain = [end]
            dist = [self._distance[end - 1]]
            nodes.remove(end)
            pchain, temp = None, -1
            while chain[0]:
                temp = self._parent[chain[0] - 1]
                if temp not in nodes:
                    pchain = self.chains[temp]
                    break
                chain.insert(0, temp)
                dist.insert(0, self._distance[temp - 1])
                nodes.remove(temp)
            if not chain[0]:
                dist.insert(0, 0)
            dsum = [sum(dist[:i + 1]) for i in range(len(dist))]
            chain = NodeChain(nodes, dsum, temp, pchain)
            if pchain:
                pchain.addBranch(temp, chain)
            chain.registerNode(self.chains)

    def _toggleBlue(self, i):
        chain = self.chains[i]
        chain.toggle(i)
        # if i not in chain.dyed:
        #     pass
        #     dist = 0
        #     while i > 0:
        #         self._subBlue[i] += 1
        #         dist += self._distance[i - 1]
        #         i = self._parent[i - 1]
        #     self._subBlue[0] += 1
        #     self._totalDist += dist

    def _distSum(self, i):
        reduntant, compensate, dist = 0, 0, 0
        while i > 0:
            p = self._parent[i - 1]
            differ = self._subBlue[p] - self._subBlue[i]
            dist += self._distance[i - 1]
            compensate += dist * differ
            reduntant += self._distance[i - 1] * self._subBlue[i]
            i = self._parent[i - 1]
        return self._totalDist - reduntant + compensate

    def color(self, N, Q, startSeed, threshold, maxDist):
        self._curValue, dxor = startSeed, 0
        self._generateInput(N, Q, threshold, maxDist)
        self._preProcess(N)
        for i in range(Q):
            qtype = self._genNextRandom() % 2 + 1
            qnode = self._genNextRandom() % N
            if qtype == 1:
                self._toggleBlue(qnode)
            else:
                dxor ^= self._distSum(qnode)
        return dxor

if __name__ == '__main__':
    tc = TreeColoring()
    # print(tc.color(100000, 100000, 123456, 500000, 474747))
    # print(tc.color(4, 5, 2, 9, 10))
    # print(tc.color(8, 8, 3, 5, 7))
    # print(tc.color(14750, 50, 29750, 1157, 21610))
    print(tc.color(100000, 100000, 654321, 1000003, 1000003))
