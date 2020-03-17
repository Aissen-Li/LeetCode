from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        maxNum = max(A)
        maxIndex = A.index(maxNum)
        if maxIndex == 0 or maxIndex == len(A) - 1:
            return False
        for i in range(0, maxIndex):
            if A[i] >= A[i+1]:
                return False
        for i in range(maxIndex, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        return True