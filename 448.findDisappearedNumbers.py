from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = nums[i] - 1
            if nums[index] > 0:
                nums[index] *= -1
        res = []
        for i in range(1, len(nums) + 1):
            if nums[i] > 0:
                res.append(i)
        return res