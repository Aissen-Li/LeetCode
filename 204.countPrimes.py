class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, n):
            if i * i < n:
                if isPrime[i]:
                    for j in range(i * i, n, i):
                        isPrime[j] = False
        res = 0
        for i in range(2, n):
            if isPrime[i]:
                res += 1
        return res     