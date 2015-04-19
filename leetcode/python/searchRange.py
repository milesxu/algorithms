class Solution:

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]

    def searchRange(self, A, target):
        start, end, mid = 0, len(A) - 1, -1
        while start < end:
            temp = (start + end) >> 1
            if A[temp] == target:
                mid = temp
                break
            elif A[temp] < target:
                start = temp + 1
            else:
                end = temp - 1
        print(mid, start, end)
        if A[mid] == target:
            if A[start] < target:
                bound = mid - 1
                while start < bound:
                    temp = (start + bound) >> 1
                    if A[temp] == target:
                        bound = temp
                    else:
                        start = temp + 1
                if A[start] < target:
                    start += 1
            if A[end] > target:
                bound = mid + 1
                while bound < end:
                    temp = (bound + end) >> 1
                    if A[temp] == target:
                        bound = temp + 1
                    else:
                        end = temp - 1
                if A[end] > target:
                    end -= 1
            return [start, end]
        if A[start] == target:
            return [start, start]
        return [-1, -1]


if __name__ == '__main__':
    sr = Solution()
    print(sr.searchRange(
        [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8], 4))
