class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            smallest = 0
        else:
            while start <= end:
                middle = (start + end) // 2
                if nums[middle] > nums[middle+1]:
                    smallest = middle + 1
                    break
                if nums[middle] < nums[start]:
                    end = middle - 1
                    continue
                else:
                    start = middle + 1
                    continue

        if target == nums[smallest]:
            return smallest
        # if target < nums[smallest]:
        #     return -1
        if smallest == 0:
            start = 0
            end = len(nums)-1
        else:
            if target <= nums[-1]:
                start = smallest
                end = len(nums)-1
            if target >= nums[0]:
                start = 0
                end = smallest
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                start = middle
                continue
            if target < nums[middle]:
                end = middle
                continue
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


s = Solution()
print(s.search([4,5,1,2,3], 1))