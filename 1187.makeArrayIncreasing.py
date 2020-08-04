import bisect
import sys
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        dp = [[sys.maxsize for _ in range(n+1)] for _ in range(n + 1)]
        dp[0][0] = -1
        for i in range(1, n+1):
            for j in range(i+1):
                if arr1[i-1] > dp[i-1][j]:
                    dp[i][j] = arr1[i-1]
                
                if j != 0:
                    pos = bisect.bisect_right(arr2, dp[i-1][j-1])
                    if pos < len(arr2):
                        dp[i][j] = min(dp[i][j], arr2[pos])
                if i == n and dp[i][j] != sys.maxsize:
                    return j
        return -1