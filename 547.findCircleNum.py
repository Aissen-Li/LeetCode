from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        visited = [0] * n
        def dfs(matrix, visited, i):
            for j in range(i, n):
                if matrix[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(matrix, visited, j)
        res = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(M, visited, i)
                res += 1
        return res
