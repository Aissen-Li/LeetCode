class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        for i in range(3, n+1):
            res = 0
            for k in range(1, i+1):
                res += dp[k-1] * dp[i-k]
            dp.append(res)
        return dp[-1]