from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currentMax = nums[0]
        currentMin = nums[0]
        res = nums[0]
        for i in range(1, n):
            tempMax = currentMax
            currentMax = max(nums[i], currentMax * nums[i], currentMin * nums[i])
            currentMin = min(nums[i], currentMin * nums[i], tempMax * nums[i])
            res = max(res, currentMax)
        return res