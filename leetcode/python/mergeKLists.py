from operator import attrgetter

# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @param a list of ListNode
    # @return a ListNode

    def mergeKLists(self, lists):

        def merge(l1, l2):
            head, prev = l1, None
            while l2:
                if l2.val <= l1.val:
                    temp, l2 = l2, l2.next
                    if prev:
                        prev.next = temp
                    else:
                        head = temp
                    prev, temp.next = temp, l1
                elif l1.next is None:
                    l1.next = l2
                    break
                else:
                    prev, l1 = l1, l1.next
            return head

        lists = [p for p in lists if p]
        while len(lists) > 1:
            temp = []
            for j in range(0, len(lists), 2):
                if j < len(lists) - 1:
                    temp.append(merge(lists[j], lists[j + 1]))
                else:
                    temp.append(lists[j])
            lists = temp
        if lists:
            return lists[0]
        return None

    def mergeKLists1(self, lists):
        nodes = []
        for p in lists:
            while p:
                nodes.append(p)
                p = p.next
        if nodes:
            nodes.sort(key=attrgetter('val'))
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            nodes[-1].next = None
            return nodes[0]
        return None
