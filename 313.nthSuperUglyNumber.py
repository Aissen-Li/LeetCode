from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pos = [0 for i in range(len(primes))]
        res = [0 for i in range(n)]
        res[0] = 1
        for i in range(1, len(res)):
            minV = min([res[pos[j]]*primes[j] for j in range(len(primes))])
            res[i] = minV
            for k in range(len(pos)):
                if res[pos[k]]*primes[k] == minV:
                    pos[k] += 1
        return res[-1]

s = Solution()
s.nthSuperUglyNumber(12, [2, 7, 13, 19])