from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        def dfs(nums, pos, target):
            if target == 0 and pos == len(nums):
               return 1
            if pos <= len(nums) - 1:
                currentNum = nums[pos]
                return dfs(nums, pos + 1, target - currentNum) + dfs(nums, pos + 1, target + currentNum)
            else:
                return 0

        return dfs(nums, 0, S)

class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        s = sum(nums)
        length = len(nums)
        dp = [dict() for _ in range(length)]
        if nums[0] == 0:
            dp[0][nums[0]] = 2
        else:
            dp[0][nums[0]] = 1
            dp[0][-nums[0]] = 1
        for i in range(1, length):
            for j in range(-s, s + 1):
                dp[i][j] = dp[i - 1].get(j - nums[i], 0) + dp[i - 1].get(j + nums[i], 0)

        return dp[length - 1].get(S, 0)



s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))
