class Solution:

    # @param nums, an integer[]
    # @return an integer

    def jump(self, nums):
        i, n = 0, 0
        while i < len(nums) - 1:
            if i + nums[i] >= len(nums) - 1:
                return n + 1
            if nums[i] == 1:
                i, n = i + 1, n + 1
            else:
                j = max([(v + k, k) for k, v in
                         enumerate(nums[i + 1: nums[i] + i + 1])])[1]
                i, n = i + j + 1, n + 1
        return n
