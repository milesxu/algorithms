# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean

    def hasCycle(self, head):
        if head is None:
            return False
        pre, top = head, head.next
        while top:
            temp = top.next
            if temp == head:
                return True
            top.next, pre, top = pre, top, temp
        return False

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        pre, top, n = None, head, 0
        while top:
            temp = top.next
            top.next, pre, top, n = pre, top, temp, n + 1
        if n > 1 and pre == head:
            m, top = n // 2, head
            while m:
                top, m = top.next, m - 1
            temp = top
            while True:
                temp, m = temp.next, m + 1
                if temp == top:
                    break
            m = m // 2
            while m:
                top, m = top.next, m - 1
            return top
        return None

    # @param head, a ListNode
    # @return a list node
    def detectCycle1(self, head):
        if head:
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    top = head
                    while top != slow:
                        top, slow = top.next, slow.next
                    return top
        return None
