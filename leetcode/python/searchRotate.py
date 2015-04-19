class Solution:

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start, end = 0, len(A) - 1
        while start < end:
            if A[start] == target:
                return start
            if A[end] == target:
                return end
            mid = (start + end) >> 1
            if A[mid] == target:
                return mid
            if A[start] < A[end]:
                if target < A[start] or target > A[end]:
                    return -1
                if target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if A[start] < A[mid]:
                    if A[start] < target < A[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if A[mid] < target < A[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
        if A[start] == target:
            return start
        return -1
