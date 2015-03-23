class Solution:

    # @return a string
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for p in strs:
            while prefix:
                if p.find(prefix) == 0:
                    break
                prefix = prefix[0: len(prefix) - 1]
            if not prefix:
                return ''
        return prefix
