from typing import List
class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        nums = sorted(nums)
        target = int(sum(nums) / 2)
        def check(subNums, nums):
            return 2 * sum(subNums) == sum(nums)
        def dfs(subNums, nums, target, pos):
            if target == 0:
                return check(subNums, nums)
            for i in range(pos, len(nums)):
                if nums[i] > target:
                    break
                subNums.append(nums[i])
                if dfs(subNums, nums, target - nums[i], i + 1):
                    return True
                subNums.pop()
        if dfs([], nums, target, 0):
            return True
        return False


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        nums = sorted(nums)
        target = int(sum(nums) / 2)
        m = len(nums)
        dp = [[False] * (target + 1) for _ in range(m)]
        dp[0][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, m):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            if dp[i][target]:
                return True
        return dp[m-1][target]
