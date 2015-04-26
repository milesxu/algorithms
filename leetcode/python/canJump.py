class Solution:

    # @param {integer[]} nums
    # @return {boolean}

    def canJump(self, nums):
        i = 0
        while i < len(nums) - 1:
            if not nums[i]:
                return False
            if i + nums[i] >= len(nums) - 1:
                return True
            i = max([(k + v, k) for k, v in
                     enumerate(nums[i + 1: i + nums[i] + 1],
                               start=i + 1)])[1]
        return True

    def canJump1(self, nums):
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last <= 0
