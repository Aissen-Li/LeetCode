from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        suffixSum = [A[0]]
        if A[0] % K == 0:
            modDict = {0: 2}
        else:
            modDict = {0: 1, A[0] % K: 1}
        res = 0
        for i in range(1, len(A)):
            suffixSum.append(suffixSum[-1] + A[i])
            modDict[suffixSum[-1] % K] = modDict.get(suffixSum[-1] % K, 0) + 1
        for value in modDict.values():
            res += value * (value - 1) / 2
        return res

s = Solution()
s.subarraysDivByK([-5], 5)