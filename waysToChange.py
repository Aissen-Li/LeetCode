class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [1] + [0] * n
        coins = [25, 10, 5, 1]

        for coin in coins:
            for value in range(coin, n+1):
                dp[value] += dp[value - coin]
        return dp[n] % (10**9 + 7)


s = Solution()
s.waysToChange(5)