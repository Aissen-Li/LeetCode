from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        def dfs(nums, sub, pos, res):
            if len(sub) >= 2:
                if sub not in res:
                    res.append(sub[:])
            for i in range(pos, len(nums)):
                if not sub or nums[i] >= sub[-1]:
                    sub.append(nums[i])
                    dfs(nums, sub, i+1, res)
                    sub.pop()
        res = []
        dfs(nums, [], 0, res)
        return res


s = Solution()
s.findSubsequences([4,6,7,7])