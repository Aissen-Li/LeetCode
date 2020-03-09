from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = sorted(coins, reverse=True)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coinValue in coins:
            if coinValue > amount:
                break
            dp[coinValue] = 1
        for amountValue in range(1, amount + 1):
            for coinValue in coins:
                if coinValue > amountValue or dp[amountValue] == 1:
                    break
                if dp[amountValue - coinValue] == 0:
                    dp[amountValue] = 0
                dp[amountValue] = min(dp[amountValue], dp[amountValue - coinValue] + 1)
        if dp[-1] == 0:
            return -1
        return dp[-1]


s = Solution()
s.coinChange([1, 2, 5], 11)
