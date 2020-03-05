from typing import List
import heapq
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(left, right, pivotIndex):
            pivot = nums[pivotIndex]
            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
            differIndex = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[differIndex] = nums[differIndex], nums[i]
                    differIndex += 1
            nums[right], nums[differIndex] = nums[differIndex], nums[right]
            return differIndex

        def select(left, right ,kthSmallest):
            if left == right:
                return nums[left]
            pivotIndex = random.randint(left, right)
            pivotIndex = quickSort(left, right, pivotIndex)
            if kthSmallest == pivotIndex:
                return nums[kthSmallest]
            elif kthSmallest < pivotIndex:
                return select(left, pivotIndex, kthSmallest)
            else:
                return select(pivotIndex, right, kthSmallest)

        return select(0, len(nums) - 1, len(nums) - k)