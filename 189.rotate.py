from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        nums[:step], nums[step:] = nums[len(nums) - step:], nums[:len(nums) - step]