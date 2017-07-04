class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sgrid = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i and j:
                    sgrid[i][j] = min(sgrid[i - 1][j], sgrid[i][j - 1])
                elif i:
                    sgrid[i][j] = sgrid[i - 1][j]
                elif j:
                    sgrid[i][j] = sgrid[i][j - 1]
                sgrid[i][j] += grid[i][j]

        return sgrid[len(grid) - 1][len(grid[0]) - 1]
