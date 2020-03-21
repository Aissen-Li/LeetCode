from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.res = 0
        def merge(nums, start, mid ,end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.res += mid + 1 - i
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            nums[start: start + len(temp)] = temp[:]

        def mergeSort(nums, start, end):
            if start >= end:
                return
            mid = int((start + end) / 2)
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)
        mergeSort(nums, 0 , len(nums)-1)
        return self.res
