class Solution:
    def numSquares(self, n: int) -> int:
        res = []
        nums = []
        for i in range(1, n):
            if i * i < n:
                nums.append(i * i)
            elif i * i == n:
                return 1
            else:
                break
        def dfs(target, nums, pos, subsets):
            if target == 0:
                res.append(len(subsets))
                return
            for i in range(pos, len(nums)):
                if nums[i] > target:
                    break
                subsets.append(nums[i])
                dfs(target - nums[i], nums, pos, subsets)
                subsets.pop()
        dfs(n, nums, 0, [])
        return min(res)


class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n)]
        for i in range(2, n+1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]
s = Solution()
print(s.numSquares(12))