# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def reverseKGroup(self, head, k):
        top, cur, first, prev, n = head, head, head, None, 0
        while cur:
            cur, n = cur.next, n + 1
            if n == k:
                h, e = self._reveseList(top, cur)
                if prev is None:
                    first = h
                else:
                    prev.next = h
                prev, top, n = e, cur, 0
        if prev and top:
            prev.next = top
        return first

    def _reveseList(self, head, bound):
        top, end, cur = bound, head, head
        while cur != bound:
            temp, cur.next = cur.next, top
            top, cur = cur, temp
        return top, end

    def reverseKGroup1(self, head, k):
        prev, cur, first, temp = None, head, head, []
        while cur:
            temp.append(cur)
            cur = cur.next
            if len(temp) == k:
                for i in range(k - 1, 0, -1):
                    temp[i].next = temp[i - 1]
                temp[0].next = None
                if prev:
                    prev.next = temp[-1]
                else:
                    first = temp[-1]
                prev, temp = temp[0], []
        if prev and temp:
            prev.next = temp[0]
        return first


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    rkg = Solution()
    temp = rkg.reverseKGroup1(node1, 2)
    print(temp.val, temp.next.val)
