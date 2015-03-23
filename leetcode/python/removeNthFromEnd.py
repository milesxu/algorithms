# Definition for singly - linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @return a ListNode

    def removeNthFromEnd(self, head, n):
        start = end = head
        for i in range(n):
            end = end.next
        if end is None:
            return start.next
        while end.next:
            start, end = start.next, end.next
        start.next = start.next.next
        return head
