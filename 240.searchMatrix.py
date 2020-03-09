class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if n == 0:
            return False
        row, col = m-1, 0
        while 0 <= row <= m-1 and 0 <= col <= n-1:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
                continue
            if matrix[row][col] < target:
                col += 1
                continue
        return False


s = Solution()
res = s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
,5)