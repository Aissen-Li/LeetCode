import heapq
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def countMidDistance(nums, target):
            left, count = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > target:
                    left += 1
                count += right - left
            return count
        
        nums.sort()
        maxDistance = nums[-1] - nums[0]
        low = 0
        high = maxDistance
        while low < high:
            mid = (low + high) // 2
            count = countMidDistance(nums, mid)
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low

s = Solution()
s.smallestDistancePair([1, 3, 1], 1)        