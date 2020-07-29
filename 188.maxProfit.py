class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices:
            return 0
        if k > n // 2:
            dp = [[0, 0] for _ in range(n)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[n-1][0]
        else:
            dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]
            for i in range(k+1):
                dp[0][i][0] = 0
                dp[0][i][1] = -prices[0]
            for i in range(1, n):
                dp[i][0][0] = 0
                dp[i][0][1] = max(dp[i-1][0][1], -prices[i])
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
            res = 0
            for i in range(k+1):
                res = max(res, dp[n-1][i][0])
            return res