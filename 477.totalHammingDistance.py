from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        for i in range(32):
            cnt1 = 0
            for j in range(n):
                cnt1 += (nums[j] >> i) & 1
            res += (n - cnt1) * cnt1
        return res 