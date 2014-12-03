class Solution:

    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start, cur, longest, charidx = 0, 0, 0, {}
        for i, p in enumerate(s):
            if p not in charidx or charidx[p][-1] < start:
                charidx[p] = [i]
                cur += 1
            else:
                start = charidx[p][-1] + 1
                longest, cur = max(longest, cur), i - charidx[p][-1]
                charidx[p].append(i)
        return max(longest, cur)
