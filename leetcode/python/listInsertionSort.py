# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def insertionSortList(self, head):
        if head is None:
            return head
        cur = head
        while cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                if head.val > cur.next.val:
                    temp = cur.next
                    cur.next = temp.next
                    temp.next, head = head, temp
                else:
                    pre, suc = head, head.next
                    while suc.val <= cur.next.val:
                        pre, suc = suc, suc.next
                    pre.next, cur.next = cur.next, cur.next.next
                    pre.next.next = suc
        return head
