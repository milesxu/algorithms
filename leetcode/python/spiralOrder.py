class Solution:

    # @param matrix, a list of lists of integers
    # @return a list of integers

    def spiralOrder(self, matrix):
        result, l, u, b, r = [], 0, 0, len(matrix),
        r = len(matrix[0]) if matrix else 0
        n = r * b
        while len(result) < n:
            result += matrix[u][l: r]
            u += 1
            result += [matrix[k][r - 1] for k in range(u, b)]
            r -= 1
            if u < b:
                result += [matrix[b - 1][k] for k in range(r - 1, l - 1, -1)]
                b -= 1
            if l < r:
                result += [matrix[k][l] for k in range(b - 1, u - 1, -1)]
                l += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[2, 3]]))
    print(s.spiralOrder([[2, 5, 8], [4, 0, -1]]))
    print(s.spiralOrder([[7], [9], [6]]))
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
