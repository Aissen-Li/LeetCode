from typing import List
class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def largestSquareArea(heights):
            heights = [0] + heights + [0]
            stack, maxArea = [], 0
            for rightIndex, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    highestIndex = stack.pop()
                    leftIndex = stack[-1]
                    squareSide = min(heights[highestIndex], rightIndex - leftIndex - 1)
                    maxArea = max(maxArea, squareSide * squareSide)
                stack.append(rightIndex)
            return maxArea
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, largestSquareArea(dp))
        return res


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        squareLength = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    squareLength = max(squareLength, dp[i][j])
        return squareLength * squareLength