class Solution:

    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate(self, nums, k):
        k %= len(nums)

        def iterate(index):
            temp, n, s = nums[index], 0, index
            while True:
                stemp = s + k
                stemp %= len(nums)
                temp, nums[stemp], s, n = nums[stemp], temp, stemp, n + 1
                if index == s:
                    return n

        x, m = 0, 0
        while m < len(nums):
            m += iterate(x)
            x += 1
