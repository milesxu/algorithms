class Solution:

    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start, end = 0, len(A) - 1
        while start < end:
            mid = (start + end) >> 1
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid
        if A[start] >= target:
            return start
        return start + 1
