class Solution:

    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        lowexpect, highexpect, norepeat = {}, {}, set(num)
        for p in norepeat:
            if p in lowexpect and p in highexpect:
                low, high = lowexpect[p], highexpect[p]
                temp = [high[0], low[1]]
                del lowexpect[p]
                del highexpect[p]
                lowexpect[high[0]] = temp
                highexpect[low[1]] = temp
            elif p in lowexpect:
                lowexpect[p][0] = p - 1
                lowexpect[p - 1] = lowexpect[p]
                del lowexpect[p]
            elif p in highexpect:
                highexpect[p][1] = p + 1
                highexpect[p + 1] = highexpect[p]
                del highexpect[p]
            else:
                temp = [p - 1, p + 1]
                lowexpect[p - 1], highexpect[p + 1] = temp, temp
        longest = 0
        for p in lowexpect.values():
            longest = max(longest, p[1] - p[0] - 1)
        return longest

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive(
        [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]))
