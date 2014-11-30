# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        top, a, b = headA, 0, 0
        while top:
            a, top = a + 1, top.next
        top = headB
        while top:
            b, top = b + 1, top.next
        topA, topB = headA, headB
        while a != b:
            if a > b:
                a, topA = a - 1, topA.next
            else:
                b, topB = b - 1, topB.next
        while a and b:
            if topA == topB:
                return topA
            a, b, topA, topB = a - 1, b - 1, topA.next, topB.next
        return None

    # @param two ListNodes
    # @return the intersected ListNode
    # to travel like a circle
    def getIntersectionNode1(self, headA, headB):
        endA, endB = None, None
        if headA and headB:
            pointA, pointB = headA, headB
            while pointA != pointB:
                if pointA.next:
                    pointA = pointA.next
                else:
                    endA, pointA = pointA, headB
                if pointB.next:
                    pointB = pointB.next
                else:
                    endB, pointB = pointB, headA
                if endA and endB and endA != endB:
                    return None
            return pointA
        return None
