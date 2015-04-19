class Solution:

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        sudoku = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        rows, cols = [set() for i in range(9)], [set() for i in range(9)]
        blks = [set() for i in range(9)]
        for i, p in enumerate(board):
            for j, q in enumerate(p):
                if q != '.':
                    blk = i - (i % 3) + (j // 3)
                    rows[i].add(q)
                    cols[j].add(q)
                    blks[blk].add(q)

        candt = []
        for i, p in enumerate(board):
            rmiss = sudoku - rows[i]
            for j, q in enumerate(p):
                if q == '.':
                    b = i - (i % 3) + (j // 3)
                    cmiss = list(rmiss - (cols[j] | blks[b]))
                    candt.append([b, i, j] + cmiss)
        candt.sort(key=len)

        def conflicttest(n, m):
            b, i, j = candt[n][: 3]
            num = candt[n][m]
            if num in (rows[i] | cols[j] | blks[b]):
                return True
            for k, p in enumerate(candt[n + 1:]):
                if (b == p[0] or i == p[1] or j == p[2]) and len(p) == 4 \
                        and p[-1] == num:
                    return True
            return False

        def updateset(n, m):
            b, i, j = candt[n][: 3]
            num, minlen = candt[n][m], n
            rows[i].add(num)
            cols[j].add(num)
            blks[b].add(num)
            for k in range(n + 1, len(candt)):
                b1, i1, j1 = candt[k][: 3]
                if b1 == b or i1 == i or j1 == j:
                    candt[k][3:] = sudoku - (rows[i1] | cols[j1] | blks[b1])
                    if minlen == n or len(candt[minlen]) > len(candt[k]):
                        minlen = k
            if minlen > n + 1:
                candt[n + 1], candt[minlen] = candt[minlen], candt[n + 1]

        def rerollset(n, m):
            b, i, j = candt[n][: 3]
            num = candt[n][m]
            rows[i].remove(num)
            cols[j].remove(num)
            blks[b].remove(num)
            for k in range(n + 1, len(candt)):
                b1, i1, j1 = candt[k][: 3]
                if b == b1 or i == i1 or j == j1:
                    candt[k][3:] = sudoku - (rows[i1] | cols[j1] | blks[b1])

        n, stack = 0, []
        while n < len(candt):
            if n == len(stack):
                m = len(candt[n]) - 1
                while m >= 3 and conflicttest(n, m):
                    m -= 1
                if m < 3:
                    n -= 1
                else:
                    updateset(n, m)
                    stack.append(m)
                    n += 1
            else:
                m = stack[-1]
                rerollset(n, m)
                m -= 1
                while m >= 3 and conflicttest(n, m):
                    m -= 1
                if m < 3:
                    stack.pop()
                    n -= 1
                else:
                    updateset(n, m)
                    stack[-1], n = m, n + 1

        for k, p in enumerate(candt):
            i, j = p[1: 3]
            num = p[stack[k]]
            board[i] = board[i][: j] + num + board[i][j + 1:]


if __name__ == '__main__':
    sudokus = Solution()
    problem1 = ["..9748...", "7........", ".2.1.9...", "..7...24.",
                ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
                "...2759.."]
    sudokus.solveSudoku(problem1)
    print(problem1)
