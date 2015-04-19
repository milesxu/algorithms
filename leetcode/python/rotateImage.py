class Solution:

    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything,
    # modify matrix in-place instead.

    def rotate(self, matrix):
        bound = len(matrix) - 1
        for i in range(len(matrix) >> 1):
            for m in range(bound):
                trn = [[i, i + m], [i + m, i + bound],
                       [i + bound, i + bound - m], [i + bound - m, i]]
                temp = matrix[trn[0][0]][trn[0][1]]
                trn.append(trn.pop(0))
                for p in trn:
                    temp, matrix[p[0]][p[1]] = matrix[p[0]][p[1]], temp
            bound -= 2


if __name__ == '__main__':
    r = Solution()
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    r.rotate(matrix1)
    print(matrix1)
