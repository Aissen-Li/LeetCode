from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        zeroRightBoundary, twoLeftBoundary = 0, n-1
        while zeroRightBoundary < n-1 and nums[zeroRightBoundary] == 0:
            zeroRightBoundary += 1
        while twoLeftBoundary > 0 and nums[twoLeftBoundary] == 2:
            twoLeftBoundary -= 1
        currentPos = zeroRightBoundary
        while currentPos <= twoLeftBoundary:
            if nums[currentPos] == 0:
                nums[zeroRightBoundary], nums[currentPos] = nums[currentPos], nums[zeroRightBoundary]
                zeroRightBoundary += 1
                currentPos += 1
                continue
            if nums[currentPos] == 2:
                nums[twoLeftBoundary], nums[currentPos] = nums[currentPos], nums[twoLeftBoundary]
                twoLeftBoundary -= 1
                continue
            if nums[currentPos] == 1:
                currentPos += 1
                continue
        return


s = Solution()
print(s.sortColors([2,0,2,1,1,0]))

