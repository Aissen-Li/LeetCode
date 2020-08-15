class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        m = 10**9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(0, n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                val = (dp[i-1][j] + m - (dp[i-1][j-i] if j >= i else 0)) % m
                dp[i][j] = (dp[i][j-1] + val) % m
        return int(dp[n][k])
        