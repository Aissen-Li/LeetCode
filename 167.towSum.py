from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 <= index2 - 1 :
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            elif numbers[index1] + numbers[index2] == target:
                break
        if numbers[index1] + numbers[index2] == target:
            return [index1 + 1, index2 + 1]
        else:
            return []

s = Solution()
s.twoSum([2, 7, 11 ,15], 9)