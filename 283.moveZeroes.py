from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        firstZero, firstNotZero = 0, 0
        n = len(nums)
        if n == 1:
            return
        while firstZero < n-1 and nums[firstZero] != 0:
            firstZero += 1
        if firstZero == n-1:
            return
        while firstNotZero < n:
            if nums[firstNotZero] == 0 or firstZero > firstNotZero:
                firstNotZero += 1
                continue
            nums[firstNotZero], nums[firstZero] = nums[firstZero], nums[firstNotZero]
            firstZero += 1
        return


s = Solution()
s.moveZeroes([0,1,0,3,12])