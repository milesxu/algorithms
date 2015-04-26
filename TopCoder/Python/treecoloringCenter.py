class TreeColoring:

    """Single Round Match 624 Round 1 - Division I, Level Three:
    TreeColoring"""

    def __init__(self):
        self._curValue = 0
        self._tmax = 100100
        self._graph = [[] for i in range(self._tmax)]
        self._totalNodes = [0] * self._tmax
        self._nextCenterDivision = [[] for i in range(self._tmax)]
        self._centers = [[] for i in range(self._tmax)]
        self._childsValue = [[] for i in range(self._tmax)]
        self._childsTotalNodes = [[] for i in range(self._tmax)]
        self._totalSum = [0] * self._tmax
        self._rootCenter = -1
        self._dist = [dict() for i in range(self._tmax)]
        self._nextPosDivision = [dict() for i in range(self._tmax)]
        self._dyed = set()

    def _genNextRandom(self):
        self._curValue = (self._curValue * 1999 + 17) % 1000003
        return self._curValue

    def _makeGraph(self, N, threshold, maxDist):
        for i in range(N - 1):
            dist = self._genNextRandom() % maxDist
            temp = self._genNextRandom()
            if temp < threshold:
                parent = i
            else:
                parent = temp % (i + 1)
            self._graph[parent + 1].append((i + 2, dist))
            self._graph[i + 2].append((parent + 1, dist))

    def _countNodes(self, node, forbidden, father):
        subNodes = lambda nd, fa: [[nd, i] for i, j in self._graph[nd]
                                   if not (i in forbidden or i == fa)]
        ndPair = subNodes(node, father)
        self._totalNodes[node], i = 1, 0
        while i < len(ndPair):
            dad, son = ndPair[i]
            self._totalNodes[son] = 1
            ndPair += subNodes(son, dad)
            i += 1
        while ndPair:
            dad, son = ndPair.pop()
            self._totalNodes[dad] += self._totalNodes[son]
        return self._totalNodes[node]

    def _findCenter(self, node, forbidden, father, totalNodes):
        def search(lst, nd, fa):
            flag, curTotal = True, 0
            for i in self._graph[nd]:
                n = i[0]
                if not (n in forbidden or n == fa):
                    if self._totalNodes[n] > totalNodes // 2:
                        flag = False
                    lst.append([nd, n])
                    curTotal += self._totalNodes[nd]
            if totalNodes - curTotal - 1 > totalNodes // 2:
                flag = False
            return flag
        ndPair = []
        if search(ndPair, node, father):
            return node
        idx = 0
        while idx < len(ndPair):
            dad, son = ndPair[idx]
            if search(ndPair, son, dad):
                return son
            idx += 1
        print("negative value returned.")
        return -1

    def _getCenter(self, node, forbidden):
        totalNodes = self._countNodes(node, forbidden, -1)
        return self._findCenter(node, forbidden, -1, totalNodes)

    def _calcDist(self, centerNode, forbidden):
        sDist = lambda nd, fa, dt: [[nd, i, j + dt]
                                    for i, j in self._graph[nd]
                                    if not (i in forbidden or i == fa)]
        self._nextPosDivision[centerNode][centerNode] = -1
        self._dist[centerNode][centerNode] = 0
        dists = sDist(centerNode, -1, 0)
        i = 0
        while dists:
            dad, son, dist = dists.pop(0)
            self._nextPosDivision[centerNode][son] = i
            self._dist[centerNode][son] = dist
            tDists = sDist(son, dad, dist)
            idx = 0
            while idx < len(tDists):
                dad, son, dist = tDists[idx]
                tDists += sDist(son, dad, dist)
                idx += 1
            while tDists:
                dad, son, dist = tDists.pop()
                self._nextPosDivision[centerNode][son] = i
                self._dist[centerNode][son] = dist
            i += 1

    def _processCenter(self, node, forbidden):
        centerNode = self._getCenter(node, forbidden)
        forbidden.add(centerNode)
        self._calcDist(centerNode, forbidden)
        for i in self._graph[centerNode]:
            nd = i[0]
            if nd not in forbidden:
                self._childsValue[centerNode].append(0)
                self._childsTotalNodes[centerNode].append(0)
                nextCenter = self._processCenter(nd, forbidden)
                self._nextCenterDivision[centerNode].append(nextCenter)
        forbidden.remove(centerNode)
        self._totalSum[centerNode] = 0
        self._totalNodes[centerNode] = 0
        return centerNode

    def _preProcess(self):
        forbidden = set()
        self._rootCenter = self._getCenter(1, forbidden)
        self._processCenter(1, forbidden)

    def _update(self, node, qnode):
        if qnode not in self._dyed:
            self._totalNodes[node] += 1
            if qnode == node:
                self._dyed.add(node)
                return
            nextPos = self._nextPosDivision[node][qnode]
            self._totalSum[node] += self._dist[node][qnode]
            # may be concised?
            self._childsValue[node][nextPos] += self._dist[node][qnode]
            self._childsTotalNodes[node][nextPos] += 1
            self._update(self._nextCenterDivision[node][nextPos], qnode)

    def _distSum(self, node, qnode):
        if qnode == node:
            return self._totalSum[node]
        distSum, nextPos = 0, self._nextPosDivision[node][qnode]
        distSum += self._totalSum[node] - self._childsValue[node][nextPos]
        nodes = self._totalNodes[node] - self._childsTotalNodes[node][nextPos]
        distSum += nodes * self._dist[node][qnode]
        distSum += self._distSum(
            self._nextCenterDivision[node][nextPos], qnode)
        return distSum

    def color(self, N, Q, startSeed, threshold, maxDist):
        self._curValue, dxor = startSeed, 0
        self._makeGraph(N, threshold, maxDist)
        self._preProcess()
        for i in range(Q):
            qtype = self._genNextRandom() % 2 + 1
            qnode = self._genNextRandom() % N + 1
            if qtype == 1:
                self._update(self._rootCenter, qnode)
            else:
                dxor ^= self._distSum(self._rootCenter, qnode)
        return dxor

if __name__ == '__main__':
    tc = TreeColoring()
    # print(tc.color(100000, 100000, 123456, 500000, 474747))
    # print(tc.color(4, 5, 2, 9, 10))
    # print(tc.color(8, 8, 3, 5, 7))
    # print(tc.color(14750, 50, 29750, 1157, 21610))
    print(tc.color(100000, 100000, 654321, 1000003, 1000003))
    # print(tc.color(100000, 10, 654321, 1000003, 1000003))
