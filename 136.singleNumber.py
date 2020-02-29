from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res