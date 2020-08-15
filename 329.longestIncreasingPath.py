from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        self.res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        record = [[0] * n for _ in range(m)]
        def dfs(pos):
            x = pos[0]
            y = pos[1]
            path = []
            for dx, dy in directions:
                if 0 <= x + dx <= m - 1 and 0 <= y + dy <= n - 1:
                    if matrix[x+dx][y+dy] > matrix[x][y]:
                        if record[x+dx][y+dy]:
                            path.append(record[x+dx][y+dy])
                        else:
                            path.append(dfs((x+dx, y+dy)))
            record[x][y] = max(path) + 1 if path else 1
            self.res = max(self.res, record[x][y])
            return record[x][y]
        for i in range(m):
            for j in range(n):
                if not record[i][j]:
                    dfs((i, j))         
        return self.res