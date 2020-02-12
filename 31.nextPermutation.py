class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]< nums[i]:
                changePosition = i-1
                flag = True
                break

        if not flag:
            nums = nums[::-1]
            return

        for i in range(len(nums)-1, changePosition, -1):
            if nums[i] > nums[changePosition]:
                nums[i], nums[changePosition] = nums[changePosition], nums[i]
                break

        resort = nums[changePosition+1:]
        resort.sort()
        nums[changePosition+1:] = resort
        return

s = Solution()
s.nextPermutation([3, 2, 1])
