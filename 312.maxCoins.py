from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def getMaxCoins(nums, i, j, dp):
            if i == j-1:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            res = 0
            for k in range(i+1, j):
                left = getMaxCoins(nums, i, k, dp)
                right = getMaxCoins(nums, k, j, dp)
                res = max(res, left + right + nums[i] * nums[k] * nums[j])
            dp[i][j] = res
            return res
        return getMaxCoins(nums, 0, n-1, dp)