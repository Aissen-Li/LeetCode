class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n)]
        for i in range(1, n):
            if s[:i+1] == s[:i+1][::-1]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if s[j+1:i+1] == s[j+1:i+1][::-1])
        return dp[n-1]