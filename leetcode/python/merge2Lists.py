# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        head, prev = l1, None
        while l2:
            if l2.val <= l1.val:
                temp, l2 = l2, l2.next
                if prev:
                    prev.next, temp.next = temp, prev.next
                else:
                    head, temp.next = temp, l1
                prev = temp
            elif l1.next is None:
                l1.next = l2
                break
            else:
                prev, l1 = l1, l1.next
        return head
