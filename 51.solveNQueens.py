from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(subset, col):
            currentRow = len(subset)
            for dx in range(currentRow):
                if subset[dx] == col or abs(subset[dx] - col) == abs(dx - currentRow):
                    return False
            return True
        def draw(subset):
            res = []
            for i in range(len(subset)):
                temp = ['.'] * len(subset)
                temp[subset[i]] = 'Q'
                res.append(temp)
            return res
        def dfs(n, subset, res):
            if len(subset) == n:
                res.append(draw(subset))
            for col in range(n):
                if not check(subset, col):
                    continue
                subset.append(col)
                dfs(n, subset, res)
                subset.pop()
        if n <= 0 :
            return [[]]
        res = []
        dfs(n, [], res)
        return res


s = Solution()
s.solveNQueens(4)