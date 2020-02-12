class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        if nums[0] == nums[-1] == target:
            return [0, len(nums)-1]
        if nums[0] == nums[-1] and nums[0] != target:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                left, right = middle, middle
                while nums[left] == nums[left - 1] and left >= 1:
                    left -= 1
                    if left == 0:
                        break
                while nums[right] == nums[right + 1] and right <= len(nums) - 2:
                    right += 1
                    if right == len(nums) - 1:
                        break
                return [left, right]
            if nums[middle] >= target:
                end = middle
            else:
                start = middle
        if nums[start] == target and nums[end] == target:
            return [start, end]
        if nums[start] == target and nums[end] != target:
            return [start, start]
        if nums[start] != target and nums[end] == target:
            return [end, end]
        return [-1, -1]