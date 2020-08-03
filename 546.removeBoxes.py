class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)] for _ in range(n)]
        def dfs(boxes,i,j,k,dp):
            if i > j:
                return 0
            if dp[i][j][k] > 0:
                return dp[i][j][k]
            while i < j and boxes[i] == boxes[i+1]:
                i += 1
                k += 1
            res = (k+1)*(k+1) + dfs(boxes,i+1,j,0,dp)
            for m in range(i+1,j+1):
                if boxes[m] == boxes[i]:
                    res = max(res,dfs(boxes,i+1,m-1,0,dp)+dfs(boxes,m,j,k+1,dp))
            dp[i][j][k] = res
            return res
        return dfs(boxes,0,n-1,0,dp)