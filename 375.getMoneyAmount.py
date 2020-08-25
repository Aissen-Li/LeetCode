import sys
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = 0
        for length in range(2, n+1):
            for i in range(1, n - length + 2):
                tmp = sys.maxsize
                for k in range(i, i + length - 1):
                    currentMin =  k + max(dp[i][k-1], dp[k+1][i + length - 1])
                    tmp = min(tmp, currentMin)
                dp[i][i + length - 1] = tmp
        return dp[1][n]