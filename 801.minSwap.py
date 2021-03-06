import sys
from typing import List
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[sys.maxsize, sys.maxsize] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp[i][0] = min(dp[i-1][1], dp[i][0])
                dp[i][1] = min(dp[i-1][0] + 1, dp[i][1])
        return min(dp[n-1][0], dp[n-1][1])