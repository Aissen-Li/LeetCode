from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for k in range(len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j-i
                    j -= 1
                else:
                    i += 1
        return res

s = Solution()
s.triangleNumber([2, 2, 3, 4])