from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res1 = 0
        res2 = 0
        if len(nums) % 2 == 0:
            median1 = nums[n//2-1]
            median2 = nums[n//2]
            for i in nums:
                res1 += abs(i-median1)
                res2 += abs(i-median2)
            return min(res1, res2)
        else:
            median1 = nums[n // 2]
            for j in nums:
                res1 += abs(j-median1)
            return res1