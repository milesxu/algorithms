class Solution:

    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        row = len(board)
        if row < 3:
            return
        col = len(board[0])
        if col < 3:
            return
        intactSet = set()
        x, y = 1, 0
        while x < row - 1:
            y += 1
            if y == col - 1:
                x, y = x + 1, 1
            if board[x][y] == 'X' or (x, y) in intactSet:
                continue
            else:
                stack, curSet, opened = [[x, y, [0, 1, 2, 3]]], set(), False
                while stack:
                    z = stack.pop()
                    curSet.add((z[0], z[1]))
                    if z[0] == 0 or z[0] == row - 1 or \
                            z[1] == 0 or z[1] == col - 1:
                        opened = True
                    while z[2]:
                        temp = z[2].pop()
                        if temp == 0 and z[0] and \
                                board[z[0] - 1][z[1]] == 'O' and \
                                (z[0] - 1, z[1]) not in curSet:
                            stack.append([z[0] - 1, z[1], [0, 1, 3]])
                        elif temp == 1 and z[1] < col - 1 and \
                                board[z[0]][z[1] + 1] == 'O' and \
                                (z[0], z[1] + 1) not in curSet:
                            stack.append([z[0], z[1] + 1, [0, 1, 2]])
                        elif temp == 2 and z[0] < row - 1 and \
                                board[z[0] + 1][z[1]] == 'O' and \
                                (z[0] + 1, z[1]) not in curSet:
                            stack.append([z[0] + 1, z[1], [1, 2, 3]])
                        elif temp == 3 and z[1] and \
                                board[z[0]][z[1] - 1] == 'O' and \
                                (z[0], z[1] - 1) not in curSet:
                            stack.append([z[0], z[1] - 1, [0, 2, 3]])
                if not opened:
                    for p in curSet:
                        board[p[0]][p[1]] = 'X'
                else:
                    intactSet.update(curSet)


if __name__ == '__main__':
    s = Solution()
    # print(s.solve())
