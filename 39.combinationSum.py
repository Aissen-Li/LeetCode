class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(candidates, tempRes, target, startIndex):
            if target == 0:
                res.append(tempRes[:])
                return
            for i in range(startIndex, len(candidates)):
                if candidates[i] > target:
                    break
                tempRes.append(candidates[i])
                dfs(candidates, tempRes, target - candidates[i], i)
                tempRes.pop()
        dfs(candidates, [], target, 0)
        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))