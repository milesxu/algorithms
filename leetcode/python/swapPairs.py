# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @param a ListNode
    # @return a ListNode

    def swapPairs(self, head):
        cur, prev = head, None
        while cur and cur.next:
            if prev:
                prev.next = cur.next
            else:
                head = cur.next
            prev, temp = cur, cur.next
            cur.next = cur.next.next
            temp.next, cur = cur, cur.next
        return head
