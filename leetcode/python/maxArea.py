class Solution:

    # @return an integer

    def maxArea(self, height):
        left, right = 0, len(height) - 1
        minh = min(height[left], height[right])
        less, area = height[left] <= height[right], minh * (right - left)
        while left + 1 < right:
            if less:
                left += 1
                if height[left] <= minh:
                    continue
            else:
                right -= 1
                if height[right] <= minh:
                    continue
            minh = min(height[left], height[right])
            area = max(area, minh * (right - left))
            less = height[left] <= height[right]
        return area


if __name__ == '__main__':
    ma = Solution()
    print(ma.maxArea([10, 14, 10, 4, 10, 2, 6, 1, 6, 12]))
