class Solution:

    # @return a string
    def convert(self, s, nRows):
        zigzag = [''] * nRows
        if len(zigzag) < 2:
            return s
        row, down = 0, True
        for p in s:
            zigzag[row] += p
            if row == 0:
                down = True
            if row == nRows - 1:
                down = False
            if down:
                row += 1
            else:
                row -= 1
        return ''.join(zigzag)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('ABC', 2))
