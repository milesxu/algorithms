# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node:
            nodes, stack = {}, [node]
            while stack:
                p = stack.pop()
                if p.label not in nodes:
                    nodes[p.label] = UndirectedGraphNode(p.label)
                cp = nodes[p.label]
                l, cl = len(p.neighbors), len(cp.neighbors)
                while l > cl:
                    q = p.neighbors[cl]
                    if q.label not in nodes:
                        nodes[q.label] = UndirectedGraphNode(q.label)
                        stack.append(q)
                    cp.neighbors.append(nodes[q.label])
                    cl += 1
            return nodes[node.label]
        return None
