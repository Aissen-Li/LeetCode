from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums
        nums = sorted(nums)
        dp = [[i] for i in nums]
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)
        return max(dp, key=len)
