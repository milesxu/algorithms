class Solution:

    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        arr, i, j = sorted(num), 0, len(num) - 1
        while i != j:
            temp = arr[i] + arr[j]
            if temp == target:
                i, j = num.index(arr[i]) + 1, num.index(arr[j]) + 1
                if i == j:
                    j = num.index(num[i], i + 1) + 1
                return (min(i, j), max(i, j))
            elif temp < target:
                i += 1
            else:
                j -= 1

    # @return a tuple, (index1, index2)
    def twoSum1(self, num, target):
        keys = {}
        for i, p in enumerate(num):
            if target - p in keys:
                return (keys[target - p], i + 1)
            keys[p] = i + 1

    def twoSum3(self, num, target):
        keys = {}
        for i, p in enumerate(num, start=1):
            if p in keys:
                return (keys[p], i)
            keys[target - p] = i

    # after sorting, index of iems are changed.
    def twoSum2(self, num, target):
        num.sort()
        i, j = 0, len(num) - 1
        while i < j:
            p = num[i] + num[j]
            if p == target:
                return (i + 1, j + 1)
            elif p < target:
                i += 1
            else:
                j -= 1
