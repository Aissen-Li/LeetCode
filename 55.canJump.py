from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = 0
        for i in range(n-1):
            ans = max(ans, i+nums[i])
            if ans < i+1:
                return False
        if ans >= n-1:
            return True
        return False

s = Solution()
s.canJump([2,3,1,1,4])