class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return 1 if n == 1 else 2
        stepRecord = [1, 2]
        for _ in range(3, n+1):
            stepRecord[0], stepRecord[1] = stepRecord[1], stepRecord[0] + stepRecord[1]
        return stepRecord[1]