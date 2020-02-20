from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(nums: list, subset: list):
            if len(subset) == n:
                res.append(subset[:])
            for i in range(n):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs(nums, subset)
                    subset.pop()
        dfs(nums, [])
        return res

s = Solution()
print(s.permute([1, 2, 3]))