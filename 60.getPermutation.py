class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res = ''
        def dfs(n, k):
            if len(self.res) == n:
                return
            currentNum = factorial(n - len(self.res) - 1)
            for i in range(1, n + 1):
                if str(i) in self.res:
                    continue
                if currentNum < k:
                    k -= currentNum
                    continue
                self.res += str(i)
                dfs(n, k)
        
        def factorial(num):
            res = 1
            while num > 0:
                res *= num
                num -= 1
            return res
        dfs(n, k)
        return self.res
