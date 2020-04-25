from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def affect(x, y):
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    if (i == x and j == y) or i < 0 or i >= m or j < 0 or j >= n:
                        continue
                    board[i][j] += 10
        for i in range(m):
            for j in range(n):
                if board[i][j] % 10 == 1:
                    affect(i, j)
        for i in range(m):
            for j in range(n):
                value = board[i][j]
                if value // 10 == 3:
                    board[i][j] = 1
                elif value // 10 == 2 and value % 10 == 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

