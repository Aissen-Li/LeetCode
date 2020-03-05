from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(grid, pos, visited):
            visited[pos[0]][pos[1]] = True
            for dir in directions:
                currentPos = (pos[0] + dir[0], pos[1] + dir[1])
                if 0 <= currentPos[0] < m and 0 <= currentPos[1] < n:
                    if grid[currentPos[0]][currentPos[1]] == '1' and not visited[currentPos[0]][currentPos[1]]:
                        dfs(grid, currentPos, visited)

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        islandNums = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islandNums += 1
                    dfs(grid, (i, j), visited)
        return islandNums
