from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if not wordDict:
            return False
        maxLen = max(len(word) for word in wordDict)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(1, min(i, maxLen) + 1):
                if dp[i-j] and s[i-j: i] in wordDict:
                    dp[i] = True
        return dp[-1]