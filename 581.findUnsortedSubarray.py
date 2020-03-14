from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxHigh, right = nums[0], 0
        for i in range(n):
            if nums[i] >= maxHigh:
                maxHigh = nums[i]
            else:
                right = i
        minLow, left = nums[-1], n
        for j in range(n-1, -1, -1):
            if nums[j] <= minLow:
                minLow = nums[j]
            else:
                left = j
        return right - left + 1 if (right - left + 1) > 0 else 0
