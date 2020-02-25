from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(subset, index, nums):
            res.append(subset[:])
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(subset, i+1, nums)
                subset.pop()
        dfs([], 0, nums)
        return res