from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[None] * n for _ in range(n)] for _ in range(n)]
        def twoPaths(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')    
            elif r1 == c1 == n-1:
                return grid[r1][c1]
            elif dp[r1][c1][c2] is not None:
                return dp[r1][c1][c2]
            else:
                res = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                res += max(twoPaths(r1, c1 + 1, c2 + 1),
                           twoPaths(r1 + 1, c1, c2 + 1),
                           twoPaths(r1, c1 + 1, c2),
                           twoPaths(r1 + 1, c1, c2))
                dp[r1][c1][c2] = res
            return res
        return max(0, twoPaths(0, 0, 0))