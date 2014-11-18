# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def sortList(self, head):

        def recursion(top):
            if top.next is None:
                return top, top
            pre, cur, tail, suc = None, top, top, None
            while tail.next:
                if tail.next.val == cur.val:
                    tail = tail.next
                else:
                    temp, tail.next = tail.next, tail.next.next
                    if temp.val < cur.val:
                        temp.next, pre = pre, temp
                    else:
                        temp.next, suc = suc, temp
            if pre:
                h, t = recursion(pre)
                t.next, cur = cur, h
            if suc:
                h, t = recursion(suc)
                tail.next, tail = h, t
            return cur, tail

        if head is None:
            return head
        head, tail = recursion(head)
        return head
