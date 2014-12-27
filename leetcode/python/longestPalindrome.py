class Solution:

    # @return a string
    def longestPalindrome(self, s):
        rs, longest, i = s[::-1], '', 0

        def palindrome(start, end):
            rend, rstart = len(s) - start, len(s) - end
            if s[start:end] == rs[rstart:rend]:
                return True
            return False

        while i < len(s) - len(longest):
            end = len(s)
            while end > i:
                end = s.rfind(s[i], i, end)
                if end + 1 - i <= len(longest) or not palindrome(i, end + 1):
                    continue
                longest = s[i:end + 1]
            i += 1
        return longest  # 返回能用雅黑字体了，哈哈哈哈
