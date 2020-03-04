from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        numsSort = sorted(nums)
        n = len(nums)
        return numsSort[int(n/2)]