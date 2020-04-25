from typing import List
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, i):
            if not i:
                return []
            res, popNum = [], len(nums) - i
            while nums:
                num = nums.pop(0)
                while popNum and res and res[-1] < num:
                    popNum -= 1
                    res.pop()
                res.append(num)
            return res[:i]
        def merge(res1, res2):
            res = []
            while res1 and res2:
                res.append(res1.pop(0) if res1 > res2 else res2.pop(0))
            res.extend(res1 or res2)
            return res
        res = []
        for i in range(k + 1):
            if i <= len(nums1) and k-i <= len(nums2):
                res = max(res, merge(pick(nums1.copy(), i), pick(nums2.copy(), k-i)))
        return res

