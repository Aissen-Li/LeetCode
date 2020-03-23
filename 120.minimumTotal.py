from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if not triangle or n == 0:
            return 0
        dp = [0] * n
        dp[0] = triangle[0][0]
        left, right = 0, 0
        for i in range(1, n):
            row = triangle[i]
            for j in range(len(row)):
                right = dp[j]
                if j == 0:
                    dp[j] = row[j] + right
                elif j == i:
                    dp[j] = row[j] + left
                else:
                    dp[j] = min(left, right) + row[j]
                left = right
        return min(dp)