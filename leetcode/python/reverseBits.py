class Solution:

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        hexs = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        result = 0
        for i in range(8):
            result, n = (result << 4) + hexs[n & 15], n >> 4
            print(result)
        return result


if __name__ == '__main__':
    rb = Solution()
    print(rb.reverseBits(1))
