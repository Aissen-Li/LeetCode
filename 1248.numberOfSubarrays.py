from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        res = 0
        for i in range(n):
            if nums[i] % 2 != 0:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd) - k):
            res += (odd[i]-odd[i-1]) * (odd[i+k] - odd[i+k-1])
        return res
