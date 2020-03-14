from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, tempSum = 0, 0
        sumDict = {0: 1}
        for i in range(len(nums)):
            tempSum += nums[i]
            if tempSum - k in sumDict:
                res += sumDict.get(tempSum-k)
            sumDict[tempSum] = sumDict.get(tempSum, 0) + 1
        return res


s = Solution()
s.subarraySum()