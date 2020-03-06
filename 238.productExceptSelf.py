from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [0] * n
        suffixProduct = [0] * n
        res = [0] * n
        prefixProduct[0] = nums[0]
        suffixProduct[n-1] = nums[n-1]
        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i]
        for i in range(n-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i]
        res[0] = suffixProduct[1]
        res[n-1] = prefixProduct[-2]
        for i in range(1, n-1):
            res[i] = prefixProduct[i-1] * suffixProduct[i+1]
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))