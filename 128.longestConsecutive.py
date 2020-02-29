from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, num = 0, set(nums)
        for low in nums:
            if low - 1 not in num:
                high = low + 1
                while high in num:
                    high += 1
                res = max(res, high - low)
        return res