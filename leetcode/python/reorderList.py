# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return nothing

    def reorderList(self, head):

        def reverse(head):
            pre = None
            while head:
                temp, head = head, head.next
                temp.next, pre = pre, temp
            return pre

        tail, n = head, 0
        while tail:
            tail, n = tail.next, n + 1
        if n > 2:
            mid, newTail = n // 2, head
            while mid:
                newTail, mid = newTail.next, mid - 1
            ins, newTail.next = reverse(newTail.next), None
            oldPre, oldSuc = head, head.next
            while ins:
                temp = ins.next
                oldPre.next, ins.next = ins, oldSuc
                ins, oldPre, oldSuc = temp, oldSuc, oldSuc.next
