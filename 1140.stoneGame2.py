from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n, record = len(piles), {}
        s = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            s[i] = s[i+1] + piles[i]
        def dp(i, M):
            if (i, M) in record:
                return record[(i, M)]
            if i >= n:
                return 0
            if i + 2*M >= n:
                return s[i]
            best = 0
            for x in range(1, 2*M + 1):
                best = max(best, s[i]- dp(i+x, max(x, M)))
            record[(i, M)] = best
            return best
        return dp(0, 1)