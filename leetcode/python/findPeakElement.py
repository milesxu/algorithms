class Solution:

    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        start, end = 0, len(num) - 1
        while start + 1 < end:
            if num[end] > num[end - 1]:
                return end
            if num[start] > num[start + 1]:
                return start
            mid = (start + end) // 2
            if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
                return mid
            elif num[mid] < num[mid + 1]:
                start = mid
            else:
                end = mid
        if num[start] < num[end]:
            return end
        else:
            return start
