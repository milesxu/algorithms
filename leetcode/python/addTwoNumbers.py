# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry, pre, top = 0, None, None
        while l1 or l2 or carry:
            node = ListNode(carry)
            carry = 0
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val > 9:
                node.val -= 10
                carry = 1
            if pre:
                pre.next, pre = node, node
            else:
                top = pre = node
        return top
