# Definition for singly-linked list with a random pointer.
class RandomListNode:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        copyLst = []
        top = head
        while top:
            temp = RandomListNode(top.label)
            tn = top.next
            temp.next, top.next = top, temp
            top = tn
            copyLst.append(temp)
        for p in copyLst:
            source = p.next
            if source.random is not None:
                cpRandom = source.random.next
                p.random = cpRandom
        if copyLst:
            for i in range(len(copyLst) - 1):
                cp, source = copyLst[i], copyLst[i].next
                cp.next, source.next = copyLst[i + 1], copyLst[i + 1].next
            copyLst[-1].next.next = None
            copyLst[-1].next = None
            return copyLst[0]
        return None
