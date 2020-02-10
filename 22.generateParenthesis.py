class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def dfs(currentList, left, right):
            if len(currentList) == 2*n:
                res.append(currentList)
                return
            if left < n:
                dfs(currentList + "(", left+1, right)
            if right < left:
                dfs(currentList + ")", left, right+1)
        dfs("", 0, 0)
        return res


s = Solution()
print(s.generateParenthesis(3))