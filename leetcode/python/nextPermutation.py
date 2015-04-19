class Solution:

    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.

    def nextPermutation(self, num):
        if len(num) < 2:
            return
        j = None
        for i in range(len(num) - 1, 0, -1):
            if num[i] > num[i - 1]:
                j = i - 1
                break
        if j is not None:
            k = len(num) - 1
            while num[j] >= num[k]:
                k -= 1
            print(j, k)
            num[j], num[k] = num[k], num[j]
            l, m = j + 1, len(num) - 1
            while l < m:
                num[l], num[m] = num[m], num[l]
                l, m = l + 1, m - 1
        else:
            num.sort()


if __name__ == '__main__':
    np = Solution()
    # num = [4, 2, 4, 4, 3]
    # np.nextPermutation(num)
    # print(num)
    num = [1, 2]
    np.nextPermutation(num)
    print(num)
