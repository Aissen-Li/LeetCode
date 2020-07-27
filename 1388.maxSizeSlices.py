from typing import List
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calculate(slices):
            n = len(slices)
            choice = (n+1) // 3
            dp = [[0] * (choice + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, choice + 1):
                    dp[i][j] = max(dp[i-1][j], (dp[i-2][j-1] if i >= 2 else 0) + slices[i-1])
            return dp[n][choice]
        return max(calculate(slices[1:]), calculate(slices[:-1]))