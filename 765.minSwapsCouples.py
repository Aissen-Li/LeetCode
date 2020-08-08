from typing import List
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def findCouple(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1
        res = 0
        for i in range(0, len(row), 2):
            current = row[i]
            currentCouple = findCouple(current)
            if row[i+1] != currentCouple:
                j = row.index(currentCouple)
                row[i+1], row[j] = row[j], row[i+1]
                res += 1
        return res      