from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if not m or not n:
            return
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(board, res, currentPos, visited):
            x = currentPos[0]
            y = currentPos[1]
            visited[x][y] = 1
            res.append((x, y))
            for dir in directions:
                nextX = x + dir[0]
                nextY = y + dir[1]
                pos = (nextX, nextY)
                if 0 <= nextX <= n - 1 and 0 <= nextY <= m - 1:
                    if board[nextX][nextY] == 'O' and visited[nextX][nextY] == 0:
                        dfs(board, res, pos, visited)
        visited = [[0] * n for _ in range(m)]
        notChanged = []
        for i in range(0, m):
            for j in [0, n-1]:
                if board[i][j] == 'O' and visited[i][j] == 0:
                    dfs(board, notChanged, (i,j), visited)
        for i in [0, m-1]:
            for j in range(0, n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    dfs(board, notChanged, (i,j), visited)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O" and (i, j) not in notChanged:
                    board[i][j] = "X"
        return

s = Solution()
s.solve([["X","O","X"],["X","O","X"],["X","O","X"]])