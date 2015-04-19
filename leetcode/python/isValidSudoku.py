class Solution:

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        rows, cols = [set() for i in range(9)], [set() for i in range(9)]
        blocks = [set() for i in range(9)]
        for i, p in enumerate(board):
            for j, q in enumerate(p):
                if q != '.':
                    block = i - (i % 3) + (j // 3)
                    if q in rows[i] or q in cols[j] or q in blocks[block]:
                        return False
                    rows[i].add(q)
                    cols[j].add(q)
                    blocks[block].add(q)
        return True
