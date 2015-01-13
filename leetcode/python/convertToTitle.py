class Solution:

    # @return a string
    def convertToTitle(self, num):
        title = ''
        while num:
            num, temp = divmod(num, 26)
            if temp == 0:
                title, num = title + 'Z', num - 1
            else:
                title += chr(ord('A') + temp - 1)
        return title[::-1]
